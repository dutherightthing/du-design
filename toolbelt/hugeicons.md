# Hugeicons — UI icon library

**What:** A large, consistent icon set for interface glyphs (arrows, settings, media, commerce, etc.) in multiple styles (stroke, solid, duotone, twotone, bulk). React/Vue/other packages plus SVG/font exports.

**Use it when:** a project needs a coherent set of **interface icons** with one visual voice. Pick one style family and stick to it across the whole UI — mixing icon styles is an instant tell of a rushed job.

**For brand/company logos** (GitHub, Google, X…), use [super-tiny-icons](super-tiny-icons.md) instead — Hugeicons is for functional UI glyphs, not third-party logos.

**Install (per project) — free tier:**
```bash
npm i @hugeicons/react @hugeicons/core-free-icons   # free MIT icons
```
```jsx
import { HugeiconsIcon } from "@hugeicons/react";
import { Home01Icon } from "@hugeicons/core-free-icons";
<HugeiconsIcon icon={Home01Icon} size={20} strokeWidth={1.5} />
```
(The older `hugeicons-react` package also exists; the `@hugeicons/*` split above is the current free packaging.)

**Access note:** `hugeicons.com` (browsing/search) is currently **blocked by the network egress policy** — the npm package installs fine, but you can't browse the catalog directly. Find an icon name from the package's exports or scrape the site's icon index via the [sources router](../sources/ROUTER.md) recipe.

**License & pricing (verified 2026-09-19 on hugeicons.com):** two tiers — Jerry's free/paid + login hunch is right here.
- **Free — 6,000+ Stroke Rounded icons, MIT License** (`@hugeicons/core-free-icons`). Use, modify, and **redistribute** anywhere, personal or commercial, no seat / key / account — just keep the MIT copyright notice in the source. This is the tier to default to. ⚠️ **Correction from the earlier draft:** the free license is **MIT, not "CC-style/attribution."**
- **Pro — 60,000+ icons in 10 styles**, behind login + purchase, **per-seat**: Pro **$99/yr** per seat, or Pro Plus **$1,197 one-time** per seat. Each person who directly uses the Pro files needs a seat; end-users of your product don't. Pro source files may **not** be redistributed. Only reach for Pro if the free 6k set genuinely lacks the glyph/style.

The `?via=` referral param Jerry shared is an affiliate link, not required for use.

**Pairs with:** [shadcn/ui](shadcn.md). Size/stroke to match the type scale — see [`../principles/typography.md`](../principles/typography.md).
