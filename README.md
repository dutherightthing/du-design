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

## Installing into a project

This repo is the single source of truth. Projects consume it — improvements here propagate everywhere.

**Point the agent at this library** (choose one):
- **As a submodule (recommended):** `git submodule add https://github.com/dutherightthing/du-design.git design/` inside a project, then tell the agent to read `design/AGENTS.md` first.
- **Ad hoc:** clone it and tell the agent "read /path/to/du-design/AGENTS.md before starting."

**Then install the referenced external skills, per project** (the chosen approach — always current, one setup step per new project):
```bash
npx skills add Leonxlnx/taste-skill zanwei/design-dna LottieFiles/motion-design-skill alchaincyf/huashu-design
```
These install into `.claude/skills/` (or `~/.claude/skills/` for all projects) and persist across sessions and sequential agents. The HyperFrames / motion skills are already present in Jerry's environment. See [`skills/README.md`](skills/README.md).
