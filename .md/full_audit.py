#!/usr/bin/env python3
"""Full CMA site audit: broken links, TL;DR photos, related posts, feature images."""

import os
import re
from pathlib import Path
from collections import defaultdict

ROOT = Path(r"C:\ZZZWebsites\chiangmaiambassador")

def get_all_html():
    files = []
    for f in ROOT.rglob("*.html"):
        # Skip template and pages/ utility pages
        rel = f.relative_to(ROOT)
        parts = rel.parts
        # Include all blog/content pages
        files.append(f)
    return sorted(files)

def get_all_images():
    imgs = set()
    for ext in ["*.webp", "*.jpg", "*.jpeg", "*.png", "*.svg"]:
        for f in ROOT.rglob(ext):
            imgs.add(f.relative_to(ROOT).as_posix())
    return imgs

def check_tldr_image(content, filepath):
    """Check if TL;DR box has an image in it."""
    # Look for TL;DR section
    tldr_match = re.search(r'Quick Summary.*?TL;DR|tldr|tl-dr', content, re.IGNORECASE)
    if not tldr_match:
        return "NO_TLDR_BOX"

    # Find the TL;DR box and check for img-right-small near it
    # Pattern: img-right-small before or within the tldr section
    tldr_area = content[max(0, tldr_match.start()-500):tldr_match.start()+200]
    if 'img-right-small' in tldr_area or 'IMAGE IN TOP RIGHT OF TL;DR' in tldr_area:
        # Check if there's an actual src in the figure
        img_in_tldr = re.search(r'img-right-small[^}]*?<img[^>]+src=["\']([^"\']+)["\']',
                                  content[max(0, tldr_match.start()-600):tldr_match.start()+400],
                                  re.DOTALL)
        if img_in_tldr:
            src = img_in_tldr.group(1)
            if src.strip():
                return f"OK: {src}"
            return "EMPTY_SRC"
        # Check for empty figure
        empty_fig = re.search(r'img-right-small[^>]*>(\s*)</figure>',
                               content[max(0, tldr_match.start()-600):tldr_match.start()+400],
                               re.DOTALL)
        if empty_fig:
            return "EMPTY_FIGURE"
        return "NO_IMG_IN_TLDR"
    return "NO_IMG_IN_TLDR"

def get_internal_links(content, filepath):
    """Find all href/src references to local files."""
    links = re.findall(r'(?:href|src)=["\']([^"\'#?]+)["\']', content)
    return [l for l in links if not l.startswith(('http', 'mailto', 'tel', '//', 'data:', '#'))]

def resolve_link(link, filepath):
    """Resolve a relative link to absolute path."""
    base = filepath.parent
    target = (base / link).resolve()
    return target

def check_broken_links(content, filepath, all_html_paths):
    broken = []
    links = get_internal_links(content, filepath)
    for link in links:
        # Skip font/css/js files for now, focus on HTML and images
        if link.endswith(('.woff2', '.woff', '.ttf')):
            continue
        target = resolve_link(link, filepath)
        if not target.exists():
            broken.append(link)
    return broken

def get_related_posts(content):
    """Extract current related posts section."""
    match = re.search(r'(related-posts|Related Posts|More.*?Posts)(.*?)(?:</section>|</div>\s*</section>)',
                       content, re.DOTALL | re.IGNORECASE)
    if match:
        return match.group(0)
    return None

def get_feature_image(content):
    """Get hero/feature image."""
    # Look for blog-hero img or og:image
    og = re.search(r'og:image.*?content=["\']([^"\']+)["\']', content)
    if og:
        return og.group(1)
    hero_img = re.search(r'blog-hero[^>]*>.*?<img[^>]+src=["\']([^"\']+)["\']', content, re.DOTALL)
    if hero_img:
        return hero_img.group(1)
    return None

def main():
    html_files = get_all_html()
    all_images = get_all_images()
    all_html_paths = set(html_files)

    print(f"Total HTML files: {len(html_files)}")
    print(f"Total images: {len(all_images)}\n")

    needs_tldr_photo = []
    has_empty_tldr = []
    no_tldr_box = []
    broken_links_report = {}
    feature_image_report = {}

    for f in html_files:
        rel = str(f.relative_to(ROOT))
        content = f.read_text(encoding='utf-8', errors='ignore')

        # TL;DR photo check
        tldr_status = check_tldr_image(content, f)
        if tldr_status == "NO_TLDR_BOX":
            no_tldr_box.append(rel)
        elif tldr_status in ("NO_IMG_IN_TLDR", "EMPTY_FIGURE", "EMPTY_SRC"):
            needs_tldr_photo.append((rel, tldr_status))

        # Broken links
        broken = check_broken_links(content, f, all_html_paths)
        if broken:
            broken_links_report[rel] = broken

        # Feature image
        fi = get_feature_image(content)
        if not fi:
            feature_image_report[rel] = "MISSING_FEATURE_IMAGE"
        else:
            feature_image_report[rel] = fi

    # Print reports
    print("=" * 60)
    print("PAGES NEEDING TL;DR PHOTO")
    print("=" * 60)
    for page, status in needs_tldr_photo:
        print(f"  [{status}] {page}")

    print(f"\nPages with no TL;DR box at all ({len(no_tldr_box)}):")
    for page in no_tldr_box:
        print(f"  {page}")

    print("\n" + "=" * 60)
    print("BROKEN INTERNAL LINKS")
    print("=" * 60)
    if not broken_links_report:
        print("  None found!")
    for page, links in broken_links_report.items():
        print(f"\n  {page}:")
        for l in links:
            print(f"    BROKEN: {l}")

    print("\n" + "=" * 60)
    print("FEATURE IMAGE STATUS")
    print("=" * 60)
    missing_fi = [(p, v) for p, v in feature_image_report.items() if v == "MISSING_FEATURE_IMAGE"]
    print(f"Missing feature image: {len(missing_fi)}")
    for p, _ in missing_fi:
        print(f"  {p}")
    print(f"\nHave feature image: {len(feature_image_report) - len(missing_fi)}")

if __name__ == "__main__":
    main()
