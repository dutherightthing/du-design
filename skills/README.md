# Skills

Deeper capabilities beyond the principles files. These are **Agent Skills** (SKILL.md format) that we adapt/reference from best-in-class open-source repos. We reference them by install command rather than vendoring copies, so they stay current — except where we fork one to bend it to Jerry's taste.

Install any of these into a project (once) with the skills CLI; they then persist across sessions and agents:

```bash
npx skills add <github-repo>
```

## The roster

### taste — anti-slop enforcement
- **Repo:** `Leonxlnx/taste-skill`
- **Use for:** run against any UI/graphic output to stop generic, boring, "AI slop" results. Encodes layout variance, spacing/type hierarchy, and quality gates. Includes aesthetic variants (soft, brutalist, minimalist).
- **When:** any web/UI/graphic build, especially if output is drifting toward the default template.
- **Install:** `npx skills add Leonxlnx/taste-skill`

### design-dna — steal a look
- **Repo:** `zanwei/design-dna`
- **Use for:** turning a reference (URL, screenshot, image) into measured tokens — color, type, spacing, shape, motion feel — as portable JSON, then reproducing that aesthetic in a new build. Three phases: structure → analyze → generate.
- **Accuracy:** needs to *see* the reference. This environment has a browser pane — navigate + screenshot the URL, then analyze. **Fallback** if no browser / site blocks: paste a screenshot, or give a hex/verbal description (looser match). Its `scripts/` do deterministic color measurement.
- **No external agent or data API required.** (Orthogonal/enrichment APIs don't help design extraction — skip them here.) Optional generate-time booster: an up-to-date-docs MCP for correct library code, with fallback to model knowledge.
- **When:** Jerry says "make it feel like X" or points at something he loves (intake Phase 3).
- **Install:** `npx skills add zanwei/design-dna`

### motion-design — motion direction (philosophy-first)
- **Repo:** `LottieFiles/motion-design-skill`
- **Use for:** strategic motion direction — timing, easing, choreography, emotion-to-motion, narrative — before touching code. Engine-agnostic (CSS, GSAP, Lottie, HyperFrames, Framer Motion). This is the biggest lever on motion *quality*.
- **When:** any video/animation or notable micro-interaction work. Pairs with [`../principles/motion.md`](../principles/motion.md).
- **Install:** `npx skills add LottieFiles/motion-design-skill`

### decks — presentation generation
- **Repo:** `alchaincyf/huashu-design`
- **Use for:** generating high-fidelity decks (HTML + editable PPTX export), interactive prototypes, infographics, and design critiques. Has a "brand asset protocol" that anchors output to real brand colors/type instead of guesses.
- **When:** slide decks and pitch material. Pairs with [`../principles/slides.md`](../principles/slides.md).
- **Install:** `npx skills add alchaincyf/huashu-design`

## Also available in this environment (not installed here)
Depending on the agent/host, these may already be present and are worth using:
- **`dataviz`** — chart/graph/dashboard color and chart-type rules. Use for any data visualization (esp. in decks).
- **`artifact-design` / `artifact-diagramming`** — design fundamentals for building Claude Artifacts and diagrams.
- **HyperFrames skill family** (`hyperframes`, `hyperframes-animation`, `hyperframes-creative`, etc.) — the default video/motion engine; deep and already wired in. See [`../toolbelt/hyperframes.md`](../toolbelt/hyperframes.md).

## Notes on forking
If we adapt a skill to Jerry's taste (e.g. bake his defaults into `taste`), fork it into a subfolder here (e.g. `skills/taste/`) and note the upstream + what we changed, so we can re-sync later.
