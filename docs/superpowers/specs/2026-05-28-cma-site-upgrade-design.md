# CMA Site Upgrade: Design Spec
**Date:** 2026-05-28
**Status:** Approved

---

## Goal

Transform Chiang Mai Ambassador from a "what to see" tourist blog into the premier city guide for mid-term slow travellers and long-term expats. The site currently has 90+ pages but lacks the navigation architecture and content depth to serve the expat audience. This upgrade fixes architecture first, then fills content gaps in priority order.

---

## Audience Split

Two distinct audiences, currently served by the same flat navigation:

- **Arriving** — First 1-4 weeks in Chiang Mai. Needs: SIM, cash, transport, short-term accommodation, visa orientation.
- **Living** — 1 month to permanent. Needs: admin (driving licence, 90-day reporting), neighbourhood selection, logistics (delivery, shopping), pets, language, long-term cost management.

---

## Phase 1: Architecture and Cross-Linking

### 1a. Nav Restructure

Current nav is flat and cluttered. New structure consolidates under two audience hubs:

**Top-level nav items:**
- Arriving in Chiang Mai (pages/just-arriving-in-thailand.html)
- Living in Chiang Mai (pages/living-better-in-thailand.html)
- Visas (pages/visas.html)
- Guides (guides/index.html)
- Food (food/)

**Moved out of top-level nav (into Living dropdown):**
- Neighbourhoods (pages/neighbourhoods.html)
- Cost of Living (pages/cost-of-living.html)

These two pages are not removed. They become dropdown items under "Living in Chiang Mai" so the nav stays clean while the pages remain fully accessible.

---

### 1b. Rewrite: just-arriving-in-thailand.html

Becomes the "Week 1 survival hub." Page sections:

1. Getting a SIM card (True/AIS/DTAC comparison, where to buy at airport vs city)
2. Getting cash (ATM fees, best banks, Wise/Revolut tips)
3. Getting around (Grab, Songthaew, renting a motorbike — link to guides/renting-a-motorbike-in-chiang-mai.html)
4. Where to stay by neighbourhood (brief intro to each area with link to full neighbourhood guides)
5. What visa did you arrive on and what comes next (summary of each entry type with specific cmlocals.com links for execution detail — see cross-linking model below)
6. First week checklist (SIM done, cash sorted, TM30 filed if renting, transport sorted)

Internal links out to: modern-transport-guide.html, renting-a-motorbike-in-chiang-mai.html, pages/neighbourhoods.html, pages/visas.html, cmlocals.com visa pages.

---

### 1c. Rewrite: living-better-in-thailand.html

Becomes the long-term expat hub. Page sections:

1. Admin and bureaucracy (driving licence, 90-day reporting, residency certificate, TM30)
2. Neighbourhood deep-dives (Nimman, Old City, Riverside, Santitham, Jed Yod, Hang Dong, Wat Ket — links to individual neighbourhood guides)
3. Cost of living (link to pages/cost-of-living.html)
4. Logistics (food delivery apps, Lazada/Shopee, 7-Eleven)
5. Health and medical (link to guides/budget-chiang-mai-medical-services.html, guides/chiang-mai-insurance.html)
6. Smoky season (link to lifestyle/smoky-season-chiang-mai.html)
7. Pets in Chiang Mai (links to all three pet guides once written)
8. Language and education (link to lifestyle/learning-languages.html, future language schools guide)

---

### 1d. thai-visa-advice.html Cross-Linking

This page currently has zero cmlocals.com links despite covering every major visa type. Apply the C-model to every visa section:

**C-model pattern:**
- CMA section: explains what the visa is, who it suits, key requirements and tradeoffs (the "what and why")
- End of each section: "Ready to apply? Full step-by-step instructions at CMLocals: [specific cmlocals.com page for that visa]"

Visa types to link: Visa Exempt, Tourist Visa, ED Visa, DTV Visa, Retirement Visa, Marriage Visa, LTR Visa, Business Visa.

---

### 1e. Visa Folder Audit (visa/)

12 pages in visa/ already link to cmlocals but inconsistently. Standardise:

Every visa page in visa/ must end with a "Ready to apply?" CTA block:

```html
<div class="callout-info">
  <p><strong>Ready to apply?</strong> Full step-by-step application guide, document checklist, and current processing times at <a href="https://cmlocals.com/[visa-page]" target="_blank" rel="noopener">CMLocals</a>.</p>
</div>
```

Pages to audit: border-run-strategy.html, business-visa.html, dtv-visa.html, ed-visa.html, ed-visa-combat-training.html, ed-visa-muay-thai.html, ed-visa-thai-language.html, ltr-visa.html, marriage-visa.html, retirement-visa.html, tourist-visa.html, visa-exempt-vs-voa.html, volunteer-visa.html.

---

## Phase 2: Content Roadmap

All new content follows the Chiang Mai Guru standard: TL;DR box, H2/H3 structure, dual options (Mainstream + Deep Cut), Guru Tip, E-E-A-T, bottom summary + CTA, cmlocals cross-links where visa-adjacent.

### Priority Order

| # | Title | Folder | Hub | Notes |
|---|---|---|---|---|
| 1 | 90-Day Reporting and TM30: The No-Nonsense Guide | guides/ | Living | Online vs physical office, common mistakes, fines |
| 2 | Residency Certificate: How to Get It Fast | guides/ | Living | Immigration office, Colonel Visa, Napa Visa, stamped envelope tip |
| 3 | Smoky Season Survival Guide (expand existing) | lifestyle/ | Arriving + Living | Air purifiers, N95s, AQI apps, escape destinations |
| 4 | Santitham Neighbourhood Guide | lifestyle/neighborhoods/ | Living | Student vibe, local food, value for money |
| 5 | Jed Yod Neighbourhood Guide | lifestyle/neighborhoods/ | Living | Real Nimman, cheaper, university-adjacent |
| 6 | Hang Dong Neighbourhood Guide | lifestyle/neighborhoods/ | Living | Families, moo baans, more space, quieter |
| 7 | Wat Ket / Riverside Neighbourhood Guide | lifestyle/neighborhoods/ | Living | Sophisticated, heritage, quieter than Old City |
| 8 | Travelling to Thailand with Pets | guides/ | Living (Pets) | Import permits, airline rules, health certs, Suvarnabhumi process |
| 9 | Finding a Pet-Friendly Home in Chiang Mai | guides/ | Living (Pets) | Landlord attitudes, lease clauses, deposits, best areas |
| 10 | Vets and Pet Care in Chiang Mai | guides/ | Living (Pets) | Tongkaew, CM Land Vet, emergency, costs, dog-friendly cafes |
| 11 | Food Delivery Apps Compared | food/ | Living | GrabFood vs FoodPanda vs ShopeeFood vs Lineman |
| 12 | Lazada and Shopee for Foreigners | guides/ | Living | Payment at 7-Eleven, COD, returns, language barriers |
| 13 | Late Night Eating in Chiang Mai | food/ | Arriving + Living | 2AM options, rice porridge spots, midnight fried chicken |
| 14 | Language Schools and the ED Visa | guides/ | Living | Which schools handle ED paperwork reliably, cmlocals ED visa link |

### Pet Mini-Pillar: Internal Linking Structure

The three pet pages form a linked cluster:

```
Travelling to Thailand with Pets
  → links to: Finding a Pet-Friendly Home (next step)
  → links to: Vets and Pet Care (once you're here)

Finding a Pet-Friendly Home
  → links to: Travelling with Pets (if pre-arrival)
  → links to: Vets and Pet Care (local resources)

Vets and Pet Care
  → links to: Finding a Pet-Friendly Home (new arrivals)
  → links to: Travelling with Pets (if considering bringing a pet)
```

All three link back to the Living hub under the "Pets" section.

---

## Cross-Linking Model (C-Model): Summary

CMA = orientation and decision layer ("what visa do I need and why")
CMLocals = execution layer ("how to actually get it, step by step")

**CMA's role:** Explain the landscape, help the reader choose the right path, then hand off to CMLocals for the procedural detail.

**Implementation rule:** Every CMA page that touches visa or immigration topics must end the relevant section with a specific cmlocals.com link, not a generic homepage link. Link to the exact page that handles that topic.

---

## What We Are NOT Doing

- No JS toggle on the homepage. The two hub pages handle audience splitting via nav.
- No duplication of cmlocals procedural content. CMA summarises, cmlocals details.
- No new nav items beyond the restructured top-level list above.
- No framework imports. Vanilla only throughout.

---

## File Inventory: Pages to Create or Rewrite

### Phase 1 (Rewrites)
- pages/just-arriving-in-thailand.html (rewrite)
- pages/living-better-in-thailand.html (rewrite)
- lifestyle/thai-visa-advice.html (cross-link injection)
- visa/*.html x13 (standardise "Ready to apply?" CTA block)

### Phase 2 (New pages, in order)
- guides/90-day-reporting-tm30-chiang-mai.html
- guides/residency-certificate-chiang-mai.html
- lifestyle/smoky-season-chiang-mai.html (expand)
- lifestyle/neighborhoods/santitham.html
- lifestyle/neighborhoods/jed-yod.html
- lifestyle/neighborhoods/hang-dong.html
- lifestyle/neighborhoods/wat-ket-riverside.html
- guides/travelling-to-thailand-with-pets.html
- guides/finding-pet-friendly-home-chiang-mai.html
- guides/vets-pet-care-chiang-mai.html
- food/food-delivery-apps-chiang-mai.html
- guides/lazada-shopee-foreigners-chiang-mai.html
- food/late-night-eating-chiang-mai.html
- guides/language-schools-ed-visa-chiang-mai.html

---

## Success Criteria

- Nav has two clear audience entry points (Arriving, Living)
- Neighbourhoods and Cost of Living accessible via Living dropdown, not top-level
- thai-visa-advice.html links to specific cmlocals pages for every visa type
- Every visa/ page ends with a standardised "Ready to apply?" CTA block
- Both hub pages serve as genuine content hubs with links to all relevant guides
- Phase 2 content follows Chiang Mai Guru standard throughout
- No broken internal links introduced
