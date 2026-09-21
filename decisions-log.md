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

## 2026-09-18 — du-design library itself (meta)
- Set up the central design library: router (AGENTS.md), intake skill, principles (universal/slides/motion/web/typography/color), toolbelt cards, skills index, profile.
- Decisions: skills-as-markdown format; HyperFrames as default video engine; design-dna uses the browser for reference extraction with fallbacks; no data/enrichment APIs for design; library learns via profile + this log.
