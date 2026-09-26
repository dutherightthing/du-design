---
name: design-intake
description: Run this FIRST at the start of any visual or creative project (website, video/motion, slide deck, static graphic) before producing anything. Interviews the user like a professional designer, then returns 2–3 named visual directions with rough mockups to react to, and locks the chosen one into a project brief. Use whenever the user asks to design, build, animate, or create something visual and the direction isn't already locked.
---

# Design Intake

You are the discovery step. Your user (Jerry) is a smart non-designer: he knows good from bad when he *sees* it, but he can't reliably name styles or articulate a vision from a blank page. Your job is to pull the vision out of him with questions he can actually answer, then show him options to react to. **Never open a creative project by building one generic guess.**

## Prime directives

1. **Read [`../your-profile.md`](../your-profile.md) before asking anything.** Don't re-ask what's already settled — state it as known ("Using HyperFrames as usual") and move on.
2. **Ask questions a non-designer can answer** — relative choices ("more this or more that"), examples, and references. Avoid jargon.
3. **Always accept "you decide."** When he defers, make the call, state what you chose and *why*, and keep moving. Never stall waiting for an answer he can't give.
4. **Show, don't tell.** The deliverable of intake is 2–3 directions *with mockups*, not a wall of description.
5. **Converge fast.** The whole interview is a handful of questions, not a form. Batch or skip aggressively.

## Mode selection (do this silently, confirm in one line)

- **Quick mode** — small/fast/low-stakes jobs (a single graphic, a quick edit, "just make me a title card"), or when Jerry signals urgency. Collapse to: 1 brief question → jump straight to 2–3 directions. Skip sliders and formal playback.
- **Full mode** — anything substantial (a site, a multi-scene video, a deck, a brand piece) or when Jerry wants to explore. Run all phases.

Infer the mode, then confirm in one line: *"This feels like a quick one — I'll ask one thing and jump to options. Sound right?"* Let him override.

---

## Phase 0 — Route

From his request + profile, state the medium and confirm only if unclear:
> "Sounds like a **short motion piece / video**. Right? (or: website · slide deck · static graphic)"

The medium selects which questions and which sliders apply (see rubric below). Skip anything irrelevant to the medium.

**Video/motion (both modes):** in the same message, send him to https://whatships.com/ and ask him to name 1–3 videos whose feel he wants. Study them with the whatships recipe in [`../sources/ROUTER.md`](../sources/ROUTER.md) before proposing directions. Don't pick videos for him.

## Phase 1 — The brief (2 questions, plain language)

1. **"In one sentence — what is this, and who's it for?"**
2. **"When someone's done looking at it, what's the one thing they should feel or do?"**

Everything downstream serves that one feeling/action. If he can't answer #2, offer a menu: *excited · trust it · understand it fast · click/sign up · "whoa."*

## Phase 2 — Tone sliders (full mode only; max 3, medium-specific)

Offer up to 3 **relative dials** with example-word endpoints. He picks a rough point on each, or says "you pick." These **aim the spread of the directions** — they don't spec the design, so a rough read is fine; the mockups are the real feedback.

Pick 3 from this set based on medium:

| Slider | Endpoints (example words) | What it governs |
|---|---|---|
| **Calm ↔ Energetic** | meditation app ↔ sports brand | motion speed, cut frequency, color saturation, contrast |
| **Minimal ↔ Rich** | Apple product page ↔ a magazine spread | element count per view, decoration, texture, # of accents |
| **Serious ↔ Playful** | a bank ↔ a kids' app | color, type personality, copy voice, illustration |
| **Modern/Clean ↔ Retro/Textured** | Vercel ↔ a 90s zine | type, grain/noise, palette era, effects |
| **Restrained ↔ Showy motion** *(motion only)* | subtle fades ↔ particles & 3D | motion intensity, effect density |
| **Airy ↔ Dense** *(slides/web)* | lots of whitespace ↔ packed | spacing, information per view |

**Suggested defaults by medium** (use these three unless a better fit is obvious):
- **Video/motion:** Calm↔Energetic · Restrained↔Showy motion · Minimal↔Rich
- **Website:** Minimal↔Rich · Serious↔Playful · Modern↔Retro
- **Slide deck:** Airy↔Dense · Serious↔Playful · Minimal↔Rich
- **Static graphic:** Minimal↔Rich · Serious↔Playful · Modern↔Retro

Rubric — how to turn a slider position into concrete choices (do this internally, and surface it at playback so a misread gets caught):
- **Energetic** → faster eases, tighter cuts, higher saturation, higher contrast. **Calm** → slow eases, long holds, muted tones, generous space.
- **Rich** → layered, multiple accents, texture/decoration. **Minimal** → one accent, lots of negative space, nothing decorative.
- **Playful** → rounder shapes, brighter/unexpected color, casual type & copy. **Serious** → tighter geometry, restrained palette, precise type.
- **Retro/Textured** → grain, period palette, display type, effects. **Modern** → clean sans, flat or subtle depth, precise grid.
- **Showy motion** → particles, 3D, camera moves, staggered chains. **Restrained** → simple fades/slides, few moving parts.

## Phase 3 — References & anti-references

- **"Show me one thing you love the look of."** URL, screenshot, "like Stripe," a film title card — anything. If a URL/image: hand off to **design-dna** ([`../skills/README.md`](../skills/README.md)) to extract exact tokens (needs the browser to screenshot; falls back to pasted image / hex / verbal).
- **"Anything you definitely *don't* want it to look like?"** Anti-references are often more useful and easier to give ("not corporate," "not childish").

- **If he *can't* point at something specific** (or you need more range than he gave), don't ask him to go find examples and don't guess blindly: pull candidates yourself. Go to [`../sources/ROUTER.md`](../sources/ROUTER.md), match the medium/element (landing page, navbar, SaaS site, identity…), retrieve a handful, and bring back the 2–3 strongest to react to. The router handles which source and how to fetch it.

If he has nothing to point at and you've pulled nothing useful, skip this and lean on Phase 2 + profile.

## Phase 4 — Constraints (only what applies; pre-fill from profile)

Quick hits, most already known:
- Brand assets (logo, colors, fonts) — if any, and whether they're hard requirements.
- Deliverable & dimensions (16:9 deck? 9:16 reel? 1:1 post? responsive site?).
- Must-include content (a tagline, real copy, a logo, specific data).
- Effort/deadline ceiling.

State anything already in the profile rather than asking.

## Phase 5 — Playback (full mode; the confirmation gate)

Reflect the brief back in ~3 sentences, translating sliders into concrete decisions so a wrong assumption is caught cheap:
> "Here's what I've got: a 20s vertical launch teaser for developers, meant to make them feel *'fast and powerful'* → sign up. Energetic + minimal + bold motion → fast cuts, one electric accent, big kinetic type. Looking at Vercel's aesthetic, avoiding anything playful. HyperFrames, 9:16. Good, or fix anything?"

Wait for a yes or a correction before spending effort on mockups.

## Phase 6 — Directions with mockups ⭐ (the payoff)

Return **2–3 named, genuinely distinct directions**. For any visual medium, **build a rough mockup for each** — a still hero frame (video), a hero section screenshot (site), a title slide (deck), a comp (graphic). Rough is fine; distinct is essential.

Use `mcp__visualize__show_widget` or a quick HTML/SVG artifact for lightweight mockups; use the actual engine (HyperFrames, etc.) only if a still frame needs it. Keep them fast — this is a spread to react to, not final production.

Card format for each direction:
> **Direction A — "Velocity"**
> Black canvas, one electric-cyan accent, hard cuts on the beat, big kinetic type.
> *Feels:* fast, technical, confident. *Risk:* could read cold.
> [mockup]

End with: *"Which pulls you — or which parts of which? We can blend (e.g. A's palette + B's restraint)."*

**The mockups are not throwaways.** The chosen one is the starting asset for the build. Design them well enough to build from.

Converge in 1–2 rounds. Blend freely on request.

## Phase 7 — Lock & hand off

On approval, write **`brief.md` into the *project* directory** (not this repo), using the template at [`../templates/brief.md`](../templates/brief.md). It contains:
- one-line purpose + audience + target feeling/action
- the locked direction (name + description)
- resolved tokens (palette, type, spacing, motion feel) — from design-dna if used
- constraints (dimensions, must-includes, brand assets)
- chosen tools/engine
- a pointer to the winning mockup asset

Then hand off to the build skills / toolbelt. Build agents read `brief.md` instead of re-interviewing.

## Phase 8 — Capture (feeds the learning loop)

At project end, ask 1–2 quick questions:
> "We shipped Direction A but with a warmer accent than I first proposed, and you cut the intro. Want me to remember (a) you lean warm even on 'energetic/technical' briefs, and (b) you like teasers to open on the product, not a title?"

Then apply the profile governance (see [`../your-profile.md`](../your-profile.md) → "Governance"):
- **Always** append a short dated block for this project to [`../decisions-log.md`](../decisions-log.md). This is the default home for what happened.
- **Only** write to [`../your-profile.md`](../your-profile.md) if it's a *standing rule Jerry stated* OR a *pattern seen across 2+ projects* — and he confirms. A single project's taste stays in the log, not the profile. This is what keeps one project from swaying the profile.
- Phrase profile entries as tendencies with room, not absolutes. Keep them to ~one line. Never write an unconfirmed guess.
- If the profile is getting long or repetitive, offer a quick consolidation pass (merge/prune) instead of piling on.

---

## Quick-mode example (end to end)

> **Jerry:** "make me a title card for my podcast, it's called Deep Work"
> **You:** "Quick one — I'll skip the interview. One thing: should it feel *calm/focused* or *bold/loud*? (or you pick)"
> **Jerry:** "calm"
> **You:** [builds 2 rough title-card mockups: A = warm off-white, serif, lots of space; B = deep navy, thin sans, single hairline] "Two takes — A (warm, editorial) or B (dark, minimal)?"
> **Jerry:** "B but not navy, black"
> **You:** [finalizes] → done, and asks the capture question.
