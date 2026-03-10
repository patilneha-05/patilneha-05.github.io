#!/usr/bin/env python3
"""
convert.py — PDF to WebP converter for certificate thumbnails.

Usage:
    python convert.py

Reads all *.pdf files from ./pdf/ directory,
converts the first page of each to a WebP image,
and saves them to ./webp/{filename}.webp

Requirements:
    pip install pdf2image Pillow
    # Also requires poppler:
    #   Ubuntu/Debian: sudo apt install poppler-utils
    #   macOS:         brew install poppler
    #   Windows:       Download from https://github.com/oschwartz10612/poppler-windows
"""

import os
import sys
from pathlib import Path

# ── Check dependencies ──
try:
    from pdf2image import convert_from_path
    from PIL import Image
except ImportError:
    print("Missing dependencies. Install with:")
    print("    pip install pdf2image Pillow")
    sys.exit(1)

# ── Config ──
SCRIPT_DIR = Path(__file__).parent
PDF_DIR = SCRIPT_DIR / "pdf"
WEBP_DIR = SCRIPT_DIR / "webp"
DPI = 150  # Resolution — higher = sharper but larger file
QUALITY = 85  # WebP quality (0-100)
MAX_WIDTH = 1200  # Max image width in pixels (auto-scales height)


def convert_pdfs():
    """Convert all PDFs in ./pdf/ to WebP images in ./webp/."""

    # Ensure directories exist
    if not PDF_DIR.exists():
        print(f"ERROR: PDF directory not found: {PDF_DIR}")
        sys.exit(1)

    WEBP_DIR.mkdir(exist_ok=True)

    # Gather all PDFs
    pdf_files = sorted(PDF_DIR.glob("*.pdf"))
    if not pdf_files:
        print(f"No PDF files found in {PDF_DIR}")
        sys.exit(0)

    print(f"Found {len(pdf_files)} PDF(s) in {PDF_DIR}")
    print(f"Output directory: {WEBP_DIR}")
    print(f"Settings: DPI={DPI}, Quality={QUALITY}, MaxWidth={MAX_WIDTH}px")
    print("-" * 60)

    success_count = 0
    error_count = 0

    for pdf_path in pdf_files:
        stem = pdf_path.stem  # filename without extension
        out_path = WEBP_DIR / f"{stem}.webp"

        print(f"  Converting: {pdf_path.name}", end="", flush=True)

        # Skip if already converted (use --force to overwrite)
        if out_path.exists() and "--force" not in sys.argv:
            print(f"  → SKIPPED (already exists, use --force to overwrite)")
            success_count += 1
            continue

        try:
            # Convert only the first page
            pages = convert_from_path(
                str(pdf_path),
                dpi=DPI,
                first_page=1,
                last_page=1,
                fmt="RGB",
            )

            if not pages:
                print(f"  → ERROR: No pages returned")
                error_count += 1
                continue

            img = pages[0]

            # Resize if wider than MAX_WIDTH
            if img.width > MAX_WIDTH:
                ratio = MAX_WIDTH / img.width
                new_size = (MAX_WIDTH, int(img.height * ratio))
                img = img.resize(new_size, Image.LANCZOS)

            # Save as WebP
            img.save(str(out_path), "WEBP", quality=QUALITY, method=6)

            kb = out_path.stat().st_size / 1024
            print(f"  → OK ({img.width}×{img.height}px, {kb:.0f} KB)")
            success_count += 1

        except Exception as e:
            print(f"  → ERROR: {e}")
            error_count += 1

    print("-" * 60)
    print(f"Done! {success_count} converted, {error_count} errors.")

    if error_count > 0:
        print("\nTip: If you see 'poppler' errors, install it first:")
        print("  Ubuntu/Debian: sudo apt install poppler-utils")
        print("  macOS:         brew install poppler")

    return error_count == 0


if __name__ == "__main__":
    ok = convert_pdfs()
    sys.exit(0 if ok else 1)
