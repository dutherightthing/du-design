# du-design

A central design library for Jerry's creative projects — websites, videos/motion, slide decks, and static graphics.

Its job: make any AI agent (Claude, ChatGPT/Codex, Cursor, Copilot) behave like a professional graphic designer and visual storyteller — one that asks the right questions, proposes real directions instead of generic defaults, and gets better at knowing Jerry's taste over time.

## Why this exists

Default agents are bad at design in two specific ways:
1. **No taste** — they reach for the generic (centered hero, three cards, gradient) unless stopped.
2. **No discovery** — they build one guess instead of pulling the vision out of you and showing options.

This library fixes both with encoded judgment + a structured intake process. The code libraries (GSAP, three.js, HyperFrames, etc.) are the easy part and are *indexed*, not copied.

## How an agent should use this

**Start every visual project by reading [`AGENTS.md`](AGENTS.md).** It's the router. In short:

1. Run the **intake skill** ([`00-intake/SKILL.md`](00-intake/SKILL.md)) first — it interviews you and comes back with 2–3 visual directions to react to.
2. Load the **principles** for the medium ([`principles/`](principles/)).
3. Pull tools from the **toolbelt** ([`toolbelt/`](toolbelt/)) as needed — index cards for GSAP, three.js, HyperFrames, Remotion, shadcn, react-bits, Lenis.
4. Use the deeper **skills** ([`skills/`](skills/)) — taste enforcement, design-dna (steal-a-look), motion design, decks.
5. Read [`your-profile.md`](your-profile.md) for standing preferences; write learnings back to it at the end.

## Two layers (don't mix them)

- **The Design Brain** — knowledge & judgment (portable markdown): [`00-intake/`](00-intake/), [`principles/`](principles/), [`skills/`](skills/).
- **The Toolbelt** — pointers to code libraries you pull into projects (not vendored): [`toolbelt/`](toolbelt/).

## Layout

```
du-design/
├── README.md              ← you are here
├── AGENTS.md              ← the router (agents read this first)
├── CLAUDE.md              ← points Claude at AGENTS.md
├── your-profile.md        ← Jerry's standing preferences (grows over time)
├── decisions-log.md       ← dated record of what shipped and why
├── 00-intake/             ← ⭐ the discovery/interview skill — run first
├── principles/            ← cross-project rules by medium
├── skills/                ← deeper skills (taste, design-dna, motion, decks)
├── toolbelt/              ← index cards for code libraries (when to use what)
└── references/            ← moodboards + annotated past work (taste inputs)
```

## Using it — just point an agent at this folder

**No installs, no commands.** Everything the agent needs — the router, the intake skill, the principles, and the vendored design skills (taste, design-dna, motion-design, decks) — lives in this repo as plain markdown. To use it, just say:

> "Read `du-design/AGENTS.md` (or the GitHub repo) before starting, and follow it."

That's the whole setup. The agent reads `AGENTS.md`, which routes it to everything else on demand (progressive disclosure — it only opens the files it needs).

Ways to make the folder available to a project, if you want a local copy alongside your work (optional — an agent with the repo link doesn't need this):
- Clone it: `git clone https://github.com/dutherightthing/du-design.git`, then point the agent at the local path.
- Or add it to a project as a submodule under `design/`.

The HyperFrames / motion engine skills are already present in Jerry's environment. The vendored skills are point-in-time copies — see [`skills/README.md`](skills/README.md) for how to refresh them (rarely needed).
