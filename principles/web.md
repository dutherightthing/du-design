# Website & app principles

For landing pages, marketing sites, and web apps. Read alongside [`universal.md`](universal.md), [`typography.md`](typography.md), [`color.md`](color.md), and [`motion.md`](motion.md) for animation.

## Structure
- **Above the fold earns the scroll.** One clear headline (the value, not the feature list), one supporting line, one primary CTA. Not five competing calls to action.
- **One primary action per page.** Secondary actions are visually quieter. Don't make everything a button.
- Establish a rhythm of sections: each does one job (hook → proof → detail → CTA). Vary layout so it doesn't feel like a stack of identical bands.

## Layout & spacing
- Use a consistent spacing scale (e.g. 4/8px base). Generous, consistent padding reads as premium.
- Constrain content width for readability (~60–75 characters per line for body text).
- Align to a grid. Break the grid deliberately for a focal moment, never by accident.

## The anti-generic mandate
Reject the default template unless there's a real reason: centered hero + 3 feature cards + gradient + generic illustration. If you're building that, stop and reach for the **taste** skill and design-dna. Distinct beats safe.

## Components
- **shadcn/ui** for accessible, unstyled-then-themed primitives (buttons, dialogs, forms). See [`../toolbelt/shadcn.md`](../toolbelt/shadcn.md). Theme it to the brief — don't ship the default look.
- **react-bits** for animated, characterful components/backgrounds. See [`../toolbelt/react-bits.md`](../toolbelt/react-bits.md). Use as accents, not everywhere.

## Motion on the web
- Smooth scroll via **Lenis**; scroll-driven reveals via **GSAP ScrollTrigger**. See [`../toolbelt/lenis.md`](../toolbelt/lenis.md), [`../toolbelt/gsap.md`](../toolbelt/gsap.md).
- 3D via **three.js** when it earns its weight (performance + purpose). See [`../toolbelt/three.md`](../toolbelt/three.md).
- Keep it subtle and purposeful; respect `prefers-reduced-motion`.

## Responsive & accessible
- Design mobile-first; verify at phone width — no horizontal scroll, comfortable tap targets, 16px+ side gutters.
- Sufficient color contrast (WCAG AA). Don't rely on color alone to convey meaning.
- Real, semantic HTML; keyboard-navigable; visible focus states.

## Performance
- Optimize images (right format/size). Lazy-load below the fold.
- Don't ship a heavy 3D scene or huge animation library for a decorative flourish.
