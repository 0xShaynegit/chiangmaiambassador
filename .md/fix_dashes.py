#!/usr/bin/env python3
"""
Replace em dashes (—) and en dashes (–) with periods or commas
Per CLAUDE.md: NEVER USE EM DASHES (—) OR EN DASHES (–)
"""

from pathlib import Path

def fix_dashes_in_file(filepath):
    """Replace dashes with appropriate punctuation."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content

    # Replace em dashes with periods (for separating clauses)
    # Em dash (—) often separates independent clauses
    content = content.replace(' — ', '. ')
    content = content.replace('—', '.')

    # Replace en dashes with hyphens (for ranges) or periods
    # En dash (–) is often used for ranges or connections
    content = content.replace(' – ', '. ')
    content = content.replace('–', '-')

    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

def get_all_html_files(project_root):
    """Get all HTML files to check."""
    files = []
    for html_file in Path(project_root).glob('*.html'):
        if html_file.name not in ['template.html', 'hero-effects-test.html']:
            files.append(html_file.name)
    for folder in ['food', 'guides', 'lifestyle', 'pages']:
        for html_file in Path(project_root).glob(f'{folder}/*.html'):
            files.append(f"{folder}/{html_file.name}")
    return sorted(files)

def main():
    project_root = Path(__file__).parent.parent

    print("Removing em/en dashes from all pages...\n")

    all_files = get_all_html_files(project_root)
    fixed_count = 0

    for filepath_rel in all_files:
        filepath = project_root / filepath_rel
        if fix_dashes_in_file(filepath):
            print(f"[FIXED] {filepath_rel}")
            fixed_count += 1

    print(f"\nTotal files fixed: {fixed_count}/{len(all_files)}")

if __name__ == "__main__":
    main()
