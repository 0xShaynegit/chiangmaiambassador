#!/usr/bin/env python3
"""
Inject TL;DR photos into pages missing them.
Selects best image from MD/images, copies to images/, injects into HTML.
"""

import re
import shutil
from pathlib import Path

ROOT = Path(r"C:\ZZZWebsites\chiangmaiambassador")
MD_IMAGES = ROOT / "MD" / "images"
IMAGES = ROOT / "images"

# Map: page_path -> best image filename from MD/images
# Chosen based on page topic and available filenames
TLDR_IMAGE_MAP = {
    # FOOD
    "food/chiang-mai-grandview-lunch.html":
        "chiang-mai-ambassador-chiangmaiambassador-Chiang-Mai-Ambassador-auf-der-au-01.webp",
    "food/dukes.html":
        "chiang-mai-ambassador-chiangmaiambassador-Chiang-Mai-Ambassador-CM-Ambassador-Mens-Meat-Up.webp",
    "food/ibis-styles-buffet-lunch.html":
        "chiang-mai-ambassador-chiangmaiambassador-Chiang-Mai-Ambassador-CM-Ambassador-ChefFuji-2.webp",
    "food/le-meridien-dinner-buffet.html":
        "chiang-mai-ambassador-chiangmaiambassador-Chiang-Mai-Ambassador-CM-Ambassador-ChefFuji-4.webp",
    "food/real-thai-restaurant.html":
        "chiang-mai-ambassador-chiangmaiambassador-chiangmaiambassador-real-thai-restaurant-16.webp",
    "food/siripanna-lunch.html":
        "chiang-mai-ambassador-chiangmaiambassador-Chiang-Mai-Ambassador-CM-Ambassador-ChefFuji-6.webp",

    # GUIDES
    "guides/chiang-mai-football-club.html":
        "chiang-mai-ambassador-chiangmaiambassador-Chiang-Mai-Ambassador-CM-Ambassador-Meals-on-Wheels-1.webp",
    "guides/license-plates.html":
        "chiang-mai-ambassador-chiangmaiambassador-Chiang-Mai-Ambassador-CM-Ambassador-TDAC-3.webp",
    "guides/motorcycle-rentals.html":
        "chiang-mai-ambassador-chiangmaiambassador-chiangmaiambassador-comfortable-sandals-2.webp",
    "guides/run-for-relief.html":
        "chiang-mai-ambassador-chiangmaiambassador-Chiang-Mai-Ambassador-CM-Ambassador-Meals-on-Wheels-4-U-1.webp",
    "guides/walking-street-markets.html":
        "chiang-mai-ambassador-chiangmaiambassador-Walking-Street-Markets-market-atmosphere-night.webp",

    # LIFESTYLE
    "lifestyle/alcohol-observations-of-a-non-drinker.html":
        "chiang-mai-ambassador-chiangmaiambassador-Chiang-Mai-Ambassador-CM-Ambassador-ChefFuji-8.webp",
    "lifestyle/expat-breakfast-club.html":
        "chiang-mai-ambassador-chiangmaiambassador-Chiang-Mai-Ambassador-Chiang-Mai-Expats-Club-Breakfast-CEC-21.webp",
    "lifestyle/songkran.html":
        "chiang-mai-ambassador-chiangmaiambassador-Chiang-Mai-Ambassador-Songkran-2.webp",
    "lifestyle/traveling-with-friends.html":
        "chiang-mai-ambassador-chiangmaiambassador-Chiang-Mai-Ambassador-CM-Ambassador-cheapest-border-run-1.webp",

    # ROOT
    "getting-social-in-chiang-mai.html":
        "chiang-mai-ambassador-chiangmaiambassador-Chiang-Mai-Ambassador-CM-Ambassador-Meals-on-Wheels-4-U-4.webp",
    "motorbike-registration-chiang-mai.html":
        "chiang-mai-ambassador-chiangmaiambassador-Chiang-Mai-Ambassador-CM-Ambassador-TDAC.webp",
    "understanding-thai-culture.html":
        "chiang-mai-ambassador-chiangmaiambassador-chiangmaiambassador-Chiang-Mai-Umbrella-Girl1.webp",

    # PAGES
    "pages/cost-of-living.html":
        "chiang-mai-ambassador-chiangmaiambassador-Chiang-Mai-Ambassador-CM-Ambassador-cheapest-border-run-100.webp",
    "pages/just-arriving-in-thailand.html":
        "chiang-mai-ambassador-chiangmaiambassador-chiangmaiambassador-don-muang-airport-1.webp",
    "pages/living-better-in-thailand.html":
        "chiang-mai-ambassador-chiangmaiambassador-Chiang-Mai-Ambassador-CM-Ambassador-Top-Tips-1.webp",
    "pages/neighbourhoods.html":
        "chiang-mai-ambassador-chiangmaiambassador-chiangmaiambassador-china-to-chiang-mai13.webp",
    "pages/planning-a-move-to-thailand.html":
        "chiang-mai-ambassador-chiangmaiambassador-chiangmaiambassador-don-muang-airport-1.webp",
    "pages/visas.html":
        "chiang-mai-ambassador-chiangmaiambassador-Chiang-Mai-Ambassador-CM-Ambassador-cheapest-border-run-14.webp",
}


def inject_tldr_image(content, img_src):
    """Inject image into TL;DR box. Finds the img-right-small figure before the TL;DR heading."""

    # Pattern: figure.img-right-small that is empty (no img inside)
    empty_fig = re.compile(
        r'(<figure class="img-right-small"[^>]*>)\s*(</figure>)',
        re.DOTALL
    )
    if empty_fig.search(content):
        return empty_fig.sub(
            rf'\1\n                        <img src="{img_src}" alt="Quick summary photo" width="280" height="210" style="width:100%;height:auto;border-radius:8px;">\n                    \2',
            content
        )

    # Pattern: figure.img-right-small with style attribute (template standard)
    styled_fig = re.compile(
        r'(<figure class="img-right-small" style="[^"]*">)\s*(<!-- IMAGE IN TOP RIGHT OF TL;DR -->)?\s*(</figure>)',
        re.DOTALL
    )
    if styled_fig.search(content):
        return styled_fig.sub(
            rf'\1\n                        <img src="{img_src}" alt="Quick summary photo" width="280" height="210" style="width:100%;height:auto;border-radius:8px;">\n                    \3',
            content
        )

    # Pattern: comment marker for TL;DR image with empty figure after
    comment_fig = re.compile(
        r'(<!-- IMAGE IN TOP RIGHT OF TL;DR -->)\s*\n\s*(<figure class="img-right-small"[^>]*>)\s*(</figure>)',
        re.DOTALL
    )
    if comment_fig.search(content):
        return comment_fig.sub(
            rf'\1\n                    \2\n                        <img src="{img_src}" alt="Quick summary photo" width="280" height="210" style="width:100%;height:auto;border-radius:8px;">\n                    \3',
            content
        )

    # Fallback: insert before the TL;DR heading
    tldr_heading = re.compile(r'(<h4>Quick Summary \(TL;DR\)</h4>)', re.IGNORECASE)
    if tldr_heading.search(content):
        figure_html = f'<figure class="img-right-small" style="margin-top: -30px; margin-bottom: 1rem; width: calc(100% - 400px); max-width: 280px;">\n                        <img src="{img_src}" alt="Quick summary photo" width="280" height="210" style="width:100%;height:auto;border-radius:8px;">\n                    </figure>\n                    '
        return tldr_heading.sub(figure_html + r'\1', content)

    return content


def main():
    copied = []
    injected = []
    errors = []

    for page_path, img_filename in TLDR_IMAGE_MAP.items():
        src_img = MD_IMAGES / img_filename
        dst_img = IMAGES / img_filename
        page_file = ROOT / page_path

        # Verify source image exists
        if not src_img.exists():
            errors.append(f"SOURCE MISSING: {img_filename}")
            continue

        # Copy image if not already in images/
        if not dst_img.exists():
            shutil.copy2(src_img, dst_img)
            copied.append(img_filename)

        # Build relative path from page to image
        depth = len(page_path.split("/")) - 1
        prefix = "../" * depth
        img_rel = f"{prefix}images/{img_filename}"

        # Read page
        if not page_file.exists():
            errors.append(f"PAGE MISSING: {page_path}")
            continue

        content = page_file.read_text(encoding="utf-8", errors="ignore")
        new_content = inject_tldr_image(content, img_rel)

        if new_content != content:
            page_file.write_text(new_content, encoding="utf-8")
            injected.append(page_path)
        else:
            errors.append(f"INJECT FAILED (pattern not found): {page_path}")

    print(f"Images copied: {len(copied)}")
    for f in copied:
        print(f"  {f}")

    print(f"\nPages updated: {len(injected)}")
    for p in injected:
        print(f"  {p}")

    if errors:
        print(f"\nErrors ({len(errors)}):")
        for e in errors:
            print(f"  {e}")


if __name__ == "__main__":
    main()
