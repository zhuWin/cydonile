#!/usr/bin/env python3
"""Convert raster images to WebP with Pillow.

Examples
--------
# Convert every file in a folder (recursively) to WebP in-place:
python res/img2webp.py docs/assets/docres

# Convert specific files into a target folder:
python res/img2webp.py -o docs/assets/docres/some/page a.png b.jpg

Requires Pillow:  pip install Pillow
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

try:
    from PIL import Image
except ImportError:  # pragma: no cover
    sys.exit("Pillow is required: pip install Pillow")

RASTER_SUFFIXES = {".png", ".jpg", ".jpeg", ".bmp", ".tif", ".tiff", ".gif", ".webp"}


def convert_one(src: Path, dst: Path, quality: int, lossless: bool) -> None:
    dst.parent.mkdir(parents=True, exist_ok=True)
    with Image.open(src) as im:
        has_alpha = im.mode in ("RGBA", "LA") or (
            im.mode == "P" and "transparency" in im.info
        )
        im = im.convert("RGBA" if has_alpha else "RGB")
        if lossless:
            im.save(dst, "WEBP", lossless=True, method=6)
        else:
            im.save(dst, "WEBP", quality=quality, method=6)


def iter_sources(paths: list[Path]) -> list[Path]:
    found: list[Path] = []
    for p in paths:
        if p.is_dir():
            found.extend(
                f for f in sorted(p.rglob("*"))
                if f.is_file() and f.suffix.lower() in RASTER_SUFFIXES
            )
        elif p.is_file():
            found.append(p)
        else:
            print(f"skip (not found): {p}", file=sys.stderr)
    return found


def main() -> int:
    ap = argparse.ArgumentParser(description="Convert raster images to WebP.")
    ap.add_argument("paths", nargs="+", type=Path, help="files or folders to convert")
    ap.add_argument("-o", "--outdir", type=Path, default=None,
                    help="output folder (default: next to each source file)")
    ap.add_argument("-q", "--quality", type=int, default=85,
                    help="lossy quality, 0-100 (default: 85)")
    ap.add_argument("--lossless", action="store_true", help="use lossless WebP")
    ap.add_argument("-f", "--force", action="store_true",
                    help="overwrite existing .webp files")
    args = ap.parse_args()

    sources = iter_sources(args.paths)
    if not sources:
        print("no source images found", file=sys.stderr)
        return 1

    converted = skipped = failed = 0
    for src in sources:
        if src.suffix.lower() == ".webp" and not args.force:
            skipped += 1
            continue
        dst = (args.outdir / (src.stem + ".webp")) if args.outdir else src.with_suffix(".webp")
        if dst.exists() and not args.force:
            skipped += 1
            continue
        try:
            convert_one(src, dst, args.quality, args.lossless)
            converted += 1
        except Exception as exc:  # noqa: BLE001
            failed += 1
            print(f"FAILED {src}: {exc}", file=sys.stderr)

    print(f"converted={converted} skipped={skipped} failed={failed}")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
