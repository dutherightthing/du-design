# Navbar patterns

Distilled judgment on site navigation. Read alongside [`../web.md`](../web.md). For live examples or current token extraction, scrape **navbar.gallery** (see [`../../sources/ROUTER.md`](../../sources/ROUTER.md); type subpaths listed below).

*Last distilled: 2026-09-19, from navbar.gallery.*

## Pick the type from the site's job

navbar.gallery taxonomizes navigation into these types. Match the site's actual need — don't default to a mega menu because it looks impressive.

| Type | Subpath | Use when | Watch out for |
|---|---|---|---|
| **Static / sticky** | `/type/static` | Small site, few destinations (marketing site, portfolio, docs landing). The default — reach here first. | Sticky that eats vertical space on mobile; shrink or hide-on-scroll-down. |
| **Dropdown / flyout** | `/type/dropdowns` | A handful of sections each with 2–6 children. | Hover-only triggers (dead on touch); flyouts that vanish before the cursor arrives. Add intent delay / bridge the gap. |
| **Mega menu** | `/type/mega-menu` | Genuinely large IA — many products, categories, resources — that needs grouping and visual hierarchy in one panel. | Using it to hide a thin IA. If you have 5 links, you don't need one. |
| **Side bar** | `/type/side-bar` | App shells, dashboards, docs with deep hierarchy. Vertical space for many persistent items. | Fixed sidebars crushing content width on laptops; make it collapsible. |
| **Search bar (in nav)** | `/type/search-bar` | Content-heavy sites where find-by-typing beats browsing (docs, stores, large blogs). | Search as decoration. If it's prominent it must actually work well (keyboard shortcut, good results). |
| **Announcement bar** | `/type/announcement` | One time-boxed message (launch, sale, notice) above the nav. | Permanent "announcement" bars — they become banner-blind furniture. Make them dismissible. |
| **Full-screen menu** | `/type/full-screen` | Editorial / agency / portfolio sites making the menu a designed moment; mobile overlay menus. | Desktop full-screen menus that add a click for no reason. Earn the drama. |
| **Breadcrumbs** | `/type/breadcrumbs` | *Secondary* nav for deep hierarchies (docs, e-commerce categories) — orientation, not primary nav. | Breadcrumbs on flat sites; treating them as the main nav. |

Also tagged on the source: progress bars (reading progress on long articles) and tabs (section switching within a page/app).

## What separates a good navbar from a generic one

- **The IA drives the type, not the reverse.** A thin site with a mega menu reads as overbuilt; a deep product site with five flat links reads as lost. Count the real destinations first.
- **One clear primary action.** The nav's CTA (Sign up / Get started / Contact) is visually distinct from wayfinding links — a filled button among text links, not one more link in the row.
- **Reduce, don't relocate.** The best fix for a crowded nav is fewer top-level items, not a bigger dropdown. Group ruthlessly.
- **State is legible.** Current section is obviously marked; hover/focus is unmistakable; the active trail shows in breadcrumbs/sidebars.
- **Mobile is a real design, not a hamburger afterthought.** Decide deliberately: collapse to a sheet, a full-screen overlay, or a bottom bar. Keep the primary CTA reachable.
- **Scroll behavior is intentional.** Shrink-on-scroll, hide-on-scroll-down/show-on-up, or plain sticky — pick one on purpose; don't ship a jittery half-implementation.

## Anti-patterns

- Mega menu masking a thin IA.
- Hover-only dropdowns with no touch/keyboard path.
- Sticky/announcement stacks that consume a third of a phone screen before content.
- A nav where the CTA is indistinguishable from the links.
- Full-screen menu drama on a plain marketing site that needed four links.

## Exemplars to go look at (verify — sites redesign)

Real mega-menu examples observed on navbar.gallery at distill time: **Cloudflare, Asana, Mistral, Frontify, Featurebase, Consensys, Velt**. These are starting points — screenshot the live site (or run `design-dna`) rather than trusting this list blindly.

## Retrieval reminder

navbar.gallery is egress-blocked → use the Orthogonal scrape recipe in the router. Index markdown is ~$0.005; screenshot a shortlisted site for ~$0.01. Pagination uses a **dynamic** `?<token>_page=N` query param (the token changes per response — read it off the "Load more" link in the scraped markdown, don't hardcode it).
