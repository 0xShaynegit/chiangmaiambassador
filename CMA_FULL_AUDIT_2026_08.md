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
- ☐ 90-day-reporting-tm30-chiang-mai.html
- ☐ blood-donation-donor-eligibility-red-cross-blood-bank-chiang-mai.html
- ☐ blood-donation-procedure.html
- ☐ bua-tong-waterfalls.html
- ☐ budget-chiang-mai-medical-services.html
- ☐ chiang-mai-driving.html
- ☐ chiang-mai-driving-licence.html
- ☐ chiang-mai-festivals.html
- ☐ chiang-mai-insurance.html
- ☐ chiang-mai-road-rules.html
- ☐ chiang-mai-vs-da-nang.html
- ☐ citylife-garden-fair.html
- ☐ finding-pet-friendly-home-chiang-mai.html
- ☐ flat-tire.html
- ☐ index.html
- ☐ language-schools-ed-visa-chiang-mai.html
- ☐ lazada-shopee-foreigners-chiang-mai.html
- ☐ license-plates.html
- ☐ motorcycle-registration-transfer.html
- ☐ motorcycle-rentals.html
- ☐ red-cross-blood-bank-chiang-mai.html
- ☐ renting-a-motorbike-in-chiang-mai.html
- ☐ residency-certificate-chiang-mai.html
- ☐ tdac-thailand-digital-arrival-card.html
- ☐ thailand-media.html
- ☐ thailand-public-holidays-2026.html
- ☐ travelling-to-thailand-with-pets.html
- ☐ vets-pet-care-chiang-mai.html
- ☐ walking-street-markets.html
- ☐ what-to-do-after-a-vehicle-accident.html
- ☐ wing-41-pass.html
- ☐ work-permit-medical-certificate.html
- ☐ yi-peng-lantern-festival.html

## lifestyle/ (27, incl. neighborhoods/)
- ☐ alcohol-observations-of-a-non-drinker.html
- ☐ chiang-mai-arrival.html
- ☐ chiang-mai-floods-2024.html
- ☐ cigar-lounge-chiang-mai.html
- ☐ currency-in-and-out-of-thailand.html
- ☐ expat-breakfast-club.html
- ☐ index.html
- ☐ internet.html
- ☐ learning-languages.html
- ☐ life-budget-chiang-mai.html
- ☐ life-on-a-budget-in-chiang-mai-covid-2022-update.html
- ☐ live-in-chiang-mai.html
- ☐ mobile-phones.html
- ☐ moving-checklist.html
- ☐ neighborhoods/hang-dong.html
- ☐ neighborhoods/jed-yod.html
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
- Keyword cannibalization: pages/cost-of-living.html, lifestyle/life-budget-chiang-mai.html, lifestyle/life-on-a-budget-in-chiang-mai-covid-2022-update.html all target cost-of-living/budget. Covid-2022 page is stale-branded, orphaned from nav.
- Homepage Organization/WebSite schema could use logo + sameAs (social profiles).

## New findings this pass
- Site-wide (123 pages) `/shared/chat-widget.js` was styled/id'd like a CMLocals clone (blue #1e57be, `cml-` ids). Backend confirmed genuinely CMA's own (Vectorize index `chiangmaiambassador-content`, built from CMA's 120 pages, reindex CI running successfully incl. today). Fixed: recolored to CMA gold/navy, ids renamed to `cma-chat-*`. One shared file, applies site-wide, no per-page edits needed. Not yet committed/pushed.
