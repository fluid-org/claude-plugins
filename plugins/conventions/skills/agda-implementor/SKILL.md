---
name: agda-implementor
description: House conventions for writing Agda. Use whenever writing or editing Agda code.
---

# Agda implementation conventions

Load the coding-conventions skill first; it holds the comment, identifier and commit rules shared
with other implementations, and the rules shared with the Isabelle skill (comments, naming after the
spec, running checkers, pull requests).

## Comments

- `line-width.py` in this directory lists overruns of the line width and, with `--joins`, wrapped
  groups that would fit on one line.

## Qualification and opens

- Open a module rather than qualifying its members (`open Category C` and `_⇒_`, not
  `Category._⇒_ C`). Import every member that does not clash; leave qualified only those that do. A
  synonym serving one or two names should be a narrowed open. `using (module X)` imports a submodule
  and shortens a deep path.
- `module-synonyms.py` in this directory lists every `module X = …` binding with its use count and
  members. Its counts are textual; see its docstring.
- Sibling instances of one module block each other from being opened. If no use site mixes them, give
  each its own block with its own open; qualify only where uses mix.
- Before importing a name, check it is not already in scope: a name reaches a file through an `open`
  without `using` without ever being written, so check what every such open exports.
- Name a synonym after what it denotes (`Tree`, `coKl`, `Fam-cat`), never by initials, primes or
  digits (`FD`, `RS'`, `S1`). When a binding appears only on its own `open` lines, spell it out; when it appears on one,
  drop it and apply the module in the open (`open M args using (…)`).
- Bind a parameter's operations under its own name (`module 𝒞 = Category 𝒞`), not a decorated one
  (`𝒞C`); modules and terms have separate namespaces. In a telescope, `(let module 𝒞 = Category 𝒞)`
  and `(let open M)` make names available to later parameter types; an `open` in the body does not
  reach the telescope.
- With two category parameters 𝒞 and 𝒟, suffix each per-category parameter with the category
  (`CM𝒞`/`CM𝒟`), never prime it.

## Records

- Copatterns, not record literals (`f x .field = …`, not `f x = record { … }`).

## Where blocks

- Do not name a term used once; write it at its use and re-lay out the line. Name terms used more than
  once, and steps whose stated type documents them. `inline-locals.py FILE [--apply]` in this directory
  inlines the one-use single-line untyped locals and reports the rest; check line widths afterwards.

## Elaboration pitfalls

- Unification cannot invert defined functions under `map`/`foldr`; pass the blocked implicits
  explicitly (`{C = …}`). Implicit binders that are only ever applied need type ascriptions
  (`∀ {G S : Gr}`).
- `with e in eq` abstracts `e` from the goal and breaks lemmas that mention `e`. When the scrutinee
  occurs in helper types, use a case helper instead
  (`bool-case : ∀ b → (b ≡ true → A) → (b ≡ false → A) → A`).
- A `where` function cannot refine the parent clause's variables by matching an equality; make the
  refined thing an explicit argument of a helper and match `≡-refl` there, dot-patterning the other
  side.

## Running agda

- Every non-trivial check: `bash ~/.claude/bin/watch-agda.sh <targets>` as a background Bash task with
  `timeout` 600000. Without the timeout a run over 120 s is killed and reported as interrupted.
- `pgrep -x agda` before a check; the build directory is `_build`.
- No Monitor tool or detached runs. If a check would exceed ten minutes, split it into sequential
  `watch-agda.sh` calls on intermediate targets.
- The log is truncated per run: read the RTS statistics before the next check.
- `touch` does not invalidate an interface; change a character.
- `-v` flags are ignored; bisect with probe files.

## Performance

- Before any performance test, propose the evaluation strategy — metric, measurement points,
  expected values and durations — and discuss it; run nothing until agreed. Prefer deterministic
  counts over timing; run the counting measurement first.
- Three separate metrics: Agda type-checking time, GHC compile time, and binary run time. Time each
  on its own; never time a script that mixes them.
- Let the compile finish untimed, then time the binary alone; compilation is incremental, so a
  mixed timing means nothing.
- Validate a change expected to be performance-neutral by the type-check and the baseline artefact
  comparison; benchmark only changes that claim an effect or touch the measured code.
- The heap cap (`GHCRTS -M12G`, set by `watch-agda.sh`) turns divergence into exit 251 within minutes;
  low productivity in the GC summary means thrashing.
- Cost is module application, not proving: a large `Miscellaneous` share in a profile is applications
  and interfaces. Reduce what is copied; tuning arguments does not help.
- Narrow every `open … public` with a `using` list, binding the application once:

      private
        module GF = some.module args
      open GF
      open GF public using (f; g)

- Give a module the smallest telescope its contents need. Splitting a large parameterised module so
  consumers instantiate only what they use is the biggest lever; check what each consumer references
  first.
