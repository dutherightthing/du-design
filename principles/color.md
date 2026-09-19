# Color principles

## Build a small, intentional palette
- **One dominant neutral** (background/surface — usually a near-white or near-black, often slightly tinted, rarely pure #fff/#000).
- **One accent** that carries brand identity and attention.
- **A few supporting tones** (a darker/lighter neutral, maybe a secondary accent for special cases).
- **Semantic colors** for UI: success/warning/error/info — muted, not neon.

That's it. A rainbow reads as amateur; restraint reads as designed.

## The accent earns attention because it's rare
Spend the accent on the one thing you want clicked/read. If everything is the accent color, nothing stands out. Most of a good composition is neutral.

## Contrast & accessibility
- Text must hit WCAG AA contrast against its background (4.5:1 body, 3:1 large text). Check it.
- Never rely on color alone to convey meaning (add text/icon/shape) — for colorblind users and legibility.

## Mood (ties to intake sliders)
- **Calm/Serious:** desaturated, cool or neutral tones, low contrast between surfaces.
- **Energetic:** higher saturation, bold accent, stronger contrast.
- **Playful:** brighter, warmer, sometimes unexpected pairings.
- **Premium/Modern:** near-monochrome + one sharp accent; deep darks; subtle tints.
- **Retro:** period palettes (muted earth tones, faded primaries, neon-on-dark for 80s).

## Practical rules
- Tint your neutrals slightly toward the accent's temperature for cohesion (e.g. warm-gray with a warm brand).
- Define colors as tokens (CSS variables / a palette object) so they're consistent and themeable — never hardcode the same hex in ten places.
- **Dark mode:** don't just invert. Use elevated dark surfaces (not pure black), reduce accent saturation slightly, keep contrast in check.
- When matching a reference, use **design-dna** to measure exact colors rather than eyeballing hex.

## Charts & data
Use the `dataviz` skill's palette rules for categorical/sequential/diverging color — chart color has its own constraints (distinguishable, colorblind-safe, consistent across a deck).
