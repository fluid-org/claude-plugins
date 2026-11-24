---
name: technical-authoring
description: House style for technical writing with Roly. Plain, factual, conventional English; no rhetorical compression or editorial colour. Use whenever drafting or revising text of any kind (papers, specifications, notes, issue bodies, code comments), and when asked to "lose the ticks".
---

# Technical authoring style

Direct, factual, conventional prose: state the thing and stop. The rules apply to every text, whether paper,
specification, notes or issue body, and whether prose or telegraphic.

## Sentence construction

Check every sentence of a draft against these rules, including a sentence rewritten only for clarity.

- Avoid negation before a noun ("needs no return", "is bound in neither branch").
- Avoid object relative clauses ("the values no case matches", "the type that the expression synthesises",
  "the values matched by no case") and possessive relatives ("a function whose cases overlap").
- Avoid a comma pivot from assertion to contrast ("It's yours, not a leftover").
- Avoid an adjectival phrase or verbless clause after a comma qualifying the preceding noun, in prose or in
  telegraphic text ("the entries, empty for a type statement"; "classes of the objects, each class with its
  field names").
- Avoid a colon standing for a connective ("records 1: disjunction cannot cancel").
- Avoid "that" after a consequential "so" unless readability or emphasis requires it ("parsed first, so that
  its errors take precedence").
- Avoid clefts ("X is what makes...", "this is where...", "is exactly...").
- Avoid a coordinated clause acting on the result of the preceding clause ("A match scrutinee synthesises a type,
  and each case checks against it").
- Avoid "following" for agreement or imitation ("following mypy", "following the call-union rule"), and a
  sentence ending on "do" or "does" standing for a verb phrase ("as mypy does").
- Avoid clause-final pro-forms ("leaves none", "the others", "so does").
- Avoid making the main point of a sentence depend on a reference back, whether a pronoun, demonstrative
  phrase or new noun for a thing already named ("a vertex maps to the vertices with it as last dependent"),
  and a pronoun standing for a whole statement ("the two must still behave as unrelated, which confirms that
  storage identity carries no meaning").
- Avoid a pronoun when the subject of the main clause or a nearer noun could also be its antecedent, by
  fitting the grammar or being of the same sort ("rejects a program by exit status 3 if it is ill-formed").
- Avoid a bare noun for a set already introduced ("no case" for "none of the cases"), and a definite
  reference in a general claim ("the variable pattern matches any shape").
- Avoid a closing clause restating what the preceding text already says.
- Avoid appending a related, but by itself insufficient, fact as though it were a reason; a reason is a fact
  from which a claim follows.
- Avoid presenting an example as a consequence ("..., so a program may bind a variable named type").
- Avoid the singular for a general claim ("a type never mentions an alias"), except for one particular
  thing, in lists, and where the singular reads more naturally, as in an example.
- Avoid gapping ("1 + 2 is an int and 1 + 2.0 a float").
- Avoid repeating an article or preposition across an enumeration ("the residual and the remaining type",
  "subtypes of bool or of float"), or a subject as a pronoun across coordinated predicates ("the subvalues
  could be stored once, and they must still behave as unrelated").
- Avoid chains of possessives or of-phrases ("the typing specification's algorithm for calls"), and a
  possessive the context implies ("their overloads").
- Avoid free relatives ("what it matches").
- Avoid a symbol unbound by the sentence or by the judgement form just before it (an unbound τ for the return
  type).
- Avoid opening a subclause with a bare abstract noun ("...: agreement, except where...").
- Avoid nested colons or semicolons.
- Avoid "and" joining two independent clauses, whether on one subject (what a thing is and how it is used)
  or on two ("..., and scientific computing is among the fields driving its use").
- Avoid a long sentence built by chaining clauses with semicolons or "and".
- Avoid a comma before a vocative that follows a short formula of greeting or thanks.
- Avoid opening a sentence with mathematics, or with a keyword, name or other identifier that starts with a
  lowercase letter (a rule or metafunction name, "mypy"), and a kind prefixed to a lowercase name to get
  round the rule ("The type checker mypy rejects").
- Avoid "where" for a condition ("where the list is empty").
- Avoid a construction before its goal, and a consequence before its reason.
- Avoid a declarative statement intended as an instruction ("a further release has a post-release suffix").

## Word choice

- Avoid editorial colour and weasel words: "honest", "fib", "conceal", "arguably", "to be fair", "clean",
  "obvious", "simply".
- Avoid metaphor and private jargon: "lands", "spine", "swept across", "destination"; "story" except
  sparingly. Avoid "rung" and "ladder" everywhere, including discussion.
- Avoid a stand-in for the referent ("the algebra", "the structure").
- Avoid "own" after a possessive, whether a possessive determiner or a genitive ("the node's own positions",
  "its own block", "a commit of its own", "on its own").
- Avoid coined or non-standard terms ("shift" for translation), and standard terms in a non-standard sense
  ("derived instance" for an instance obtained from a constraint), in the text or in conversation.
- Avoid "meet" or "join" as a verb.
- Avoid subordinating "though"; "even though" and adverbial "though" are fine.
- Avoid telling the reader what they "should use".
- Avoid full forms in code comments, test fixtures, READMEs and other documentation ("do not" for "don't"),
  and contractions in papers and specifications.

## Terminology and notation

- Avoid relying on a term before its concept is introduced, and italics after the first definition.
- Avoid an unqualified noun used for more than one kind of thing ("entry" for a context entry or a class entry).
- Avoid shortening a compound term to its head noun ("table" for "hash table").
- Avoid changing variable sort within a section.
- Avoid a primed metavariable while one of the sort is unused (τ and τ′ for σ and τ); a prime marks a third of the
  sort, or the same thing at a later stage.
- Avoid a second notation for an object already given one in an earlier section.
- Avoid introducing a structure with significant components without its tuple form.
- Avoid introducing a symbol for a single quantification.
- Avoid "our earlier work" in a double-blind submission.

## Telegraphic text

Telegraphic text omits articles and a final full stop, and makes one main point per item, without framing or
hedging clauses ("Rebinds variable"); a parenthesis or a clause after a semicolon may clarify or qualify the
main point. Text of several sentences is prose, with full stops. Clarity takes
precedence over telegraphic style: keep any word without which the text becomes ambiguous or hard to read.

- Section headings, table cells, figure captions, rule side conditions, todo, design and planning notes,
  and the items of a bulleted or numbered list are telegraphic. Steps of a procedure take the imperative; a
  list of questions keeps full sentences.
- A gloss in apposition keeps one leading article and no other: "head, a literal, class or list of length n".
- Avoid a figure caption of more than one line where a single line is possible.

## Comments and checklists

- Check a date or time against the clock or the record before stating it.
- Code comments: see the coding-conventions skill.
- Avoid meta-commentary about the document (moves, supersessions) in the text or in change markup.
- Avoid keeping, contrasting or annotating a superseded claim.
- Avoid reporting completed items alongside remaining items.

## Structure

- After adding or changing text, reread the surrounding paragraph to check that it still flows.
- Avoid machinery irrelevant to the one dimension of a contrast.
- Avoid non-parallel headings for sibling sections, and shared setup repeated across siblings.
- Avoid stating a conjecture as a result.

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
- Avoid a quote block around a draft message for the user to send (Slack, email).
- When the user is reviewing a document and objects to a passage, avoid diagnosing the passage or explaining
  its intended flow.
