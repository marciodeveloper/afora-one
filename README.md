# AforaONE — Global Ecosystem Prototype

**Um só ecossistema, sem fronteiras.**

AforaONE is a global platform concept for Brazilians living abroad. It brings people, businesses, services, opportunities and community together in one connected experience.

This repository contains the first interactive visual prototype of the product, designed for GitHub Pages.

## Product pillars

| Pillar | Purpose |
| --- | --- |
| Marketplace | Buy, sell, donate, discover housing and find services |
| Community | Groups, conversations, local knowledge and belonging |
| Business | Brazilian-owned businesses and independent professionals around the world |
| Opportunities | Jobs, projects and professional connections |
| Afora Media | Guides, information, culture and stories |

## Prototype experience

- Global discovery homepage with country/market context
- Market selector and destination exploration
- Search and category filters for sample listings
- Listing detail modal
- Save/favorite interactions
- Community feed preview
- Business directory preview
- Opportunities list
- Editorial / media cards
- Country-aware PT-BR / EN localization: Brazil defaults to Portuguese; other countries default to English, with a manual language override and detected-country flag
- Responsive desktop, tablet and mobile layouts
- Demonstration sign-up and contact flows

## Brand system

| Token | Value | Usage |
| --- | --- | --- |
| Deep Navy | `#0B1F38` | Primary brand foundation |
| Graphite | `#2C2F35` | Secondary dark neutral |
| Off-white | `#F5F3EA` | Main canvas and light typography |
| Champagne Gold | `#D4AF6B` | Accent, horizon and emphasis |

Typography:
- **Playfair Display** — expressive editorial headlines and wordmark direction
- **DM Sans** — interface, body copy and navigation
- **Manrope** — supporting UI/system typography

The AforaONE symbol is a geometric A with a golden horizon arc. The visual language is premium, contemporary, international and welcoming. It intentionally avoids generic travel iconography.

## Run locally

No build step or package installation is required.

1. Clone the repository.
2. Open `index.html` in a browser, or serve the root folder with any static HTTP server.

Example:

```bash
python -m http.server 8080
```

Then visit `http://localhost:8080`.

## GitHub Pages

The workflow at `.github/workflows/pages.yml` stages and publishes only the public static artifact (`index.html`, `founding-partners.html`, `assets/` and `.nojekyll`) when changes are pushed to `main`.

If Pages has not yet been initialized for this repository, verify that **Settings → Pages → Build and deployment → Source** is set to **GitHub Actions**.

Expected URLs:

- `https://marciodeveloper.github.io/afora-one/`
- `https://marciodeveloper.github.io/afora-one/founding-partners.html`

## Country-aware language and country flag

The static site detects the visitor's country through the IP-to-country endpoint at `https://api.country.is/`:

- Brazil (`BR`) defaults to Brazilian Portuguese (`pt-BR`).
- Every other detected country defaults to English (`en`).
- The country flag and localized country name appear in the header.
- Visitors can manually switch languages; that preference is saved in local storage and takes precedence over automatic detection.
- The detected country code is cached locally for 12 hours to avoid repeated lookups.
- The feature does not request browser GPS permission. It makes an approximate country lookup using the visitor's public IP through the third-party API; the site does not store the IP address.
- If the IP lookup is unavailable, the browser locale region (for example, `en-US` or `pt-BR`) is used as a best-effort fallback.
- Flag images are loaded from FlagCDN; if that image cannot load, a Unicode flag emoji is used as a fallback.

A previous selector mismatch caused the localization routine to stop before country detection could run. Multi-element operations now use the shared `selectAll()` helper, while single-element lookups continue to use `$()`.

## Social sharing preview

The page includes static Open Graph and Twitter Card metadata, plus a 1200 × 630 branded image. This enables link previews on WhatsApp, Facebook, LinkedIn and other platforms that read these metadata tags.

The social preview is intentionally language-neutral in its brand identity and uses the approved Portuguese slogan: **Um só ecossistema, sem fronteiras.** Social crawlers generally read the HTML metadata without executing browser JavaScript, so the share card uses the default Portuguese metadata even when a visitor's browser interface is in English.

The social preview PNG is generated from `assets/aforaone-social-preview.svg` during the GitHub Pages workflow. To generate it locally:

```bash
python -m venv .venv
# Windows: .venv\\Scripts\\activate
# macOS / Linux: source .venv/bin/activate
pip install cairosvg
python scripts/build-social-preview.py
```

## Important: demonstration data

This is a **visual product prototype**, not a production service.

All people, companies, listings, prices, job openings, community posts, activity counts and verification labels shown in the interface are fictional and exist only to demonstrate the experience. No authentication, messaging, payment, database or personal-data submission is connected. Demo forms are simulated in the browser and do not send or persist information.

Images are loaded from Unsplash image CDN URLs. Google Fonts are loaded remotely.

## Next product-design steps

1. Validate the information architecture and the global-market entry point.
2. Refine the listing detail and trust/safety experience.
3. Define the account, profile and publishing flows.
4. Map the five pillars to the existing BRDeals foundation and its multi-market capabilities.
5. Convert the approved visual language into reusable components and design tokens for the production application.

---

**AforaONE**  
*Um só ecossistema, sem fronteiras.*


## Cinematic hero video

The hero keeps its original AforaONE orbital composition and adds a restrained, documentary-style people-and-city video layer behind it. The footage uses wide and high-angle compositions to avoid close-up facial and limb artifacts; the Deep Navy overlay preserves text contrast and the approved brand palette.

- Desktop: wide 3840 × 2160 city-square clip, 19 seconds, 60 FPS, by Talha Uğuz. The wider framing keeps pedestrians at a natural distance instead of emphasizing close-up faces and limbs.
  Source: https://www.pexels.com/video/bustling-city-square-with-people-walking-34547986/
- Mobile: portrait 2160 × 3840 high-angle urban-square clip, 9 seconds, 30 FPS, by Shruthi Pradeep. The elevated framing keeps people in context and avoids close-up motion artifacts on narrow screens.
  Source: https://www.pexels.com/video/aerial-view-of-busy-urban-square-with-crowd-37439457/
- Both clips are streamed from the Pexels CDN; they are not copied into this repository. The mobile source is portrait-native rather than a crop of the desktop footage.
- The player is muted, inline, and loops without audio. It selects the landscape or portrait source at the 800px breakpoint.
- The still poster remains visible if playback is unavailable. Video playback is skipped for reduced-motion preferences and browsers that advertise data-saving mode.
- The videos are published under the Pexels License. Attribution is not required, but the creators and source pages are documented here. The footage is illustrative and does not imply that depicted people endorse AforaONE.

Pexels license information: https://www.pexels.com/license/
