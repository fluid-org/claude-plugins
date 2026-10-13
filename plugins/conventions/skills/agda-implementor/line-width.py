#!/usr/bin/env python3
"""Report Agda lines over a width limit, and wrapped groups that would fit within it.

  python3 line-width.py [root] [--limit N] [--joins]

Widths count characters, not bytes: a multi-byte identifier is one column per glyph.
Two kinds of group are reported under --joins:

  head      a line plus the more-indented lines under it, where no continuation opens a
            new layout block (where/with/let/do/record/data/module/in) or carries a comment
  bracket   a parenthesised item spanning several lines, such as one parameter of a module
            telescope; the brackets already delimit it, so joining cannot disturb layout
"""
import os, re, sys, unicodedata

BLOCK = re.compile(r"\b(where|with|let|do|record|data|module|in)\b")
COMMENT = re.compile(r"--|\{-")


def width(s):
    return sum(0 if unicodedata.combining(c) else 1 for c in s)


def indent(s):
    return len(s) - len(s.lstrip(' '))


def head_groups(lines):
    i = 0
    while i < len(lines):
        line = lines[i]
        if not line.strip() or COMMENT.search(line):
            i += 1
            continue
        ind = indent(line)
        j = i + 1
        group = [line]
        while (j < len(lines) and lines[j].strip() and indent(lines[j]) > ind
               and not COMMENT.search(lines[j])):
            group.append(lines[j])
            j += 1
        if len(group) >= 2 and not any(BLOCK.search(g) for g in group[1:]):
            yield i + 1, group
        i = j if j > i + 1 else i + 1


def bracket_groups(lines):
    for i, line in enumerate(lines):
        stripped = line.strip()
        if not stripped.startswith('(') or COMMENT.search(line):
            continue
        depth = 0
        for j in range(i, len(lines)):
            if COMMENT.search(lines[j]):
                break
            depth += lines[j].count('(') - lines[j].count(')')
            if depth <= 0:
                if j > i:
                    yield i + 1, lines[i:j + 1]
                break


def joined(group):
    return group[0].rstrip() + ' ' + ' '.join(g.strip() for g in group[1:])


def main():
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    flags = {a for a in sys.argv[1:] if a.startswith('--')}
    root = args[0] if args else '.'
    limit = 110
    for f in flags:
        if f.startswith('--limit'):
            limit = int(f.split('=')[1]) if '=' in f else limit
    if '--limit' in sys.argv:
        limit = int(sys.argv[sys.argv.index('--limit') + 1])

    over, joins = {}, []
    for dirpath, _, files in os.walk(root):
        for f in sorted(files):
            if not f.endswith('.agda'):
                continue
            p = os.path.join(dirpath, f)
            lines = open(p).read().split('\n')
            n = [(k + 1, width(l)) for k, l in enumerate(lines) if width(l) > limit]
            if n:
                over[p] = n
            if '--joins' in flags:
                seen = set()
                for kind, gen in (('head', head_groups), ('bracket', bracket_groups)):
                    for start, group in gen(lines):
                        w = width(joined(group))
                        if w <= limit and (start, len(group)) not in seen:
                            seen.add((start, len(group)))
                            joins.append((p, start, len(group), w, kind))

    print(f'lines over {limit}:')
    for p, ns in sorted(over.items(), key=lambda kv: -len(kv[1])):
        print(f'  {len(ns):4}  {p}  (worst {max(w for _, w in ns)})')
    print('total over:', sum(len(v) for v in over.values()))

    if '--joins' in flags:
        print(f'\nwrapped groups that fit in {limit} (file:line, lines, joined width, kind):')
        for p, start, n, w, kind in joins:
            print(f'  {p}:{start}  {n} lines  {w}  {kind}')
        print('total joinable:', len(joins))


if __name__ == '__main__':
    main()
