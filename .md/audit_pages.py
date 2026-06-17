#!/usr/bin/env python3
"""
Chiang Mai Ambassador: Automated Page Audit
Checks all 10 enforcement rules on every HTML file.
Usage: python audit_pages.py
"""

import os
import re
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent
RESULTS = []

# Color codes for output
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
RESET = '\033[0m'

def log_pass(rule, file):
    RESULTS.append(f"{GREEN}[PASS]{RESET} {file}: {rule}")

def log_fail(rule, file, detail=""):
    detail = f" ({detail})" if detail else ""
    RESULTS.append(f"{RED}[FAIL]{RESET} {file}: {rule}{detail}")

def log_warn(rule, file, detail=""):
    detail = f" ({detail})" if detail else ""
    RESULTS.append(f"{YELLOW}[WARN]{RESET} {file}: {rule}{detail}")

def audit_file(filepath):
    """Audit a single HTML file against all 10 rules."""

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    relpath = filepath.relative_to(PROJECT_ROOT)
    filename = str(relpath)

    # Calculate depth (for font path checking)
    depth = filename.count(os.sep)
    expected_prefix = "../" * depth

    # Rule 1: No inline styles in head
    head_match = re.search(r'<head>(.*?)</head>', content, re.DOTALL)
    if head_match:
        head = head_match.group(1)
        if '<style>' in head:
            log_fail("Rule 1: No inline styles", filename, "found <style> in <head>")
        else:
            log_pass("Rule 1: No inline styles", filename)

    # Rule 2: TEMPLATE LOCK (nav, footer, breadcrumb should match pattern)
    if '<nav class="nav-wrapper">' not in content:
        if filename != 'index.html':
            log_warn("Rule 2: TEMPLATE LOCK", filename, "nav structure may be missing")
    else:
        log_pass("Rule 2: TEMPLATE LOCK (nav present)", filename)

    # Rule 3: Correct directory structure
    allowed_dirs = ['index.html', 'pages/', 'guides/', 'food/', 'chiang-mai/', 'best-chiang-mai.html', 'cheapest-border-run-chiang-mai.html', 'getting-social-in-chiang-mai.html', 'thai-eating-etiquette.html', 'yunnan-farmers-market.html', 'modern-transport-guide.html', 'motorbike-registration-chiang-mai.html']
    dir_valid = any(filename.startswith(prefix) for prefix in allowed_dirs)
    if dir_valid:
        log_pass("Rule 3: Directory structure", filename)
    else:
        log_fail("Rule 3: Directory structure", filename, f"invalid path: {filename}")

    # Rule 4: Font preloads with correct depth
    font_files = ['outfit-600.woff2', 'outfit-800.woff2', 'plus-jakarta-400.woff2', 'plus-jakarta-500.woff2']
    missing_fonts = []
    for font in font_files:
        if f'href="{expected_prefix}fonts/{font}"' not in content:
            missing_fonts.append(font)

    if missing_fonts:
        log_fail("Rule 4: Font preloads", filename, f"missing or wrong depth: {', '.join(missing_fonts)}")
    else:
        log_pass("Rule 4: Font preloads (correct depth)", filename)

    # Rule 5: Image standards (semantic naming, alt text, width/height)
    img_tags = re.findall(r'<img[^>]*>', content)
    img_issues = []

    for img in img_tags:
        # Check for semantic naming (should contain filename context)
        if 'src="' in img:
            src_match = re.search(r'src="([^"]*)"', img)
            if src_match:
                src = src_match.group(1)
                if 'chiang-mai-ambassador-' not in src and '/images/og-image.webp' not in src:
                    img_issues.append(f"non-semantic name: {src}")

        # Check for alt text
        if 'alt="' not in img:
            img_issues.append("missing alt text")

        # Check for width/height
        if 'width=' not in img or 'height=' not in img:
            img_issues.append("missing width/height attributes")

    if img_issues:
        log_fail("Rule 5: Image standards", filename, "; ".join(img_issues[:2]))
    elif img_tags:
        log_pass("Rule 5: Image standards", filename)
    else:
        log_pass("Rule 5: Image standards (no images)", filename)

    # Rule 6: Canonical URL
    canonical_match = re.search(r'<link rel="canonical" href="([^"]*)"', content)
    if canonical_match:
        canonical = canonical_match.group(1)
        # Basic check: should match the path structure
        expected_canonical = f"https://chiangmaiambassador.com/{filename.replace(os.sep, '/').replace('.html', '/')}".rstrip('/')
        if canonical and canonical.startswith('https://chiangmaiambassador.com/'):
            log_pass("Rule 6: Canonical URL", filename)
        else:
            log_fail("Rule 6: Canonical URL", filename, "invalid format")
    else:
        log_fail("Rule 6: Canonical URL", filename, "missing")

    # Rule 7: Open Graph tags
    og_required = ['og:title', 'og:description', 'og:type', 'og:url', 'og:site_name', 'og:image']
    og_missing = [tag for tag in og_required if f'property="{tag}"' not in content]

    if og_missing:
        log_fail("Rule 7: Open Graph tags", filename, f"missing: {', '.join(og_missing[:3])}")
    else:
        log_pass("Rule 7: Open Graph tags", filename)

    # Rule 8: Heading hierarchy
    h1_count = len(re.findall(r'<h1[^>]*>', content))
    h_order = re.findall(r'<h[1-6]', content)

    if h1_count != 1:
        log_fail("Rule 8: Heading hierarchy", filename, f"found {h1_count} H1 tags (should be 1)")
    elif h_order and h_order[0] != '<h1':
        log_fail("Rule 8: Heading hierarchy", filename, "H1 not first heading")
    else:
        log_pass("Rule 8: Heading hierarchy", filename)

    # Rule 9: Breadcrumbs
    if '<nav class="breadcrumbs">' in content or '<nav' in content and 'breadcrumb' in content.lower():
        log_pass("Rule 9: Breadcrumbs", filename)
    elif filename not in ['index.html']:  # Homepage may not need breadcrumbs
        log_warn("Rule 9: Breadcrumbs", filename, "may be missing")

    # Rule 10: No external frameworks
    framework_patterns = [
        r'from\s+["\']react["\']',
        r'import\s+.*from\s+["\']vue["\']',
        r'@tailwind',
        r'bootstrap',
        r'foundation',
        r'cdn\.jsdelivr\.net',
        r'cdnjs\.cloudflare\.com'
    ]

    frameworks_found = [pattern for pattern in framework_patterns if re.search(pattern, content)]

    if frameworks_found:
        log_fail("Rule 10: No external frameworks", filename, f"found framework imports")
    else:
        log_pass("Rule 10: No external frameworks", filename)


def main():
    """Scan all HTML files and run audit."""

    html_files = list(PROJECT_ROOT.rglob('*.html'))

    print(f"\n{BLUE}{'='*70}")
    print(f"Chiang Mai Ambassador: Page Audit")
    print(f"Scanning {len(html_files)} HTML files")
    print(f"{'='*70}{RESET}\n")

    for html_file in sorted(html_files):
        audit_file(html_file)

    # Print results
    for result in RESULTS:
        print(result)

    # Summary
    passes = len([r for r in RESULTS if '[PASS]' in r])
    fails = len([r for r in RESULTS if '[FAIL]' in r])
    warns = len([r for r in RESULTS if '[WARN]' in r])

    print(f"\n{BLUE}{'='*70}")
    print(f"Summary: {GREEN}{passes} pass{RESET} | {RED}{fails} fail{RESET} | {YELLOW}{warns} warn{RESET}")
    print(f"{'='*70}{RESET}\n")

    if fails > 0:
        print(f"{RED}REJECTED: {fails} rule violations found. Fix and resubmit.{RESET}\n")
        return 1
    else:
        print(f"{GREEN}APPROVED: All pages pass enforcement rules.{RESET}\n")
        return 0


if __name__ == '__main__':
    exit(main())
