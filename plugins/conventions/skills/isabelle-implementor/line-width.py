#!/usr/bin/env python3
"""List lines of Isabelle theories wider than the limit, measured in rendered characters: a symbol
escape such as \\<rho> counts as one character and a control escape such as \\<^sub> as none.

Usage: line-width.py [--limit N] FILE...
"""
import argparse
import re


def rendered_width(line: str) -> int:
    return len(re.sub(r"\\<\^\w+>", "", re.sub(r"\\<\w+>", "x", line.rstrip("\n"))))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--limit", type=int, default=112)
    parser.add_argument("files", nargs="+")
    args = parser.parse_args()
    for file in args.files:
        with open(file) as f:
            for number, line in enumerate(f, 1):
                width = rendered_width(line)
                if width > args.limit:
                    print(f"{file}:{number}: {width}")


if __name__ == "__main__":
    main()
