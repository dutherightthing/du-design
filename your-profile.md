# Jerry's design profile

Jerry's **durable, cross-project** design preferences. The intake skill reads this **first** and must not re-ask what's settled here.

This file is deliberately **lean** — it is a distilled summary, NOT a project log. Per-project history lives in [`decisions-log.md`](decisions-log.md); full project artifacts (briefs, mockups) stay in each project's own repo.

## Governance — how this file is allowed to change (read before writing to it)

1. **One project = a data point, not a rule.** A single project's choices are logged in `decisions-log.md`. They do **not** get written here. This is what stops any one project from swaying the profile.
2. **Promote to this file only when EITHER:**
   - Jerry states a **standing/general rule** explicitly ("always...", "I never want..."), OR
   - the **same signal shows up across 2+ projects** (a real pattern),
   AND Jerry confirms it at capture time.
3. **Phrase preferences as tendencies with room, not absolutes** — "leans warm, especially on calm briefs," not "always use warm." Absolutes only when Jerry stated one.
4. **Contradictions don't flip the profile.** If a new project contradicts an entry, log it as an *exception* in `decisions-log.md`. Only revise the profile entry if the contradiction recurs (back to rule #2).
5. **Stay lean.** Keep every entry to ~one line. If a section grows past a handful of lines or entries start overlapping, run a **consolidation pass**: merge duplicates, generalize specifics, delete stale/contradicted items. Target: this whole file stays skimmable in well under a screen.
6. **Human-readable and prunable.** No raw dumps. Jerry can delete any entry; treat these as living, not sacred.

_Last updated: 2026-09-23 (promoted two aesthetic tendencies seen in orth-moneymaker + jev-selector)._

## About Jerry
- Non-designer by training; strong instincts, judges design well **when he sees it**, but can't reliably name styles or specify a vision from a blank page. → Always propose options with mockups; don't ask him to articulate a look cold.
- Works on personal projects and Orthogonal (Growth role) content.

## Defaults & tooling
- **Video / motion is his most common and most-cared-about medium.**
- **Default video engine: HyperFrames** (already uses it for Orthogonal videos). Remotion only if a project is React-native + needs programmatic video.
- Also does websites, slide decks, and static graphics (all four mediums in play).
- Packaging preference for this library: **Agent Skills authored as readable markdown**, one central `du-design` repo, installed once per project.

## Aesthetic preferences
- **Real brand marks, not stand-ins.** When a brand/company appears, use its real, crisp logo — no generic icons, placeholders, or low-res favicons. Generic *concepts* (dollar, star) can be simple emoji/badges. _(moneymaker, jev-selector)_
- **Calm chrome, one loud focal element.** Leans restrained on UI chrome (borders, panels, buttons) so one element — a colorful wheel, a physics pile — carries the energy. Restraint rules apply to the chrome, not the focal piece. _(moneymaker, jev-selector)_

## Dislikes / anti-patterns
- Generic "AI slop" defaults (this whole library exists to avoid them).
- Decks that repeat the same idea 3 ways on one slide (headline + body + graphic all restating it). **Say it once.** ← his explicit, strongly-held rule.

## Process preferences
- Wants a **discovery interview + 2–3 directions with mockups** to react to, not one guess.
- Wants the library to **grow and learn his taste over time.**
- Fine with the agent building **rough mockups** at the direction stage (saves build effort later; the winning mockup seeds the build).
- Comfortable adding optional external tools (e.g. up-to-date-docs) as fallbacked options; not interested in bolting on data/enrichment APIs where they don't improve design quality.

## Open questions to resolve through use
- Favored palettes / color temperature?
- Favored type personalities (editorial vs geometric vs playful)?
- Motion taste: how showy vs restrained does he actually land, in practice?
