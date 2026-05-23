#!/usr/bin/env python3
"""
Batch SEO Optimization: Apply titles and meta descriptions to 45 subdirectory pages.
Backs up originals, applies changes, logs results.
"""

import os
import re
from pathlib import Path
from datetime import datetime
import shutil

# Define all optimizations as tuples: (filepath_relative, new_title, new_description)
OPTIMIZATIONS = [
    # FOOD FOLDER (10 pages)
    ("food/auf-der-au-best-buffet-chiang-mai.html", "Auf der Au Buffet | German Dining in Chiang Mai", "Auf der Au brings German family-style dining to Chiang Mai near CM Gymkhana. Authentic buffet lunch, quality food, and homemade flavours. Perfect for expat cravings."),
    ("food/butter-is-better.html", "Butter is Better | American Diner in Chiang Mai", "Butter is Better serves authentic American comfort food in Chiang Mai. Small-town diner atmosphere, home-style cooking. The expat favourite for breakfast and lunch."),
    ("food/chiang-mai-grandview-lunch.html", "Grandview Restaurant | Lunch Buffet Chiang Mai", "Grandview offers quality lunch buffets in Chiang Mai with diverse menu options. Convenient location, good value. Popular with expats and locals alike."),
    ("food/dukes.html", "The Dukes | Pizza & Bar in Chiang Mai", "The Dukes serves premium pizza and cocktails in Chiang Mai. Full bar, casual atmosphere, excellent food quality. Your go-to spot for evening out."),
    ("food/food-delivery-services.html", "Food Delivery in Chiang Mai | Apps & Services", "Food delivery services in Chiang Mai make ordering easy. Grab, Food Panda, and local options. Guide to fastest delivery, best restaurants, and apps available."),
    ("food/ibis-styles-buffet-lunch.html", "Ibis Styles Buffet | Lunch in Chiang Mai", "Ibis Styles buffet lunch offers international cuisine in Chiang Mai. Hotel restaurant quality, diverse menu, friendly service. Great mid-range option."),
    ("food/le-meridien-dinner-buffet.html", "Le Meridien Buffet | Premium Dinner Chiang Mai", "Le Meridien dinner buffet delivers premium dining experience in Chiang Mai. International cuisine, high-quality ingredients, elegant setting. Special occasion worthy."),
    ("food/meela-peanut-butter.html", "Meela Peanut Butter | Best in Chiang Mai", "Meela produces the best peanut butter in Chiang Mai. Handmade, natural, no additives. Local favourite for smooth or crunchy. Perfect for expat cravings."),
    ("food/real-thai-restaurant.html", "Real Thai | Authentic Restaurant Chiang Mai", "Real Thai serves authentic Thai cuisine in Chiang Mai. Traditional recipes, local ingredients, genuine flavours. Expat-friendly with expert guidance on spice levels."),
    ("food/siripanna-lunch.html", "Siripanna Buffet | Best Lunch Chiang Mai", "Siripanna lunch buffet ranks among Chiang Mai's best. Extensive menu, quality food, fair prices. Local and expat favourite. Great group dining."),

    # GUIDES FOLDER (13 pages)
    ("guides/blood-donation-donor-eligibility-red-cross-blood-bank-chiang-mai.html", "Blood Donation Eligibility | Red Cross Chiang Mai", "Blood donation eligibility requirements at Red Cross Blood Bank Chiang Mai. Health checks, age limits, frequency rules. Help local community. Full process guide."),
    ("guides/blood-donation-procedure.html", "Blood Donation Procedure | Red Cross Guide", "Step-by-step blood donation procedure at Red Cross Chiang Mai. Screening, donation, recovery. First-time guide. Comfortable experience, community help."),
    ("guides/bua-tong-waterfalls.html", "Bua Tong Waterfalls | Day Trip Chiang Mai", "Bua Tong sticky waterfalls offer unique climbing experience near Chiang Mai. Day trip guide with directions, timing, tips. Natural phenomenon worth experiencing."),
    ("guides/budget-chiang-mai-medical-services.html", "Budget Medical Services | Healthcare Chiang Mai", "Affordable medical services in Chiang Mai without insurance. Government hospitals, pharmacies, clinics. Cost breakdown, quality standards, practitioner tips."),
    ("guides/chiang-mai-driving.html", "Chiang Mai Driving Guide | Safe Tips & Rules", "Safe driving in Chiang Mai requires local knowledge. Road hazards, traffic rules, insurance tips, emergency numbers. Complete guide for expat drivers."),
    ("guides/chiang-mai-football-club.html", "Chiang Mai Football Club | Join & Participate", "Chiang Mai football club connects expats for regular games. Skills welcome, fun atmosphere, friendly community. Schedule, contact, and how to join."),
    ("guides/chiang-mai-insurance.html", "Insurance in Chiang Mai | Coverage & Providers", "Insurance options in Chiang Mai include health, motor, home. Providers, coverage types, costs, claims process. Protect your expat life properly."),
    ("guides/flat-tire.html", "Motorcycle Flat Tire | Fix & Repair Chiang Mai", "Fix a motorcycle flat tire in Chiang Mai. DIY steps, repair shops, costs, prevention. Quick guide for common commute problem."),
    ("guides/license-plates.html", "Thai License Plates | Numbering System", "Understanding Thai vehicle license plates in Chiang Mai. Province codes, numbering, colours. Read and identify plates like a local."),
    ("guides/motorcycle-registration-transfer.html", "Motorcycle Registration Transfer | Chiang Mai", "Transfer motorcycle registration in Chiang Mai as expat. Documents needed, DMV process, costs, timeline. Step-by-step buyer and seller guide."),
    ("guides/motorcycle-rentals.html", "Motorcycle Rentals | Rates & Shops Chiang Mai", "Rent motorcycles in Chiang Mai at best rates. Shop recommendations, daily costs, insurance, safety tips. Complete rental guide for expats."),
    ("guides/red-cross-blood-bank-chiang-mai.html", "Red Cross Blood Bank | Chiang Mai Location", "Red Cross Blood Bank Chiang Mai welcomes donors year-round. Address, hours, eligibility, appointment booking. Help local community, simple process."),
    ("guides/renting-a-motorbike-in-chiang-mai.html", "Motorbike Rental | Long-Term Rates Chiang Mai", "Rent motorcycles long-term in Chiang Mai at monthly rates. Shop deals, contract terms, maintenance responsibility, insurance options."),
    ("guides/run-for-relief.html", "Run for Relief | Charity Event Chiang Mai", "Run for Relief charity event in Chiang Mai supports local causes. Participant info, registration, routes. Join expat community for good."),
    ("guides/tdac-thailand-digital-arrival-card.html", "Thailand Digital Arrival Card | TDAC Guide", "Thailand Digital Arrival Card (TDAC) replaces TM.6 form. Online registration, timeline, requirements. Complete guide for entry to Thailand."),
    ("guides/walking-street-markets.html", "Walking Street Markets | Shopping Chiang Mai", "Walking Street night markets in Chiang Mai offer crafts, food, souvenirs. Market guide, best times, negotiating, what to buy."),
    ("guides/wing-41-pass.html", "Wing 41 Pass | Mountain Road Chiang Mai", "Wing 41 mountain pass near Chiang Mai offers scenic views and riding challenge. Directions, hazards, best time to visit, photo spots."),
    ("guides/work-permit-medical-certificate.html", "Work Permit Medical Certificate | Thailand", "Thai work permit medical certificate requirements explained. Required tests, approved hospitals, costs, timeline. Get certified for legal employment."),

    # LIFESTYLE FOLDER (16 pages)
    ("lifestyle/alcohol-observations-of-a-non-drinker.html", "Non-Drinker in Chiang Mai | Social Life Guide", "Social life for non-drinkers in Chiang Mai works well. Coffee culture, alternative venues, activities, acceptance. Guide to enjoying nightlife without alcohol."),
    ("lifestyle/chiang-mai-arrival.html", "Chiang Mai Arrival | Getting Started Guide", "Chiang Mai arrival guide for expats moving in. First steps, accommodation, banking, permits, making friends. Quick settlement checklist."),
    ("lifestyle/currency-in-and-out-of-thailand.html", "Moving Money to Thailand | Currency Guide", "Move money into and out of Thailand safely. Transfer methods, exchange rates, banks, minimums, costs. Complete guide for expat finances."),
    ("lifestyle/expat-breakfast-club.html", "Expat Breakfast Club | Meet & Connect", "Expat Breakfast Club in Chiang Mai brings people together. Casual networking, friendships, community. How to join, frequency, locations."),
    ("lifestyle/learning-languages.html", "Learning Thai | Language Classes Chiang Mai", "Learn Thai in Chiang Mai with quality schools and private tutors. Course types, costs, duration. Tips for expats. Build local relationships."),
    ("lifestyle/life-budget-chiang-mai.html", "Cost of Living Chiang Mai | Budget Guide", "Budget for living in Chiang Mai as expat. Housing, food, transport, utilities monthly costs. Sample budgets for different lifestyles."),
    ("lifestyle/life-on-a-budget-in-chiang-mai-covid-2022-update.html", "Living on Budget | Thrifty Chiang Mai Tips", "Live comfortably on tight budget in Chiang Mai. Savings hacks, local markets, free activities. Stretch money further without sacrificing quality."),
    ("lifestyle/live-in-chiang-mai.html", "Live in Chiang Mai | Expat Living Guide", "Complete guide to living in Chiang Mai as expat. Visa options, accommodation, neighbourhoods, healthcare, lifestyle benefits."),
    ("lifestyle/smoky-season-chiang-mai.html", "Smoky Season Chiang Mai | Survival Guide", "Smoky season (March-April) impacts Chiang Mai air quality. Health tips, masks, activities, when it ends. Prepare and cope with air quality issues."),
    ("lifestyle/songkran.html", "Songkran Festival | Water Festival Guide", "Songkran Thai New Year water festival transforms Chiang Mai. Dates, traditions, locations, safety, what to expect. First-timer guide."),
    ("lifestyle/thai-visa-advice.html", "Thai Visa Advice | Expat Visa Guide", "Thai visa advice for expats living in Chiang Mai. Options, requirements, extensions, re-entry permits. Honest guidance on documentation."),
    ("lifestyle/top-tips.html", "Top Tips | Living in Chiang Mai", "Top tips for thriving in Chiang Mai from experienced expats. Practical advice on culture, safety, money, relationships. Survival essentials."),
    ("lifestyle/traveling-alone.html", "Traveling Alone | Solo Travel Chiang Mai", "Solo travel in Chiang Mai is safe and rewarding. Solo-friendly activities, accommodation, safety tips, making friends. Complete solo guide."),
    ("lifestyle/traveling-with-friends.html", "Traveling with Friends | Group Trip Guide", "Travel with friends to Chiang Mai and Thailand. Group activities, accommodation options, budget splitting, group dynamics. Trip planning guide."),
    ("lifestyle/us-expat-tax-guide.html", "US Expat Tax Guide | Thailand Edition", "US expat tax obligations while living in Thailand. FEIE, FATCA, reporting requirements, penalties. Accurate guidance to stay compliant."),
    ("lifestyle/vientiane-visa-run.html", "Vientiane Visa Run | Laos Trip Guide", "Visa run to Vientiane from Chiang Mai explained. Travel options, costs, timing, what to bring. Extend Thai stay with border run."),

    # PAGES FOLDER (4 pages)
    ("pages/about.html", "About Chiang Mai Ambassador | Our Mission", "Chiang Mai Ambassador provides practical, honest guidance for expats settling in. Local knowledge, real advice, community. Learn our story."),
    ("pages/cost-of-living.html", "Cost of Living Chiang Mai | Monthly Breakdown", "Complete cost of living breakdown for Chiang Mai. Housing, food, transport, utilities by lifestyle. Budget examples, savings opportunities."),
    ("pages/neighbourhoods.html", "Chiang Mai Neighbourhoods | Where to Live", "Chiang Mai neighbourhoods guide. Each area profile, costs, vibe, expat density, proximity to amenities. Find your perfect neighbourhood."),
    ("pages/visas.html", "Thailand Visas Explained | ED to Retirement", "Thailand visa guide for expats. ED visa, Elite, retirement, digital nomad, tourist options. Requirements, costs, timeline. Real advice."),
]

def apply_optimizations(project_root):
    """Apply all SEO optimizations."""
    project_root = Path(project_root)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_dir = project_root / f"backup_seo_{timestamp}"
    backup_dir.mkdir(exist_ok=True)

    log = []
    successful = 0
    failed = 0

    log.append(f"SEO Optimization Batch Job started at {datetime.now().isoformat()}")
    log.append(f"Backup directory: {backup_dir}\n")
    log.append(f"Total pages to optimize: {len(OPTIMIZATIONS)}\n")

    for filepath_rel, new_title, new_desc in OPTIMIZATIONS:
        filepath = project_root / filepath_rel

        if not filepath.exists():
            failed += 1
            log.append(f"SKIP: {filepath_rel} (file not found)")
            continue

        try:
            # Read original file
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()

            # Create backup
            backup_file = backup_dir / filepath_rel.replace('/', '_')
            backup_file.parent.mkdir(parents=True, exist_ok=True)
            with open(backup_file, 'w', encoding='utf-8') as f:
                f.write(content)

            # Replace title tag
            content = re.sub(
                r'<title>.*?</title>',
                f'<title>{new_title}</title>',
                content,
                count=1
            )

            # Replace meta description
            content = re.sub(
                r'<meta name="description" content="[^"]*">',
                f'<meta name="description" content="{new_desc}">',
                content,
                count=1
            )

            # Write back
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)

            successful += 1
            log.append(f"OK: {filepath_rel}")

        except Exception as e:
            failed += 1
            log.append(f"ERROR: {filepath_rel} - {str(e)}")

    # Write log
    log_file = project_root / "MD" / f"SEO_BATCH_LOG_{timestamp}.txt"
    log_file.parent.mkdir(parents=True, exist_ok=True)

    log.append(f"\n{'='*60}")
    log.append(f"Results: {successful} successful, {failed} failed")
    log.append(f"Completed: {datetime.now().isoformat()}")

    with open(log_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(log))

    print('\n'.join(log))
    print(f"\nLog file: {log_file}")
    return successful, failed

if __name__ == "__main__":
    project_root = Path(__file__).parent.parent
    apply_optimizations(project_root)
