#!/usr/bin/env python3
"""
Fix root page asset paths: remove incorrect ../ from root-level HTML files
"""

from pathlib import Path
import re

ROOT_PAGES = [
    'best-chiang-mai.html',
    'cheapest-border-run-chiang-mai.html',
    'getting-social-in-chiang-mai.html',
    'khun-joe-school.html',
    'motorbike-registration-chiang-mai.html',
    'thai-eating-etiquette.html',
    'understanding-thai-culture.html',
    'womens-prison-massage.html',
    'yunnan-farmers-market.html',
]

def fix_root_page(filepath):
    """Fix asset paths in root page."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content

    # Replace ../css/ with css/
    content = content.replace('href="../css/', 'href="css/')

    # Replace ../fonts/ with fonts/
    content = content.replace('href="../fonts/', 'href="fonts/')
    content = content.replace("href='../fonts/", "href='fonts/")

    # Replace ../images/ with images/
    content = content.replace('src="../images/', 'src="images/')

    # Replace ../js/ with js/
    content = content.replace('src="../js/', 'src="js/')

    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

def main():
    project_root = Path(__file__).parent.parent

    print("Fixing root page asset paths...\n")

    fixed_count = 0
    for page in ROOT_PAGES:
        filepath = project_root / page
        if filepath.exists():
            if fix_root_page(filepath):
                print(f"[FIXED] {page}")
                fixed_count += 1
            else:
                print(f"[OK] {page}")
        else:
            print(f"[MISSING] {page}")

    print(f"\nTotal fixed: {fixed_count}/{len(ROOT_PAGES)}")

if __name__ == "__main__":
    main()
