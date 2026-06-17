#!/usr/bin/env python3
"""
Image Alt Text Audit: Check all images for proper alt text
"""

import re
from pathlib import Path
from datetime import datetime

def audit_images(filepath):
    """Check images in file for alt text."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    issues = []
    images = []

    # Find all img tags
    img_pattern = r'<img[^>]*>'
    for match in re.finditer(img_pattern, content):
        img_tag = match.group(0)
        src_match = re.search(r'src="([^"]*)"', img_tag)
        alt_match = re.search(r'alt="([^"]*)"', img_tag)

        if src_match:
            src = src_match.group(1)
            alt_text = alt_match.group(1) if alt_match else None

            images.append({
                'src': src,
                'alt': alt_text,
                'has_alt': alt_match is not None,
                'alt_length': len(alt_text) if alt_text else 0
            })

            # Check issues
            if not alt_match:
                issues.append(f"Missing alt text: {src}")
            elif alt_text.lower() in ['image', 'photo', 'picture', 'img']:
                issues.append(f"Generic alt text: {src} (alt='{alt_text}')")
            elif len(alt_text) > 125:
                issues.append(f"Alt text too long: {src} ({len(alt_text)} chars)")

    return images, issues

def get_all_html_files(project_root):
    """Get all HTML files."""
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
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    log = []
    all_files = get_all_html_files(project_root)

    total_images = 0
    total_issues = 0
    files_with_images = 0
    files_with_issues = 0

    log.append(f"Image Alt Text Audit started at {datetime.now().isoformat()}")
    log.append(f"Total pages to check: {len(all_files)}\n")

    for filepath_rel in all_files:
        filepath = project_root / filepath_rel

        try:
            images, issues = audit_images(filepath)

            if images:
                files_with_images += 1
                total_images += len(images)

            if issues:
                files_with_issues += 1
                total_issues += len(issues)
                log.append(f"\n{filepath_rel} ({len(images)} images):")
                for issue in issues:
                    log.append(f"  - {issue}")

        except Exception as e:
            log.append(f"ERROR: {filepath_rel} - {str(e)}")

    # Summary
    log.append(f"\n{'='*60}")
    log.append("IMAGE ALT TEXT AUDIT SUMMARY")
    log.append(f"{'='*60}")
    log.append(f"Total pages checked: {len(all_files)}")
    log.append(f"Pages with images: {files_with_images}")
    log.append(f"Total images found: {total_images}")
    log.append(f"Pages with issues: {files_with_issues}")
    log.append(f"Total issues: {total_issues}")
    log.append(f"")

    if total_issues == 0:
        log.append("[PASS] All images have proper alt text.")
    else:
        log.append(f"[NEEDS WORK] {total_issues} alt text issue(s) found.")
        log.append(f"Fix rate needed: {((total_images - total_issues) / total_images * 100):.1f}%")

    log.append(f"\nCompleted: {datetime.now().isoformat()}")

    # Write log
    log_file = project_root / "MD" / f"IMAGE_ALT_AUDIT_{timestamp}.txt"
    with open(log_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(log))

    try:
        print('\n'.join(log))
    except UnicodeEncodeError:
        safe_log = [line.encode('ascii', 'replace').decode('ascii') for line in log]
        print('\n'.join(safe_log))

    print(f"\nLog file: {log_file}")

if __name__ == "__main__":
    main()
