# Skills

Deeper capabilities beyond the principles files. **These skills are vendored into this repo** (their knowledge, as markdown) so you never have to install anything — pointing an agent at `du-design` is enough. Read the relevant `SKILL.md` directly.

> Only the *knowledge* (SKILL.md + reference markdown) is vendored. Heavy demo media, scripts, and image assets were intentionally left in the upstream repos to keep this light — see each folder's `UPSTREAM.md` for the source and how to grab those if ever needed.

## The roster

### `taste/` — anti-slop enforcement
- **Upstream:** `Leonxlnx/taste-skill`
- **Use for:** run against any UI/graphic output to stop generic, boring "AI slop." Encodes layout variance, spacing/type hierarchy, quality gates.
- **Files:** [`taste/taste-skill/SKILL.md`](taste/taste-skill/SKILL.md) (primary), plus aesthetic variants: [`minimalist-skill`](taste/minimalist-skill/SKILL.md), [`brutalist-skill`](taste/brutalist-skill/SKILL.md), [`soft-skill`](taste/soft-skill/SKILL.md).
- **When:** any web/UI/graphic build, especially if output drifts toward the default template.

### `design-dna/` — steal a look
- **Upstream:** `zanwei/design-dna`
- **Use for:** turning a reference (URL, screenshot, image) into measured tokens — color, type, spacing, shape, motion feel — then reproducing that aesthetic. Read [`design-dna/SKILL.md`](design-dna/SKILL.md) + [`references/schema.md`](design-dna/references/schema.md), [`references/generation-guide.md`](design-dna/references/generation-guide.md).
- **Accuracy:** needs to *see* the reference. This environment has a browser pane — navigate + screenshot the URL, then analyze. **Fallback:** paste a screenshot, or give a hex/verbal description. (The upstream `scripts/` do deterministic color measurement — left upstream; use only if you need exact-hex precision.)
- **No external agent or data API required.**
- **When:** Jerry says "make it feel like X" (intake Phase 3).

### `motion-design/` — motion direction (philosophy-first)
- **Upstream:** `LottieFiles/motion-design-skill`
- **Use for:** strategic motion direction — timing, easing, choreography, emotion-to-motion, narrative — before code. Engine-agnostic. The biggest lever on motion *quality*. Start at [`motion-design/SKILL.md`](motion-design/SKILL.md); deep dives in `director/`, recipes in `patterns/`, lookups in `reference/`.
- **When:** any video/animation or notable micro-interaction. Pairs with [`../principles/motion.md`](../principles/motion.md).

### `emil/` — design-engineering & motion taste
- **Upstream:** `emilkowalski/skills` (MIT — Emil Kowalski, ex-Vercel/Linear).
- **Use for:** the craft layer — UI polish, component decisions, and *correct* animation (curves, durations, what to animate) plus a rubric to grade motion against. This is taste for interaction, complementary to `taste/` (anti-slop) and `motion-design/` (choreography).
- **Files:** [`emil/emil-design-eng/SKILL.md`](emil/emil-design-eng/SKILL.md) (philosophy), [`emil/animate/SKILL.md`](emil/animate/SKILL.md) + [`RECIPES.md`](emil/animate/RECIPES.md) (build), [`emil/review-animations/SKILL.md`](emil/review-animations/SKILL.md) + [`STANDARDS.md`](emil/review-animations/STANDARDS.md) (grade).
- **When:** any web micro-interaction or animation; run `review-animations` before calling motion done. The other 10 skills in the suite were left upstream — see [`emil/UPSTREAM.md`](emil/UPSTREAM.md).

### `decks/` — presentation generation
- **Upstream:** `alchaincyf/huashu-design`
- **Use for:** high-fidelity decks (HTML + editable PPTX), prototypes, infographics, critiques. Has a "brand asset protocol" that anchors output to real brand colors/type. Start at [`decks/SKILL.md`](decks/SKILL.md); slide `references/` (slide-decks, typography, pptx export, brand-asset-protocol, critique-guide…); video/animation notes were trimmed — use HyperFrames + motion-design + emil.
- **Note:** some references assume upstream `assets/`/`scripts/` (render pipeline, PPTX export) that were left upstream. The *design knowledge* is all here; if you need the actual export tooling, see [`decks/UPSTREAM.md`](decks/UPSTREAM.md).
- **When:** slide decks and pitch material. Pairs with [`../principles/slides.md`](../principles/slides.md).

## Also available in this environment (not vendored)
Depending on the agent/host these may already be present:
- **`dataviz`** — chart/graph/dashboard color and chart-type rules.
- **`artifact-design` / `artifact-diagramming`** — fundamentals for Claude Artifacts and diagrams.
- **HyperFrames skill family** — the default video/motion engine, already wired in. See [`../toolbelt/hyperframes.md`](../toolbelt/hyperframes.md).

## Keeping vendored skills fresh
They're a point-in-time copy. To re-sync one, re-pull its upstream (in each folder's `UPSTREAM.md`) and copy the markdown back over. No rush — design fundamentals don't churn fast.
