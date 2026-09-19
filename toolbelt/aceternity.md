# Aceternity UI — animated React components

**What:** A large library of ready-made, heavily animated React components — hero sections, animated backgrounds, cards, text effects, scroll interactions. Built on **React + Tailwind + Motion (Framer Motion)**. Copy-paste / CLI, you own the code.

**Use it when:** a React/Tailwind site needs a high-impact animated section fast — an eye-catching hero, an animated background, a scroll-driven reveal — and hand-building it would burn the budget.

**Use sparingly:** these are showpieces. One hero effect elevates; a page stacked with them looks like a demo reel and tanks performance. Pick effects that serve the brief's tone, then tune timing/easing to match — the defaults are recognizable. Run the **taste** skill and check motion against [`../skills/emil/`](../skills/emil/) (`review-animations`) after dropping one in.

**Access note:** the site (`ui.aceternity.com`) is currently **blocked by the network egress policy** — you can't browse it directly. To see what's available, either work from a component name you already know, or scrape the components index via the [sources router](../sources/ROUTER.md) Orthogonal recipe. Installing into a project still works (npm/registry are allow-listed).

**Install (per project):**
```bash
# needs tailwind + motion in the project first
npm i motion clsx tailwind-merge
npx shadcn@latest add "https://ui.aceternity.com/registry/<component>.json"
```
(Many components are also plain copy-paste from the site.)

**Pairs with:** [shadcn/ui](shadcn.md) for structural primitives, [react-bits](react-bits.md) for smaller animated accents, [GSAP](gsap.md)/[Lenis](lenis.md) for custom/scroll motion. Tone guidance in [`../principles/motion.md`](../principles/motion.md).

**License:** free / open components (MIT). *Believed accurate — re-verify on the site's license/pricing page, since it wasn't reachable to confirm at vendoring time.*
