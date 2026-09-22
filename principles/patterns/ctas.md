# CTA patterns

Distilled judgment on calls-to-action — sections and buttons. Read alongside [`../web.md`](../web.md) ("One primary action per page"). For live examples, scrape **cta.gallery** (see [`../../sources/ROUTER.md`](../../sources/ROUTER.md); categories below).

*Last distilled: 2026-09-19, from cta.gallery.*

## Pick by intent

cta.gallery sorts CTAs by what you're asking the user to do. Name the intent first — the copy and design follow from it.

| Intent | Category | Typical ask | Notes |
|---|---|---|---|
| **Button** | `/categories/button` | The atomic CTA — one decisive action. | Label the outcome ("Start free trial"), not the mechanic ("Submit"). |
| **Call-to-buy** | `/categories/call-to-buy` | Purchase / start checkout. | High commitment — pair with a risk-reducer (price, guarantee, "no card"). |
| **Download** | `/categories/download` | Get the app / file / asset. | Say what and how big; show the platform (App Store / Play / .dmg). |
| **Form** | `/categories/form` | Capture details (contact, demo, waitlist). | Every extra field costs conversions. Ask only what you'll use. |
| **Modal / pop-up** | `/categories/modal-pop-up` | Interrupt for one focused ask. | Justify the interruption; make dismissal obvious. Timing/trigger matters more than the design. |
| **Navigation** | `/categories/navigation` | Push toward the next step (nav CTA, in-page). | The one filled button among links (see [`navbars.md`](navbars.md)). |
| **Newsletter** | `/categories/newsletter` | Subscribe. | Sell the value ("what you'll get, how often"), not the act of subscribing. |
| **Pricing / subscription** | `/categories/pricing` | Choose a plan. | The CTA is the whole pricing card's job — one recommended plan visually led. |

## What makes a CTA convert (and not read as generic)

- **Verb + outcome, first person if it fits.** "Get my report" beats "Submit." The label states what happens next.
- **One primary CTA per view.** Everything else (secondary link, "learn more") is visually quieter. Competing equal-weight buttons kill the decision — this is the web.md rule made concrete.
- **Reduce friction at the ask.** Fewer form fields; "no credit card required"; social proof or a guarantee sitting right next to a high-commitment button.
- **Contrast earns the click.** The primary CTA is the highest-contrast interactive element in its section — not lost in a field of same-weight buttons or low-contrast against the background (still WCAG AA).
- **Context sells the click.** The strongest CTA sections pair the button with the single most relevant proof or benefit line, not a generic "Ready to get started?".
- **Placement matches commitment.** Low-commitment asks (newsletter) can be inline/persistent; high-commitment asks (buy, demo) earn a dedicated, well-supported section.

## Anti-patterns

- "Submit" / "Click here" / "Learn more" as a primary CTA label.
- Two or three equal-weight buttons competing for the same click.
- A high-commitment ask (buy, long form) with zero risk reduction beside it.
- Pop-ups that fire on load with a hidden or hostile close.
- A CTA section whose supporting copy is a generic "Ready to get started?" with nothing specific.

## Retrieval reminder

cta.gallery is egress-blocked → use the Orthogonal scrape recipe in the router (index markdown ~$0.005; screenshot a specific `/cta/<slug>` for ~$0.01). It's Framer-hosted; individual entries live at `/cta/<slug>` and category indexes at `/categories/<name>`. Note the site itself curates conversion-oriented copy tips under `/cta-tips` if you want more depth on wording.
