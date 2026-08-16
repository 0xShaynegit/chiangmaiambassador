# CMA Full Site Audit — Accuracy, Freshness, SEO Backend, FAQ Relevance

Started: 2026-08-16
Method: page-by-page, no batching. Each page checked for:
1. **Accuracy/freshness** — prices, dates, hours, named venues/hotels, event dates, anything stated as fact
2. **Internal links** — resolve, no dead/orphaned hrefs
3. **Image relevance & alt text** — matches topic, alt present
4. **SEO backend** — title, meta description, canonical, OG/Twitter tags, schema (JSON-LD), heading structure
5. **FAQ relevance** — every FAQ question/answer actually matches this page's topic

Excluded (not live content pages): `.md/*`, `blog-template.html`, `pages/page-template.html`, `_scripts/chat-widget.html`, `404.html`, `search.html`, `index.html.old`

Status key: ☐ not started · 🔍 in progress · ✅ checked/clean · ✏️ fixed · ⚠️ flagged (needs decision)

## Root / core (7)
- ✏️ index.html — fixed: reworded stale "Breaking News" banner (30-day visa exempt change no longer new), added logo+sameAs to Organization schema
- ✅ best-chiang-mai.html — clean. FAQ relevant, schema (Article+FAQPage) correct, meta/OG fine. Body is a long list of external Facebook group links (not individually link-checked — flagging as a known gap, not verified dead/alive one by one).
- ✅ cheapest-border-run-chiang-mai.html — clean. FAQ on-topic, schema present, no stale 60/30-day or land-border-cap assumptions.
- ✅ chiang-mai-mattress-guide.html — clean, FAQ relevant, dateModified 2026-08-06
- ✅ chiang-mai-scams.html — clean, FAQ relevant, dateModified 2026-06-15
- ✅ dental-care-chiang-mai.html — clean, FAQ relevant, dateModified 2026-06-15
- ✅ dying-in-thailand.html — clean, FAQ relevant, dateModified 2026-06-29
- ✅ getting-social-in-chiang-mai.html — clean, FAQ relevant, dateModified 2026-05-25
- ✅ khun-joe-school.html — clean, FAQ relevant, dateModified 2026-05-25
- ✅ modern-transport-guide.html — clean, FAQ relevant, dateModified 2026-06-03
- ✅ motorbike-registration-chiang-mai.html — clean, FAQ relevant, dateModified 2026-05-25
- ✅ pest-control-chiang-mai.html — clean, FAQ relevant, dateModified 2026-08-06
- ✅ thai-eating-etiquette.html — clean, FAQ relevant, dateModified 2026-05-25
- ✅ understanding-thai-culture.html — clean, FAQ relevant, dateModified 2026-05-25
- ✏️ visa-exempt-status-2026-returning-to-30-days.html — fixed: page + homepage banner wrongly stated 30-day change was already in effect; actual status (per user, verbally confirmed) is Cabinet approved May 19 2026 but still pending Royal Gazette publication as of Aug 2026, so still 60 days for now. Corrected H1, TL;DR, "What Happened", Key Takeaways, Common Questions, dateModified. FAQ schema was already correctly hedged.
- ✅ where-to-stay-in-chiang-mai.html — clean, FAQ relevant, dateModified 2026-06-03
- ✅ womens-prison-massage.html — clean, FAQ relevant, dateModified 2026-05-25
- ✅ yunnan-farmers-market.html — clean, FAQ relevant, dateModified 2026-05-25
- ✅ chiang-mai/index.html — clean, hub page (no FAQ, none needed), meta/canonical present. Minor: OG title text differs slightly from <title> tag, cosmetic only, not fixed.

## food/ (10)
- ✅ auf-der-au-best-buffet-chiang-mai.html — clean, FAQ relevant, dateModified 2026-05-25
- ✅ butter-is-better.html — clean, FAQ relevant, dateModified 2026-05-25
- ✅ chiang-mai-grandview-white-elephant-buffet.html — clean, FAQ relevant, dateModified 2026-08-03
- ✏️ chiang-mai-marriott-hotel-dining.html — fixed: FAQ question+answer self-contradicted ("same as the old Marriott" comparing Marriott to Marriott). Corrected to Le Meridien per confirmed rebrand history, in both JSON-LD and visible FAQ.
- ✅ food-delivery-apps-chiang-mai.html — clean, FAQ relevant, dateModified 2026-05-28
- ✅ food-delivery-services.html — clean, FAQ relevant, dateModified 2026-05-25
- ✅ late-night-eating-chiang-mai.html — clean, FAQ relevant, dateModified 2026-05-28
- ✅ meela-peanut-butter.html — clean, FAQ relevant, dateModified 2026-05-25
- ✅ siripanna-lunch.html — clean, FAQ relevant, dateModified 2026-05-25
- ✅ the-dukes.html — clean, FAQ relevant, dateModified 2026-05-25
- ✅ the-happy-frog-secret-buffet.html — clean, FAQ relevant, dateModified 2026-05-25

## guides/ (32)
- ✅ 90-day-reporting-tm30-chiang-mai.html — clean, FAQ relevant, dateModified 2026-05-28
- ✅ blood-donation-donor-eligibility-red-cross-blood-bank-chiang-mai.html — clean, FAQ relevant, dateModified 2026-05-25
- ✅ blood-donation-procedure.html — clean, FAQ relevant, dateModified 2026-05-25
- ✅ bua-tong-waterfalls.html — clean, FAQ relevant, dateModified 2026-05-25
- ✅ budget-chiang-mai-medical-services.html — clean, FAQ relevant, dateModified 2026-05-25
- ✅ chiang-mai-driving.html — clean, FAQ relevant, dateModified 2026-05-25
- ✅ chiang-mai-driving-licence.html — clean, FAQ relevant, dateModified 2026-05-28
- ✅ chiang-mai-festivals.html — clean, FAQ relevant, dateModified 2026-06-08
- ✅ chiang-mai-insurance.html — clean, FAQ relevant, dateModified 2026-05-25
- ✅ chiang-mai-road-rules.html — clean, FAQ relevant, dateModified 2026-05-25
- ✏️ chiang-mai-vs-da-nang.html — fixed: Article schema was missing dateModified and publisher (had only datePublished+author). Added both.
- ✅ citylife-garden-fair.html — clean, FAQ relevant, dateModified 2026-08-05
- ✅ finding-pet-friendly-home-chiang-mai.html — clean, FAQ relevant, dateModified 2026-05-28
- ✅ flat-tire.html — clean, FAQ relevant, dateModified 2026-05-25
- ✅ index.html (guides hub) — clean, no FAQ needed on hub page
- ✅ language-schools-ed-visa-chiang-mai.html — clean, FAQ relevant, dateModified 2026-05-28
- ✅ lazada-shopee-foreigners-chiang-mai.html — clean, FAQ relevant, dateModified 2026-05-28
- ✅ license-plates.html — clean, FAQ relevant, dateModified 2026-05-25
- ✅ motorcycle-registration-transfer.html — clean, FAQ relevant, dateModified 2026-05-25
- ✅ motorcycle-rentals.html — clean, FAQ relevant, dateModified 2026-05-25. Note: overlaps with renting-a-motorbike-in-chiang-mai.html, see open issues log.
- ✅ red-cross-blood-bank-chiang-mai.html — clean, FAQ relevant, dateModified 2026-05-25
- ✅ renting-a-motorbike-in-chiang-mai.html — clean, FAQ relevant, dateModified 2026-05-25. Note: overlaps with motorcycle-rentals.html, see open issues log.
- ✅ residency-certificate-chiang-mai.html — clean, FAQ relevant, dateModified 2026-05-28
- ✅ tdac-thailand-digital-arrival-card.html — clean, FAQ relevant, dateModified 2026-05-25
- ✅ thailand-media.html — clean, FAQ relevant, dateModified 2026-06-08
- ✅ thailand-public-holidays-2026.html — clean, FAQ relevant, dateModified 2026-08-05
- ✅ travelling-to-thailand-with-pets.html — clean, FAQ relevant, dateModified 2026-05-28
- ✅ vets-pet-care-chiang-mai.html — clean, FAQ relevant, dateModified 2026-05-28
- ✅ walking-street-markets.html — clean, FAQ relevant, dateModified 2026-05-25
- ✅ what-to-do-after-a-vehicle-accident.html — clean, FAQ relevant, dateModified 2026-06-08
- ✅ wing-41-pass.html — clean, FAQ relevant, dateModified 2026-05-25
- ✅ work-permit-medical-certificate.html — clean, FAQ relevant, dateModified 2026-05-25
- ✅ yi-peng-lantern-festival.html — clean, FAQ relevant, dateModified 2026-05-25

## lifestyle/ (27, incl. neighborhoods/)
- ✅ alcohol-observations-of-a-non-drinker.html — clean, FAQ relevant, dateModified 2026-05-25
- ✅ chiang-mai-arrival.html — clean, FAQ relevant, dateModified 2026-05-25
- ✅ chiang-mai-floods-2024.html — clean, FAQ relevant, dateModified 2026-08-05
- ✅ cigar-lounge-chiang-mai.html — clean, FAQ relevant, dateModified 2026-06-28
- ✅ currency-in-and-out-of-thailand.html — clean, FAQ relevant, dateModified 2026-05-25
- ✅ expat-breakfast-club.html — clean, FAQ relevant, dateModified 2026-05-25
- ✅ index.html (lifestyle hub) — clean, no FAQ needed on hub page
- ✅ internet.html — clean, FAQ relevant, dateModified 2026-05-25, price recently refreshed (398 THB, per recent commit)
- ✅ learning-languages.html — clean, FAQ relevant, dateModified 2026-05-25
- ✅ life-budget-chiang-mai.html — clean, FAQ relevant, dateModified 2026-05-25. Part of cannibalization group, see open issues.
- ✅ life-on-a-budget-in-chiang-mai-covid-2022-update.html — content itself is current (2026 prices), but URL slug still says covid-2022. Part of cannibalization group, see open issues. Not renamed/redirected without decision.
- ✅ live-in-chiang-mai.html — clean, FAQ relevant, dateModified 2026-06-08
- ✅ mobile-phones.html — clean, FAQ relevant, dateModified 2026-05-25
- ✅ moving-checklist.html — clean, FAQ relevant, dateModified 2026-05-25
- ✅ neighborhoods/hang-dong.html — clean, FAQ relevant, dateModified 2026-05-28
- ✅ neighborhoods/jed-yod.html — clean, FAQ relevant, dateModified 2026-05-28
- ☐ neighborhoods/nimman.html
- ☐ neighborhoods/old-city.html
- ☐ neighborhoods/riverside.html
- ☐ neighborhoods/santitham.html
- ☐ neighborhoods/wat-ket-riverside.html
- ☐ smoky-season-chiang-mai.html
- ☐ songkran.html
- ☐ television.html
- ☐ thai-visa-advice.html
- ☐ top-tips.html
- ☐ traveling-alone.html
- ☐ traveling-with-friends.html
- ☐ us-expat-tax-guide.html
- ☐ vientiane-visa-run.html
- ☐ vip-concierge-chiang-mai.html

## pages/ (9)
- ☐ about.html
- ☐ cost-of-living.html
- ☐ disclaimer.html
- ☐ embassies-consulates.html
- ☐ just-arriving-in-thailand.html
- ☐ living-better-in-thailand.html
- ☐ neighbourhoods.html
- ☐ planning-a-move-to-thailand.html
- ☐ privacy.html
- ☐ terms.html
- ☐ visas.html

## visa/ (12)
- ☐ border-run-strategy.html
- ☐ business-visa.html
- ☐ dtv-visa.html
- ☐ ed-visa.html
- ☐ ed-visa-combat-training.html
- ☐ ed-visa-muay-thai.html
- ☐ ed-visa-thai-language.html
- ☐ index.html
- ☐ ltr-visa.html
- ☐ marriage-visa.html
- ☐ retirement-visa.html
- ☐ tourist-visa.html
- ☐ visa-exempt-vs-voa.html
- ☐ volunteer-visa.html

---

## Open issues log (carried from prior handover, verify still relevant)
- New: guides/motorcycle-rentals.html and guides/renting-a-motorbike-in-chiang-mai.html appear to cover the same topic (motorbike rental) as separate pages — potential cannibalization, not fixed.
- Keyword cannibalization: pages/cost-of-living.html, lifestyle/life-budget-chiang-mai.html, lifestyle/life-on-a-budget-in-chiang-mai-covid-2022-update.html all target cost-of-living/budget. Covid-2022 page is stale-branded, orphaned from nav.
- Homepage Organization/WebSite schema could use logo + sameAs (social profiles).

## New findings this pass
- Site-wide (123 pages) `/shared/chat-widget.js` was styled/id'd like a CMLocals clone (blue #1e57be, `cml-` ids). Backend confirmed genuinely CMA's own (Vectorize index `chiangmaiambassador-content`, built from CMA's 120 pages, reindex CI running successfully incl. today). Fixed: recolored to CMA gold/navy, ids renamed to `cma-chat-*`. One shared file, applies site-wide, no per-page edits needed. Not yet committed/pushed.
