---
name: isabelle-implementor
description: House conventions for writing Isabelle/HOL. Use whenever writing or editing Isabelle theories.
---

# Isabelle implementation conventions

Load the coding-conventions skill first; it holds the comment, identifier and commit rules shared
with other implementations, and the rules shared with the Agda skill.

## Naming

- Spec rule names in camel case (`EvalSeq` for `eval-seq`), since hyphens are not legal in names.
- Inversion lemmas by `inductive_cases`, one per syntactic form, named `<Form>E`.

## Pitfalls

- `o` is syntax for function composition, and a datatype `t` claims the fact names `t.simps` and
  `t.induct`, so a function named `t` clashes.
- Datatype constructors are global, so two datatypes cannot share a constructor name.
- `fun` completes missing patterns with `undefined`, about which nothing can be proved.
- A `definition` is opaque to the simplifier until unfolded; an `abbreviation` is notation only.
- In a case of `inductive_cases` with `case_names`, the first fact is the equation on the
  conclusion's result, followed by the rule's premises in order.
- Mutual induction takes one `arbitrary` list per judgement, separated by `and`.

## Running isabelle

- Build through the project's own build target where it has one, otherwise `isabelle build -D <dir>`,
  as a background Bash task with `timeout` 600000. Errors: `isabelle build_log -H Error <session>`.
- Two builds of one session at once fail on the session database (`SQLITE_CONSTRAINT_PRIMARYKEY`).
- Measure line width in rendered characters: a symbol escape counts as one and a control escape such
  as a subscript as none. `line-width.py` in this directory lists overruns.
