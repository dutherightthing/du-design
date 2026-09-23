# du-design lookup (MCP + CLI)

Lets any agent find the right principle, pattern, skill section, or gallery site in one or two calls instead of browsing the repo. Plain Python 3, nothing to install.

| Tool | What it returns |
|---|---|
| `find(query, brief?)` | Top matching **sections** (id, heading, snippet). With `brief` + a TypeSafe key, Jev reranks by fit to the project. |
| `read(id)` | Just that section's text. |
| `refs(query, source?, brief?)` | Live example sites from the cached galleries (navbar.gallery, cta.gallery, landing.love, saaspo), matched on category tags. Source `design-md` returns ready DESIGN.md files for ~74 real brands, matched on a description of their look. |

No MCP? Same thing from a shell: `python3 tools/du.py find "navbar mega menu"`. No shell? Read [`../INDEX.md`](../INDEX.md).

## Connect it

Claude Code (all projects):
```bash
claude mcp add -s user du-design -- python3 /Users/jerrydu/du-design/tools/du.py serve
```
Inside this repo, `.mcp.json` already registers it.

Codex (`~/.codex/config.toml`):
```toml
[mcp_servers.du-design]
command = "python3"
args = ["/Users/jerrydu/du-design/tools/du.py", "serve"]
```

Cursor / Windsurf / others (`mcpServers` JSON):
```json
{ "du-design": { "command": "python3", "args": ["/Users/jerrydu/du-design/tools/du.py", "serve"] } }
```

For Awwwards award-tier sites, add the separate [awwwards-mcp](https://github.com/INSANE0777/Awwards-mcp) next to this one (`npx -y awwwards-mcp`); don't rebuild it here.

## Upkeep

- `python3 tools/du.py index` — regenerate `INDEX.md` after adding or editing library files.
- `python3 tools/du.py refresh [source]` — re-scrape the galleries into `.cache/refs.db` (gitignored; never commit scraped content). Galleries use the `orth` CLI at about $0.005 per page (around $0.85 and 7 minutes for all four; monthly is plenty). `refresh design-md` is free (plain GitHub). `refs` reports how old the cache is.
- Jev rerank: put `TYPESAFE_API_KEY=...` in `.env.local` at the repo root (gitignored). Cost is about $0.04 per million input tokens, so a rerank is a fraction of a cent. With no key, `find` just skips the rerank.
- `python3 tools/test_du.py` — self-check (offline).
- To add a gallery: add a line to `SOURCES` in `du.py` (home URL + regex for its category pages) and a row in `sources/ROUTER.md`.
