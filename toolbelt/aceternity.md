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

**Free vs paid (verified 2026-09-19):** two tiers, and Jerry's hunch is right — some content is free, some is behind login/payment.
- **Free ($0):** the named single **Components** (Aurora Background, Bento Grid, Lamp Effect, Timeline, etc.) — copy-paste, no account. This is what an agent reaches for.
- **Paid (All-Access, login required):** 200+ premium **Blocks** (multi-section: hero/CTA/pricing sections) + 12+ full **Templates**. Pricing: **Lifetime $199 one-time** (most popular), Annual $169/yr, Team $1590. Don't assume you can pull a Block/Template — those need a purchased account.

**License (verified 2026-09-19):** The published [licence page](https://ui.aceternity.com/licence) is the **Aceternity License** governing *paid Pro* items: use in unlimited personal/commercial end products, modify freely, but **no** redistributing/reselling the source and **no** building competing templates/themes. Some items bundle third-party components under their own OSS/CC licenses (flagged per item). ⚠️ **Correction from the earlier draft:** the site does **not** publish an explicit MIT/open-source license for the *free* components — they're free to copy-paste and use, but "MIT" was an unverified guess. Treat the free components as free-to-use, check the individual component page for any third-party license, and don't relabel them MIT in a project.
