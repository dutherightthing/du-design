# SuperTinyIcons — brand/logo SVGs

**What:** ~480 miniscule SVG logos of popular sites, apps, and services (GitHub, Google, X, Discord, languages, tools…). Each averages **under 534 bytes**, on a 512×512 viewbox fitting a circle of r=256. Public repo, licensed for reuse.

**Use it when:** you need recognizable **brand/company logos** — social footer, "sign in with", integration grids, tech-stack strips — at tiny file cost and razor-crisp scaling.

**For functional UI glyphs** (arrows, settings, etc.), use [hugeicons](hugeicons.md) instead.

**Access:** GitHub is allow-listed, so pull directly — no scrape needed.
```bash
# clone the whole set into a project asset folder
git clone --depth 1 https://github.com/edent/SuperTinyIcons

# or grab one icon by name from the CDN / raw GitHub
# https://raw.githubusercontent.com/edent/SuperTinyIcons/master/images/svg/<name>.svg
```
Icons are plain inline-able SVG — drop the markup straight into components; no runtime dep.

**License:** MIT (see the repo's `LICENSE`). Note these reproduce **third-party trademarks**; use logos to *refer to* the real brand (links, integrations), not to imply endorsement or to rebrand.

**Pairs with:** [hugeicons](hugeicons.md) for the rest of the icon system. Keep logo sizing consistent per row; see [`../principles/universal.md`](../principles/universal.md).
