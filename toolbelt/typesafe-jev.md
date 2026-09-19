# TypeSafe / Jev — judgment layer (NOT a design generator)

**What it is:** TypeSafe's Jev is a "System One" model that returns **typed judgments + probabilities**, not text or images. You give it state + a question; it returns one of: **Choice** (pick one of a set), **Noul** (probability a condition holds), **Score** (degree along a described dimension). It's "programmable common sense" you call from *code*.

**Read this before reaching for it — it's easy to misuse here.**

## What it will NOT do
- It does **not** generate designs, layouts, copy, mockups, or animations. It can't draw anything.
- It will **not** make websites/slides/videos faster to *build*. That's generative work — Claude's job, not Jev's.
- Do not try to "design with Jev." Wrong tool.

## Where it *could* fit du-design (only if we build actual code/tooling)
1. **Automated taste gate (best fit):** wrap the `taste` principles in a script that asks Jev to **Score** a candidate output against the brief — e.g. "hierarchy clarity," "on-brief tone match," "generic-slop likelihood" — and flag low scores before they reach Jerry. This is the "verify & escalate" pattern. Only worth it once there's a repeatable pipeline, not for one-off manual builds.
2. **Intake routing:** **Choice** over medium / tone / quick-vs-full. Low value — Claude already does this inline; wrapping it is mostly overhead.
3. **Learning-loop hygiene:** **Noul** — "is this a durable preference or a one-off?" before writing to `your-profile.md`.

## Where it actually shines (separate from design)
**Inside the products Jerry builds.** If a project *is* an app that needs to route requests, rank items, extract fields, verify claims, or score something semantically, Jev is an excellent primitive for that feature. That's a product capability, not a design accelerant.

## Verdict
Not wired into this library today. Revisit for the taste-gate (#1) if/when we build a "design linter" or a project pipeline. Meanwhile, treat it as an app-building primitive, not a design tool.

Docs: https://docs.typesafe.ai/llms.txt · skill: `typesafe:typesafe-ai`
