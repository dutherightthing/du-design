# Sources Router — where to look, and how to retrieve

**Purpose:** so an agent never has to be told "go to craftwork.design." You match the *design need* to a row below, then retrieve using the stated method. This is the **only** place you decide where external inspiration/assets come from — **do not free-search the web** for design references when a row here covers the need.

## How to use this (the deterministic flow)

0. **Try `refs("<need>")` first** (du-design MCP, or `python3 tools/du.py refs "<need>"`). It searches a local cache of navbar.gallery, cta.gallery, landing.love, saaspo (by category) and awesome-design-md (brand design systems, by look), costs nothing, and returns live site URLs. Scrape (below) only when the cache has no hits or is stale.
1. From the brief, name what you actually need right now (a navbar? a landing hero? a color/identity direction? an icon set? motion taste?).
2. Find the matching row in the **dispatch table**. Match on the *Need* keywords.
3. Retrieve by the row's **Access** method:
   - **vendored** → read the file already in this repo (zero cost, no network).
   - **install** → it's a code library; read its `toolbelt/` card, install into the *project*.
   - **direct** → plain GitHub/CDN fetch (allowed through the network policy).
   - **scrape** → the domain is blocked by the network egress policy; retrieve via the **Orthogonal recipe** at the bottom. This is proven to work and cheap.
   - **note, then scrape** → read the in-repo distilled note first (free, in-context); scrape the source only if you still need to see current examples or extract tokens.
4. Galleries return *indexes of other people's live sites*. The usual chain is: **scrape the gallery index → pick 2–3 example site URLs → screenshot or run `design-dna` on those** to extract tokens. The gallery gives you candidates; the extraction gives you the actual look.
5. **Check for a distilled note first.** Some needs already have an in-repo pattern note (our own encoded judgment) under [`../principles/patterns/`](../principles/patterns/) — read it before scraping; it front-loads the judgment so a scrape (if you still need one to *see* current examples or extract tokens) is cheaper and targeted. Notes exist for: navbars ([`patterns/navbars.md`](../principles/patterns/navbars.md)), CTAs ([`patterns/ctas.md`](../principles/patterns/ctas.md)).
6. **Do not commit scraped output into this repo.** Fetch at build time and use it in the project. This keeps the library small and sidesteps copyright on other people's designs. Distilled *pattern notes* (our own words) are the only gallery-derived thing that belongs in-repo — see [`../principles/patterns/`](../principles/patterns/).

## Dispatch table

| Need (match on these) | Source | Access | Notes / retrieval |
|---|---|---|---|
| Overall site look, "what good looks like", award-tier sites | craftwork.design/curated/websites · landing.love | scrape | Broad taste. Scrape index → pick 2–3 → `design-dna` them. |
| Landing page: hero, structure, section flow | landing.love · saaspo.com | scrape | landing.love = landing-page focused; saaspo = SaaS pages. |
| SaaS marketing site patterns (pricing, features, onboarding pages) | saaspo.com | scrape | Browse by page-type / category. |
| Navbar / navigation / header / menu | [`../principles/patterns/navbars.md`](../principles/patterns/navbars.md) → navbar.gallery | note, then scrape | **Read the note first.** Type subpaths: `/type/static`, `/type/dropdowns`, `/type/mega-menu`, `/type/side-bar`, `/type/search-bar`, `/type/announcement`, `/type/full-screen`, `/type/breadcrumbs`. Paginate with `?<token>_page=N` — the token is **dynamic**, read it off the "Load more" link in the scraped markdown (don't hardcode); or use `scrolls`. |
| CTA / conversion section / button copy + layout | [`../principles/patterns/ctas.md`](../principles/patterns/ctas.md) → cta.gallery | note, then scrape | **Read the note first.** Categories: `/categories/button`, `/call-to-buy`, `/download`, `/form`, `/modal-pop-up`, `/navigation`, `/newsletter`, `/pricing`. Entries at `/cta/<slug>`; copy tips at `/cta-tips`. Framer-hosted. |
| Branding, rebrand, visual identity, logo systems | rebrand.gallery | scrape | Identity-level inspiration, not page layout. |
| Real-world UI styles by aesthetic; a ready DESIGN.md (colors, type, spacing, components) from a real brand | awesome-design-md (MIT, ~74 brands: Stripe, Linear, Vercel, Wise, Apple…) via `refs("<look>", source="design-md")` | direct (cached) | Search by look ("lime fintech", "warm editorial serif", "dark developer"); each hit is a raw DESIGN.md URL to fetch into the project. Pass `brief` to rerank. **Not styles.refero.design:** its robots.txt blocks AI crawlers and its MCP is paid, so we don't use it (decided 2026-09-23). |
| Component patterns: naming, variants, states, anatomy (cross–design-system) | component.gallery | scrape | Reference for *how a component should behave/what to call it*, not visual flair. |
| Animated React components to drop in (heroes, backgrounds, text FX) | [`../toolbelt/aceternity.md`](../toolbelt/aceternity.md) · [`../toolbelt/react-bits.md`](../toolbelt/react-bits.md) | install | React + Tailwind + Motion. Seasoning, not the meal — see cards. |
| UI icons (interface glyphs: arrows, settings, etc.) | [`../toolbelt/hugeicons.md`](../toolbelt/hugeicons.md) | install | Large set, free tier + pro. |
| Brand / company / logo icons (GitHub, Google, Shopify, X…) | Simple Icons → [`../toolbelt/super-tiny-icons.md`](../toolbelt/super-tiny-icons.md) → Wikimedia Commons | direct | Try in order. Simple Icons (3,000+ brands, CC0, single-color): `https://cdn.jsdelivr.net/npm/simple-icons@latest/icons/<slug>.svg` (verified 2026-09-23). SuperTinyIcons for full-color rounded marks. Wikimedia only as a last resort. Never ship a placeholder for a real brand. |
| Motion & interaction taste; grade or fix animations | [`../skills/emil/`](../skills/emil/) · [`../skills/motion-design/`](../skills/motion-design/) | vendored | Read in-repo. `emil-design-eng` (philosophy), `animate` (curves/durations), `review-animations` (grading). |
| "Make it feel like <a specific site/image>" | [`../skills/design-dna/`](../skills/design-dna/) | vendored | Extract tokens from a reference. Feed it a gallery pick or a URL Jerry names. |

If a need genuinely isn't covered here, *then* fall back to a web search — and consider adding the good source you find as a new row (see Maintenance).

## Free vs. paid / login-gated (verified 2026-09-19)

Some sources gate their best content behind login or payment. Retrieval still works (scrape/install), but know what you can actually use:

- **Free, no login** — the inspiration galleries (navbar.gallery, cta.gallery, and by design the others), and **component.gallery** (a free reference collection of components from real design systems — for *naming & patterns*, not ready-to-use code; no paywall).
- **Freemium (free tier is enough; paid behind login)** — **Hugeicons**: 6,000+ Stroke Rounded icons are **MIT** (free, redistributable); 60k+ Pro icons are paid per-seat ($99/yr or $1,197 lifetime). Default to the free set. See [`../toolbelt/hugeicons.md`](../toolbelt/hugeicons.md). **Aceternity UI**: single Components are free copy-paste; Blocks + Templates need a paid All-Access account ($199 lifetime / $169 yr). Don't assume a Block/Template is pullable. See [`../toolbelt/aceternity.md`](../toolbelt/aceternity.md).
- **Fully free/open** — **SuperTinyIcons** (MIT, GitHub). See [`../toolbelt/super-tiny-icons.md`](../toolbelt/super-tiny-icons.md).

When scraping a freemium/gallery source, you're pulling the *public* index/preview — enough to shortlist and screenshot. Don't build a login/scrape flow to reach gated content; use the free tier, or install the paid library into the project only if Jerry has an account.

## Orthogonal retrieval recipe (for `scrape` rows)

The blocked domains are reachable through Orthogonal's `ScrapeGraphAI` API (its endpoint is allow-listed, so it tunnels past the egress block). Verified working.

**Tool:** `mcp__orthogonal__use` → `api: "scrapegraphai"`, `path: "/api/scrape"`

**Index / listing (default, cheapest — get names, links, tags):**
```json
{ "url": "https://www.navbar.gallery/type/mega-menu",
  "formats": [{ "type": "markdown", "mode": "normal" }],
  "fetchConfig": { "mode": "js", "wait": 2500 } }
```
→ ~$0.005. `mode: "js"` renders the page; raise `wait` (ms) or add `"scrolls": 5` for lazy-loaded / load-more grids.

**See the design (when you need to actually look):**
```json
{ "url": "<a specific example site>", "formats": [{ "type": "screenshot" }],
  "fetchConfig": { "mode": "js", "wait": 3000 } }
```
→ ~$0.01 per screenshot.

**Extract one site's tokens (palette / fonts / logo):** add `{ "type": "branding" }` → ~$0.125. Use sparingly; overlaps with the `design-dna` skill (prefer design-dna if you can screenshot).

**Cost discipline:** markdown to find candidates, screenshot only the 2–3 you shortlist, branding only when you can't get it any other way. A typical inspiration pull is a few cents.

## Maintenance

- This table is the source of truth for source selection. Adding a source = adding a row (Need keywords, URL, access method, retrieval note). Keep rows one line where possible.
- Blocked-vs-allowed can change with the network policy. If a `direct` fetch starts failing with a 403/egress error, switch that row to `scrape`; if a blocked domain becomes reachable, switch it to `direct`. Re-verify with one cheap fetch before editing.
- Full source detail (license, what each is good/bad at) lives in the `toolbelt/` cards for the install rows and in the gallery's own About page for scrape rows — this router stays terse on purpose.
