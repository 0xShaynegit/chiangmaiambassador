# CMA Phase 1: Architecture and Cross-Linking Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Restructure CMA navigation, rewrite both audience hub pages, and standardise all visa cross-links to cmlocals.com.

**Architecture:** Nav gets two top-level audience entry points (Arriving, Living). Neighbourhoods and Cost of Living move into the Living dropdown. Both hub pages become genuine content hubs. All visa pages get a standardised "Ready to apply?" CTA block. thai-visa-advice.html gets a full rewrite with per-visa cmlocals links.

**Tech Stack:** Vanilla HTML/CSS. Python for batch nav updates across 95 pages. No frameworks. All paths relative.

---

## File Map

| File | Action | Notes |
|---|---|---|
| index.html | Modify nav block | Source of truth for new nav HTML |
| All 95 .html pages | Batch replace nav | Python script using index.html as source |
| pages/just-arriving-in-thailand.html | Rewrite | Week 1 survival hub |
| pages/living-better-in-thailand.html | Rewrite | Long-term expat hub |
| lifestyle/thai-visa-advice.html | Rewrite | C-model orientation page with cmlocals links |
| visa/*.html (13 pages) | Inject CTA block | Standardised "Ready to apply?" block at end of each |

---

## Task 1: Update index.html Nav

**Files:**
- Modify: `index.html` (nav-links div, lines ~135-238)

The new nav adds two top-level audience links, moves Neighbourhoods and Cost of Living into a Living dropdown, and keeps Food, Guides, Lifestyle, Visas as dropdowns.

- [ ] **Step 1: Replace the nav-links block in index.html**

Replace the entire `<div class="nav-links">...</div>` block with:

```html
        <div class="nav-links">
            <a href="pages/just-arriving-in-thailand.html">Arriving</a>

            <div class="nav-dropdown">
                <button class="nav-dropdown-toggle">Living Here</button>
                <div class="nav-dropdown-menu">
                    <a href="pages/living-better-in-thailand.html">Living Better in Chiang Mai</a>
                    <a href="pages/neighbourhoods.html">Neighbourhoods</a>
                    <a href="pages/cost-of-living.html">Cost of Living</a>
                    <a href="lifestyle/smoky-season-chiang-mai.html">Smoky Season</a>
                    <a href="lifestyle/live-in-chiang-mai.html">Live in Chiang Mai</a>
                    <a href="lifestyle/moving-checklist.html">Moving Checklist</a>
                    <a href="pages/planning-a-move-to-thailand.html">Planning Your Move</a>
                </div>
            </div>

            <div class="nav-dropdown">
                <button class="nav-dropdown-toggle">Food</button>
                <div class="nav-dropdown-menu">
                    <a href="food/auf-der-au-best-buffet-chiang-mai.html">Auf der Au Buffet</a>
                    <a href="food/butter-is-better.html">Butter is Better</a>
                    <a href="food/food-delivery-services.html">Food Delivery Services</a>
                    <a href="food/le-meridien-dinner-buffet.html">Le Meridien Dinner Buffet</a>
                    <a href="food/meela-peanut-butter.html">Meela Peanut Butter</a>
                    <a href="food/siripanna-lunch.html">Siripanna Lunch</a>
                    <a href="thai-eating-etiquette.html">Thai Eating Etiquette</a>
                    <a href="yunnan-farmers-market.html">Yunnan Farmers Market</a>
                </div>
            </div>

            <div class="nav-dropdown">
                <button class="nav-dropdown-toggle">Guides</button>
                <div class="nav-dropdown-menu">
                    <a href="best-chiang-mai.html">Best of Chiang Mai</a>
                    <a href="guides/budget-chiang-mai-medical-services.html">Budget Medical Services</a>
                    <a href="cheapest-border-run-chiang-mai.html">Cheapest Border Run</a>
                    <a href="guides/chiang-mai-driving-licence.html">Driving Licence</a>
                    <a href="guides/chiang-mai-festivals.html">Chiang Mai Festivals</a>
                    <a href="guides/chiang-mai-insurance.html">Chiang Mai Insurance</a>
                    <a href="guides/chiang-mai-road-rules.html">Road Rules</a>
                    <a href="guides/chiang-mai-vs-da-nang.html">Chiang Mai vs Da Nang</a>
                    <a href="modern-transport-guide.html">Transport Guide</a>
                    <a href="guides/motorcycle-registration-transfer.html">Motorcycle Registration</a>
                    <a href="guides/renting-a-motorbike-in-chiang-mai.html">Renting a Motorbike</a>
                    <a href="guides/tdac-thailand-digital-arrival-card.html">TDAC Digital Arrival Card</a>
                    <a href="guides/walking-street-markets.html">Walking Street Markets</a>
                    <a href="guides/what-to-do-after-a-vehicle-accident.html">After a Vehicle Accident</a>
                    <a href="guides/yi-peng-lantern-festival.html">Yi Peng Lantern Festival</a>
                </div>
            </div>

            <div class="nav-dropdown">
                <button class="nav-dropdown-toggle">Lifestyle</button>
                <div class="nav-dropdown-menu">
                    <a href="lifestyle/chiang-mai-arrival.html">Chiang Mai Arrival</a>
                    <a href="lifestyle/currency-in-and-out-of-thailand.html">Currency In and Out</a>
                    <a href="lifestyle/expat-breakfast-club.html">Expat Breakfast Club</a>
                    <a href="getting-social-in-chiang-mai.html">Getting Social</a>
                    <a href="lifestyle/internet.html">Internet in Thailand</a>
                    <a href="lifestyle/learning-languages.html">Learning Languages</a>
                    <a href="lifestyle/mobile-phones.html">Mobile Phones</a>
                    <a href="lifestyle/songkran.html">Songkran</a>
                    <a href="lifestyle/television.html">Television in Thailand</a>
                    <a href="lifestyle/thai-visa-advice.html">Thai Visa Advice</a>
                    <a href="lifestyle/top-tips.html">Top Tips</a>
                    <a href="understanding-thai-culture.html">Understanding Thai Culture</a>
                    <a href="lifestyle/us-expat-tax-guide.html">US Expat Tax Guide</a>
                    <a href="lifestyle/vientiane-visa-run.html">Vientiane Visa Run</a>
                </div>
            </div>

            <div class="nav-dropdown">
                <button class="nav-dropdown-toggle">Visas</button>
                <div class="nav-dropdown-menu">
                    <a href="visa/ed-visa.html">ED Visa</a>
                    <a href="visa/ed-visa-thai-language.html">ED Visa: Thai Language</a>
                    <a href="visa/ed-visa-muay-thai.html">ED Visa: Muay Thai</a>
                    <a href="visa/ed-visa-combat-training.html">ED Visa: Combat Training</a>
                    <a href="visa/dtv-visa.html">DTV Visa</a>
                    <a href="visa/business-visa.html">Business Visa</a>
                    <a href="visa/retirement-visa.html">Retirement Visa</a>
                    <a href="visa/marriage-visa.html">Marriage Visa</a>
                    <a href="visa/ltr-visa.html">LTR Visa</a>
                    <a href="visa/volunteer-visa.html">Volunteer Visa</a>
                    <a href="visa/tourist-visa.html">Tourist Visa</a>
                    <a href="visa/visa-exempt-vs-voa.html">Visa Exempt vs VOA</a>
                    <a href="visa-exempt-status-2026-returning-to-30-days.html">Visa Exempt 2026 Update</a>
                    <a href="visa/border-run-strategy.html">Border Run Strategy</a>
                    <a href="pages/visas.html">Visa Hub</a>
                </div>
            </div>

        </div>
        <a href="#start" class="btn-primary magnetic-item">Start Here</a>
```

- [ ] **Step 2: Verify in browser**

Open `index.html` in browser. Check:
- "Arriving" appears as a top-level link
- "Living Here" dropdown contains Neighbourhoods and Cost of Living
- No broken links visible in dropdown menus

- [ ] **Step 3: Commit index.html**

```bash
cd "C:/ZZZWebsites/chiangmaiambassador"
git add index.html
git commit -m "Restructure nav: Arriving link, Living Here dropdown with Neighbourhoods and Cost of Living"
```

---

## Task 2: Batch Propagate Nav to All 95 Pages

**Files:**
- Create: `_scripts/update-nav.py` (temp script, not committed)
- Modify: All 95 .html pages

The nav HTML varies by path depth. Root pages use `href="pages/..."`, depth-1 pages use `href="../pages/..."`, depth-2 pages use `href="../../pages/..."`. The script detects depth and adjusts all paths accordingly.

- [ ] **Step 1: Create the nav update script**

Create `C:/ZZZWebsites/chiangmaiambassador/_scripts/update-nav.py`:

```python
import os
import re

ROOT = "C:/ZZZWebsites/chiangmaiambassador"

# New nav template — uses {D} as depth prefix placeholder
NAV_TEMPLATE = '''        <div class="nav-links">
            <a href="{D}pages/just-arriving-in-thailand.html">Arriving</a>

            <div class="nav-dropdown">
                <button class="nav-dropdown-toggle">Living Here</button>
                <div class="nav-dropdown-menu">
                    <a href="{D}pages/living-better-in-thailand.html">Living Better in Chiang Mai</a>
                    <a href="{D}pages/neighbourhoods.html">Neighbourhoods</a>
                    <a href="{D}pages/cost-of-living.html">Cost of Living</a>
                    <a href="{D}lifestyle/smoky-season-chiang-mai.html">Smoky Season</a>
                    <a href="{D}lifestyle/live-in-chiang-mai.html">Live in Chiang Mai</a>
                    <a href="{D}lifestyle/moving-checklist.html">Moving Checklist</a>
                    <a href="{D}pages/planning-a-move-to-thailand.html">Planning Your Move</a>
                </div>
            </div>

            <div class="nav-dropdown">
                <button class="nav-dropdown-toggle">Food</button>
                <div class="nav-dropdown-menu">
                    <a href="{D}food/auf-der-au-best-buffet-chiang-mai.html">Auf der Au Buffet</a>
                    <a href="{D}food/butter-is-better.html">Butter is Better</a>
                    <a href="{D}food/food-delivery-services.html">Food Delivery Services</a>
                    <a href="{D}food/le-meridien-dinner-buffet.html">Le Meridien Dinner Buffet</a>
                    <a href="{D}food/meela-peanut-butter.html">Meela Peanut Butter</a>
                    <a href="{D}food/siripanna-lunch.html">Siripanna Lunch</a>
                    <a href="{D}thai-eating-etiquette.html">Thai Eating Etiquette</a>
                    <a href="{D}yunnan-farmers-market.html">Yunnan Farmers Market</a>
                </div>
            </div>

            <div class="nav-dropdown">
                <button class="nav-dropdown-toggle">Guides</button>
                <div class="nav-dropdown-menu">
                    <a href="{D}best-chiang-mai.html">Best of Chiang Mai</a>
                    <a href="{D}guides/budget-chiang-mai-medical-services.html">Budget Medical Services</a>
                    <a href="{D}cheapest-border-run-chiang-mai.html">Cheapest Border Run</a>
                    <a href="{D}guides/chiang-mai-driving-licence.html">Driving Licence</a>
                    <a href="{D}guides/chiang-mai-festivals.html">Chiang Mai Festivals</a>
                    <a href="{D}guides/chiang-mai-insurance.html">Chiang Mai Insurance</a>
                    <a href="{D}guides/chiang-mai-road-rules.html">Road Rules</a>
                    <a href="{D}guides/chiang-mai-vs-da-nang.html">Chiang Mai vs Da Nang</a>
                    <a href="{D}modern-transport-guide.html">Transport Guide</a>
                    <a href="{D}guides/motorcycle-registration-transfer.html">Motorcycle Registration</a>
                    <a href="{D}guides/renting-a-motorbike-in-chiang-mai.html">Renting a Motorbike</a>
                    <a href="{D}guides/tdac-thailand-digital-arrival-card.html">TDAC Digital Arrival Card</a>
                    <a href="{D}guides/walking-street-markets.html">Walking Street Markets</a>
                    <a href="{D}guides/what-to-do-after-a-vehicle-accident.html">After a Vehicle Accident</a>
                    <a href="{D}guides/yi-peng-lantern-festival.html">Yi Peng Lantern Festival</a>
                </div>
            </div>

            <div class="nav-dropdown">
                <button class="nav-dropdown-toggle">Lifestyle</button>
                <div class="nav-dropdown-menu">
                    <a href="{D}lifestyle/chiang-mai-arrival.html">Chiang Mai Arrival</a>
                    <a href="{D}lifestyle/currency-in-and-out-of-thailand.html">Currency In and Out</a>
                    <a href="{D}lifestyle/expat-breakfast-club.html">Expat Breakfast Club</a>
                    <a href="{D}getting-social-in-chiang-mai.html">Getting Social</a>
                    <a href="{D}lifestyle/internet.html">Internet in Thailand</a>
                    <a href="{D}lifestyle/learning-languages.html">Learning Languages</a>
                    <a href="{D}lifestyle/mobile-phones.html">Mobile Phones</a>
                    <a href="{D}lifestyle/songkran.html">Songkran</a>
                    <a href="{D}lifestyle/television.html">Television in Thailand</a>
                    <a href="{D}lifestyle/thai-visa-advice.html">Thai Visa Advice</a>
                    <a href="{D}lifestyle/top-tips.html">Top Tips</a>
                    <a href="{D}understanding-thai-culture.html">Understanding Thai Culture</a>
                    <a href="{D}lifestyle/us-expat-tax-guide.html">US Expat Tax Guide</a>
                    <a href="{D}lifestyle/vientiane-visa-run.html">Vientiane Visa Run</a>
                </div>
            </div>

            <div class="nav-dropdown">
                <button class="nav-dropdown-toggle">Visas</button>
                <div class="nav-dropdown-menu">
                    <a href="{D}visa/ed-visa.html">ED Visa</a>
                    <a href="{D}visa/ed-visa-thai-language.html">ED Visa: Thai Language</a>
                    <a href="{D}visa/ed-visa-muay-thai.html">ED Visa: Muay Thai</a>
                    <a href="{D}visa/ed-visa-combat-training.html">ED Visa: Combat Training</a>
                    <a href="{D}visa/dtv-visa.html">DTV Visa</a>
                    <a href="{D}visa/business-visa.html">Business Visa</a>
                    <a href="{D}visa/retirement-visa.html">Retirement Visa</a>
                    <a href="{D}visa/marriage-visa.html">Marriage Visa</a>
                    <a href="{D}visa/ltr-visa.html">LTR Visa</a>
                    <a href="{D}visa/volunteer-visa.html">Volunteer Visa</a>
                    <a href="{D}visa/tourist-visa.html">Tourist Visa</a>
                    <a href="{D}visa/visa-exempt-vs-voa.html">Visa Exempt vs VOA</a>
                    <a href="{D}visa-exempt-status-2026-returning-to-30-days.html">Visa Exempt 2026 Update</a>
                    <a href="{D}visa/border-run-strategy.html">Border Run Strategy</a>
                    <a href="{D}pages/visas.html">Visa Hub</a>
                </div>
            </div>

        </div>
        <a href="#start" class="btn-primary magnetic-item">Start Here</a>'''

SKIP = {'_scripts', 'MD', '.git', 'docs', 'node_modules'}

def get_depth_prefix(filepath):
    rel = os.path.relpath(filepath, ROOT).replace('\\', '/')
    depth = rel.count('/') - 1  # subtract 1 because file itself is counted
    # root-level files: depth prefix is empty
    # one folder deep: ../
    # two folders deep: ../../
    parts = rel.split('/')
    folder_depth = len(parts) - 1  # number of folders above root
    if folder_depth == 0:
        return ''
    return '../' * folder_depth

def update_nav(filepath):
    with open(filepath, 'r', encoding='utf-8', errors='replace') as f:
        content = f.read()

    if 'nav-links' not in content:
        return False

    depth = get_depth_prefix(filepath)
    new_nav = NAV_TEMPLATE.replace('{D}', depth)

    # Match from <div class="nav-links"> to </div>\n        <a href="#start"
    pattern = r'<div class="nav-links">.*?</div>\s*\n\s*<a href="#start"[^>]*>[^<]*</a>'
    replacement = new_nav
    new_content, count = re.subn(pattern, replacement, content, flags=re.DOTALL)

    if count == 0:
        print(f"  SKIP (no match): {filepath}")
        return False

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    return True

updated = []
skipped = []

for dirpath, dirnames, filenames in os.walk(ROOT):
    dirnames[:] = [d for d in dirnames if d not in SKIP]
    for filename in filenames:
        if not filename.endswith('.html'):
            continue
        filepath = os.path.join(dirpath, filename)
        result = update_nav(filepath)
        if result:
            updated.append(filepath)
        else:
            skipped.append(filepath)

print(f"\nUpdated: {len(updated)} files")
print(f"Skipped: {len(skipped)} files")
for f in skipped:
    print(f"  {f}")
```

- [ ] **Step 2: Run the script**

```bash
cd "C:/ZZZWebsites/chiangmaiambassador"
python _scripts/update-nav.py
```

Expected output: `Updated: ~95 files`, Skipped: 0 or only MD/template files.

- [ ] **Step 3: Spot-check three pages at different depths**

Open these three in a browser and confirm the nav renders correctly and "Arriving" / "Living Here" are visible:
- `index.html` (root, depth 0)
- `guides/chiang-mai-driving-licence.html` (depth 1)
- `lifestyle/neighborhoods/nimman.html` (depth 2)

- [ ] **Step 4: Commit all updated pages**

```bash
cd "C:/ZZZWebsites/chiangmaiambassador"
git add -A
git commit -m "Propagate new nav to all 95 pages (Arriving + Living Here dropdown)"
git push origin master
```

---

## Task 3: Rewrite just-arriving-in-thailand.html

**Files:**
- Modify: `pages/just-arriving-in-thailand.html`

This page becomes the Week 1 survival hub for new arrivals. Copy the existing `pages/page-template.html` structure and fill with content. Path depth: 1 (`../`).

- [ ] **Step 1: Read current file to understand existing structure**

Read `pages/just-arriving-in-thailand.html` to see what content currently exists (keep any useful content, replace the page structure with the hub format).

- [ ] **Step 2: Rewrite the page**

The page must contain these sections in order:

**Meta:**
- Title: `Just Arrived in Chiang Mai: Your Week 1 Survival Guide`
- Description: `Everything you need to sort in your first week in Chiang Mai. SIM card, cash, transport, where to stay, and what your visa means for what comes next.`
- Canonical: `https://chiangmaiambassador.com/pages/just-arriving-in-thailand.html`

**TL;DR box (article-sidebar) contents:**
- Get a SIM at the airport (True Move H or AIS, 299-499 THB for 30 days)
- Use airport ATMs only once (250 THB fee per transaction). Get a Wise or Bangkok Bank account for regular withdrawals.
- Grab works everywhere. Red Songthaews (shared trucks) run fixed routes for 30-50 THB. Rent a motorbike only after you have a licence or IDP.
- Your visa type determines your next move within 30-90 days. Do not ignore this.
- File your TM30 within 24 hours of checking into any accommodation (landlord usually does this, but verify).
- Chiang Mai has two immigration offices. Promenada Mall handles most extensions. Airport Road handles Residency Certificates, TM30, and reporting.

**Page sections (H2 headings):**

1. **Getting a SIM Card**
   Content: True Move H and AIS are the two reliable options. Buy at Suvarnabhumi or CNX airport arrival hall before exiting. Tourist SIM (30 days, 299-499 THB) covers most of Thailand with 4G. Avoid DTAC (coverage gaps outside city). If staying long-term, register your SIM with your passport at a True/AIS branch within 30 days.
   Internal link: `../lifestyle/mobile-phones.html`

2. **Getting Cash**
   Content: Every Thai ATM charges foreigners 220-250 THB per transaction on top of your bank's foreign fee. Use ATMs sparingly. Open a Bangkok Bank or Kasikorn account if staying more than 2 months (requires Non-Immigrant visa or proof of address). Wise card holders: withdraw from any ATM, Wise absorbs part of the fee. Best rate: transfer via Wise to a Thai bank account. Worst rate: airport currency exchange booths.
   Internal link: `../lifestyle/currency-in-and-out-of-thailand.html`

3. **Getting Around Chiang Mai**
   Content: Grab (the Uber of Southeast Asia) is the default. Set it up before you arrive. Red Songthaews are shared trucks running semi-fixed routes, 30-50 THB, hail from the roadside. Tuk-tuks are tourist-priced (100-200 THB). Renting a motorbike is practical but requires either a Thai driving licence or a valid International Driving Permit (IDP) endorsed for motorbikes. Driving without one voids your insurance.
   Internal link: `../modern-transport-guide.html` and `../guides/renting-a-motorbike-in-chiang-mai.html`

4. **Your Visa Situation and What Comes Next**
   Content: Most people land on either a Visa Exempt stamp (30 days, extendable to 60) or a Tourist Visa (60 days, extendable to 90). If you plan to stay longer, you need to decide before your stamp expires. The decision is not complicated but the timing matters. CMA's visa pages explain each option. For the full application process, CMLocals has step-by-step guides.

   Visa type cards with cmlocals links:
   - Visa Exempt (30 days): `../visa/visa-exempt-vs-voa.html` + `https://cmlocals.com/visa-exempt/`
   - Tourist Visa (TR, 60 days): `../visa/tourist-visa.html` + `https://cmlocals.com/tourist-visa/`
   - DTV Visa (180 days, digital nomads/remote workers): `../visa/dtv-visa.html` + `https://cmlocals.com/dtv-visa/`
   - ED Visa (education, up to 1 year): `../visa/ed-visa.html` + `https://cmlocals.com/ed-visa/`
   - Retirement Visa (50+): `../visa/retirement-visa.html` + `https://cmlocals.com/retirement-visa/`

5. **Filing Your TM30**
   Content: If you are renting an apartment or house, your landlord is legally required to file a TM30 (foreigner notification form) within 24 hours of your arrival. Most do this automatically. If staying in a hotel, the hotel files it for you. If your landlord does not file it, you can file it yourself online at immigration.go.th. Failure to have a TM30 on file can complicate visa extensions.

6. **Where to Stay by Neighbourhood**
   Content: Brief 2-sentence description of each area with a link to the full guide.
   - Nimman: trendy, digital nomad, coffee shops, higher rents. `../lifestyle/neighborhoods/nimman.html`
   - Old City: temples, culture, backpacker-adjacent, cheap street food. `../lifestyle/neighborhoods/old-city.html`
   - Riverside/Wat Ket: quieter, sophisticated, long-stay expats. `../lifestyle/neighborhoods/riverside.html`
   - Santitham: local vibe, student area, best value. (Guide coming soon)
   - Full overview: `../pages/neighbourhoods.html`

**Bottom CTA:** "Got your first week sorted? The next step is setting up for the long term. Start with the Living Better in Chiang Mai guide." Link to `./living-better-in-thailand.html`.

- [ ] **Step 3: Verify in browser**

Open `pages/just-arriving-in-thailand.html`. Check:
- Nav renders correctly (depth-1 paths)
- All internal links are relative (no absolute chiangmaiambassador.com links in href)
- cmlocals links open in new tab (target="_blank" rel="noopener")
- No broken image paths

- [ ] **Step 4: Commit**

```bash
cd "C:/ZZZWebsites/chiangmaiambassador"
git add pages/just-arriving-in-thailand.html
git commit -m "Rewrite just-arriving-in-thailand.html as Week 1 survival hub"
```

---

## Task 4: Rewrite living-better-in-thailand.html

**Files:**
- Modify: `pages/living-better-in-thailand.html`

This page becomes the long-term expat hub. Same page-template.html structure. Path depth: 1 (`../`).

- [ ] **Step 1: Read current file**

Read `pages/living-better-in-thailand.html` to see existing content.

- [ ] **Step 2: Rewrite the page**

**Meta:**
- Title: `Living Better in Chiang Mai: The Long-Term Expat Hub`
- Description: `Admin, neighbourhoods, logistics, health, pets, and everything else for people building a real life in Chiang Mai.`
- Canonical: `https://chiangmaiambassador.com/pages/living-better-in-thailand.html`

**TL;DR box contents:**
- Get your Thai driving licence sorted early. DLT Hang Dong is the go-to office for foreigners.
- 90-day reporting is mandatory for all Non-Immigrant visa holders. Do it online or at Airport Road Immigration.
- Santitham and Jed Yod offer the best value-for-money neighbourhoods. Nimman is convenient but overpriced for long-termers.
- GrabFood and Lineman are the two delivery apps worth installing. Lineman has the best local Thai-only restaurant menus.
- Smoky season (Feb-April) is real. An air purifier (Xiaomi or Blueair) in your bedroom is not optional if you have any respiratory sensitivity.

**Page sections (H2 headings):**

1. **Admin and Bureaucracy**
   Sub-items as a card grid, each with title, one sentence, and link:
   - Thai Driving Licence: `../guides/chiang-mai-driving-licence.html`
   - 90-Day Reporting and TM30: `../guides/90-day-reporting-tm30-chiang-mai.html` (coming soon — note as such)
   - Residency Certificate: `../guides/residency-certificate-chiang-mai.html` (coming soon)
   - Visa extensions: `../pages/visas.html`
   - Work Permit Medical Certificate: `../guides/work-permit-medical-certificate.html`

2. **Neighbourhoods**
   Brief intro + links to all neighbourhood guides:
   - Nimman: `../lifestyle/neighborhoods/nimman.html`
   - Old City: `../lifestyle/neighborhoods/old-city.html`
   - Riverside: `../lifestyle/neighborhoods/riverside.html`
   - Santitham: coming soon
   - Jed Yod: coming soon
   - Hang Dong: coming soon
   - Wat Ket: coming soon
   - Full comparison: `../pages/neighbourhoods.html`

3. **Cost of Living**
   2-sentence overview + link to `../pages/cost-of-living.html`

4. **Logistics and Daily Life**
   Sub-items:
   - Food delivery apps: `../food/food-delivery-services.html` (expanded guide coming soon)
   - Internet and SIM: `../lifestyle/internet.html`
   - Mobile phones: `../lifestyle/mobile-phones.html`
   - Television: `../lifestyle/television.html`

5. **Health and Medical**
   Sub-items:
   - Budget medical services: `../guides/budget-chiang-mai-medical-services.html`
   - Health insurance: `../guides/chiang-mai-insurance.html`

6. **Smoky Season**
   2-sentence intro + link to `../lifestyle/smoky-season-chiang-mai.html`

7. **Pets in Chiang Mai**
   Intro: "Chiang Mai is surprisingly pet-friendly once you know how to navigate the landlord landscape and the local vet scene."
   Sub-items (all "coming soon" links until guides are built):
   - Travelling to Thailand with Pets: coming soon
   - Finding a Pet-Friendly Home: coming soon
   - Vets and Pet Care in Chiang Mai: coming soon

8. **Language and Education**
   Sub-items:
   - Learning languages: `../lifestyle/learning-languages.html`
   - Language schools and ED Visa: coming soon

**Bottom CTA:** "Just arrived and need to sort your first week? Start with the Arriving in Chiang Mai guide." Link to `./just-arriving-in-thailand.html`.

- [ ] **Step 3: Verify in browser**

Open `pages/living-better-in-thailand.html`. Check nav, internal links, no broken paths.

- [ ] **Step 4: Commit**

```bash
cd "C:/ZZZWebsites/chiangmaiambassador"
git add pages/living-better-in-thailand.html
git commit -m "Rewrite living-better-in-thailand.html as long-term expat hub"
```

---

## Task 5: Rewrite thai-visa-advice.html (C-Model)

**Files:**
- Modify: `lifestyle/thai-visa-advice.html`

Current page is a pointer to a Facebook group. Replace with a proper C-model orientation page: CMA explains each visa type (what it is, who it suits, key considerations), then links to the specific cmlocals.com page for application detail. Path depth: 1 (`../`).

- [ ] **Step 1: Read current file**

Read `lifestyle/thai-visa-advice.html` lines 400-470 to understand existing structure (nav, blog-hero, article structure). Keep the structural HTML, replace body content only.

- [ ] **Step 2: Update meta tags**

Replace title, description, canonical, OG tags:
```html
<title>Thai Visa Options Explained | Chiang Mai Ambassador</title>
<meta name="description" content="Which Thailand visa is right for your situation? Plain-English breakdown of every visa option for Chiang Mai expats, with links to full application guides.">
<link rel="canonical" href="https://chiangmaiambassador.com/lifestyle/thai-visa-advice.html">
```

- [ ] **Step 3: Replace H1 and excerpt**

```html
<h1>Thai Visa Options: <span class="gold-gradient-text">Which One Is Right for You?</span></h1>
<p class="blog-excerpt">Every visa option for living in Chiang Mai explained plainly. Once you know which route fits your situation, the full step-by-step application guide is one click away at CMLocals.</p>
```

- [ ] **Step 4: Replace TL;DR sidebar content**

```html
<div class="article-sidebar">
    <h4>Quick Summary (TL;DR)</h4>
    <ul>
        <li>Just arrived and want to extend your 30-day stamp? Apply for a 30-day extension at Promenada Immigration (1,900 THB).</li>
        <li>Staying 2-3 months? A Tourist Visa (TR) gives you 60 days plus a 30-day extension at the border or consulate.</li>
        <li>Remote worker or digital nomad? The DTV Visa gives 180-day stays with multiple entries. No work permit required for foreign-source income.</li>
        <li>Studying Thai, Muay Thai, or another discipline? The ED Visa covers up to 1 year with school enrolment.</li>
        <li>Retired (50+) with income or savings? The Retirement Visa (OA/OX) is the most stable long-term option.</li>
        <li>Married to a Thai national? The Marriage Visa is renewable annually and the most straightforward path to long-term stay.</li>
        <li>For every visa: CMA explains what it is. CMLocals explains how to get it.</li>
    </ul>
</div>
```

- [ ] **Step 5: Write the body sections**

Replace the blog-body content with these sections. Each section follows the C-model: 2-3 paragraphs of orientation, then a "Ready to apply?" block.

The "Ready to apply?" block HTML pattern to use at the end of each visa section:
```html
<div class="callout-info">
    <p><strong>Ready to apply?</strong> Full step-by-step guide, document checklist, and current processing times at <a href="https://cmlocals.com/[VISA-SLUG]/" target="_blank" rel="noopener">CMLocals: [Visa Name] Guide</a>.</p>
</div>
```

**Section 1: Visa Exempt Entry (30 days)**
Content: Most nationalities enter Thailand visa-free for 30 days (recently extended to 60 days for many). This is not a visa. It is a stamp. You cannot "renew" it inside Thailand. You can extend it once at Immigration for 30 days (1,900 THB). After that, you need to leave and re-enter or switch to a proper visa.
CTA block: `https://cmlocals.com/visa-exempt/` — "CMLocals: Visa Exempt Guide"
Internal link: `../visa/visa-exempt-vs-voa.html`

**Section 2: Tourist Visa (TR, 60 days)**
Content: A Tourist Visa is purchased at a Thai consulate before you arrive (or via the Thai e-Visa system online). It gives 60 days on arrival, extendable for 30 more days at Immigration (1,900 THB). Total: up to 90 days. You can get multiple-entry tourist visas (METV) which allow 6 months of visits. Good for people testing the waters before committing to a longer visa.
CTA block: `https://cmlocals.com/tourist-visa/` — "CMLocals: Tourist Visa Guide"
Internal link: `../visa/tourist-visa.html`

**Section 3: DTV Visa (Destination Thailand Visa)**
Content: Launched in 2024, the DTV is Thailand's answer to the digital nomad visa. 180-day single entry, multiple entries allowed on the same visa over 5 years. No work permit needed for income earned outside Thailand. You apply online. Requirements: proof of remote work or freelance income, 500,000 THB in savings or equivalent income. Cost: 10,000 THB. Best option for location-independent workers who want flexibility without annual reporting obligations.
CTA block: `https://cmlocals.com/dtv-visa/` — "CMLocals: DTV Visa Guide"
Internal link: `../visa/dtv-visa.html`

**Section 4: ED Visa (Education)**
Content: The ED Visa covers genuine study. Thai language, Muay Thai, martial arts, yoga, and other disciplines qualify if the school is registered with the Ministry of Education. Gives 90 days initially, extendable for 90 more at Immigration while enrolled. Total up to 1 year. The school handles the paperwork. You show up, study, and report to Immigration every 90 days. Choose your school carefully: some are "visa mills" with no real curriculum.
CTA block: `https://cmlocals.com/ed-visa/` — "CMLocals: ED Visa Guide"
Internal links: `../visa/ed-visa.html`, `../visa/ed-visa-thai-language.html`, `../visa/ed-visa-muay-thai.html`

**Section 5: Retirement Visa (OA / OX)**
Content: Available to anyone 50 or older. The OA (Non-Immigrant O-A) requires 800,000 THB in a Thai bank account or proof of monthly pension/income of 65,000 THB. Annual renewal at Immigration. You must report every 90 days. The OX is a 10-year long-stay version with higher financial requirements. The Retirement Visa is the most stable option for long-term residents who qualify.
CTA block: `https://cmlocals.com/retirement-visa/` — "CMLocals: Retirement Visa Guide"
Internal link: `../visa/retirement-visa.html`

**Section 6: Marriage Visa (Non-Immigrant O)**
Content: For foreign nationals legally married to a Thai citizen. Gives 1 year stay, renewable annually. Financial requirement: 400,000 THB in a Thai bank account or monthly income of 40,000 THB. Must report every 90 days. The most administratively straightforward long-term option if you qualify.
CTA block: `https://cmlocals.com/marriage-visa/` — "CMLocals: Marriage Visa Guide"
Internal link: `../visa/marriage-visa.html`

**Section 7: LTR Visa (Long-Term Resident)**
Content: Thailand's premium 10-year visa for wealthy retirees, remote workers with high income, and highly skilled professionals. Four categories: Wealthy Global Citizen (1M USD assets), Wealthy Pensioner (80,000 USD/year income), Work-From-Thailand Professional (40,000 USD/year minimum), and Highly Skilled Professional (specific BOI-approved industries). Benefits include 90-day reporting exemption and a 17% flat income tax rate. Not for everyone, but worth knowing about.
CTA block: `https://cmlocals.com/ltr-visa/` — "CMLocals: LTR Visa Guide"
Internal link: `../visa/ltr-visa.html`

**Section 8: The Thai Visa Advice Facebook Group**
Content: Keep the existing reference to the Thai Visa Advice Facebook Group (https://www.facebook.com/groups/1395920320731833/). Frame it as: "For real-time questions and edge cases, the Thai Visa Advice Facebook group is the most reliable community resource. The admins work with Immigration daily and give better answers than most lawyers."

- [ ] **Step 6: Verify in browser**

Open `lifestyle/thai-visa-advice.html`. Check:
- All 7 visa sections present
- Each has a "Ready to apply?" callout block with correct cmlocals URL
- Internal links use `../visa/` paths (not absolute URLs)
- External cmlocals links open in new tab

- [ ] **Step 7: Commit**

```bash
cd "C:/ZZZWebsites/chiangmaiambassador"
git add lifestyle/thai-visa-advice.html
git commit -m "Rewrite thai-visa-advice.html: C-model orientation with per-visa cmlocals links"
```

---

## Task 6: Standardise visa/ Folder CTA Blocks

**Files:**
- Modify: `visa/border-run-strategy.html`, `visa/business-visa.html`, `visa/dtv-visa.html`, `visa/ed-visa.html`, `visa/ed-visa-combat-training.html`, `visa/ed-visa-muay-thai.html`, `visa/ed-visa-thai-language.html`, `visa/ltr-visa.html`, `visa/marriage-visa.html`, `visa/retirement-visa.html`, `visa/tourist-visa.html`, `visa/visa-exempt-vs-voa.html`, `visa/volunteer-visa.html`

Each page must end with a standardised "Ready to apply?" CTA block immediately before the `</article>` or `blog-related` section. Pages that already have a cmlocals link should have that link replaced with the standardised block.

- [ ] **Step 1: Check each visa page for existing cmlocals links**

For each of the 13 pages, grep for existing cmlocals links to understand current state:

```bash
cd "C:/ZZZWebsites/chiangmaiambassador"
grep -l "cmlocals" visa/*.html
grep -L "cmlocals" visa/*.html
```

- [ ] **Step 2: Add standardised CTA block to each page**

The CTA block to inject before the closing `</article>` tag (or before `blog-related` section if no article tag):

```html
<div class="callout-info" style="margin-top: 2rem;">
    <p><strong>Ready to apply?</strong> Full step-by-step application guide, document checklist, and current processing times at <a href="https://cmlocals.com/[VISA-SLUG]/" target="_blank" rel="noopener">CMLocals: [Visa Name] Guide</a>.</p>
</div>
```

CMLocals URL mapping for each page:
- border-run-strategy.html: `https://cmlocals.com/border-run/` — "Border Run Guide"
- business-visa.html: `https://cmlocals.com/business-visa/` — "Business Visa Guide"
- dtv-visa.html: `https://cmlocals.com/dtv-visa/` — "DTV Visa Guide"
- ed-visa.html: `https://cmlocals.com/ed-visa/` — "ED Visa Guide"
- ed-visa-combat-training.html: `https://cmlocals.com/ed-visa/hand-to-hand-combat/` — "ED Visa: Combat Training Guide"
- ed-visa-muay-thai.html: `https://cmlocals.com/ed-visa/muay-thai/` — "ED Visa: Muay Thai Guide"
- ed-visa-thai-language.html: `https://cmlocals.com/ed-visa/thai-language/` — "ED Visa: Thai Language Guide"
- ltr-visa.html: `https://cmlocals.com/ltr-visa/` — "LTR Visa Guide"
- marriage-visa.html: `https://cmlocals.com/marriage-visa/` — "Marriage Visa Guide"
- retirement-visa.html: `https://cmlocals.com/retirement-visa/` — "Retirement Visa Guide"
- tourist-visa.html: `https://cmlocals.com/tourist-visa/` — "Tourist Visa Guide"
- visa-exempt-vs-voa.html: `https://cmlocals.com/visa-exempt/` — "Visa Exempt Guide"
- volunteer-visa.html: `https://cmlocals.com/volunteer-visa/` — "Volunteer Visa Guide"

Work through each page individually. Read the file, find the correct injection point, add the block.

- [ ] **Step 3: Verify spot-check**

Open `visa/dtv-visa.html` and `visa/retirement-visa.html` in browser. Confirm the CTA block appears at the bottom of the article content, before the "More from the Ambassador" related posts section.

- [ ] **Step 4: Commit all visa pages**

```bash
cd "C:/ZZZWebsites/chiangmaiambassador"
git add visa/
git commit -m "Standardise Ready to Apply CTA blocks across all 13 visa pages with cmlocals links"
git push origin master
```

---

## Final Check

After all 6 tasks are complete:

- [ ] Open `index.html` and click through "Arriving" and "Living Here" nav items
- [ ] Open `pages/just-arriving-in-thailand.html` and follow one internal link to confirm it resolves
- [ ] Open `pages/living-better-in-thailand.html` and follow one internal link
- [ ] Open `lifestyle/thai-visa-advice.html` and confirm 7 visa sections with CTA blocks
- [ ] Open any visa/ page and confirm CTA block is present
- [ ] Run a final git push if any changes were made after the last commit

```bash
cd "C:/ZZZWebsites/chiangmaiambassador"
git status
git push origin master
```

---

*Phase 2 content roadmap plan will be written separately once Phase 1 is complete and merged.*
