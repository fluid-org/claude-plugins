---
name: coding-conventions
description: Shared conventions for code in any language (comments, docstrings, identifiers, defensive code, commit granularity). Use whenever writing or editing code, alongside the language-specific skill (agda-implementor, spec-implementor).
---

# Coding conventions

## Recording guidance

- Never save guidance to Claude's memory. Record a lasting rule in the skill it belongs to, in this plugin
  (fluid-org/claude-plugins) or in a project's own skill if only that project needs it, and commit it.
  Project state belongs in the issue tracker.

Language-specific skills (agda-implementor, spec-implementor) add to these; correspondence with a
specification (inventories, naming, diagnostics, corpus testing) is in spec-implementor.

## Comments and docstrings

- Comment only what the code cannot show: no process commentary, reasoning, source-file names,
  history or plans. Plans and remaining work belong in the issue tracker, not the codebase. Sole
  exception: a transitional definition (below).
- One line where possible, telegraphic, without articles, as in a table cell ("Collapse duplicate
  rows", not "This collapses the duplicate rows"); bare imperative for operations ("Collapse", not
  "Collapses"); contractions fine. Same in test fixtures.
- No comment on a definition named after a construct of the specification or paper; the
  specification describes it. Refer to a construct by name, never by quoted notation.
- Standard terms, in comments and identifiers alike; never coin a word or jargon ("carry no type",
  not "typeless").
- No code identifiers in a comment or docstring, since a rename leaves them stale; describe the
  operation in words ("type resolution", not "resolve_type"). Parameters of the documented definition
  are exempt.
- A transitional definition (a bridge between an old and a new representation, say) states the
  anomaly and the change that removes it ("retire with the α-graph"), so that nothing new builds on
  it; the plan itself stays in the issue tracker.
- A comment sits on the definition it describes, not on a caller.

## Identifiers

- Name a thing after what it denotes, in the specification's terms (`rNoMatch`, the outcome of the
  no-match path), not an image (`rFall`) and not by initials.
- Follow the specification's or paper's metavariables, not a library's: one name per sort (`cxt` for
  every context, whether the paper writes Γ or Δ; `ρ` for environments; `v`, `u` for values). Where
  names run short, a suffix naming what was added (`cxt_αs`, the context with type parameters), not
  a digit.

## Code

- Build on existing helpers and naming; scan the codebase before writing.
- No defensive coding: assert a case that shouldn't arise rather than returning a safe default.
  User-facing failures go through the monad, with a message naming the construct and the offending
  element, without pronouns ("Class C extends int, which is not a class").
- Inline a local used once; bind an expression used twice once. A pure helper that doesn't close over
  locals goes to top level.
- In Haskell and PureScript, a local that depends only on the arguments goes in `where`, not `let`.
- Function clauses rather than a `case` on an argument.
- A short monadic chain as one expression, not a `do` block.
- Type annotations on the binding, not the expression.
- Related definitions adjacent.
- Wrap at about column 110; a little over is fine.
- In fluid, no new JavaScript: scripts in Bash or Python, and code that must run on Node in PureScript
  (a command of the command-line tool, say).

## Tests

- No test whose only purpose is to pin a fixed bug.

## Commits

- Commit each verified unit of work without asking first; conventions in the github skill.

## Reporting

- Report the current state, not how it got there (no pre-commit moves or intermediate names);
  mention history only when the user must act on it (a rebase to pull).
- Leave out mistakes, failed attempts and problems resolved before the report, unless the user must
  act on them.
