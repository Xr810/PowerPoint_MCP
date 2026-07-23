#!/usr/bin/env python3
"""Warn about likely text layout problems in a PPTX using only stdlib XML parsing."""

from __future__ import annotations

import argparse
import re
import sys
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET


NS = {
    "a": "http://schemas.openxmlformats.org/drawingml/2006/main",
    "p": "http://schemas.openxmlformats.org/presentationml/2006/main",
}


def local_name(tag: str) -> str:
    return tag.rsplit("}", 1)[-1]


def shape_box(shape: ET.Element):
    xfrm = shape.find(".//a:xfrm", NS)
    if xfrm is None:
        xfrm = shape.find(".//p:xfrm", NS)
    if xfrm is None:
        return None
    off = next((e for e in xfrm if local_name(e.tag) == "off"), None)
    ext = next((e for e in xfrm if local_name(e.tag) == "ext"), None)
    if off is None or ext is None:
        return None
    try:
        return tuple(int(v) for v in (off.get("x"), off.get("y"), ext.get("cx"), ext.get("cy")))
    except (TypeError, ValueError):
        return None


def intersection_ratio(a, b) -> float:
    ax, ay, aw, ah = a
    bx, by, bw, bh = b
    iw = max(0, min(ax + aw, bx + bw) - max(ax, bx))
    ih = max(0, min(ay + ah, by + bh) - max(ay, by))
    if not iw or not ih:
        return 0.0
    return (iw * ih) / max(1, min(aw * ah, bw * bh))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("pptx", type=Path)
    args = parser.parse_args()
    if not args.pptx.is_file():
        parser.error(f"file not found: {args.pptx}")

    warnings: list[str] = []
    with zipfile.ZipFile(args.pptx) as archive:
        presentation = ET.fromstring(archive.read("ppt/presentation.xml"))
        size = presentation.find("p:sldSz", NS)
        slide_w = int(size.get("cx", "0")) if size is not None else 0
        slide_h = int(size.get("cy", "0")) if size is not None else 0
        slide_names = sorted(
            (name for name in archive.namelist() if re.fullmatch(r"ppt/slides/slide\d+\.xml", name)),
            key=lambda name: int(re.search(r"\d+", Path(name).stem).group()),
        )
        for slide_no, name in enumerate(slide_names, 1):
            root = ET.fromstring(archive.read(name))
            text_shapes = []
            for shape in root.findall(".//p:sp", NS):
                text = " ".join(t.text or "" for t in shape.findall(".//a:t", NS)).strip()
                box = shape_box(shape)
                if not text or box is None:
                    continue
                shape_name = shape.find(".//p:cNvPr", NS)
                label = shape_name.get("name", "text shape") if shape_name is not None else "text shape"
                text_shapes.append((label, text, box))
                x, y, w, h = box
                if slide_w and slide_h and (x < 0 or y < 0 or x + w > slide_w or y + h > slide_h):
                    warnings.append(f"slide {slide_no}: OUT_OF_BOUNDS {label!r}")
                width_in = w / 914400
                height_in = h / 914400
                capacity = max(1.0, width_in * height_in * 25.0)
                if len(text) > capacity:
                    warnings.append(
                        f"slide {slide_no}: DENSITY_RISK {label!r} has {len(text)} chars in {width_in:.2f}x{height_in:.2f} in"
                    )
            for i, (name_a, _text_a, box_a) in enumerate(text_shapes):
                for name_b, _text_b, box_b in text_shapes[i + 1 :]:
                    ratio = intersection_ratio(box_a, box_b)
                    if ratio >= 0.02:
                        warnings.append(
                            f"slide {slide_no}: TEXT_OVERLAP {name_a!r} vs {name_b!r} ({ratio:.0%} of smaller box)"
                        )

    if warnings:
        print("\n".join(warnings))
        print(f"WARNINGS={len(warnings)}")
        return 1
    print("PASS: no text-box intersections, out-of-bounds text boxes, or density risks detected")
    return 0


if __name__ == "__main__":
    sys.exit(main())
