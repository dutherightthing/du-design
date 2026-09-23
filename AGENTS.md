# AGENTS.md — the router

You are working on a creative/visual project for Jerry. This file tells you how to use the `du-design` library so you behave like a professional designer, not a default code generator. Follow it before you produce anything visual.

## The one rule that matters most

**Do not jump straight to building.** A default agent's failure mode is to take a vague request and immediately produce one generic guess. That is exactly what this library exists to prevent. The sequence is always: **understand → propose directions → get a reaction → then build.**

## Finding things in this library (read first)

Don't browse the folders. Use the **`du-design` MCP**: `find("<need>")` → `read(id)` for library sections, `refs("<category>")` for live gallery sites. Add `brief` to `find` when you have one; Jev then reranks by project fit. No MCP? Run `python3 tools/du.py find "<need>"`. No shell? Read [`INDEX.md`](INDEX.md), then open only the line ranges you need. Setup: [`tools/README.md`](tools/README.md).

## Step-by-step

### 1. Read Jerry's profile first
Read [`your-profile.md`](your-profile.md). It holds standing preferences (favored aesthetics, defaults, things he dislikes, default tools). **Never re-ask something already answered there** — state it as known and move on.

### 2. Run intake
Load and follow [`00-intake/SKILL.md`](00-intake/SKILL.md). It will:
- figure out the medium (website / video-motion / slide deck / static graphic),
- run a short interview (brief → tone sliders → references → constraints),
- play the brief back for confirmation,
- return **2–3 named directions with rough mockups** for Jerry to react to,
- lock the chosen direction into a `brief.md` in the *project* (not this repo).

Pick **quick mode** for small/fast jobs, **full mode** for larger ones (the skill explains the trigger).

### 3. Load the principles for the medium
Read the relevant file(s) in [`principles/`](principles/):
- Always: [`universal.md`](principles/universal.md), [`typography.md`](principles/typography.md), [`color.md`](principles/color.md)
- Websites/apps: [`web.md`](principles/web.md)
- Video/motion: [`motion.md`](principles/motion.md)
- Slide decks: [`slides.md`](principles/slides.md)

### 4. Reach for deeper skills as needed
These are **vendored into this repo** — no install needed, just read the relevant `SKILL.md` under [`skills/`](skills/). See [`skills/README.md`](skills/README.md). Highlights:
- **Taste enforcement** — run against any UI/graphic output to kill generic "slop."
- **design-dna** — when Jerry points at a reference ("make it feel like X"), extract its tokens and reproduce them. Needs a browser to screenshot a URL (this environment has one); falls back to pasted images/hex.
- **motion-design** — philosophy-first motion direction; always relevant for video/animation and micro-interactions. Quality comes from *these principles*, not the engine.
- **emil** — design-engineering craft + correct animation (curves, durations) and a rubric to grade motion; run `review-animations` before calling any interaction done.
- **decks** — presentation generation.

### 5. Pull tools from the toolbelt
See [`toolbelt/`](toolbelt/). These are *index cards* (what a tool is for, when to use it vs alternatives, install line, canonical snippets) — the actual libraries get installed into the project, never copied into this repo. Key routing:
- **Video / motion graphics →** HyperFrames (default). Remotion only if the project is already React and needs programmatic/data-driven video.
- **Interactive website animation →** GSAP (+ Lenis for smooth scroll), three.js for 3D. NOT for producing video files.
- **UI components →** shadcn/ui (structure), react-bits (animated bits).

### 5b. Need external inspiration or assets? Route, don't hunt.
When you need a reference or asset — a navbar to riff on, landing-page structure, a color/identity direction, icons, or motion taste — **go to [`sources/ROUTER.md`](sources/ROUTER.md) and match the need to a row.** It tells you the exact source and how to retrieve it (some inspiration sites are blocked by the network policy and must be pulled via the Orthogonal scrape recipe the router documents). Don't free-search the web when a row covers the need, and don't wait for Jerry to name a site. This is deliberately deterministic: spend your effort on *executing* the brief, not on finding where to look.

### 6. Build the chosen direction
Build from the locked `brief.md` and the winning mockup — the mockup is the *starting asset*, not a throwaway. Re-run taste enforcement before calling it done.

### 7. Capture what you learned
At the end, ask Jerry 1–2 quick questions about what changed from your first proposal, and — only after he confirms — append the takeaway to [`your-profile.md`](your-profile.md) and a dated line to [`decisions-log.md`](decisions-log.md). This is how the library learns. Only write confirmed preferences; keep entries human-readable.

## Guardrails
- Prefer showing over telling: mockups and options beat paragraphs of description.
- When Jerry says "you decide," decide — then state what you chose and why, don't stall.
- Keep this repo (the library) and the project (the deliverable) separate. `brief.md`, generated assets, and code live in the *project*; only learnings flow back here.
