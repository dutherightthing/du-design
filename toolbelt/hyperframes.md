# HyperFrames — default video / motion engine

**What:** HTML-based composition framework for videos, motion graphics, animated decks, and overlays. Deterministic, seek-safe, single paused timeline; renders to MP4 (local, cloud, Lambda, Cloud Run). Already wired into this environment with a deep skill family.

**Use it when:** any video or motion-graphic deliverable — promos, explainers, teasers, title cards, captioned clips, multi-scene pieces, social cuts. **This is Jerry's default** (used for Orthogonal videos); lowest friction to a rendered video.

**Prefer over Remotion unless:** the project is already a React/TS codebase *and* needs heavy programmatic/data-driven generation. Otherwise HyperFrames wins on friction.

**How to work with it:** don't hand-build from scratch — the skill family owns the workflow. Entry point is the **`hyperframes`** skill (mandatory first read for any video task); it routes to:
- `hyperframes-core` — composition contract, timing attributes, tracks
- `hyperframes-animation` — motion rules, blueprints, runtime adapters (GSAP default + Lottie/Three/Anime/CSS/WAAPI/TypeGPU)
- `hyperframes-keyframes` — punch-ins, camera moves, seek-safe keyframes
- `hyperframes-creative` — design spec, palettes, beats, narration
- `hyperframes-audio` — mixing, ducking, effects
- `hyperframes-cli` — init/preview/render/publish
- `hyperframes-registry` — ~400 prebuilt blocks/effects (search BEFORE hand-building a named look: glitch, CRT, film grain, charts, confetti, etc.)
- `media-use` — sourcing/generating BGM, SFX, images, voice, LUTs

**Rule:** for any fresh video, start at the `hyperframes` skill. Search the registry before hand-coding a named effect. Motion quality still comes from [`../principles/motion.md`](../principles/motion.md) + the motion-design skill.
