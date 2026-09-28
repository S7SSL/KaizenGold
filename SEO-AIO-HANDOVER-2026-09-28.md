# SEO / AEO handover — 28 Sep 2026

Same playbook as ClearLegacy and kianlocks, minus local listings (no Google Business Profile, no address).

## What changed
- **One entity.** Organization `@id https://kaizengold.com/#organization` defined once per page (legalName KAIZEN GOLD LTD, company no. 14518346, Companies House `sameAs`, logo, founding date); articles, About and the knowledge hub reference it by `@id`.
- **Company disclosure** in every footer: trading name, legal name, registered in England & Wales, company number (linked to Companies House). No address published, per owner.
- **Meta hygiene.** All 29 article descriptions cut to ≤160 chars; FAQ and one article title cut to ≤65; homepage now has a canonical (`https://kaizengold.com/`), trailing-slash og:url, `max-snippet:-1` robots meta, og:image + `summary_large_image`, and a `/llms.txt` alternate link.
- **Share image** `assets/og-default.png` (1200×630).
- **Homepage answers.** New "Kaizen Gold at a Glance" section with 4 visible Q&As (matching FAQPage schema) and 6 links into the Knowledge Centre.
- **Claim wording.** Home hero: "We issue banking instruments" → "We coordinate banking instruments". See CLAIMS-REGISTER.md.
- **robots.txt** names the main search and AI crawlers explicitly; disallows `/kyc/` (private portal) and `/gen/` (generator source).
- **Sitemap** lastmod is per page (not one date for everything).
- **llms.txt** gains a company-facts section and a "don't invent figures" line.
- **404.html** (noindex).
- **IndexNow** key file + `gen/indexnow.py`; pinged automatically after each push.
- **CI** `.github/workflows/seo.yml`: fails if generated files are stale or `gen/seo_check.py` finds a problem (title/meta length, h1 count, canonical, JSON-LD parse, placeholders, AggregateRating, hidden FAQ questions, broken links, sitemap coverage).

## How to edit
Content lives in `gen/content/*.py`. Run `python3 gen/build.py && python3 gen/seo_check.py`, then commit everything.
Set `MODIFIED = "YYYY-MM-DD"` in an article module when its content really changes, so dates stay honest.

## Still open (owner)
1. Name the UAE refinery partner and its accreditation, or drop "leading/premier" (claims register).
2. Consider a named expert author (Person schema) for the Knowledge Centre — strongest E-E-A-T signal for a financial-adjacent topic.
3. Add sources to Knowledge Centre articles on the next content pass.
4. The contact form posts to a Formspree placeholder and falls back to email; wire a real endpoint or remove the form.
