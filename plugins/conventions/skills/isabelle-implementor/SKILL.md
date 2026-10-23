---
name: isabelle-implementor
description: House conventions for writing Isabelle/HOL. Use whenever writing or editing Isabelle theories.
---

# Isabelle implementation conventions

Load the coding-conventions skill first; it holds the rules shared with other implementations.

- Line width in rendered characters: a symbol escape counts as one, a control escape such as a
  subscript as none. `line-width.py` in this directory lists overruns.
- Names come from the specification's PDF, never its LaTeX source: a macro name or file name is not a
  term of the specification.
- While iterating, as in a review, check each change by building the session alone and commit it;
  run the code export, its tests and the corpus once the iteration is complete. Pushing starts the full
  build on GitHub, so push a batch of small changes rather than each one.
