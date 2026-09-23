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

## 2026-09-23 — du-design lookup MCP + INDEX.md (meta)
- Built `tools/du.py`, a stdlib-only tool that works as an MCP server or from the shell. `find`/`read` return a single section instead of a whole file. `refs` searches a local cache of navbar.gallery, cta.gallery, landing.love and saaspo (gitignored `.cache/`). Jev reranks `find` results when a brief is passed and `TYPESAFE_API_KEY` is in `.env.local`. Also generated `INDEX.md`, a ~2K-token map with line ranges for big files.
- Why: the repo is only ~280K tokens, but agents read whole files (taste-skill alone is ~22K) and re-scraped galleries every project. The real references live off-repo, so the cache matters more than the repo search.
- Refero Styles was rejected: its robots.txt blocks AI crawlers and its MCP is paid, which Jerry said no to. Replaced it with awesome-design-md (MIT, 74 brand DESIGN.md files, free GitHub fetch), cached as `refs` source `design-md` and searchable by look.
- Promoted to profile (Jerry confirmed): "real brand marks, not stand-ins" and "calm chrome, one loud focal element", each seen in moneymaker and jev-selector. Awwwards is left to the existing awwwards-mcp rather than rebuilt here.

## 2026-09-22 — Jev selector fluid API discovery (website)
- Chosen direction: warm light search surface with real API marks behaving as a physics pile, then resolving into an upright comparison carousel and endpoint/code detail view.
- What changed from the first proposal: removed masking, symmetry, generic icon tiles, duplicate marks, excessive force, rotated results, stale resize geometry, and lingering faded state; motion became one clear transition from discovery to comparison.
- Preference learned (if any): candidate — Jerry likes responsive, game-like object motion inside otherwise minimal product UI. One project only, so this is documented in `references/your-past-work/jev-selector-fluid-api-discovery.md` and not promoted to the standing profile.

## 2026-09-21 — orth-moneymaker wheel spinner, round 4 (website)
- Chosen direction: added a light theme (same chrome, palette flips via CSS variables) and a generic icon library for user-created segments — the 8 fetched brand logos stay as-is, but new generic options (dollar, briefcase, star, etc.) are a plain emoji centered on a neutral badge rather than sourced/hand-drawn art.
- What changed from the first proposal: round 3 established "the wheel is the colorful focal element, restraint governs the chrome around it, not the wheel itself" — this round's light theme confirms that split cleanly: only chrome tokens (bg/card/ink/surface) flip with theme, the wheel's saturated per-segment colors stay theme-invariant. Also: the earlier hard rule about brand logos ("must be the real, recognizable mark," which cost 3 failed attempts on Shopify) doesn't apply to generic/non-brand icon needs — an emoji badge is legible and sufficient there, no equivalent bar to clear.
- Preference learned (if any): candidate — "a real/pixel-perfect logo is only required for actual brand marks; generic conceptual icons (dollar sign, star, briefcase) can be a plain emoji-on-badge, no asset hunt needed." One project so far; needs a second to confirm before promoting. The chrome-vs-focal-element split (round 3) got a second data point here (light theme) but still needs a second *project*, not just a second round, to promote per the gate.

## 2026-09-21 — orth-moneymaker wheel spinner, round 3 (website)
- Chosen direction: removed the wheel's colored border ring entirely, gave the 8 wedges 8 distinct colors (no alternating 2-tone pattern), and stripped every thick colored border from the surrounding UI (button, hub, panel, result card) in favor of soft shadows and solid white/neutral fills — closer to Apple/Claude chrome, with the wheel itself as the colorful focal point.
- What changed from the first proposal: round 2's "restraint reads as quality" fix (from color.md) over-applied minimalism to the wheel's own color variety, cutting it down to a 2-tone alternating pattern. Jerry's correction: restraint belongs on the UI chrome (borders, glow, gradients) — the wheel itself is the fun/colorful centerpiece and should look like the original multi-color reference images he'd shared, not a muted 2-tone pie.
- Preference learned (if any): candidate — "a colorful decorative focal element (the wheel) and the minimal UI chrome around it (buttons, panels, borders) are different design surfaces; color.md's restraint principle governs the chrome, not necessarily the focal element." Needs a second project to confirm before promoting; logged here so future work on a similarly-structured project (bold focal piece + minimal shell) doesn't over-apply restraint to the wrong layer.

## 2026-09-21 — orth-moneymaker wheel spinner, round 2 (website)
- Chosen direction: "Cobalt Premium" — near-black background, cobalt-blue/near-black alternating wedges, one blue accent reserved for rim/seams/button/title. Picked by Jerry from 3 options after he called the gold-casino-roulette v1 "stupid and cheap."
- What changed from the first proposal: v1 spent the gold accent everywhere at once (rim, seams, glowing button, glowing title, poker-chip hub) — the opposite of color.md's "accent earns attention because it's rare." Dispatched a subagent to research real premium dark-UI references (DraftKings/Linear/Vercel-style) instead of guessing a second palette myself, then used AskUserQuestion to let Jerry pick from 3 named, hex-specified options before touching code.
- Preference learned (if any): confirms the existing process rule (universal.md: "propose directions, don't guess one") rather than adding a new one — this is the first project where skipping it drew a direct complaint, worth watching if it recurs. Not promoted as a new item.

## 2026-09-21 — orth-moneymaker wheel spinner (website)
- Chosen direction: casino/poker roulette look — alternating red/black wedges with gold hairline seams and rim, poker-chip center hub, gold-gradient glowing title and spin button, dark green felt background. Replaced an initial pastel flat-color wheel after Jerry called it out as too soft.
- What changed from the first proposal: v1 used abstract single-color icon-free wedges with muted pastel colors and made-up category names. Jerry wanted real, recognizable brand logos (Meta, TikTok, Instagram, Amazon, Google Maps, Gmail, LinkedIn, Shopify — fetched from Wikimedia Commons) on every segment, two-word labels matching real money-making plays, and saturated casino-vivid colors, not pastel.
- Preference learned (if any): not yet promoted — single project. Candidate: "for playful/marketing-facing tools aimed at a social audience, prefer real recognizable brand logos over abstract icons, and saturated/thematic color palettes over soft pastels." Needs a second project to confirm before promoting to your-profile.md.

## 2026-09-19 — verified license/pricing facts (meta)
- Verified the three "believed, unverified" flags by scraping the live pages (Orthogonal, ~$0.025 total). Results:
  - **Hugeicons**: earlier guess was **wrong** — free tier is **MIT** (6,000+ Stroke Rounded, `@hugeicons/core-free-icons`, redistributable, no attribution-in-UI), not "CC-style/attribution." Pro = 60k+ icons, paid **per-seat** ($99/yr or $1,197 lifetime). Card corrected; install line updated to current `@hugeicons/*` packaging.
  - **Aceternity UI**: earlier "free/open MIT" was **overstated** — the published licence page governs *paid Pro* items (Blocks/Templates, $199 lifetime / $169 yr / $1590 team, login required); free single Components are copy-paste but carry **no explicit MIT/open-source license** on-site. Card corrected to stop calling them MIT.
  - **component.gallery**: fully **free, no login**; it's a *reference* collection of components from real design systems (naming/patterns), explicitly **not** ready-to-use code. No correction needed; noted as free.
- Confirmed Jerry's free/paid hunch and added a "Free vs. paid / login-gated" section to the router so agents default to free tiers and don't try to reach gated content.

## 2026-09-19 — distilled pattern notes, POC (meta)
- Added `principles/patterns/` with `navbars.md` + `ctas.md`, distilled from real navbar.gallery + cta.gallery scrapes (~$0.01 total via Orthogonal). Taxonomy/categories are the sources'; the judgment (when-to-use, anti-patterns, exemplars) is ours. Router now routes navbar/CTA needs to the note first, scrape second ("note, then scrape").
- POC finding: a distilled note beats a live scrape for *judgment* (which variant, what's generic, what to avoid) at zero cost/context; the scrape still wins for *seeing* current examples + token extraction. Notes carry a distill date + the source subpath so they can be refreshed when exemplars go stale. So the two are complementary, not either/or — the note makes any follow-up scrape cheaper and targeted.
- Fixed router bugs found by actually scraping: navbar.gallery pagination token is dynamic (was hardcoded `d25fafcb`), and cta.gallery uses `/categories/<name>` subpaths (were undocumented). Also corrected the Orthogonal `use` call shape: params go in a flat `params` object, not a `body` string.

## 2026-09-19 — external sources + retrieval routing (meta)
- Added `sources/ROUTER.md`: a need→source→retrieval dispatch table so agents auto-select where to look (navbar/landing/SaaS/CTA/rebrand/styles/components/icons/motion) instead of being told a site. Goal: make retrieval deterministic, free the agent's effort for execution.
- Access reality: GitHub sources fetch directly; the inspiration galleries + aceternity/refero/component.gallery/hugeicons are blocked by the network egress policy. Reachable via Orthogonal `ScrapeGraphAI` (verified on navbar.gallery, ~$0.005 markdown / $0.01 screenshot). Recipe documented in the router.
- Vendored (MIT) the taste-relevant core of `emilkowalski/skills` → `skills/emil/` (emil-design-eng, animate, review-animations); rest left upstream.
- New toolbelt cards: `aceternity.md`, `hugeicons.md`, `super-tiny-icons.md`.
- Decision: don't mirror gallery contents into the repo (bloat + copyright) — fetch at build time; only our own distilled pattern notes belong in-repo (future `principles/patterns/`).

## 2026-09-18 — du-design library itself (meta)
- Set up the central design library: router (AGENTS.md), intake skill, principles (universal/slides/motion/web/typography/color), toolbelt cards, skills index, profile.
- Decisions: skills-as-markdown format; HyperFrames as default video engine; design-dna uses the browser for reference extraction with fallbacks; no data/enrichment APIs for design; library learns via profile + this log.
