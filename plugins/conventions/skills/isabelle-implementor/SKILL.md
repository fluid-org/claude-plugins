---
name: isabelle-implementor
description: House conventions for writing Isabelle/HOL. Use whenever writing or editing Isabelle theories.
---

# Isabelle implementation conventions

Load the coding-conventions skill first; it holds the comment, identifier and commit rules shared
with other implementations, and the rules shared with the Agda skill (comments, naming after the
spec, running checkers, pull requests).

## Naming

- Spec metavariables as Isabelle symbols (`\<rho>`, `\<tau>`). Datatypes named after the spec's sort
  where the name is free.
- A name the host reserves gets the nearest free name: `o` is syntax for function composition, and a
  datatype `t` claims the fact names `t.simps` and `t.induct`, so a function of the same name clashes.
- Datatype constructors are global, so two sorts cannot share a constructor. A sort the spec reuses
  with different payloads is one parametrised datatype.
- Rules of an inductive judgement are named after the spec's rule names in camel case (`EvalSeq` for
  `eval-seq`); the induction principle of a mutual definition is bound once, `lemmas … = ….inducts`.
- Inversion lemmas by `inductive_cases`, one per syntactic form, named `<Form>E` (`SeqE`). Give one
  `case_names` after the rules when a structured proof needs to pick a case; the first fact of a case
  is the equation on the conclusion's result, then the rule's premises in order.

## Definitions

- A spec metafunction is a `fun`, or a `definition` when not recursive. A metafunction the spec leaves
  undefined on some arguments returns `option`, `Some` exactly where the spec defines it, and a rule
  using it has the premise `f x = Some y`, as the spec's rule is inapplicable there. Never leave
  patterns missing: `fun` completes them with `undefined`, about which nothing can be proved.
- One spec function over several sorts is one `fun` per sort, suffixed with the sort where the names
  would clash.
- A monadic bind in the conclusion of a spec rule is a function on results, so one rule covers the
  value and failure cases as the spec's rule does; a separate rule only where the spec has one.
- A short name for a constructor term is an `abbreviation`, not a `definition`, so proofs see the
  constructors and goals print the short name.

## Proofs

- Isar; `apply` scripts only inside a `by`.
- A proof over a mutual judgement: `induction arbitrary: … rule: …`, one `arbitrary` variable per
  judgement, joined with `and`.
- In a case, `from X.prems X.hyps show ?case by (auto elim!: FormE dest: X.IH)`. Never chain the
  induction hypothesis with `then`: a meta-quantified assumption makes `auto` loop.
- When an induction hypothesis's premise mentions a term built from the case's variables, `auto` fails
  after substituting them away. Write that case as `proof (cases rule: FormE)` with the named case,
  derive the equalities from the hypotheses with `[OF …]`, and discharge the other cases with
  `qed (use X.hyps in \<open>auto dest: X.IH\<close>)`.

## Running isabelle

- Build through the project's own build target where it has one, otherwise `isabelle build -D <dir>`,
  as a background Bash task with `timeout` 600000. Errors: `isabelle build_log -H Error <session>`.
- Two builds of one session at once fail on the session database (`SQLITE_CONSTRAINT_PRIMARYKEY`); if
  the user is building, wait and rerun.
- Only the first failing command of a theory is reported; fix it and rebuild.
- Measure line width in rendered characters: a symbol escape counts as one and a control escape such
  as a subscript as none. `line-width.py` in this directory lists overruns.
