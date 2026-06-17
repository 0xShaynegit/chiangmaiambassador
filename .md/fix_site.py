#!/usr/bin/env python3
"""
CMA Site Fix Script - Pre-publish pass
1. Fix related posts (correct paths + randomise with relevant content)
2. Fix broken visa image paths
3. Fix ed-visa sub-pages using wrong depth
4. Report TL;DR photo needs
"""

import re
import random
from pathlib import Path

ROOT = Path(r"C:\ZZZWebsites\chiangmaiambassador")

# ============================================================
# PAGE CATALOG - all publishable blog/content pages
# (path relative to ROOT, title, description, best image)
# ============================================================
PAGES = [
    # ROOT level
    {
        "path": "cheapest-border-run-chiang-mai.html",
        "title": "Cheapest Border Run from Chiang Mai",
        "desc": "The complete guide to doing a cheap border run from Chiang Mai, including costs, transport, and what to expect.",
        "img": "images/chiang-mai-ambassador-chiangmaiambassador-Chiang-Mai-Ambassador-CM-Ambassador-cheapest-border-run-10.webp",
        "tags": ["visa", "travel", "border"],
    },
    {
        "path": "getting-social-in-chiang-mai.html",
        "title": "Getting Social in Chiang Mai",
        "desc": "How to meet people, find your community, and build a genuine social life in Chiang Mai.",
        "img": "images/chiang-mai-ambassador-chiangmaiambassador-Chiang-Mai-Ambassador-116.webp",
        "tags": ["lifestyle", "community", "social"],
    },
    {
        "path": "thai-eating-etiquette.html",
        "title": "Thai Eating Etiquette",
        "desc": "What you need to know about eating like a local in Thailand. Customs, dos and don'ts, and the unwritten rules.",
        "img": "images/chiang-mai-ambassador-chiangmaiambassador-Chiang-Mai-Ambassador-thai-eating-etiquette-1.webp",
        "tags": ["food", "culture", "lifestyle"],
    },
    {
        "path": "understanding-thai-culture.html",
        "title": "Understanding Thai Culture",
        "desc": "A practical guide to Thai customs, values, and social norms for expats and long-term visitors.",
        "img": "images/chiang-mai-ambassador-chiangmaiambassador-Chiang-Mai-Ambassador-Thai-Culture-1.webp",
        "tags": ["culture", "lifestyle"],
    },
    {
        "path": "motorbike-registration-chiang-mai.html",
        "title": "Motorbike Registration in Chiang Mai",
        "desc": "Step-by-step guide to registering a motorbike in Chiang Mai as a foreigner.",
        "img": "images/chiang-mai-ambassador-chiangmaiambassador-Chiang-Mai-Ambassador-20.webp",
        "tags": ["motorbike", "guides", "transport"],
    },
    {
        "path": "modern-transport-guide.html",
        "title": "Modern Transport Guide: Chiang Mai 2026",
        "desc": "Grab, Bolt, songthaews, and ride-sharing in Chiang Mai. What to use, what to avoid, and current prices.",
        "img": "images/chiang-mai-ambassador-chiangmaiambassador-Chiang-Mai-Ambassador-modern-transport-1.webp",
        "tags": ["transport", "lifestyle", "guides"],
    },
    {
        "path": "womens-prison-massage.html",
        "title": "Women's Prison Massage Chiang Mai",
        "desc": "The famous women's prison massage in Chiang Mai. Prices, what to expect, and how to get there.",
        "img": "images/chiang-mai-ambassador-chiangmaiambassador-Chiang-Mai-Ambassador-womens-prison-massage-1.webp",
        "tags": ["lifestyle", "chiang-mai", "guides"],
    },
    {
        "path": "yunnan-farmers-market.html",
        "title": "Yunnan Farmers Market Chiang Mai",
        "desc": "The best fresh produce market in Chiang Mai. Chinese vegetables, herbs, and local foods you won't find elsewhere.",
        "img": "images/chiang-mai-ambassador-chiangmaiambassador-Chiang-Mai-Ambassador-yunnan-farmers-market-1.webp",
        "tags": ["food", "markets", "chiang-mai"],
    },
    {
        "path": "visa-exempt-status-2026-returning-to-30-days.html",
        "title": "Visa Exempt Status 2026: Back to 30 Days",
        "desc": "Thailand's visa exemption changes in 2026. What the return to 30 days means for you.",
        "img": "images/chiang-mai-ambassador-chiangmaiambassador-Chiang-Mai-Ambassador-Visa.webp",
        "tags": ["visa", "travel"],
    },
    {
        "path": "khun-joe-school.html",
        "title": "Khun Joe's School: Learn Thai",
        "desc": "One of the best places to learn Thai language in Chiang Mai. Honest review and what to expect.",
        "img": "images/chiang-mai-ambassador-chiangmaiambassador-Chiang-Mai-Ambassador-Khun-Joe-School-10.webp",
        "tags": ["lifestyle", "learning", "language"],
    },
    # FOOD
    {
        "path": "food/auf-der-au-best-buffet-chiang-mai.html",
        "title": "Auf Der Au: Best Buffet in Chiang Mai",
        "desc": "German-Thai buffet that's one of the most unique dining experiences in Chiang Mai.",
        "img": "images/chiang-mai-ambassador-chiangmaiambassador-Auf-Der-Au-best-buffet-chiang-mai-1.webp",
        "tags": ["food", "buffet", "restaurants"],
    },
    {
        "path": "food/butter-is-better.html",
        "title": "Butter is Better: Chiang Mai Bakery",
        "desc": "A hidden gem bakery in Chiang Mai with proper butter croissants and European-style pastries.",
        "img": "images/chiang-mai-ambassador-chiangmaiambassador-Chiang-Mai-Ambassador-butter-is-better-1.webp",
        "tags": ["food", "cafe", "bakery"],
    },
    {
        "path": "food/chiang-mai-grandview-lunch.html",
        "title": "Grandview Lunch: Rooftop Dining",
        "desc": "The Grandview's lunch buffet with panoramic Chiang Mai views. Worth it or not?",
        "img": "images/chiang-mai-ambassador-chiangmaiambassador-Chiang-Mai-Ambassador-grandview-lunch-1.webp",
        "tags": ["food", "buffet", "restaurants"],
    },
    {
        "path": "food/dukes.html",
        "title": "Duke's: American Food in Chiang Mai",
        "desc": "Duke's is the go-to for burgers, ribs, and American comfort food in Chiang Mai.",
        "img": "images/chiang-mai-ambassador-chiangmaiambassador-Chiang-Mai-Ambassador-dukes-1.webp",
        "tags": ["food", "restaurants", "western"],
    },
    {
        "path": "food/food-delivery-services.html",
        "title": "Food Delivery Services in Chiang Mai",
        "desc": "Grab Food, Foodpanda, LINE MAN. What works, what doesn't, and which restaurants deliver.",
        "img": "images/chiang-mai-ambassador-chiangmaiambassador-Chiang-Mai-Ambassador-food-delivery-1.webp",
        "tags": ["food", "delivery", "lifestyle"],
    },
    {
        "path": "food/ibis-styles-buffet-lunch.html",
        "title": "Ibis Styles Buffet Lunch",
        "desc": "The Ibis Styles lunch buffet. Great value for a hotel lunch in Nimmanhaemin.",
        "img": "images/chiang-mai-ambassador-chiangmaiambassador-Chiang-Mai-Ambassador-ibis-styles-1.webp",
        "tags": ["food", "buffet", "restaurants"],
    },
    {
        "path": "food/le-meridien-dinner-buffet.html",
        "title": "Le Meridien Dinner Buffet",
        "desc": "Le Meridien's dinner buffet is one of the best hotel dining experiences in Chiang Mai.",
        "img": "images/chiang-mai-ambassador-chiangmaiambassador-Chiang-Mai-Ambassador-le-meridien-dinner-buffet-1.webp",
        "tags": ["food", "buffet", "restaurants"],
    },
    {
        "path": "food/meela-peanut-butter.html",
        "title": "Meela: Natural Peanut Butter Chiang Mai",
        "desc": "Chiang Mai's famous local peanut butter. Where to buy it, what makes it special.",
        "img": "images/chiang-mai-ambassador-chiangmaiambassador-Chiang-Mai-Ambassador-meela-peanut-butter-1.webp",
        "tags": ["food", "local", "shopping"],
    },
    {
        "path": "food/real-thai-restaurant.html",
        "title": "Real Thai Restaurant: Where Locals Eat",
        "desc": "Skip the tourist traps. This is where to eat real Thai food in Chiang Mai.",
        "img": "images/chiang-mai-ambassador-chiangmaiambassador-Chiang-Mai-Ambassador-real-thai-1.webp",
        "tags": ["food", "thai", "local"],
    },
    {
        "path": "food/siripanna-lunch.html",
        "title": "Siripanna Villa Lunch Buffet",
        "desc": "Quiet, elegant, and excellent value. The Siripanna lunch buffet is a hidden Chiang Mai gem.",
        "img": "images/chiang-mai-ambassador-chiangmaiambassador-Chiang-Mai-Ambassador-siripanna-lunch-1.webp",
        "tags": ["food", "buffet", "restaurants"],
    },
    {
        "path": "food/the-dukes.html",
        "title": "The Dukes: Premium American Dining",
        "desc": "The upgraded Duke's experience. What's changed and why it's worth a visit.",
        "img": "images/chiang-mai-ambassador-chiangmaiambassador-Chiang-Mai-Ambassador-dukes-1.webp",
        "tags": ["food", "restaurants", "western"],
    },
    # GUIDES
    {
        "path": "guides/blood-donation-donor-eligibility-red-cross-blood-bank-chiang-mai.html",
        "title": "Blood Donation Eligibility: Chiang Mai Red Cross",
        "desc": "Can you donate blood in Chiang Mai as a foreigner? Eligibility rules, what to bring, and what to expect.",
        "img": "images/chiang-mai-ambassador-chiangmaiambassador-Chiang-Mai-Ambassador-Red-Cross-blood-bank-1.webp",
        "tags": ["guides", "health", "community"],
    },
    {
        "path": "guides/blood-donation-procedure.html",
        "title": "Blood Donation Procedure at Chiang Mai Red Cross",
        "desc": "Step-by-step: what happens when you donate blood at the Chiang Mai Red Cross Blood Bank.",
        "img": "images/chiang-mai-ambassador-chiangmaiambassador-Chiang-Mai-Ambassador-Red-Cross-blood-bank-1.webp",
        "tags": ["guides", "health", "community"],
    },
    {
        "path": "guides/bua-tong-waterfalls.html",
        "title": "Bua Tong (Sticky) Waterfalls",
        "desc": "The limestone waterfalls north of Chiang Mai that you can actually climb. How to get there and what to bring.",
        "img": "images/chiang-mai-ambassador-chiangmaiambassador-Chiang-Mai-Ambassador-bua-tong-waterfalls-1.webp",
        "tags": ["guides", "daytrip", "nature"],
    },
    {
        "path": "guides/budget-chiang-mai-medical-services.html",
        "title": "Budget Medical Services in Chiang Mai",
        "desc": "Good, affordable medical care in Chiang Mai. Clinics, hospitals, and costs.",
        "img": "images/chiang-mai-ambassador-chiangmaiambassador-Chiang-Mai-Ambassador-medical-1.webp",
        "tags": ["guides", "health", "budget"],
    },
    {
        "path": "guides/chiang-mai-driving.html",
        "title": "Driving in Chiang Mai",
        "desc": "What it's actually like to drive in Chiang Mai. Traffic, rules, and survival tips.",
        "img": "images/chiang-mai-ambassador-chiangmaiambassador-Chiang-Mai-Ambassador-driving-1.webp",
        "tags": ["guides", "transport", "motorbike"],
    },
    {
        "path": "guides/chiang-mai-football-club.html",
        "title": "Chiang Mai Football Club",
        "desc": "Watch live football in Chiang Mai. Stadium guide, ticket prices, and match atmosphere.",
        "img": "images/chiang-mai-ambassador-chiangmaiambassador-Chiang-Mai-Ambassador-football-1.webp",
        "tags": ["guides", "sport", "lifestyle"],
    },
    {
        "path": "guides/chiang-mai-insurance.html",
        "title": "Health Insurance in Chiang Mai",
        "desc": "What insurance expats use in Chiang Mai. Options, prices, and what to watch out for.",
        "img": "images/chiang-mai-ambassador-chiangmaiambassador-Chiang-Mai-Ambassador-insurance-1.webp",
        "tags": ["guides", "health", "finance"],
    },
    {
        "path": "guides/chiang-mai-road-rules.html",
        "title": "Chiang Mai Road Rules",
        "desc": "Traffic laws, road rules, and practical driving knowledge for Chiang Mai.",
        "img": "images/chiang-mai-ambassador-chiangmaiambassador-Chiang-Mai-Ambassador-road-rules-1.webp",
        "tags": ["guides", "transport", "motorbike"],
    },
    {
        "path": "guides/flat-tire.html",
        "title": "Got a Flat Tire in Chiang Mai?",
        "desc": "What to do when you get a flat tyre in Chiang Mai. Repair shops, costs, and roadside tips.",
        "img": "images/chiang-mai-ambassador-chiangmaiambassador-Chiang-Mai-Ambassador-flat-tire-1.webp",
        "tags": ["guides", "motorbike", "transport"],
    },
    {
        "path": "guides/license-plates.html",
        "title": "Understanding Thai License Plates",
        "desc": "What the colours and characters on Thai license plates actually mean.",
        "img": "images/chiang-mai-ambassador-chiangmaiambassador-Chiang-Mai-Ambassador-license-plates-1.webp",
        "tags": ["guides", "transport", "thai"],
    },
    {
        "path": "guides/motorcycle-registration-transfer.html",
        "title": "Motorbike Registration Transfer",
        "desc": "How to transfer a motorbike registration in Chiang Mai when you buy a second-hand bike.",
        "img": "images/chiang-mai-ambassador-chiangmaiambassador-Chiang-Mai-Ambassador-20.webp",
        "tags": ["guides", "motorbike", "transport"],
    },
    {
        "path": "guides/motorcycle-rentals.html",
        "title": "Motorbike Rentals in Chiang Mai",
        "desc": "Best places to rent a motorbike in Chiang Mai. Prices, insurance, and what to check before you ride.",
        "img": "images/chiang-mai-ambassador-chiangmaiambassador-Chiang-Mai-Ambassador-motorbike-rentals-1.webp",
        "tags": ["guides", "motorbike", "transport"],
    },
    {
        "path": "guides/red-cross-blood-bank-chiang-mai.html",
        "title": "Chiang Mai Red Cross Blood Bank",
        "desc": "Everything you need to know about the Red Cross Blood Bank in Chiang Mai.",
        "img": "images/chiang-mai-ambassador-chiangmaiambassador-Chiang-Mai-Ambassador-Red-Cross-blood-bank-1.webp",
        "tags": ["guides", "health", "community"],
    },
    {
        "path": "guides/renting-a-motorbike-in-chiang-mai.html",
        "title": "Renting a Motorbike in Chiang Mai",
        "desc": "The complete guide to renting a motorbike safely in Chiang Mai.",
        "img": "images/chiang-mai-ambassador-chiangmaiambassador-Chiang-Mai-Ambassador-motorbike-1.webp",
        "tags": ["guides", "motorbike", "transport"],
    },
    {
        "path": "guides/run-for-relief.html",
        "title": "Run for Relief: Chiang Mai",
        "desc": "Chiang Mai's charity fun run. What it is, how to join, and why it matters.",
        "img": "images/chiang-mai-ambassador-chiangmaiambassador-Chiang-Mai-Ambassador-run-for-relief-1.webp",
        "tags": ["guides", "community", "sport"],
    },
    {
        "path": "guides/tdac-thailand-digital-arrival-card.html",
        "title": "Thailand Digital Arrival Card (TDAC)",
        "desc": "How to complete the Thailand Digital Arrival Card before you land. Step-by-step guide.",
        "img": "images/chiang-mai-ambassador-chiangmaiambassador-Chiang-Mai-Ambassador-TDAC-3.webp",
        "tags": ["guides", "visa", "travel"],
    },
    {
        "path": "guides/walking-street-markets.html",
        "title": "Chiang Mai Walking Street Markets",
        "desc": "Saturday and Sunday night markets in Chiang Mai. Where they are, what to buy, and best food stalls.",
        "img": "images/chiang-mai-ambassador-chiangmaiambassador-Chiang-Mai-Ambassador-walking-street-markets-1.webp",
        "tags": ["guides", "markets", "lifestyle"],
    },
    {
        "path": "guides/wing-41-pass.html",
        "title": "Wing 41 Airport Pass for Motorbikes",
        "desc": "The Wing 41 pass lets you ride your motorbike through the airport shortcut. Here's how to get it.",
        "img": "images/chiang-mai-ambassador-chiangmaiambassador-Chiang-Mai-Ambassador-wing-41-pass-1.webp",
        "tags": ["guides", "motorbike", "transport"],
    },
    {
        "path": "guides/work-permit-medical-certificate.html",
        "title": "Work Permit Medical Certificate Chiang Mai",
        "desc": "Where to get a medical certificate for your Thai work permit in Chiang Mai. Costs and process.",
        "img": "images/chiang-mai-ambassador-chiangmaiambassador-Chiang-Mai-Ambassador-medical-1.webp",
        "tags": ["guides", "visa", "work"],
    },
    # LIFESTYLE
    {
        "path": "lifestyle/alcohol-observations-of-a-non-drinker.html",
        "title": "Alcohol in Thailand: A Non-Drinker's View",
        "desc": "What expat drinking culture is really like in Chiang Mai, from someone who doesn't drink.",
        "img": "images/chiang-mai-ambassador-chiangmaiambassador-Chiang-Mai-Ambassador-alcohol-1.webp",
        "tags": ["lifestyle", "culture"],
    },
    {
        "path": "lifestyle/chiang-mai-arrival.html",
        "title": "Arriving in Chiang Mai: First Steps",
        "desc": "What to do in your first 48 hours in Chiang Mai. SIM card, accommodation, getting around.",
        "img": "images/chiang-mai-ambassador-arrival.webp",
        "tags": ["lifestyle", "arrival", "travel"],
    },
    {
        "path": "lifestyle/currency-in-and-out-of-thailand.html",
        "title": "Thai Baht: Currency In and Out of Thailand",
        "desc": "ATMs, money changers, and the best ways to handle Thai Baht.",
        "img": "images/chiang-mai-ambassador-chiangmaiambassador-Chiang-Mai-Ambassador-currency-1.webp",
        "tags": ["lifestyle", "finance", "travel"],
    },
    {
        "path": "lifestyle/expat-breakfast-club.html",
        "title": "Chiang Mai Expat Breakfast Club",
        "desc": "The weekly Chiang Mai Expat Breakfast Club. Who goes, what to expect, and why it's worth it.",
        "img": "images/chiang-mai-ambassador-chiangmaiambassador-Chiang-Mai-Ambassador-Chiang-Mai-Expats-Club-Breakfast-CEC-10.webp",
        "tags": ["lifestyle", "community", "social"],
    },
    {
        "path": "lifestyle/learning-languages.html",
        "title": "Learning Languages in Chiang Mai",
        "desc": "Learning Thai and other languages in Chiang Mai. Schools, apps, and the expat approach.",
        "img": "images/chiang-mai-ambassador-chiangmaiambassador-Chiang-Mai-Ambassador-learning-languages-1.webp",
        "tags": ["lifestyle", "learning", "language"],
    },
    {
        "path": "lifestyle/life-budget-chiang-mai.html",
        "title": "Life on a Budget in Chiang Mai",
        "desc": "Real costs for living in Chiang Mai. Rent, food, transport, and what you actually need.",
        "img": "images/chiang-mai-ambassador-chiangmaiambassador-Chiang-Mai-Ambassador-152.webp",
        "tags": ["lifestyle", "finance", "budget"],
    },
    {
        "path": "lifestyle/smoky-season-chiang-mai.html",
        "title": "Smoky Season in Chiang Mai",
        "desc": "What the smoky season is really like in Chiang Mai. When it happens, how bad it gets, and how to cope.",
        "img": "images/chiang-mai-ambassador-chiangmaiambassador-Chiang-Mai-Ambassador-smoky-season-1.webp",
        "tags": ["lifestyle", "health", "chiang-mai"],
    },
    {
        "path": "lifestyle/songkran.html",
        "title": "Songkran in Chiang Mai",
        "desc": "Chiang Mai's Songkran water festival is the biggest in Thailand. What to expect and how to survive it.",
        "img": "images/chiang-mai-ambassador-chiangmaiambassador-Chiang-Mai-Ambassador-Songkran-1.webp",
        "tags": ["lifestyle", "festival", "culture"],
    },
    {
        "path": "lifestyle/traveling-alone.html",
        "title": "Traveling Alone to Chiang Mai",
        "desc": "Solo travel in Chiang Mai. Safety, social scene, and making the most of it alone.",
        "img": "images/chiang-mai-ambassador-chiangmaiambassador-Chiang-Mai-Ambassador-traveling-alone-1.webp",
        "tags": ["lifestyle", "travel", "solo"],
    },
    {
        "path": "lifestyle/traveling-with-friends.html",
        "title": "Traveling with Friends to Chiang Mai",
        "desc": "Group travel dynamics in Chiang Mai. What works, what causes friction, and how to plan well.",
        "img": "images/chiang-mai-ambassador-chiangmaiambassador-Chiang-Mai-Ambassador-traveling-with-friends-1.webp",
        "tags": ["lifestyle", "travel"],
    },
    {
        "path": "lifestyle/vientiane-visa-run.html",
        "title": "Vientiane Visa Run from Chiang Mai",
        "desc": "How to do the Vientiane visa run from Chiang Mai. Flights, costs, and what to do there.",
        "img": "images/chiang-mai-ambassador-chiangmaiambassador-Chiang-Mai-Ambassador-vientiane-visa-run-1.webp",
        "tags": ["lifestyle", "visa", "travel"],
    },
    {
        "path": "lifestyle/us-expat-tax-guide.html",
        "title": "US Expat Tax Guide: Living in Thailand",
        "desc": "FBAR, FATCA, and US taxes for Americans living in Thailand. What you need to know.",
        "img": "images/chiang-mai-ambassador-chiangmaiambassador-US-Expat-Tax-Guide-chiang-mai-ambassador-chiangmaiambassador-thai-visa-thaivisa-tax-advice-us-expats-17.webp",
        "tags": ["lifestyle", "finance", "tax"],
    },
    {
        "path": "lifestyle/top-tips.html",
        "title": "Top Tips for Living in Chiang Mai",
        "desc": "The best practical tips for living well in Chiang Mai, from years of experience.",
        "img": "images/chiang-mai-ambassador-chiangmaiambassador-Chiang-Mai-Ambassador-13.webp",
        "tags": ["lifestyle", "tips", "guides"],
    },
    # VISA
    {
        "path": "visa/border-run-strategy.html",
        "title": "Border Run Strategy: Thailand",
        "desc": "How to plan your border runs for maximum visa-free days in Thailand.",
        "img": "images/chiang-mai-ambassador-chiangmaiambassador-Chiang-Mai-Ambassador-CM-Ambassador-cheapest-border-run-10.webp",
        "tags": ["visa", "border", "travel"],
    },
    {
        "path": "visa/business-visa.html",
        "title": "Thai Business Visa (Non-B)",
        "desc": "Everything about the Thai Non-Immigrant B (business) visa. Requirements, costs, and process.",
        "img": "images/chiang-mai-ambassador-chiangmaiambassador-Chiang-Mai-Ambassador-Visa.webp",
        "tags": ["visa", "business", "work"],
    },
    {
        "path": "visa/dtv-visa.html",
        "title": "Thailand DTV Visa: Digital Nomad Visa",
        "desc": "Thailand's Destination Thailand Visa for remote workers and digital nomads. Complete guide.",
        "img": "images/chiang-mai-ambassador-chiangmaiambassador-Chiang-Mai-Ambassador-Visa.webp",
        "tags": ["visa", "digital-nomad", "remote"],
    },
    {
        "path": "visa/ed-visa.html",
        "title": "Thai ED Visa: Student Visa Guide",
        "desc": "How to get and maintain a Thai Education visa in Chiang Mai. Requirements, schools, and extensions.",
        "img": "images/chiang-mai-ambassador-chiangmaiambassador-Chiang-Mai-Ambassador-Visa.webp",
        "tags": ["visa", "education", "study"],
    },
    {
        "path": "visa/ed-visa-combat-training.html",
        "title": "ED Visa via Combat Sports Training",
        "desc": "Getting a Thai ED visa through Muay Thai or combat sports training in Chiang Mai.",
        "img": "images/chiang-mai-ambassador-chiangmaiambassador-Chiang-Mai-Ambassador-Visa.webp",
        "tags": ["visa", "sport", "muay-thai"],
    },
    {
        "path": "visa/ed-visa-muay-thai.html",
        "title": "ED Visa via Muay Thai",
        "desc": "How to get a Thai ED visa through a registered Muay Thai gym in Chiang Mai.",
        "img": "images/chiang-mai-ambassador-chiangmaiambassador-Chiang-Mai-Ambassador-Visa.webp",
        "tags": ["visa", "sport", "muay-thai"],
    },
    {
        "path": "visa/ed-visa-thai-language.html",
        "title": "ED Visa via Thai Language Study",
        "desc": "Getting a Thai student visa through language school in Chiang Mai.",
        "img": "images/chiang-mai-ambassador-chiangmaiambassador-Chiang-Mai-Ambassador-Visa.webp",
        "tags": ["visa", "language", "study"],
    },
    {
        "path": "visa/ltr-visa.html",
        "title": "Thailand LTR Visa (Long-Term Resident)",
        "desc": "The Thailand Long-Term Resident visa. Who qualifies, what it costs, and how to apply.",
        "img": "images/chiang-mai-ambassador-chiangmaiambassador-Chiang-Mai-Ambassador-Visa.webp",
        "tags": ["visa", "retirement", "long-term"],
    },
    {
        "path": "visa/marriage-visa.html",
        "title": "Thai Marriage Visa",
        "desc": "Living in Thailand on a marriage visa. Requirements, renewal, and what to watch out for.",
        "img": "images/chiang-mai-ambassador-chiangmaiambassador-Chiang-Mai-Ambassador-Visa.webp",
        "tags": ["visa", "marriage", "long-term"],
    },
    {
        "path": "visa/retirement-visa.html",
        "title": "Thai Retirement Visa (Non-O-A)",
        "desc": "Complete guide to retiring in Thailand on a Non-Immigrant O-A visa.",
        "img": "images/chiang-mai-ambassador-chiangmaiambassador-Chiang-Mai-Ambassador-Visa.webp",
        "tags": ["visa", "retirement", "long-term"],
    },
    {
        "path": "visa/tourist-visa.html",
        "title": "Thai Tourist Visa",
        "desc": "When and how to get a Thai tourist visa. Who needs one and how to apply.",
        "img": "images/chiang-mai-ambassador-chiangmaiambassador-Chiang-Mai-Ambassador-Visa.webp",
        "tags": ["visa", "travel", "tourist"],
    },
    {
        "path": "visa/visa-exempt-vs-voa.html",
        "title": "Visa Exempt vs Visa on Arrival Thailand",
        "desc": "The difference between Thai visa exemption and visa on arrival. Which applies to you?",
        "img": "images/chiang-mai-ambassador-chiangmaiambassador-Chiang-Mai-Ambassador-Visa.webp",
        "tags": ["visa", "travel"],
    },
    {
        "path": "visa/volunteer-visa.html",
        "title": "Thailand Volunteer Visa",
        "desc": "Volunteering in Thailand legally. The volunteer visa options and how to qualify.",
        "img": "images/chiang-mai-ambassador-chiangmaiambassador-Chiang-Mai-Ambassador-Visa.webp",
        "tags": ["visa", "volunteer", "community"],
    },
]

# Fallback images that definitely exist
FALLBACK_IMAGES = [
    "images/chiang-mai-ambassador-chiangmaiambassador-Chiang-Mai-Ambassador-13.webp",
    "images/chiang-mai-ambassador-chiangmaiambassador-Chiang-Mai-Ambassador-116.webp",
    "images/chiang-mai-ambassador-chiangmaiambassador-Chiang-Mai-Ambassador-4.webp",
    "images/chiang-mai-ambassador-chiangmaiambassador-Chiang-Mai-Ambassador-152.webp",
    "images/chiang-mai-ambassador-chiangmaiambassador-Chiang-Mai-Ambassador-22.webp",
    "images/chiang-mai-ambassador-chiangmaiambassador-Chiang-Mai-Ambassador-23.webp",
    "images/chiang-mai-ambassador-chiangmaiambassador-Chiang-Mai-Ambassador-46.webp",
    "images/chiang-mai-ambassador-chiangmaiambassador-Chiang-Mai-Ambassador-109.webp",
]


def get_subdir(path):
    """Return the subdirectory prefix (e.g. 'food', 'visa', '') """
    parts = path.split("/")
    if len(parts) > 1:
        return parts[0]
    return ""


def relative_img(img_path, page_path):
    """Convert images/... path to relative from page location."""
    depth = len(page_path.split("/")) - 1
    prefix = "../" * depth
    return prefix + img_path


def relative_link(target_path, from_path):
    """Build relative href from from_path to target_path."""
    from_dir = "/".join(from_path.split("/")[:-1])
    if not from_dir:
        return target_path
    target_parts = target_path.split("/")
    from_parts = from_dir.split("/") if from_dir else []
    # Simple relative path builder
    prefix = "../" * len(from_parts)
    return prefix + target_path


def pick_related(current_page, count=3):
    """Pick count related pages for current_page, prefer tag overlap."""
    current = next((p for p in PAGES if p["path"] == current_page), None)
    if not current:
        candidates = [p for p in PAGES if p["path"] != current_page]
        return random.sample(candidates, min(count, len(candidates)))

    current_tags = set(current["tags"])
    current_dir = get_subdir(current_page)

    # Score candidates by tag overlap + same directory bonus
    scored = []
    for p in PAGES:
        if p["path"] == current_page:
            continue
        overlap = len(current_tags & set(p["tags"]))
        same_dir = 1 if get_subdir(p["path"]) == current_dir else 0
        score = overlap * 2 + same_dir + random.uniform(0, 0.5)
        scored.append((score, p))

    scored.sort(key=lambda x: -x[0])
    return [p for _, p in scored[:count]]


def build_related_section(page_path):
    """Build HTML for the related posts section."""
    related = pick_related(page_path)
    cards = []
    for r in related:
        img = relative_img(r["img"], page_path)
        # Check if image exists, use fallback if not
        img_abs = ROOT / r["img"]
        if not img_abs.exists():
            fb = random.choice(FALLBACK_IMAGES)
            img = relative_img(fb, page_path)
        link = relative_link(r["path"], page_path)
        cards.append(f"""                <article class="blog-card reveal">
                    <img src="{img}" alt="{r['title']}" width="400" height="200">
                    <h3>{r['title']}</h3>
                    <p>{r['desc']}</p>
                    <a href="{link}" class="arrow-link">Read more &rarr;</a>
                </article>""")

    return f"""        <section class="blog-related container">
            <h2>More from the Ambassador</h2>
            <div class="blog-grid">
{chr(10).join(cards)}
            </div>
        </section>"""


def fix_visa_images(content, page_path):
    """Replace broken visa placeholder image paths with existing ones."""
    broken_visa_imgs = [
        "border-run-laos.webp",
        "visa-exempt-placeholder.webp",
        "dtv-visa-digital-nomad.webp",
        "ed-visa-thailand-study.webp",
        "retirement-visa-placeholder.webp",
        "retirement-visa-50plus.webp",
        "marriage-visa-thailand.webp",
        "tourist-visa-thailand.webp",
        "ltr-visa-elite.webp",
        "dtv-visa-placeholder.webp",
        "volunteer-visa-thailand.webp",
        "ed-visa-thailand.webp",
        "dtv-visa.webp",
        "retirement-visa.webp",
        "tourist-visa.webp",
        "ed-visa-thai-language.webp",
        "ed-visa-muay-thai.webp",
        "ed-visa-combat-training.webp",
    ]
    depth = len(page_path.split("/")) - 1
    prefix = "../" * depth

    for broken in broken_visa_imgs:
        # Match any path ending in this filename
        pattern = r'["\'][^"\']*' + re.escape(broken) + r'["\']'
        replacement = f'"{prefix}{random.choice(FALLBACK_IMAGES)}"'
        content = re.sub(pattern, replacement, content)
    return content


def fix_ed_visa_subpage_paths(content, page_path):
    """Fix ed-visa sub-pages that use ../../ when they're only 1 level deep."""
    if not page_path.startswith("visa/ed-visa-"):
        return content
    # These pages use ../../ for css, fonts, js, images - should be ../
    # Replace ../../css/, ../../js/, ../../fonts/, ../../images/, ../../favicon, ../../pages/
    content = content.replace("../../css/", "../css/")
    content = content.replace("../../js/", "../js/")
    content = content.replace("../../fonts/", "../fonts/")
    content = content.replace("../../images/", "../images/")
    content = content.replace("../../favicon.svg", "../favicon.svg")
    content = content.replace("../../pages/", "../pages/")
    return content


def fix_old_tag_links(content, page_path):
    """Remove or fix old WordPress-style tag links that point to nonexistent files."""
    # These are bare links in tags sections that don't have proper paths
    # They appear in <div class="blog-tags"> or similar
    # Pattern: href="somefile.html" where somefile is an old tag
    # These are NOT in the related posts section (which we rebuild)
    # They appear in the tags cloud - just remove broken ones that point nowhere

    # Known broken bare links that are old WP tags (no path prefix, point to nothing)
    old_tags = [
        "digital-nomads.html", "answers-to-questions.html", "bakery.html",
        "basics.html", "chiang-mai.html", "chiang-mai-ambassador.html",
        "community.html", "eating.html", "foreigner.html", "good-info.html",
        "groups.html", "holiday.html", "information.html", "life-in-chiang-mai.html",
        "motorbike.html", "movies.html", "moving.html", "networking.html",
        "new-to-chiang-mai.html", "nomads.html", "organic.html", "pat.html",
        "people-to-meet.html", "search-before-asking.html", "tourist.html",
        "vegetables.html", "buffet.html", "dinner.html", "food.html",
        "german-food.html", "germany.html", "great-food.html", "lunch.html",
        "all-natural.html", "peanut-butter.html", "live-in-chiang-mai.html",
        "desserts.html", "experience.html", "quiet-atmosphere.html", "salads.html",
        "staying-in-thailand.html", "very-nice-dinner.html", "5-star.html",
        "american-cuisine.html", "expat.html", "pizza.html", "great-food.html",
        "coffee.html", "social.html", "vegetarian.html", "be-a-hero.html",
        "blood-bank.html", "activities.html", "waterfalls.html", "budget.html",
        "finances.html", "hospital.html", "traveling-tips.html",
        "bargains.html", "must-do.html", "must-see.html", "shopping.html",
        "weekend.html", "airport.html", "hacks.html", "vehicles.html",
        "breakfast.html", "expat-club.html", "expats.html", "friday.html",
        "friends.html", "meetings.html", "retirees.html", "money-exchange.html",
        "currency.html", "money.html", "smoke.html", "smoky-season.html",
        "alone.html", "traveling.html", "aitaxadvisers.html",
        "american-international-tax-advisers.html", "american-tax.html",
        "benefits-for-expats.html", "business-class-asia.html",
        "business-formation.html", "businessclassasia.html", "company-formation.html",
        "expat-tax.html", "fatca.html", "fbar.html", "investment-planning.html",
        "payoneer.html", "stimulus-checks.html", "streamline-filing-program.html",
        "tax-for-expats.html", "tax-planning.html", "tax-returns.html",
        "us-tax.html", "us-tax-treaty.html", "visa.html", "visa-run.html",
        "border-run.html", "dtv.html", "laos-border.html", "tdac.html",
        "thailand-digital-arrival-card.html", "getting-a-license.html",
        "license.html", "motorbikes.html", "rentals.html", "riding.html",
        "scams.html", "motorbike-renting.html", "problems.html", "renting.html",
        "thailand.html", "daily-life.html", "good-to-check-out.html",
        "life.html", "thai-food.html", "culture.html", "respect.html",
        "how-to.html", "top-tips.html",
    ]

    for tag in old_tags:
        # Only remove if it's a bare link (no path separator before it)
        # Match href="tag.html" but not href="../something/tag.html"
        pattern = r'href="' + re.escape(tag) + r'"'
        content = re.sub(pattern, 'href="#"', content)

    return content


def fix_known_broken_links(content, page_path):
    """Fix specific known broken links to correct paths."""
    depth = len(page_path.split("/")) - 1
    prefix = "../" * depth

    # Files that exist but at wrong relative path
    known_fixes = {
        # Guides
        "walking-street-markets.html": f"{prefix}guides/walking-street-markets.html",
        "expat-breakfast-club.html": f"{prefix}lifestyle/expat-breakfast-club.html",
        "getting-social-in-chiang-mai.html": f"{prefix}getting-social-in-chiang-mai.html",
        # Motorbike
        "motorbike-registration-chiang-mai.html": f"{prefix}motorbike-registration-chiang-mai.html",
        "chiang-mai-motorbike-registration-transfer.html": f"{prefix}guides/motorcycle-registration-transfer.html",
        "motorcycle-registration-transfer.html": f"{prefix}guides/motorcycle-registration-transfer.html",
        "motorcycle-rentals.html": f"{prefix}guides/motorcycle-rentals.html",
        # Root pages
        "best-chiang-mai.html": f"{prefix}best-chiang-mai.html",
        "real-thai-restaurant.html": f"{prefix}food/real-thai-restaurant.html",
        "chiang-mai-insurance.html": f"{prefix}guides/chiang-mai-insurance.html",
        "food-delivery-services.html": f"{prefix}food/food-delivery-services.html",
        "cheapest-border-run-chiang-mai.html": f"{prefix}cheapest-border-run-chiang-mai.html",
        "learning-languages.html": f"{prefix}lifestyle/learning-languages.html",
        # Visa
        "cost-of-living.html": f"{prefix}pages/cost-of-living.html",
    }

    for broken, fixed in known_fixes.items():
        # Only match bare filenames (not already prefixed)
        pattern = r'href="' + re.escape(broken) + r'"'
        replacement = f'href="{fixed}"'
        content = re.sub(pattern, replacement, content)

    return content


def fix_css_style_link(content, page_path):
    """Fix stray ../css/style.css references."""
    depth = len(page_path.split("/")) - 1
    prefix = "../" * depth
    content = content.replace('href="../css/style.css"', f'href="{prefix}css/blog.css"')
    content = content.replace('href="css/style.css"', f'href="{prefix}css/blog.css"')
    return content


def fix_related_posts_section(content, page_path):
    """Replace the entire related posts section with fresh relevant content."""
    pattern = r'<section class="blog-related container">.*?</section>'
    new_section = build_related_section(page_path)
    result = re.sub(pattern, new_section, content, flags=re.DOTALL)
    return result


def check_tldr_needs_photo(content, page_path):
    """Check if page needs a TL;DR photo."""
    tldr = re.search(r'Quick Summary.*?TL;DR|tldr', content, re.IGNORECASE)
    if not tldr:
        return False
    area = content[max(0, tldr.start()-600):tldr.start()+300]
    if 'img-right-small' not in area:
        return True
    # Has the class but check if empty figure
    if re.search(r'img-right-small[^"]*">\s*</figure>', area):
        return True
    # Has img with src
    if re.search(r'img-right-small.*?<img[^>]+src=["\'][^"\']+["\']', area, re.DOTALL):
        return False
    return True


def process_file(filepath):
    """Process a single HTML file."""
    rel = filepath.relative_to(ROOT)
    page_path = rel.as_posix()

    # Skip non-content pages
    skip = ["template.html", "pages/template.html", "MD/", "TEAM_NOTICE", "ENFORCEMENT",
            "visa/index.html", "chiang-mai/index.html", "guides/index.html",
            "lifestyle/index.html", "pages/disclaimer.html", "pages/privacy.html",
            "pages/terms.html", "pages/about.html"]
    if any(s in page_path for s in skip):
        return False, page_path

    content = filepath.read_text(encoding="utf-8", errors="ignore")
    original = content

    # Apply fixes in order
    content = fix_ed_visa_subpage_paths(content, page_path)
    content = fix_css_style_link(content, page_path)
    content = fix_visa_images(content, page_path)
    content = fix_known_broken_links(content, page_path)
    content = fix_old_tag_links(content, page_path)
    content = fix_related_posts_section(content, page_path)

    if content != original:
        filepath.write_text(content, encoding="utf-8")
        return True, page_path
    return False, page_path


def main():
    random.seed(42)  # Reproducible randomisation

    all_html = list(ROOT.rglob("*.html"))
    all_html = [f for f in all_html if "MD/" not in f.as_posix().replace("\\", "/")]

    print(f"Processing {len(all_html)} HTML files...\n")

    tldr_needs = []
    fixed = []
    skipped = []

    for f in sorted(all_html):
        was_fixed, page_path = process_file(f)
        if was_fixed:
            fixed.append(page_path)
        else:
            skipped.append(page_path)

        # Check TL;DR
        content = f.read_text(encoding="utf-8", errors="ignore")
        if check_tldr_needs_photo(content, page_path):
            tldr_needs.append(page_path)

    print(f"Fixed: {len(fixed)} files")
    print(f"Unchanged: {len(skipped)} files")

    print("\n" + "=" * 60)
    print("PAGES NEEDING TL;DR PHOTO (content pages only)")
    print("=" * 60)
    # Filter to real content pages
    content_tldr = [p for p in tldr_needs if not any(
        s in p for s in ["template", "disclaimer", "privacy", "terms", "MD/", "index.html"]
    )]
    for p in content_tldr:
        print(f"  {p}")
    print(f"\nTotal: {len(content_tldr)} pages")

    print("\n" + "=" * 60)
    print("FILES FIXED")
    print("=" * 60)
    for f in fixed:
        print(f"  {f}")


if __name__ == "__main__":
    main()
