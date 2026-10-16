---
name: isabelle-implementor
description: House conventions for writing Isabelle/HOL. Use whenever writing or editing Isabelle theories.
---

# Isabelle implementation conventions

Load the coding-conventions skill first; it holds the comment, identifier and commit rules shared
with other implementations, and the rules shared with the Agda skill (comments, naming after the
spec, running checkers, pull requests).

## Naming

- Spec metavariables as Isabelle symbols: `\<rho>` for environments, `\<kappa>` for termination
  kinds, `\<tau>` for types. Datatypes named after the spec's sort where the name is free.
- Names the host reserves, and the nearest replacement: `o` is syntax for function composition, so
  the outcome variable is `oc` and the outcome type `outcome`; a datatype `result` claims
  `result.simps`, so the metafunction on outcomes is `call_result`.
- Datatype constructors are global, so two sorts cannot share a constructor. A sort the spec reuses
  with different payloads (a result carrying a value, a sequence of values or an outcome) is one
  parametrised datatype, `'a result`.
- Rules of an inductive judgement are named after the spec's rule names in camel case
  (`EvalSeqReturn` for `eval-seq-return`); the induction principle of a mutual definition is bound
  once, `lemmas eval_induct = ….inducts`.
- Inversion lemmas by `inductive_cases`, one per syntactic form, named `<Form>E` (`BinOpE`, `SeqE`).
  Give one `case_names` after the rules when a structured proof needs to pick a case; the first fact
  of a case is the equation on the conclusion's result, then the rule's premises in order.

## Definitions

- A spec metafunction is a `fun`; `fun` completes missing patterns with `undefined`, so a partial
  function such as composition of outcomes is written with just its defined equations.
- Monadic propagation in the spec (the `mlet` binder) is a bind over results, so one rule covers
  the value and abort cases as the spec's rule does; a separate rule only where the spec has one.
- A short name for a constructor term (`true` for the Boolean literal value) is an `abbreviation`,
  not a `definition`, so proofs see the constructors and goals print the short name.

## Proofs

- Isar; `apply` scripts only inside a `by`.
- Determinism or any proof over a mutual judgement: `induction arbitrary: … rule: eval_induct`, one
  `arbitrary` variable per judgement, joined with `and`.
- In a case, `from X.prems X.hyps show ?case by (auto elim!: FormE dest: X.IH)`. Never chain the
  induction hypothesis with `then`: a meta-quantified assumption makes `auto` loop.
- When an induction hypothesis's premise mentions a term built from the case's variables (the
  environment of a function body), `auto` fails after substituting them away. Write that case as
  `proof (cases rule: FormE)` with the named case, derive the equalities from the hypotheses with
  `[OF …]`, and discharge the other cases with `qed (use X.hyps in \<open>auto dest: X.IH\<close>)`.

## Running isabelle

- `isabelle build -o document=false -D .` in the session directory, as a background Bash task with
  `timeout` 600000; the session's `ROOT` lists the theories. Errors: `isabelle build_log -H Error
  <session>`.
- Only the first failing command of a theory is reported; fix it and rebuild.
- `line-width.py` in this directory lists overruns of the line width in rendered characters.
