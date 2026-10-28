---
name: coding-conventions
description: Shared conventions for code in any language (comments, docstrings, identifiers, defensive code, commit granularity). Use whenever writing or editing code, alongside the language-specific skill (agda-implementor, isabelle-implementor, spec-implementor).
---

# Coding conventions

## Recording guidance

- Never save guidance to Claude's memory, or to notes or any other file outside a repository. Record a
  lasting rule in the skill it belongs to, in this plugin or in a project's own skill, and commit it.
  Project state belongs in the issue tracker.
- Writing a skill: see the skill-authoring skill.

Language-specific skills (agda-implementor, isabelle-implementor, spec-implementor) add to these;
correspondence with a specification (inventories, naming, diagnostics, corpus testing) is in
spec-implementor.

## Comments and docstrings

- Comment only what the code cannot show: no process commentary, source-file names, history or plans,
  except for a transitional definition (below).
- One line where possible, telegraphic as defined in the technical-authoring skill ("Collapse duplicate
  rows", not "This collapses the duplicate rows"); bare imperative for operations ("Collapse", not
  "Collapses"); contractions rather than formal verbs ("can't", not "cannot"). Same in test fixtures.
- A comment speaks of the definition it sits on, as an operation or a noun phrase, never as a bare
  fact about the domain: "Bind a function at its type when its signature has no type parameters", not
  "A signature without type parameters is a type". A fact may follow as the reason ("..., since ...").
- No comment on a definition named after a construct of the specification or paper; the
  specification describes it. Refer to a construct by name, never by quoted notation.
- Standard terms in comments and identifiers; never coin a word ("carry no type", not "typeless").
- No code identifiers in a comment or docstring, except parameters of the documented definition;
  describe the operation in words ("type resolution", not "resolve_type").
- No notation from the specification or paper in a comment (`C[τs]`, `Γ ⊢ e`); write it in words,
  naming parameters of the documented definition where needed. Prefer a name that makes the comment
  unnecessary.
- A transitional definition (a bridge between an old and a new representation, say) states the
  anomaly and the change that removes it ("delete with the α-graph").
- A comment sits on the definition it describes, not on a caller.

## Identifiers

- Name a thing after what it denotes, in the specification's terms (`rNoMatch`, the outcome of the
  no-match path), not an image (`rFall`) and not by initials.
- Follow the specification's or paper's metavariables, not a library's: one name per sort (`cxt` for
  every context, whether the paper writes Γ or Δ; `ρ` for environments; `v`, `u` for values). Where
  names run short, a prime (`cxt'`); a suffix naming the content (`cxt_αs`, the context of type
  parameters) only where a second prime would be needed; never a digit.

## Code

- Build on existing helpers and naming; scan the codebase before writing.
- No defensive coding: assert a case that shouldn't arise rather than returning a safe default.
  User-facing failures go through the monad, with a message naming the construct and the offending
  element, without pronouns ("Class C extends int, which is not a class").
- Inline a local used once; bind an expression used twice once.
- In Haskell and PureScript, a local that depends only on the arguments goes in `where`, not `let`.
- Function clauses rather than a `case` on an argument.
- A short monadic chain as one expression, not a `do` block.
- Type annotations on the binding, not the expression.
- Related definitions adjacent.
- Wrap at about column 110; a little over is fine.
- End every file with exactly one newline: no blank line at the end, and no missing final newline (symbolic links excepted).
- In fluid, no new JavaScript: scripts in Bash or Python, and code that must run on Node in PureScript
  (a command of the command-line tool, say).

## Proof assistants

Shared by the Agda and Isabelle skills.

- Never cite the paper or specification in a comment (sections, figures, rule names as references).
  State the mathematics; the paper cites the mechanisation, not the reverse.
- Run every non-trivial check as a background Bash task with an explicit `timeout`; never two checkers
  over one build directory.
- Pull requests as in the github skill; bump the parent repository's submodule pointer once one merges.
  Refer to commits by their messages, not their hashes.

## Tests

- No test whose only purpose is to pin a fixed bug.

## Commits

- Commit each verified unit of work without asking first; conventions in the github skill.

## Reporting

- Report the current state, not how it got there; leave out history, mistakes, failed attempts and
  problems already resolved, unless the user must act on them.
- Refer to programs, commands and scripts by the names the repository gives them (their entries in
  `pyproject.toml`, say), never by descriptions such as "driver".
