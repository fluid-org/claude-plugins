---
name: technical-authoring
description: House style for drafting and editing technical prose (papers, specifications, notes, issues, code comments) with Roly. Plain, factual, conventional English; no rhetorical compression or editorial colour. Use whenever drafting or revising paper or specification text, and when asked to "lose the ticks".
---

# Technical authoring style

Direct, factual, conventional prose: state the thing and stop.

## Sentence construction

Check every sentence of a draft against these rules, including a sentence rewritten only for clarity.

- **Negation on the verb**, never before a noun: "does not need a return", not "needs no return"; "is not
  bound in either branch", not "is bound in neither branch". Prefer an affirmative that says the same
  thing: "admits values of every length".
- **No object relative clauses**: "the values no case matches", "the type that the expression
  synthesises", "the values matched by no case". Make the head noun the subject of its modifier: a term
  where one exists ("the residual"); otherwise a passive participle with a plain agent ("the type
  synthesised by the expression"); otherwise a "which" clause with the negation on the verb ("the values
  which are not matched by any of the cases"). Possessive relatives likewise: "a function with
  overlapping cases", not "a function whose cases overlap".
- No comma pivot from assertion to contrast: "It's yours, not a leftover."
- No verbless clause after a comma qualifying the preceding noun ("the entries, empty for a type
  statement"); give it a verb or a sentence of its own.
- Spell out connectives: "records 1, because disjunction cannot cancel", not "records 1: disjunction
  cannot cancel".
- Drop "that" after "so" where the sentence stays clear: "parsed first, so its errors take precedence".
- No clefts ("X is what makes...", "this is where...", "is exactly..."): "Idempotent addition induces an
  order".
- Subordinate a clause that acts on the result of the one before: "A match scrutinee synthesises a type,
  against which each case is checked", not "..., and each case checks against it".
- Lead a comparison with "following", not a trailing "as in X" or "as X do"; never end a sentence on
  "do" or "does" standing for a verb phrase.
- No clause-final pro-forms ("leaves none", "the others", "so does"); repeat the noun or restructure.
- Do not restate in a closing clause what the preceding text already says.
- Refer definitely to a set already introduced ("any of the cases"); a general claim keeps the bare noun
  ("a variable pattern matches any shape").
- General claims in the plural: "types never mention aliases", not "a type never mentions an alias". The
  singular stays for one particular thing and in lists.
- Repeat the verb in a coordinated clause rather than leave it implicit (gapping): "1 + 2 is an int and
  1 + 2.0 is a float", not "1 + 2 is an int and 1 + 2.0 a float".
- Do not repeat an article or preposition across an enumeration: "the residual and remaining type",
  "subtypes of bool or float".
- No chains of possessives or of-phrases ("the typing specification's algorithm for calls"); restructure, or
  drop a possessive the context implies ("the overloads", not "their overloads").
- Nouns, not free relatives: "matched shapes", not "what it matches".
- Bind every symbol in the sentence or in the judgement form just before it; otherwise name the thing
  ("the return type", not an unbound τ).
- Do not open a subclause with a bare abstract noun ("...: agreement, except where..."); give it a
  subject and verb.
- No nested colons or semicolons.
- No comma before a vocative that follows a short formula of greeting or thanks.
- Never open a sentence with mathematics, or with a keyword, name or other identifier that starts with a
  lowercase letter (a rule or metafunction name, "mypy"): "The var rule applies...". Restructure rather than
  prefix a lowercase name with its kind: "For mypy, the code is unreachable", "is rejected by mypy", not "The
  type checker mypy rejects".
- Conditions take "if" or "when"; reserve "where" for positions and for binding a symbol ("where n is the
  arity").
- Goal before construction, reason before consequence.

## Word choice

- No editorial colour or weasel words: "honest", "fib", "conceal", "arguably", "to be fair", "clean",
  "obvious", "simply".
- No metaphor or private jargon: "lands", "spine", "swept across", "destination"; "story" sparingly.
  "Rung" and "ladder" are banned everywhere, including discussion.
- Name the referent, not "the algebra" or "the structure".
- No "own" as a distinguishing qualifier ("the node's own positions"); state the distinction.
- Standard terms only ("translation", not "shift"); check that a term is standard before relying on it,
  and never coin one, in the text or in conversation.
- "Meet" and "join" are nouns, not verbs.
- "Although", not subordinating "though"; "even though" and adverbial "though" are fine.
- Report a trade-off factually; do not tell the reader what they "should use".

## Terminology and notation

- Introduce a term where its concept first appears, before relying on it. Italicise on first definition
  only.
- Qualify a noun used for more than one kind of thing: a context entry or a class entry, not "entry".
- Never shorten a compound term to its head noun: "hash table", never "table".
- Keep variable sorts consistent within a section.
- Use every metavariable of a sort before priming: σ and τ, not τ and τ′. A prime marks a third of the
  sort, or the same thing at a later stage.
- One notation per object, following earlier sections.
- Write a structure out as a tuple at first use if its components matter.
- Prefer prose quantification ("changes by at most δ") over symbols not used again.
- In double-blind submissions: "earlier work on X", never "our earlier work".

## Telegraphic text

Telegraphic text omits articles and a final full stop, and makes one point per item, without framing or
hedging clauses ("Rebinds variable"). Text of several sentences is prose, with full stops. Clarity takes
precedence over telegraphic style: keep any word without which the text becomes ambiguous or hard to read.

- Section headings, table cells, figure captions, rule side conditions, todo notes and the items of a
  bulleted or numbered list are telegraphic. Steps of a procedure take the imperative; a list of questions
  keeps full sentences.
- A gloss in apposition keeps one leading article and no other: "head, a literal, class or list of length n".
- Keep a figure caption to a single line where possible.

## Comments and checklists

- Check a date or time against the clock or the record before stating it.
- Code comments: see the coding-conventions skill.
- Checklists and issues: state the task directly ("Move X here; add Y").
- Meta-commentary about the document (moves, supersessions) belongs in the issue tracker, never in the
  text or in change markup.
- State the current design only; delete superseded claims rather than contrasting or annotating them.
- When reporting remaining items, give only those.

## Structure

- After adding or changing text, reread the surrounding paragraph to check that it still flows.
- Frame a contrast around its one dimension, leaving out machinery irrelevant to it.
- Parallel headings for sibling sections; state shared setup once, in a common parent.
- Mark conjectures as conjectures.

## LaTeX

- Name a source file after its definitions and a figure label after its file; rename both when the
  definitions change.
- Name a macro after its rendering (\baseType for base-type), and rename it when the rendering changes.
- After a build, look at each changed page: nothing may run off the page or into the margin.
- Report a build only if it fails.
- Align subfigures placed side by side at the top, and their captions at the bottom.
- Unless instructed otherwise, make edits to a LaTeX document in change markup, prose, rules and figures
  alike: `\added`, `\deleted` and `\replaced{new}{old}` inline, the capitalised variants for a margin change
  bar, and `AddedBlock` and `DeletedBlock` for whole paragraphs or display material. Rewrite a section body
  as a `DeletedBlock` of the old text followed by an `AddedBlock` of the new.
- End the old text inside `\replaced` with a space, so that the deleted and added runs do not abut.
- Markup is accepted later, in a commit titled "Change markup accepted"; the final build mode renders the
  clean version.
- Align the side conditions of a definition alike, all in the condition column or all on their own
  line, with none left overfull. A bare "otherwise" follows its equation after a `\quad`, in parentheses.

## References in conversation

- Refer to a figure, lemma, definition or section by name and by its number in the current PDF, taken
  from the `.aux` of a draft build.
- Refer to prose by its place in the PDF (section, page and opening words), never by its position in the
  LaTeX source or by a macro.
