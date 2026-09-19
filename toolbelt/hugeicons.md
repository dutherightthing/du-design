# Hugeicons — UI icon library

**What:** A large, consistent icon set for interface glyphs (arrows, settings, media, commerce, etc.) in multiple styles (stroke, solid, duotone, twotone, bulk). React/Vue/other packages plus SVG/font exports.

**Use it when:** a project needs a coherent set of **interface icons** with one visual voice. Pick one style family and stick to it across the whole UI — mixing icon styles is an instant tell of a rushed job.

**For brand/company logos** (GitHub, Google, X…), use [super-tiny-icons](super-tiny-icons.md) instead — Hugeicons is for functional UI glyphs, not third-party logos.

**Install (per project):**
```bash
npm i hugeicons-react   # React; other framework packages exist
```
```jsx
import { Home01Icon } from "hugeicons-react";
<Home01Icon size={20} strokeWidth={1.5} />
```

**Access note:** `hugeicons.com` (browsing/search) is currently **blocked by the network egress policy** — the npm package installs fine, but you can't browse the catalog directly. Find an icon name from the package's exports or scrape the site's icon index via the [sources router](../sources/ROUTER.md) recipe.

**License:** freemium — a large free set (CC-style, attribution) plus a paid Pro tier with the full library. *Believed accurate; confirm the current free-vs-Pro split and attribution terms on their license page before shipping, since the site wasn't reachable to verify.* The `?via=` referral param Jerry shared is an affiliate link, not required for use.

**Pairs with:** [shadcn/ui](shadcn.md). Size/stroke to match the type scale — see [`../principles/typography.md`](../principles/typography.md).
