---
name: spec-implementor
description: Discipline for keeping the checker (and other implementations) in one-to-one correspondence with the spec. Use whenever syncing implementation with spec, or reviewing either against the other.
---

# Spec implementor

Load the coding-conventions skill first, which holds the shared comment, identifier and commit rules.

A sync is complete when the spec and the implementation are in one-to-one correspondence,
checked in both directions; agreement of verdicts is not enough.

## Method

1. Build two inventories: spec constructs (judgements, rules, metafunctions,
   operators, technical terms, section headings) and implementation identifiers
   (functions, classes, constants, test taxonomy, docs).
2. Match by name. Every unmatched item, in either direction, gets one of:
   - **rename** to the spec's name (the spec is the reference; `wraps` in the
     spec means a function called `wraps` in the checker);
   - **delete** as dead code or a displaced term (unused macros, stale labels,
     helpers with no callers).
3. One name must not mean different things on the two sides: the spec
   distinguishes override from extend, so the implementation does too.
4. Diagnostics may refine the spec's single failure mode into specific reasons.
   Name each reason after the prohibition or premise it enforces, and word its
   message as the spec describes the failure: telegraphic, in the form of the
   existing messages, stating the expectation and the finding ("call expects 1
   arguments, given 2").
5. Run the inventory comparison even when all tests pass; verdict checks miss
   misnamed functions, displaced terminology, dead helpers and stale taxonomy.

## Sequential check against the spec

Check both directions in order, not the suspected parts first. Read the specification top down,
finding for each judgement, rule and metafunction the implementation definition with the same name and
purpose. Then read the implementation top down, finding for each definition its construct in the
specification; a definition without exactly one is renamed, moved or deleted. Fix each discrepancy
where the reading reaches it.

## Order of work

Spec first, then tests, then implementation. When the spec changes, write or
adjust the failing test before touching the checker.

## Implementation style

Write in the functional subset of the host language: no
reassignment of a variable once bound, no in-place mutation, no loops that accumulate into a variable.
Build each value in one expression, by comprehension, recursion or a fold (`functools.reduce` in
Python), so that a definition reads like its rule.

## Testing

A test is a small program with an expected outcome: accepted, rejected, or
producing particular output when run.

- **Differential**: every program also runs under the reference
  implementation, and the test's category states the required relationship
  (well-formed: both accept; ill-formed: both reject; prohibited: reference
  accepts, we reject). A misfiled test is itself a failure.
- **Metamorphic**: when the spec says a change is harmless (a commutative or
  idempotent operation), apply it to a passing program: swap sibling imports,
  repeat an import. Verdict and output must not change.
- **Differing pairs**: when the spec says a difference matters (a biased
  operation, a law noted not to hold), the two programs must come out
  differently; the counterexample in the spec is usually the pair to use.
- **Minimal pairs**: for each condition in a rule, two programs differing as
  little as possible, one just meeting it and one just missing it. Error
  messages are not the unit of coverage; one message can arise from several
  unrelated situations, each needing a pair.
- **Whole-program conditions**: test both sides of the boundary, the smallest
  broken case and the largest legal case that resembles one (a self-import
  and a two-module cycle against a diamond).
- **Spec prose**: every worked example, counterexample and justifying sentence
  describes a program; each should exist as a test.
- An implementation other than the reference checker runs the spec's corpus
  whole through a differential harness rather than copying it into its own
  suite, which holds only programs without a corpus counterpart.
- Use programs large enough that recursive rules recurse; a one-level
  example can pass for the wrong reason.
- Audit the suite by mutation: weaken the implementation deliberately and
  confirm a test fails.

## Tooling

Point checkers at whole directories rather than named files, and occasionally
verify that every checker still sees every file.
