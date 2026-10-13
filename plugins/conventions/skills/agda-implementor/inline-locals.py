"""Inline where-block locals that are used exactly once.

usage: inline-locals.py FILE [--apply] [--max N] [--skip NAME,...]

A local is a where-block line `name = rhs` with a single-line right-hand side and no type signature.
Its one use is replaced by `(rhs)` and the definition removed; a where line left with no
declarations is removed too. Multi-line, typed and unused locals, and those whose right-hand side is longer than N characters
(--max, default unlimited), are reported, not touched.
"""
import re, sys

path = sys.argv[1]
apply = '--apply' in sys.argv
maxlen = int(sys.argv[sys.argv.index('--max') + 1]) if '--max' in sys.argv else None
skip = set(sys.argv[sys.argv.index('--skip') + 1].split(',')) if '--skip' in sys.argv else set()
lines = open(path).read().split('\n')

def indent(l): return len(l) - len(l.lstrip(' '))

NAME = r"[^\s:=(){}]+"
def boundary(name):
    return r'(?<![\w\'′₀-₉ᵢₖₗₘₙₒₚₛₜ\-\.])' + re.escape(name) + r'(?![\w\'′₀-₉ᵢₖₗₘₙₒₚₛₜ])'

inlined, skipped = [], []
changed = True
while changed:
    changed = False
    i = 0
    while i < len(lines):
        if not re.match(r'^\s*where\s*$', lines[i]):
            i += 1; continue
        w = indent(lines[i])
        # block: following lines with indent >= w (blank lines allowed), until a non-blank line with indent < w
        j = i + 1
        while j < len(lines) and (lines[j].strip() == '' or indent(lines[j]) >= w): j += 1
        while j > i + 1 and lines[j-1].strip() == '': j -= 1
        # head: nearest preceding non-blank line with indent < w
        h = i - 1
        while h >= 0 and (lines[h].strip() == '' or indent(lines[h]) >= w): h -= 1
        scope = list(range(h, j))
        block = list(range(i + 1, j))
        for k in block:
            m = re.match(r'^ {%d}(%s)\s*=\s*(\S.*)$' % (w, NAME), lines[k])
            if not m: continue
            name, rhs = m.group(1), m.group(2).rstrip()
            if name in ('open',) or name in skip or rhs.endswith('where'): continue
            # single-line rhs: next line is not a continuation (indent > w)
            if k + 1 < j and lines[k+1].strip() != '' and indent(lines[k+1]) > w:
                skipped.append((k+1, name, 'multi-line')); continue
            if any(re.match(r'^ {%d}%s\s*:' % (w, re.escape(name)), lines[t]) for t in block):
                continue
            if maxlen is not None and len(rhs) > maxlen:
                skipped.append((k+1, name, f'{len(rhs)} chars')); continue
            defs = [t for t in block if re.match(r'^ {%d}%s(\s|$)' % (w, re.escape(name)), lines[t])]
            if len(defs) != 1: continue
            pat = re.compile(boundary(name))
            uses = [(t, mm) for t in scope if t != k for mm in pat.finditer(lines[t])]
            if len(uses) == 0:
                skipped.append((k+1, name, 'unused')); continue
            if len(uses) != 1: continue
            t, mm = uses[0]
            before, after = lines[t][:mm.start()], lines[t][mm.end():]
            atomic = re.fullmatch(r'[^\s()]+', rhs) is not None or (rhs.startswith('(') and rhs.endswith(')') and rhs.count('(') == 1)
            head = re.search(r'(^|[({=→⟨;,]\s*)$', before) is not None
            bare = atomic or (before.endswith('{') and after.startswith('}')) or (head and re.match(r'\s*\.', after) is not None)
            repl = rhs if bare else '(' + rhs + ')'
            lines[t] = before + repl + after
            del lines[k]
            inlined.append((k+1, name, len(repl)))
            # the block may now hold no declarations
            j2 = i + 1
            while j2 < len(lines) and (lines[j2].strip() == '' or indent(lines[j2]) >= w): j2 += 1
            if all(lines[t2].strip() == '' for t2 in range(i + 1, j2)):
                del lines[i:j2]
            changed = True
            break
        if changed: break
        i = j

skipped = sorted(set(skipped))
print(f'{path}: inlined {len(inlined)}, skipped {len(skipped)}')
for k, n, ln in inlined: print(f'  inline {n} ({ln} chars) at ~{k}')
for k, n, why in skipped: print(f'  skip {n} at {k}: {why}')
if apply:
    open(path, 'w').write('\n'.join(lines))
    print('applied')
else:
    print('dry run')
