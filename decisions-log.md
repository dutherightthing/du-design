# Decisions log

The raw, append-only history of what shipped and why — the record behind [`your-profile.md`](your-profile.md). **This is where per-project details live, so the profile can stay lean.** Append one short block per project at capture time (intake Phase 8); newest at top. Keep each entry brief — full artifacts (briefs, mockups, code) stay in each project's own repo, not here. Log contradictions/exceptions here too; they only change the profile if they recur.

Format:
```
## YYYY-MM-DD — <project name> (<medium>)
- Chosen direction: <name — one line>
- What changed from the first proposal: <the useful signal>
- Preference learned (if any): <what got added to your-profile.md>
```

---

## 2026-09-19 — external sources + retrieval routing (meta)
- Added `sources/ROUTER.md`: a need→source→retrieval dispatch table so agents auto-select where to look (navbar/landing/SaaS/CTA/rebrand/styles/components/icons/motion) instead of being told a site. Goal: make retrieval deterministic, free the agent's effort for execution.
- Access reality: GitHub sources fetch directly; the inspiration galleries + aceternity/refero/component.gallery/hugeicons are blocked by the network egress policy. Reachable via Orthogonal `ScrapeGraphAI` (verified on navbar.gallery, ~$0.005 markdown / $0.01 screenshot). Recipe documented in the router.
- Vendored (MIT) the taste-relevant core of `emilkowalski/skills` → `skills/emil/` (emil-design-eng, animate, review-animations); rest left upstream.
- New toolbelt cards: `aceternity.md`, `hugeicons.md`, `super-tiny-icons.md`.
- Decision: don't mirror gallery contents into the repo (bloat + copyright) — fetch at build time; only our own distilled pattern notes belong in-repo (future `principles/patterns/`).

## 2026-09-18 — du-design library itself (meta)
- Set up the central design library: router (AGENTS.md), intake skill, principles (universal/slides/motion/web/typography/color), toolbelt cards, skills index, profile.
- Decisions: skills-as-markdown format; HyperFrames as default video engine; design-dna uses the browser for reference extraction with fallbacks; no data/enrichment APIs for design; library learns via profile + this log.
