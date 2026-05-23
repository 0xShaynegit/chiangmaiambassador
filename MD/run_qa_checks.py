#!/usr/bin/env python3
"""
Automated QA Checks: Link validation, alt text audit, meta tags verification
"""

import re
from pathlib import Path
from datetime import datetime
from urllib.parse import urlparse

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

def check_meta_tags(content):
    """Check for required meta tags."""
    issues = []
    if '<title>' not in content:
        issues.append("Missing title tag")
    if 'meta name="description"' not in content:
        issues.append("Missing meta description")
    if 'rel="canonical"' not in content:
        issues.append("Missing canonical tag")
    if 'og:title' not in content:
        issues.append("Missing OG title")
    if 'og:description' not in content:
        issues.append("Missing OG description")
    return issues

def check_images_alt_text(content):
    """Check for missing alt text on images."""
    issues = []
    img_pattern = r'<img[^>]*src="([^"]*)"[^>]*>'
    images = re.findall(img_pattern, content)

    for match in re.finditer(r'<img[^>]*>', content):
        img_tag = match.group(0)
        if 'alt=' not in img_tag:
            src_match = re.search(r'src="([^"]*)"', img_tag)
            if src_match:
                src = src_match.group(1)
                issues.append(f"Missing alt text: {src}")

    return issues

def check_internal_links(content, filepath_rel, all_files):
    """Check for broken internal links."""
    issues = []

    # Find all href references
    link_pattern = r'href="([^"]*)"'

    for match in re.finditer(link_pattern, content):
        href = match.group(1)

        # Skip external links, anchors, special protocols
        if href.startswith(('http', '#', 'mailto', 'tel', '/')):
            continue

        # Resolve relative path
        if filepath_rel.startswith(('food', 'guides', 'lifestyle', 'pages')):
            # Subfolder file
            if href.startswith('../'):
                # Going up one level (to root)
                resolved = href.replace('../', '')
            elif href.startswith('./'):
                # Current folder
                folder = filepath_rel.split('/')[0]
                resolved = f"{folder}/{href.replace('./', '')}"
            else:
                # Assume same folder
                folder = filepath_rel.split('/')[0]
                resolved = f"{folder}/{href}"
        else:
            # Root file
            resolved = href

        # Remove trailing slash for comparison
        resolved_clean = resolved.rstrip('/')

        # Check if file exists
        found = False
        for f in all_files:
            f_clean = f.replace('.html', '').rstrip('/')
            if f_clean == resolved_clean or f.rstrip('/') == resolved.rstrip('/'):
                found = True
                break

        if not found and resolved_clean and not '#' in resolved:
            issues.append(f"Broken link: {href} -> resolves to {resolved}")

    return issues

def check_external_links(content):
    """Check external links formatting."""
    issues = []

    # Find external links
    link_pattern = r'href="(https?://[^"]*)"'
    for match in re.finditer(link_pattern, content):
        href = match.group(1)
        # Check if it has target="_blank"
        # This is a simplified check
        if 'http://' in href and not href.startswith('https'):
            issues.append(f"Non-HTTPS link: {href}")

    return issues

def check_no_em_dashes(content):
    """Check for em dashes and en dashes."""
    issues = []
    if '—' in content:
        issues.append("Em dash (—) found")
    if '–' in content:
        issues.append("En dash (–) found")
    return issues

def run_qa_checks(project_root):
    """Run all QA checks."""
    project_root = Path(project_root)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    log = []
    all_files = get_all_html_files(project_root)

    log.append(f"QA Checks started at {datetime.now().isoformat()}")
    log.append(f"Total pages to check: {len(all_files)}\n")

    summary = {
        'meta_tag_issues': 0,
        'alt_text_issues': 0,
        'broken_links': 0,
        'external_link_issues': 0,
        'em_dash_issues': 0,
        'total_files_checked': 0,
        'pages_with_issues': 0
    }

    for filepath_rel in all_files:
        filepath = project_root / filepath_rel
        summary['total_files_checked'] += 1

        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()

            page_issues = []

            # Run all checks
            page_issues.extend(check_meta_tags(content))
            page_issues.extend(check_images_alt_text(content))
            page_issues.extend(check_internal_links(content, filepath_rel, all_files))
            page_issues.extend(check_external_links(content))
            page_issues.extend(check_no_em_dashes(content))

            if page_issues:
                summary['pages_with_issues'] += 1
                log.append(f"\n{filepath_rel}:")
                for issue in page_issues:
                    log.append(f"  - {issue}")
                    # Update summary counts
                    if 'alt text' in issue.lower():
                        summary['alt_text_issues'] += 1
                    elif 'broken link' in issue.lower():
                        summary['broken_links'] += 1
                    elif 'meta' in issue.lower():
                        summary['meta_tag_issues'] += 1
                    elif 'http://' in issue.lower():
                        summary['external_link_issues'] += 1
                    elif 'dash' in issue.lower():
                        summary['em_dash_issues'] += 1

        except Exception as e:
            log.append(f"ERROR reading {filepath_rel}: {str(e)}")

    # Summary
    log.append(f"\n{'='*60}")
    log.append("QA CHECK SUMMARY")
    log.append(f"{'='*60}")
    log.append(f"Total files checked: {summary['total_files_checked']}")
    log.append(f"Pages with issues: {summary['pages_with_issues']}")
    log.append(f"")
    log.append(f"Meta tag issues: {summary['meta_tag_issues']}")
    log.append(f"Alt text issues: {summary['alt_text_issues']}")
    log.append(f"Broken links: {summary['broken_links']}")
    log.append(f"External link issues: {summary['external_link_issues']}")
    log.append(f"Em/en dash issues: {summary['em_dash_issues']}")
    log.append(f"")

    if summary['pages_with_issues'] == 0:
        log.append("✅ ALL CHECKS PASSED - No issues found!")
    else:
        log.append(f"⚠️ {summary['pages_with_issues']} page(s) need attention")

    log.append(f"\nCompleted: {datetime.now().isoformat()}")

    # Write log
    log_file = project_root / "MD" / f"QA_RESULTS_{timestamp}.txt"
    with open(log_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(log))

    try:
        print('\n'.join(log))
    except UnicodeEncodeError:
        # Fallback for encoding issues on Windows
        safe_log = [line.encode('ascii', 'replace').decode('ascii') for line in log]
        print('\n'.join(safe_log))
    print(f"\nLog file: {log_file}")
    return summary

if __name__ == "__main__":
    project_root = Path(__file__).parent.parent
    run_qa_checks(project_root)
