#!/usr/bin/env python3
"""du-design lookup: section search over this repo, a cached gallery index, optional Jev rerank.

Stdlib only, so any agent can run it with plain `python3`.

  python3 tools/du.py find "navbar mega menu" [--brief "..."]   # ranked sections
  python3 tools/du.py read "<id>"                               # one section
  python3 tools/du.py refs "saas pricing" [--source saaspo]      # cached gallery sites
  python3 tools/du.py index                                     # regenerate INDEX.md
  python3 tools/du.py refresh [source ...]                      # re-scrape galleries (Orthogonal, ~$0.005/page)
  python3 tools/du.py serve                                     # MCP server over stdio
"""
import json, os, re, sqlite3, ssl, subprocess, sys, time, urllib.error, urllib.request
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CACHE = ROOT / ".cache"
REFS_DB = CACHE / "refs.db"
SKIP_DIRS = {".git", ".cache", "node_modules", "tools"}
BIG = 4000  # tokens; files above this get their sections listed in INDEX.md

# Gallery sources: home page + which internal links are category pages worth scraping.
SOURCES = {
    "navbar.gallery": ("https://www.navbar.gallery", r"^https://www\.navbar\.gallery/type/[\w-]+$"),
    "cta.gallery": ("https://www.cta.gallery", r"^https://www\.cta\.gallery/categories/[\w-]+$"),
    "landing.love": ("https://www.landing.love", r"^https://www\.landing\.love/(categories|collection|platform)/[\w-]+/$"),
    "saaspo": ("https://saaspo.com", r"^https://saaspo\.com/(industry|type|assets|page|style)/[\w-]+$"),
    # MIT-licensed DESIGN.md files for ~74 real brands; plain GitHub fetch, free. Pattern None = not a scraped gallery.
    "design-md": ("https://github.com/VoltAgent/awesome-design-md", None),
}
# Hosts that show up as links on gallery pages but are ads, socials, or assets, not sites.
JUNK = re.compile(r"framer\.link|framerusercontent|twitter\.com|x\.com|bsky\.app|carbonads|buysellads|mobbin|dub\.sh|"
                  r"substack|website-files|cdn\.|screenshotone|linkedin\.com|instagram\.com|youtube\.com|github\.com|"
                  r"framer\.com|webflow\.com|figma\.com|\.(png|jpe?g|webp|avif|svg|gif)(\?|$)")


# ---------- repo sections ----------

def tokens(s):
    return len(s) // 4


def md_files():
    for p in sorted(ROOT.rglob("*.md")):
        if not SKIP_DIRS & set(p.relative_to(ROOT).parts) and p.name != "INDEX.md":
            yield p


def sections(path):
    """Split a markdown file on #/##/### headings. Table rows become their own chunks so
    ROUTER-style dispatch rows are individually findable."""
    rel = str(path.relative_to(ROOT))
    lines = path.read_text(errors="ignore").splitlines()
    trail, out, start, fence = [], [], 0, False

    def close(end):
        body = "\n".join(lines[start:end]).strip()
        if body:
            out.append({"path": rel, "heading": " > ".join(trail) or path.stem,
                        "start": start + 1, "end": end, "text": body})

    for i, line in enumerate(lines):
        if line.startswith("```"):
            fence = not fence
        m = None if fence else re.match(r"^(#{1,3})\s+(.*)", line)
        if m:
            close(i)
            level = len(m.group(1))
            trail = trail[:level - 1] + [m.group(2).strip()]
            start = i
    close(len(lines))

    rows = []
    for s in out:
        tl = s["text"].splitlines()
        for j, line in enumerate(tl):
            is_sep = lambda l: set(l.strip()) <= set("|-: ")
            header = j + 1 < len(tl) and is_sep(tl[j + 1])
            if line.startswith("|") and line.count("|") > 2 and not is_sep(line) and not header:
                n = s["start"] + j
                rows.append({"path": rel, "heading": s["heading"] + " > row", "start": n, "end": n, "text": line})
    return out + rows


def sid(s):
    return f'{s["path"]}:{s["start"]}-{s["end"]}'


_db = None


def db():
    """In-memory FTS index of every section; rebuilt per process (the repo is small, this takes ms)."""
    global _db
    if _db is None:
        _db = sqlite3.connect(":memory:")
        _db.execute("create virtual table s using fts5(id unindexed, path, heading, text, tokenize='porter')")
        for p in md_files():
            _db.executemany("insert into s values (?,?,?,?)",
                            [(sid(x), x["path"], x["heading"], x["text"]) for x in sections(p)])
    return _db


def fts_query(q):
    words = [w for w in re.findall(r"[a-z0-9]+", q.lower()) if len(w) > 1]
    return " OR ".join(f'"{w}"*' for w in words)


def find(query, k=5, brief=None):
    q = fts_query(query)
    if not q:
        return []
    pool = k * 4 if brief else k
    # bm25 weights: path, heading count more than body text.
    rows = db().execute(
        "select id, path, heading, snippet(s, 3, '', '', ' … ', 24), bm25(s, 3.0, 5.0, 1.0) from s "
        "where s match ? order by 5 limit ?", (q, pool)).fetchall()
    hits = [{"id": r[0], "heading": r[2], "snippet": " ".join(r[3].split())} for r in rows]
    if brief and len(hits) > 1:
        hits = rerank(query, brief, hits, lambda h: {"file": h["id"], "heading": h["heading"], "text": read(h["id"])[:1500]})[:k]
    return hits


def read(id_, limit=12000):
    m = re.match(r"(.+):(\d+)-(\d+)$", id_)
    if not m:
        return f"bad id {id_!r}; expected path:start-end from find()"
    p = (ROOT / m.group(1)).resolve()
    if ROOT not in p.parents or not p.is_file():
        return f"no such file: {m.group(1)}"
    lines = p.read_text(errors="ignore").splitlines()[int(m.group(2)) - 1:int(m.group(3))]
    text = "\n".join(lines)
    return text if len(text) <= limit else text[:limit] + f"\n… [truncated; read the file at {id_} for the rest]"


def build_index():
    """INDEX.md: every file with a token size; big files also list their ## sections with line ranges,
    so an agent without the MCP can `sed -n` just the part it needs."""
    out = ["# INDEX — generated by `python3 tools/du.py index`; do not edit by hand",
           "",
           "Fastest path: the `du-design` MCP (`find` → `read`). Without it, run `python3 tools/du.py find \"<need>\"`.",
           "Otherwise pick a file below; for big files read only the line range you need.",
           ""]
    for p in md_files():
        rel = str(p.relative_to(ROOT))
        text = p.read_text(errors="ignore")
        out.append(f"- `{rel}` ~{tokens(text)//100/10}k tok")
        if tokens(text) > BIG:
            for s in sections(p):
                if s["heading"].count(" > ") <= 1 and not s["heading"].endswith("> row") and tokens(s["text"]) > 150:
                    out.append(f"  - L{s['start']}-{s['end']} {s['heading'].split(' > ')[-1]} (~{tokens(s['text'])} tok)")
    (ROOT / "INDEX.md").write_text("\n".join(out) + "\n")
    return len(out)


# ---------- gallery refs ----------

def scrape(url):
    body = {"url": url, "formats": [{"type": "markdown", "mode": "normal"}],
            "fetchConfig": {"mode": "js", "wait": 2500, "scrolls": 3}}
    r = subprocess.run(["orth", "run", "--raw", "scrapegraphai", "/api/scrape", "--body", json.dumps(body)],
                       capture_output=True, text=True, timeout=180)
    t = r.stdout
    if r.returncode or "{" not in t:
        raise RuntimeError(f"scrape failed for {url}: {r.stderr.strip()[:200]}")
    j, _ = json.JSONDecoder().raw_decode(t[t.index("{"):])
    return j["results"]["markdown"]["data"][0]


def site_links(md, gallery_host):
    """External site links on a gallery page -> {url: name}. Galleries tag outbound links differently,
    so this is a generic heuristic: any non-junk external link, name = best link text seen."""
    # ponytail: heuristic extraction, no per-gallery parser; add one if a gallery's results look noisy.
    found = {}
    md = re.sub(r"!\[[^\]]*\]\([^)]*\)", "", md)  # drop images so image-wrapped links parse
    for text, url, title in re.findall(r"\[([^\]]*)\]\((https?://[^)\s]+)(?:\s+\"([^\"]*)\")?\)", md):
        text = text or re.sub(r"^visit\s+|\s+website$", "", title or "", flags=re.I)
        clean = re.sub(r"[?#].*$", "", url).rstrip("/")
        host = re.sub(r"^https?://(www\.)?", "", clean).split("/")[0]
        if gallery_host in host or JUNK.search(url) or not host:
            continue
        name = re.sub(r"!\[[^\]]*\]\([^)]*\)|visit( individual navigation page| website)?", "", text, flags=re.I).strip()
        if len(name) > len(found.get(clean, "")) and len(name) < 60:
            found[clean] = name
        found.setdefault(clean, "")
    return found


def refs_db():
    CACHE.mkdir(exist_ok=True)
    c = sqlite3.connect(REFS_DB)
    c.execute("create table if not exists refs (url text, name text, source text, tag text, page text, fetched real,"
              " primary key (url, tag))")
    return c


def get(url):
    ctx = ssl.create_default_context(cafile="/etc/ssl/cert.pem" if os.path.exists("/etc/ssl/cert.pem") else None)
    return urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "du-design"}), timeout=30,
                                  context=ctx).read().decode()


def design_md_rows(home):
    """One row per brand: url = raw DESIGN.md (fetch it and drop into a project), tag = its style description."""
    repo = home.split("github.com/")[1]
    brands = [d["name"] for d in json.loads(get(f"https://api.github.com/repos/{repo}/contents/design-md")) if d["type"] == "dir"]
    raw = lambda b: f"https://raw.githubusercontent.com/{repo}/main/design-md/{b}/DESIGN.md"

    def one(b):
        try:
            m = re.search(r"^description:\s*(.+)$", get(raw(b)), re.M)
            return (raw(b), b, "design-md", m.group(1).strip() if m else b, home)
        except Exception:
            return None

    with ThreadPoolExecutor(8) as pool:
        return [r for r in pool.map(one, brands) if r]


def refresh(names=None, log=print):
    c = refs_db()
    cost = 0
    for name in names or SOURCES:
        home, pat = SOURCES[name]
        if pat is None:
            rows = design_md_rows(home)
            c.execute("delete from refs where source=?", (name,))
            c.executemany("insert or replace into refs values (?,?,?,?,?,?)", [r + (time.time(),) for r in rows])
            c.commit()
            log(f"{name}: {len(rows)} DESIGN.md files (free)")
            continue
        host = re.sub(r"^https?://(www\.)?", "", home)
        md = scrape(home); cost += 1
        pages = sorted({re.sub(r"[?#].*$", "", u) for u in re.findall(r"\]\((https?://[^)\s]+)\)", md)
                        if re.match(pat, re.sub(r"[?#].*$", "", u))})
        log(f"{name}: {len(pages)} category pages")
        rows = [(u, n, name, "home", home) for u, n in site_links(md, host).items()]

        def one(page):
            try:
                return page, scrape(page)
            except Exception as e:
                log(f"  skip {page}: {e}")
                return page, None

        with ThreadPoolExecutor(6) as pool:
            for page, pmd in pool.map(one, pages):
                if pmd is None:
                    continue
                cost += 1
                tag = page.rstrip("/").rsplit("/", 1)[-1].replace("-saas-websites-inspiration", "")
                rows += [(u, n, name, tag, page) for u, n in site_links(pmd, host).items()]
        # Sponsors/ads repeat on most pages of a gallery; real entries don't. Drop the repeaters.
        seen = {}
        for r in rows:
            seen.setdefault(r[0], set()).add(r[4])
        ads = {u for u, ps in seen.items() if len(ps) >= max(3, len(pages) / 2)}
        rows = [r for r in rows if r[0] not in ads and not re.search(r"advertis|sponsor|template", r[1], re.I)]
        now = time.time()
        c.execute("delete from refs where source=?", (name,))
        c.executemany("insert or replace into refs values (?,?,?,?,?,?)", [r + (now,) for r in rows])
        c.commit()
        log(f"  {len({r[0] for r in rows})} sites")
    log(f"~${cost * 0.005:.2f} spent ({cost} pages)")


def refs(query, source=None, k=10, brief=None):
    if not REFS_DB.exists():
        return {"error": "gallery cache is empty; run `python3 tools/du.py refresh` (~$0.85, ~7 minutes)"}
    c = refs_db()
    words = [w for w in re.findall(r"[a-z0-9]+", query.lower()) if len(w) > 2]
    rows = c.execute("select url, name, source, group_concat(tag, ', '), max(fetched) from refs "
                     + ("where source=? " if source else "") + "group by url",
                     (source,) if source else ()).fetchall()
    # Score = how many query words hit the tags/name/url; tags count double.
    scored = []
    for url, name, src, tags, fetched in rows:
        hay = f"{name} {url}".lower()
        s = sum(2 * (w in tags) + (w in hay) for w in words)
        if s:
            t = tags if len(tags) <= 280 else tags[:280].rsplit(" ", 1)[0] + "…"
            scored.append((s, f"{url}{' — ' + name if name else ''} [{src}: {t}]"))
    scored.sort(key=lambda x: -x[0])
    if not scored:
        tags = sorted({t for r in rows if r[2] != "design-md" for t in r[3].split(", ")} - {"home"})
        return {"total": 0, "hint": "no match; retry with one of these tags", "tags": tags}
    age = (time.time() - max(r[4] for r in rows)) / 86400 if rows else None
    return {"cache_age_days": round(age, 1) if age is not None else None, "total": len(scored),
            "sites": pick([s for _, s in scored], query, brief, k)}


def pick(lines, query, brief, k):
    if not brief or len(lines) < 2:
        return lines[:k]
    items = [{"site": l} for l in lines[:k * 4]]
    return [it["site"] for it in rerank(query, brief, items, lambda it: it["site"])[:k]]


# ---------- Jev rerank ----------

def env_key():
    if os.environ.get("TYPESAFE_API_KEY"):
        return os.environ["TYPESAFE_API_KEY"]
    for f in (".env.local", ".env"):
        p = ROOT / f
        if p.exists():
            m = re.search(r"^TYPESAFE_API_KEY[ \t]*=[ \t]*['\"]?([^'\"\s]+)", p.read_text(), re.M)
            if m:
                return m.group(1)


def rerank(query, brief, items, describe):
    """One Jev request, one Noul per candidate; sort by probability. Falls back to input order."""
    key = env_key()
    if not key:
        return items
    questions = {str(i): {"type": "noul", "instructions": {
        "candidate": describe(it),
        "question": "Would reading `candidate` directly help an agent do `need` for the project described in `brief`?"},
        "criteria": {"true": "It gives specific, usable guidance or examples for this need and project.",
                     "false": "It is off-topic, generic, or only loosely related."}}
        for i, it in enumerate(items)}
    req = urllib.request.Request("https://api.typesafe.ai/v1/systemone", method="POST",
                                 headers={"Authorization": f"Bearer {key}", "Content-Type": "application/json"},
                                 data=json.dumps({"model": "jev-latest", "state": {"need": query, "brief": brief},
                                                  "questions": questions}).encode())
    # python.org builds on macOS ship without CA certs; fall back to the system bundle.
    ctx = ssl.create_default_context(cafile="/etc/ssl/cert.pem" if os.path.exists("/etc/ssl/cert.pem") else None)
    for attempt in range(4):
        try:
            ans = json.load(urllib.request.urlopen(req, timeout=30, context=ctx))["answers"]
            break
        except urllib.error.HTTPError as e:
            if e.code not in (429, 500, 502, 503, 529) or attempt == 3:
                print(f"jev rerank skipped: {e}", file=sys.stderr)
                return items
            time.sleep(float(e.headers.get("retry-after") or 2 ** attempt))  # busy: back off like the SDKs do
        except Exception as e:
            print(f"jev rerank skipped: {e}", file=sys.stderr)
            return items
    for i, it in enumerate(items):
        it["fit"] = round(ans[str(i)]["noul"], 2)
    return sorted(items, key=lambda it: -it["fit"])


# ---------- MCP (JSON-RPC 2.0 over stdio, newline-delimited) ----------

TOOLS = [
    {"name": "find", "description": "Search du-design's own guidance (principles, patterns, skills, toolbelt, past work) by need. "
     "Returns ranked section ids + snippets; call read(id) for the ones you want. Pass brief to rerank by project fit.",
     "inputSchema": {"type": "object", "required": ["query"], "properties": {
         "query": {"type": "string", "description": "What you need, in keywords, e.g. 'navbar mega menu' or 'easing durations'"},
         "brief": {"type": "string", "description": "Optional one-paragraph project brief; enables Jev rerank"},
         "k": {"type": "integer", "default": 5}}}},
    {"name": "read", "description": "Return one section's text by the id from find().",
     "inputSchema": {"type": "object", "required": ["id"], "properties": {"id": {"type": "string"}}}},
    {"name": "refs", "description": "Use this (not find) whenever you need real example websites or a real brand's design system. "
     "Searches ~1,400 cached sites from navbar.gallery, cta.gallery, landing.love, saaspo by tag ('mega menu', 'pricing', "
     "'dark-mode', 'finance', 'webgl'), plus source 'design-md': ready DESIGN.md files (colors, type, spacing) for ~74 brands "
     "like Stripe, Linear, Wise, searchable by look ('lime fintech', 'editorial serif'). Pass brief to rerank by fit. "
     "No match returns the tag list.",
     "inputSchema": {"type": "object", "required": ["query"], "properties": {
         "query": {"type": "string"},
         "source": {"type": "string", "enum": list(SOURCES)},
         "brief": {"type": "string", "description": "Optional project brief; enables Jev rerank"},
         "k": {"type": "integer", "default": 10}}}},
]


def call(name, a):
    if name == "find":
        return find(a["query"], a.get("k", 5), a.get("brief"))
    if name == "read":
        return read(a["id"])
    if name == "refs":
        return refs(a["query"], a.get("source"), a.get("k", 10), a.get("brief"))
    raise ValueError(f"unknown tool {name}")


def serve():
    for line in sys.stdin:
        if not line.strip():
            continue
        msg = json.loads(line)
        mid, method = msg.get("id"), msg.get("method")
        if mid is None:
            continue  # notification
        try:
            if method == "initialize":
                res = {"protocolVersion": msg["params"].get("protocolVersion", "2025-06-18"),
                       "capabilities": {"tools": {}}, "serverInfo": {"name": "du-design", "version": "1"}}
            elif method == "tools/list":
                res = {"tools": TOOLS}
            elif method == "tools/call":
                out = call(msg["params"]["name"], msg["params"].get("arguments") or {})
                text = out if isinstance(out, str) else json.dumps(out, separators=(",", ":"), ensure_ascii=False)
                res = {"content": [{"type": "text", "text": text}]}
            elif method == "ping":
                res = {}
            else:
                raise LookupError(method)
            reply = {"jsonrpc": "2.0", "id": mid, "result": res}
        except LookupError as e:
            reply = {"jsonrpc": "2.0", "id": mid, "error": {"code": -32601, "message": f"method not found: {e}"}}
        except Exception as e:
            reply = {"jsonrpc": "2.0", "id": mid, "result": {"isError": True, "content": [{"type": "text", "text": str(e)}]}}
        sys.stdout.write(json.dumps(reply) + "\n")
        sys.stdout.flush()


def main(argv):
    cmd, rest = (argv[0], argv[1:]) if argv else ("help", [])
    opt = lambda f: rest[rest.index(f) + 1] if f in rest else None
    args = [a for i, a in enumerate(rest) if not a.startswith("--") and (i == 0 or not rest[i - 1].startswith("--"))]
    if cmd == "serve":
        serve()
    elif cmd == "find":
        print(json.dumps(find(" ".join(args), int(opt("--k") or 5), opt("--brief")), indent=1, ensure_ascii=False))
    elif cmd == "read":
        print(read(args[0]))
    elif cmd == "refs":
        print(json.dumps(refs(" ".join(args), opt("--source"), int(opt("--k") or 10), opt("--brief")), indent=1, ensure_ascii=False))
    elif cmd == "index":
        print(f"INDEX.md: {build_index()} lines")
    elif cmd == "refresh":
        refresh(args or None)
    else:
        print(__doc__)


if __name__ == "__main__":
    main(sys.argv[1:])
