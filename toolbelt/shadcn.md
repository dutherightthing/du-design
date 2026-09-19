# shadcn/ui — component primitives

**What:** Not a component *dependency* — a collection of accessible, well-built React components (Radix + Tailwind) you **copy into your project** and own. You style them; there's no library to fight.

**Use it when:** building a React/Tailwind web app or site that needs solid UI primitives — buttons, dialogs, dropdowns, forms, tabs, tables, toasts — with accessibility handled.

**Critical:** theme it to the brief. The default shadcn look is everywhere; shipping it unstyled = generic. Set your palette/radius/type tokens (from the intake `brief.md` / design-dna) so it looks like *this* project, not "another shadcn site." Run the **taste** skill against the result.

**Install (per project):**
```bash
npx shadcn@latest init
npx shadcn@latest add button dialog input
```

**Pairs with:** [react-bits](react-bits.md) for animated accents, [GSAP](gsap.md) for motion. Theming guidance in [`../principles/color.md`](../principles/color.md) + [`../principles/typography.md`](../principles/typography.md).
