#!/usr/bin/env python3
"""Entry point: copy the pre-rendered poster to the grader's output path.

The image is built by build_image.py and shipped in this repository as
entry.png. This program only copies it, so both grader runs write the same
bytes. Standard library only; no network.
"""

import os
import shutil
import sys


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    print("copied", src, "->", dst, os.path.getsize(dst), "bytes")
    return 0


if __name__ == "__main__":
    sys.exit(main())
