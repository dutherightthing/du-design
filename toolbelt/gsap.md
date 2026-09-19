# GSAP — web animation engine

**What:** The industry-standard JS animation library. Precise timelines, tweens, and plugins (ScrollTrigger, Flip, SplitText, MotionPath). Framework-agnostic (vanilla, React, Vue, Svelte). As of 2025 the full plugin suite is free.

**Use it when:** animating an **interactive website/app** — scroll-driven reveals, sequenced timelines, hero animations, complex micro-interactions. NOT for producing standalone video files (use [HyperFrames](hyperframes.md) for that; though HyperFrames uses GSAP internally as its default adapter).

**Pairs with:** [Lenis](lenis.md) for smooth scroll feeding ScrollTrigger; [three.js](three.md) for animating 3D.

**Install:**
```bash
npm i gsap
```

**Sketch (timeline + scroll):**
```js
import gsap from 'gsap';
import { ScrollTrigger } from 'gsap/ScrollTrigger';
gsap.registerPlugin(ScrollTrigger);

gsap.timeline({ defaults: { ease: 'power3.out', duration: 0.6 } })
  .from('.title', { y: 40, opacity: 0 })
  .from('.sub', { y: 20, opacity: 0 }, '-=0.3')      // overlap
  .from('.card', { y: 24, opacity: 0, stagger: 0.08 }, '-=0.2'); // stagger group

gsap.from('.reveal', {
  scrollTrigger: { trigger: '.reveal', start: 'top 80%' },
  y: 60, opacity: 0, duration: 0.8, ease: 'power2.out'
});
```

**Direction:** ease-out for entrances, stagger groups ~40–100ms, keep durations snappy. See [`../principles/motion.md`](../principles/motion.md). Respect `prefers-reduced-motion`.
