---
name: technical-authoring
description: House style for drafting and editing technical prose (papers, specifications, notes, issues, code comments) with Roly. Plain, factual, conventional English; no rhetorical compression or editorial colour. Use whenever drafting or revising paper or specification text, and when asked to "lose the ticks".
---

# Technical authoring style

Direct, factual, conventional prose: state the thing and stop.

## Sentence construction

Check every sentence of a draft against these rules, including a sentence rewritten only for clarity.

- No negation before a noun ("needs no return", "is bound in neither branch").
- No object relative clauses ("the values no case matches", "the type that the expression synthesises", "the
  values matched by no case"); no possessive relatives ("a function whose cases overlap").
- No comma pivot from assertion to contrast ("It's yours, not a leftover").
- No verbless clause after a comma qualifying the preceding noun ("the entries, empty for a type
  statement").
- No colon standing for a connective ("records 1: disjunction cannot cancel").
- No "that" after a consequential "so" unless readability or emphasis requires it ("parsed first, so that
  its errors take precedence").
- No clefts ("X is what makes...", "this is where...", "is exactly...").
- No coordinated clause acting on the result of the one before ("A match scrutinee synthesises a type, and
  each case checks against it").
- No "following" for agreement or imitation ("following mypy", "following the call-union rule"). No sentence
  ending on "do" or "does" standing for a verb phrase ("as mypy does").
- No clause-final pro-forms ("leaves none", "the others", "so does").
- No pronoun where the subject of the main clause or a nearer noun could also be its antecedent ("rejects a
  program by exit status 3 if it is ill-formed").
- No bare noun for a set already introduced ("no case" for "none of the cases"); no definite reference in a
  general claim ("the variable pattern matches any shape").
- No closing clause restating what the preceding text already says.
- No related, but by itself insufficient, fact appended as though it were a reason; a reason is a fact from
  which a claim follows.
- No example presented as a consequence ("..., so a program may bind a variable named type").
- No singular for a general claim ("a type never mentions an alias"), except for one particular thing, in
  lists, and where the singular reads more naturally, as in an example.
- No gapping ("1 + 2 is an int and 1 + 2.0 a float").
- No article or preposition repeated across an enumeration ("the residual and the remaining type", "subtypes
  of bool or of float").
- No chains of possessives or of-phrases ("the typing specification's algorithm for calls"); no possessive the
  context implies ("their overloads").
- No free relatives ("what it matches").
- No symbol unbound by the sentence or by the judgement form just before it (an unbound τ for the return
  type).
- No subclause opening with a bare abstract noun ("...: agreement, except where...").
- No nested colons or semicolons.
- No "and" joining two independent clauses, whether on one subject (what a thing is and how it is used) or
  on two ("..., and scientific computing is among the fields driving its use").
- No long sentence built by chaining clauses with semicolons or "and".
- No comma before a vocative that follows a short formula of greeting or thanks.
- No sentence opening with mathematics, or with a keyword, name or other identifier that starts with a
  lowercase letter (a rule or metafunction name, "mypy"); no kind prefixed to a lowercase name to avoid it
  ("The type checker mypy rejects").
- No "where" for a condition; "where" binds a symbol ("where n is the arity") or gives a position.
- No construction before its goal; no consequence before its reason.

## Word choice

- No editorial colour or weasel words: "honest", "fib", "conceal", "arguably", "to be fair", "clean",
  "obvious", "simply".
- No metaphor or private jargon: "lands", "spine", "swept across", "destination"; "story" sparingly.
  "Rung" and "ladder" are banned everywhere, including discussion.
- No stand-in for the referent ("the algebra", "the structure").
- No "own" after a possessive, whether a possessive determiner or a genitive ("the node's own positions", "its
  own block", "a commit of its own", "on its own").
- No coined or non-standard term ("shift" for translation), in the text or in conversation; check that a term
  is standard before relying on it.
- No "meet" or "join" as a verb.
- No subordinating "though"; "even though" and adverbial "though" are fine.
- No telling the reader what they "should use"; a trade-off is reported factually.
- No full forms in code comments, test fixtures, READMEs and other documentation ("do not" for "don't"); no
  contractions in papers and specifications.

## Terminology and notation

- No reliance on a term before its concept is introduced; no italics after the first definition.
- No unqualified noun used for more than one kind of thing ("entry" for a context entry or a class entry).
- No compound term shortened to its head noun ("table" for "hash table").
- No change of variable sort within a section.
- No primed metavariable while one of the sort is unused (τ and τ′ for σ and τ); a prime marks a third of the
  sort, or the same thing at a later stage.
- No second notation for an object already given one in an earlier section.
- No structure whose components matter introduced without its tuple form.
- No symbol introduced for a single quantification ("changes by at most δ" in prose instead).
- No "our earlier work" in a double-blind submission.

## Telegraphic text

Telegraphic text omits articles and a final full stop, and makes one main point per item, without framing or
hedging clauses ("Rebinds variable"); a parenthesis or a clause after a semicolon may clarify or qualify the
main point. Text of several sentences is prose, with full stops. Clarity takes
precedence over telegraphic style: keep any word without which the text becomes ambiguous or hard to read.

- Section headings, table cells, figure captions, rule side conditions, todo, design and planning notes,
  and the items of a bulleted or numbered list are telegraphic. Steps of a procedure take the imperative; a
  list of questions keeps full sentences.
- A gloss in apposition keeps one leading article and no other: "head, a literal, class or list of length n".
- No figure caption of more than one line where a single line is possible.

## Comments and checklists

- Check a date or time against the clock or the record before stating it.
- Code comments: see the coding-conventions skill.
- No indirect statement of a task in a checklist or issue ("we could perhaps move X").
- No meta-commentary about the document (moves, supersessions) in the text or in change markup; it belongs
  in the issue tracker.
- No superseded claim kept, contrasted or annotated; the text states the current design only.
- No reporting of completed items alongside remaining ones.

## Structure

- After adding or changing text, reread the surrounding paragraph to check that it still flows.
- No machinery irrelevant to the one dimension of a contrast.
- No non-parallel headings for sibling sections; no shared setup repeated across siblings instead of stated
  once in a common parent.
- No conjecture stated as a result.

## LaTeX

- Name a source file after its definitions and a figure label after its file; rename both when the
  definitions change.
- Name a macro after its rendering (\baseType for base-type), and rename it when the rendering changes.
- After a build, look at each changed page: nothing may run off the page or into the margin.
- Align subfigures placed side by side at the top, and their captions at the bottom.
- Unless instructed otherwise, make edits to a LaTeX document in change markup, prose, rules and figures
  alike: `\added`, `\deleted` and `\replaced{new}{old}` inline, the capitalised variants for a margin change
  bar, and `AddedBlock` and `DeletedBlock` for whole paragraphs or display material. Rewrite a section body
  as a `DeletedBlock` of the old text followed by an `AddedBlock` of the new.
- Mark up at the grain of the change: a changed phrase within a sentence, a rewritten sentence, a new
  sentence. Keep unchanged text outside the markup; do not replace several sentences as one run when only
  some of them change.
- End the old text inside `\replaced` with a space, so that the deleted and added runs do not abut.
- Markup is accepted later, in a commit titled "Change markup accepted"; the final build mode renders the
  clean version.
- Align the side conditions of a definition alike, all in the condition column or all on a separate
  line, with none left overfull. A bare "otherwise" follows its equation after a `\quad`, in parentheses.

## References in conversation

- Refer to a figure, lemma, definition or section by name and by its number in the current PDF, taken
  from the `.aux` of a draft build.
- Refer to prose by its place in the PDF (section, page and opening words), not by its position in the
  LaTeX source or by a macro.
- No quote block around a draft message for the user to send (Slack, email); plain text instead.
- When the user is reviewing a document and objects to a passage, the reply is the replacement text alone: no
  diagnosis of the passage, no account of the rules it breaks or of its intended flow.
