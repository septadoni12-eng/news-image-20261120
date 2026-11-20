#!/usr/bin/env python3
"""news-image-20261120 entrypoint.

Copies the committed entry.png to the grader's output location.
Standard library only; no network, no clock, no randomness: two runs
write byte-identical files.
"""
import hashlib
import os
import shutil
import sys


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    # the two graded runs must write the same bytes: refuse a bad copy
    if sha256(src) != sha256(dst):
        print("error: copied entry.png does not match the committed file",
              file=sys.stderr)
        return 1
    print(f"wrote {dst} ({os.path.getsize(dst)} bytes)")


if __name__ == "__main__":
    sys.exit(main())
