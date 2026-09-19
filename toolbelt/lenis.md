# Lenis — smooth scroll

**What:** Lightweight smooth-scroll library (by darkroom.engineering). Normalizes scroll into a smooth, controllable value — the modern, performant way to do "buttery" scrolling.

**Use it when:** building a website where scroll feel matters (marketing sites, scroll-driven storytelling). Feeds GSAP ScrollTrigger nicely.

**Don't overdo it:** heavy smoothing can feel laggy or disorienting and hurts accessibility. Keep it subtle; never trap or drastically slow the user's scroll. Respect `prefers-reduced-motion` (disable smoothing).

**Install:**
```bash
npm i lenis
```

**Sketch:**
```js
import Lenis from 'lenis';
const lenis = new Lenis({ lerp: 0.1, smoothWheel: true });
function raf(time){ lenis.raf(time); requestAnimationFrame(raf); }
requestAnimationFrame(raf);

// hand scroll position to GSAP ScrollTrigger:
lenis.on('scroll', ScrollTrigger.update);
```

Pairs with [GSAP](gsap.md). See scroll guidance in [`../principles/web.md`](../principles/web.md).
