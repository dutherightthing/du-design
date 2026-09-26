"""Self-check: python3 tools/test_du.py  (no network, no key needed)"""
import json, subprocess, sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import du

# Search routes needs to the right place.
assert du.find("navbar mega menu")[0]["id"].startswith("principles/patterns/navbars.md")
assert any("slides.md" in h["id"] for h in du.find("one idea per slide", 3))
assert du.find("   ") == [] and du.find("!!!") == []

# Router table rows are individually findable, and read() returns just that row.
row = next(h for h in du.find("brand logo icons", 5) if h["id"].startswith("sources/ROUTER.md"))
assert "Simple Icons" in du.read(row["id"]) and du.read(row["id"]).count("\n") == 0

# Video inspiration routes to whatships.
assert any("whatships" in du.read(h["id"]) for h in du.find("launch video inspiration", 5))

# Animation needs reach the motion skills, not deck notes.
assert any(h["id"].startswith(("skills/emil", "skills/motion-design", "principles/motion")) for h in du.find("animation easing", 3))

# read() refuses paths outside the repo.
assert du.read("../../etc/passwd:1-5").startswith("no such file")

# Gallery link extraction keeps real sites, drops ads/socials/images, strips ?ref.
md = ("[ Visit Website](https://velt.dev/?ref=navbar.gallery) Velt [Velt](https://velt.dev/) "
      "[x](https://twitter.com/navbargallery) ![](https://cdn.x.com/a.webp) [Home](https://www.navbar.gallery/)")
assert du.site_links(md, "navbar.gallery") == {"https://velt.dev": "Velt"}, du.site_links(md, "navbar.gallery")

# Every gallery source is either a scraped gallery (regex) or a free GitHub source (None).
assert "design-md" in du.SOURCES and du.SOURCES["design-md"][1] is None

# MCP handshake over stdio.
msgs = [{"jsonrpc": "2.0", "id": 1, "method": "initialize", "params": {"protocolVersion": "2025-06-18"}},
        {"jsonrpc": "2.0", "method": "notifications/initialized"},
        {"jsonrpc": "2.0", "id": 2, "method": "tools/list"},
        {"jsonrpc": "2.0", "id": 3, "method": "tools/call", "params": {"name": "find", "arguments": {"query": "cta pricing"}}}]
out = subprocess.run([sys.executable, str(Path(du.__file__)), "serve"], input="\n".join(map(json.dumps, msgs)) + "\n",
                     capture_output=True, text=True, timeout=30).stdout.splitlines()
r = [json.loads(l) for l in out]
assert [x["id"] for x in r] == [1, 2, 3]
assert {t["name"] for t in r[1]["result"]["tools"]} == {"find", "read", "refs"}
assert "ctas.md" in r[2]["result"]["content"][0]["text"]
print("ok")
