"""
Add "Ready to apply?" CTA callout-info blocks to visa/ pages.
Inserts a styled callout-info block just before </div></div></article> close.
"""
import re
import os

BASE = r'C:\ZZZWebsites\chiangmaiambassador'

PAGES = {
    'visa/border-run-strategy.html': ('https://cmlocals.com/border-run/', 'Border Run Guide'),
    'visa/business-visa.html': ('https://cmlocals.com/business-visa/', 'Business Visa Guide'),
    'visa/dtv-visa.html': ('https://cmlocals.com/dtv-visa/', 'DTV Visa Guide'),
    'visa/ed-visa.html': ('https://cmlocals.com/ed-visa/', 'ED Visa Guide'),
    'visa/ed-visa-combat-training.html': ('https://cmlocals.com/ed-visa/hand-to-hand-combat/', 'ED Visa Combat Training Guide'),
    'visa/ed-visa-muay-thai.html': ('https://cmlocals.com/ed-visa/muay-thai/', 'ED Visa Muay Thai Guide'),
    'visa/ed-visa-thai-language.html': ('https://cmlocals.com/ed-visa/thai-language/', 'ED Visa Thai Language Guide'),
    'visa/ltr-visa.html': ('https://cmlocals.com/ltr-visa/', 'LTR Visa Guide'),
    'visa/marriage-visa.html': ('https://cmlocals.com/marriage-visa/', 'Marriage Visa Guide'),
    'visa/retirement-visa.html': ('https://cmlocals.com/retirement-visa/', 'Retirement Visa Guide'),
    'visa/tourist-visa.html': ('https://cmlocals.com/tourist-visa/', 'Tourist Visa Guide'),
    'visa/visa-exempt-vs-voa.html': ('https://cmlocals.com/visa-exempt/', 'Visa Exempt Guide'),
    'visa/volunteer-visa.html': ('https://cmlocals.com/volunteer-visa/', 'Volunteer Visa Guide'),
}

# Skip if already has the standardised callout-info CTA
ALREADY_DONE = re.compile(r'<div class="callout-info">.*?Ready to apply\?', re.DOTALL)

# The closing sequence we target: end of blog-body -> </div> article wrapper -> </article>
# Pattern: closing </div> of blog-body, then </div> of article inner, then </article>
CLOSE_PATTERN = re.compile(
    r'(\s*</div>\s*\n\s*</div>\s*\n\s*</article>)',
    re.DOTALL
)

for rel_path, (url, label) in PAGES.items():
    full_path = os.path.join(BASE, rel_path)
    if not os.path.exists(full_path):
        print(f'MISSING FILE: {rel_path}')
        continue

    with open(full_path, 'r', encoding='utf-8', errors='replace') as f:
        content = f.read()

    if ALREADY_DONE.search(content):
        print(f'SKIP (already has CTA): {rel_path}')
        continue

    cta_block = f'''
                    <div class="callout-info">
                        <p><strong>Ready to apply?</strong> Full step-by-step guide, document checklist, and current processing times at <a href="{url}" target="_blank" rel="noopener">CMLocals: {label}</a>.</p>
                    </div>'''

    # Find the first </article> that closes the main article
    # Strategy: find <article and then its closing </article>
    article_start = content.find('<article')
    if article_start == -1:
        print(f'NO ARTICLE TAG: {rel_path}')
        continue

    article_end = content.find('</article>', article_start)
    if article_end == -1:
        print(f'NO CLOSING ARTICLE: {rel_path}')
        continue

    # Find the </div></div> just before </article>
    before_article = content[article_start:article_end]
    # Insert CTA just before the last two closing divs before </article>
    inner_match = re.search(r'(\s*</div>\s*\n\s*</div>\s*)$', before_article)
    if not inner_match:
        print(f'NO MATCH for closing divs: {rel_path}')
        continue

    insert_pos = article_start + inner_match.start()
    new_content = content[:insert_pos] + '\n' + cta_block + content[insert_pos:]

    with open(full_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f'UPDATED: {rel_path}')
