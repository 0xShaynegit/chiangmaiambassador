#!/usr/bin/env python3
"""
Batch OG Tags Application: Add og:title, og:description, og:url, og:type, og:image to 54 pages.
Backs up originals, applies changes, logs results.
"""

import os
import re
from pathlib import Path
from datetime import datetime
import shutil

BASE_URL = "https://chiangmaiambassador.com"
OG_IMAGE_URL = f"{BASE_URL}/images/og-image.webp"

def get_canonical_url(filepath_rel):
    """Convert file path to canonical URL."""
    # Remove .html extension and convert path
    path = filepath_rel.replace('\\', '/').replace('.html', '').lower()

    # Handle special cases
    if path == 'index':
        return f"{BASE_URL}/"

    # All URLs have trailing slash
    if not path.endswith('/'):
        path = path + '/'

    return f"{BASE_URL}/{path}"

def get_page_type(filepath_rel):
    """Determine og:type based on page category."""
    if filepath_rel.startswith('guides/') or filepath_rel.startswith('lifestyle/') or filepath_rel.startswith('food/'):
        return "article"
    else:
        return "website"

def extract_title_and_description(content):
    """Extract title and description from HTML content."""
    title_match = re.search(r'<title>(.*?)</title>', content)
    desc_match = re.search(r'<meta name="description" content="([^"]*)">', content)

    title = title_match.group(1) if title_match else "Chiang Mai Ambassador"
    description = desc_match.group(1) if desc_match else "Premium guide for expats and visitors in Chiang Mai, Thailand."

    return title, description

def generate_og_tags(title, description, url, page_type):
    """Generate OG tag HTML."""
    og_tags = f'''    <meta property="og:title" content="{title}">
    <meta property="og:description" content="{description}">
    <meta property="og:type" content="{page_type}">
    <meta property="og:url" content="{url}">
    <meta property="og:site_name" content="Chiang Mai Ambassador">
    <meta property="og:image" content="{OG_IMAGE_URL}">
    <meta property="og:image:width" content="1200">
    <meta property="og:image:height" content="630">'''

    return og_tags

def get_all_html_files(project_root):
    """Get all HTML files to process (54 pages)."""
    files = []

    # Root pages
    for html_file in Path(project_root).glob('*.html'):
        # Skip template files
        if html_file.name not in ['template.html', 'hero-effects-test.html']:
            rel_path = html_file.name
            files.append(rel_path)

    # Subdirectory pages
    for folder in ['food', 'guides', 'lifestyle', 'pages']:
        for html_file in Path(project_root).glob(f'{folder}/*.html'):
            rel_path = f"{folder}/{html_file.name}"
            files.append(rel_path)

    return sorted(files)

def apply_og_tags(project_root):
    """Apply OG tags to all HTML files."""
    project_root = Path(project_root)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_dir = project_root / f"backup_og_{timestamp}"
    backup_dir.mkdir(exist_ok=True)

    log = []
    successful = 0
    failed = 0

    log.append(f"OG Tags Batch Job started at {datetime.now().isoformat()}")
    log.append(f"Backup directory: {backup_dir}\n")

    files = get_all_html_files(project_root)
    log.append(f"Total pages to process: {len(files)}\n")

    for filepath_rel in files:
        filepath = project_root / filepath_rel

        try:
            # Read original file
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()

            # Create backup
            backup_file = backup_dir / filepath_rel.replace('/', '_')
            backup_file.parent.mkdir(parents=True, exist_ok=True)
            with open(backup_file, 'w', encoding='utf-8') as f:
                f.write(content)

            # Extract title and description
            title, description = extract_title_and_description(content)

            # Generate values
            canonical_url = get_canonical_url(filepath_rel)
            page_type = get_page_type(filepath_rel)
            og_tags = generate_og_tags(title, description, canonical_url, page_type)

            # Check if OG tags already exist
            if 'og:title' in content:
                # Replace existing OG tags
                og_pattern = r'    <meta property="og:title".*?</meta>\n(?:    <meta property="og:[^"]*"[^>]*>\n)*'
                content = re.sub(og_pattern, og_tags + '\n', content)
            else:
                # Insert after canonical tag (or after meta robots if no canonical)
                if '<link rel="canonical"' in content:
                    canonical_pos = content.find('</a>')
                    insert_pos = content.find('\n', content.find('<link rel="canonical"')) + 1
                else:
                    insert_pos = content.find('<meta name="robots"')
                    insert_pos = content.find('\n', insert_pos) + 1

                # Find the correct place (after robots meta tag)
                content = re.sub(
                    r'(<meta name="robots"[^>]*>\n)',
                    r'\1' + og_tags + '\n',
                    content,
                    count=1
                )

            # Write back
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)

            successful += 1
            log.append(f"OK: {filepath_rel} -> {canonical_url}")

        except Exception as e:
            failed += 1
            log.append(f"ERROR: {filepath_rel} - {str(e)}")

    # Write log
    log_file = project_root / "MD" / f"OG_BATCH_LOG_{timestamp}.txt"
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
    apply_og_tags(project_root)
