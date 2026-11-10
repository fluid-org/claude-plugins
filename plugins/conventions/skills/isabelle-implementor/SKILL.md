---
name: isabelle-implementor
description: House conventions for writing Isabelle/HOL. Use whenever writing or editing Isabelle theories.
---

# Isabelle implementation conventions

Load the coding-conventions skill first; it holds the rules shared with other implementations.

- Line width in rendered characters: a symbol escape counts as one, a control escape such as a
  subscript as none. `line-width.py` in this directory lists overruns.
- A name presented to the user, as in a diagnostic, comes from the specification's PDF, never its LaTeX
  source: a macro name, label or file name is not a term of the specification.
- While iterating, as in a review, check each change by building the session alone and commit it;
  run the code export, its tests and the corpus once the iteration is complete. A change only to comments
  or documentation needs no build.
- A batch build reports nothing until it ends, so a stalled or timed-out build gives no position. Trace the
  theories instead with `trace.ML` in this directory, which runs each command under a timeout and recovers
  from a failure by sorry, so one pass lists every failing and slow command:
  `TRACE_FILES="A.thy B.thy" isabelle console -d DIR -l PARENT -o quick_and_dirty < trace.ML`, with
  `PARENT` the built session the theories import and the files in import order. Fix all the failures
  found, then trace again; try alternative proofs of one step with `TRACE_STOP` and `TRACE_CANDIDATES`
  rather than a trace per attempt. Build the session once the trace is clean.
