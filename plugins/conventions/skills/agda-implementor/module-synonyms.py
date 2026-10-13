#!/usr/bin/env python3
"""Inventory the module synonyms in an Agda tree, with the members each one serves.

  python3 module-synonyms.py [root] [--min N]

For every `module X = …` binding it reports how many qualified uses `X.` has, which files
use it, and how the uses break down by first member segment. That breakdown is the input to
the naming decision: members with few uses may be candidates for a direct import, leaving
the synonym for the remainder.

The counts are textual, and wrong in two directions. A member absent from this listing may
still be in scope through an `open` with no `using` list. The bare counts cover only the
files that already use the synonym, so a name the import would export onward can still clash
in a file downstream. Treat a low count as a reason to look, never as a licence to import
without checking. Only the compiler settles that.
"""
import os, re, sys
from collections import Counter, defaultdict

BINDING = re.compile(r"^\s*(?:private\s+)?module\s+([^\s=(){}]+)\s*=", re.M)


def qualified(name):
    return re.compile(r"(?<![\w'\-])" + re.escape(name) + r"\.([^\s)}⟩,;{]+)")


def bare(name):
    return re.compile(r"(?<![\w'\-\.])" + re.escape(name) + r"(?![\w'\-])")


def main():
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    root = args[0] if args else '.'
    lo = 1
    if '--min' in sys.argv:
        lo = int(sys.argv[sys.argv.index('--min') + 1])

    src = {}
    for dirpath, _, files in os.walk(root):
        for f in sorted(files):
            if f.endswith('.agda'):
                p = os.path.join(dirpath, f)
                src[p] = open(p).read()

    bindings = defaultdict(list)
    for p, s in src.items():
        for m in BINDING.finditer(s):
            bindings[m.group(1)].append((p, s[:m.start()].count('\n') + 1))

    rows = []
    for name, sites in bindings.items():
        pat = qualified(name)
        members, files = Counter(), Counter()
        for p, s in src.items():
            hits = pat.findall(s)
            if hits:
                files[p] = len(hits)
                members.update(h.split('.')[0] for h in hits)
        rows.append((sum(members.values()), name, sites, members, files))

    for total, name, sites, members, files in sorted(rows, reverse=True):
        if total < lo:
            continue
        where = ' '.join(f'{p}:{n}' for p, n in sites[:3])
        if len(sites) > 3:
            where += f' and {len(sites) - 3} more'
        print(f'{name}  ({total} qualified uses)  bound at {where}')
        if len(sites) > 1:
            print(f'    NOTE {len(sites)} bindings share this name; the counts below are their sum')
        for p, n in files.most_common():
            print(f'    {n:4}  {p}')
        for m, n in members.most_common():
            b = sum(len(bare(m).findall(src[p])) for p in files)
            print(f'    {n:4}  .{m:<28} bare elsewhere in those files: {b}')
        print()


if __name__ == '__main__':
    main()
