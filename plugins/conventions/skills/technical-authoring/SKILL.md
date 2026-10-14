---
name: technical-authoring
description: House style for drafting and editing technical prose (papers, specifications, notes, issues, code comments) with Roly. Plain, factual, conventional English; no rhetorical compression or editorial colour. Use whenever drafting or revising paper or specification text, and when asked to "lose the ticks".
---

# Technical authoring style

Direct, factual, conventional prose: state the thing and stop.

## Sentence construction

Check every sentence of a draft against the rules below before sending it, including a sentence rewritten
only for clarity; a rewrite for clarity alone reintroduces breaches.

- **Negation on the verb.** Never put "no", "none", "nothing" or "neither" before a noun, whether the noun
  is a subject, an object or the agent of a participle: "does not need a return statement", not "needs no
  return"; "does not fix any length", not "fixes no length"; "is not bound in either branch", not "is bound
  in neither branch". Where an affirmative statement says the same thing, prefer it: "admits values of
  every length".
- **No object relative clauses**, in which the head noun is the object of the verb inside the clause:
  "the values no case matches", "the type that the expression synthesises", "the values matched by no
  case", "every edge a rule adds". Make the head noun the subject of its modifier. Name the thing where a
  term exists ("the residual", "the matched shapes"); otherwise use a passive participle with a plain agent
  ("the type synthesised by the expression", "every edge added by a rule"); otherwise write a full
  "which" clause with the negation on the verb ("the values which are not matched by any of the cases").
  A possessive relative falls under the same rule: "a function with overlapping cases", not "a function
  whose cases overlap".
- No pithy constructions pivoting on a comma from assertion to contrast: "It's yours, not a leftover."
- No verbless clause after a comma qualifying the preceding noun ("the class table entries, empty for a
  type statement"); give it a verb ("which are empty for a type statement") or a separate sentence.
- Spell out logical connectives ("because X", "so that X") rather than a bare colon-assertion: "records 1,
  because disjunction cannot cancel", not "records 1: disjunction cannot cancel".
- No cleft constructions ("X is what makes...", "this is where...", "is exactly...", "is precisely...");
  use a direct verb with a named subject: "Idempotent addition induces an order", not "Idempotent addition
  is what relates the algebra to an order".
- Where a second clause acts on the result of the first, subordinate it rather than coordinating with
  "and" and a pronoun: "A match scrutinee synthesises a type, against which each case is checked", not
  "..., and each case checks against it".
- Lead a comparison with "following" rather than a trailing "as in X" or "as X do", and never end a
  sentence on "do" or "does" standing in for an earlier verb phrase: "takes the scrutinee's type into
  account, following the uncovered sets of Karachalias et al."
- Avoid clause-final pro-forms ("leaves none", "the others", "the same holds", "so does"); repeat the noun
  or restructure.
- Do not restate a point in a closing clause or sentence that the preceding text already makes.
- Refer definitely to a finite set already introduced: "not matched by any of the cases", "each of the
  branches". A general claim keeps the bare noun: "a variable pattern matches any shape".
- Make a general claim in the plural: "so types never mention aliases", not "so a type never mentions an
  alias". The singular stays where one particular thing is meant, and in lists.
- Do not repeat an article across the items of an enumeration: "the residual and remaining type".
- Name things with nouns rather than free relative clauses: "matched shapes", not "what it matches".
- Bind a symbol in the sentence or by a judgement form stated just before it; otherwise name the thing:
  "checks its expression against the return type", not "against τ" with τ unbound.
- Do not open a subclause with a bare abstract noun ("...: agreement, except where..."); give it a subject
  and verb ("the two agree, except where...").
- No nested colons or semicolons within a sentence.
- Never open a sentence with a metafunction name, a rule name, or other mathematics; lead with a word
  ("The set of ... is captures(s)", "The var rule applies whenever ...").
- A condition takes "if" or "when", not "where". Reserve "where" for positions ("the rows differ where the
  pattern is a literal") and for binding a symbol ("where n is the arity").
- State the goal before the construction, and the reason before the consequence: not "we require the meet
  to cohere" before saying what coherence achieves.

## Word choice

- Editorial colour and weasel-words: "honest"/"honestly", "fib", "conceal", "arguably", "to be fair", "clean", "obvious", "simply".
- Metaphor and private jargon: "lands", "spine", "swept across", "walking the axis", "destination", "stage-factorisation" and similar compounds. "Story" sparingly; prefer a concrete noun ("the semimodule picture").
- "Rung" and "ladder": banned project-wide, in prose and in discussion.
- Vague nominal back-reference: "the algebra", "the structure". Name the referent.
- "Own" as a distinguishing qualifier ("the node's own positions"): state the distinction instead
  (the positions at the node itself, not those of its descendants).
- Invented terms where standard ones exist: "translation" not "shift"; "the other factor" not "cofactor". Check a term is standard before leaning on it, and cite where useful. Do not coin terminology, in the text or in conversation ("foreign module", "fresh position"); use the document's own terms or plain description ("a module other than the current one").
- "Meet" and "join" are nouns, not verbs: "the matched type is the meet of the scrutinee type and float", not "the scrutinee type meets float".
- "though" as a subordinating conjunction: prefer "although". The fixed phrase "even though" and the adverbial "though" meaning however are unaffected.
- Guidance-speak when the content is a trade-off: report the trade-off factually rather than telling the reader what they "should use".

## Terminology and notation

- Introduce a term before relying on it; if it first appears mid-argument ("orthogonality", "specialising", "De Morgan dual"), move its introduction to where the concept first appears. Italicise on first definition only, and drop italics that add nothing.
- Qualify a noun used by the document for more than one kind of thing wherever the bare noun could be misread: a context entry or a class entry, not "entry".
- Do not shorten a compound term to its head noun: "hash table", never "table" on its own, even on a
  second mention in the same paragraph.
- Keep variable sorts consistent within a section (a, b for scalars; x, y for semimodule elements).
- Use every metavariable of a sort before reaching for a prime: two types are sigma and tau, not tau and tau prime. A prime is for the third of a sort, or where the two are the same thing at different stages.
- One notation per object across the paper: S² rather than a mix of S ⊕ S and 𝕀; follow whichever convention earlier sections established.
- Write a structure out as a tuple at first use if its components matter.
- Prefer prose quantification ("changes by at most δ") over symbols not reused by the text (δx).
- In double-blind submissions: "earlier work on X", never "our earlier work".

## Telegraphic text

- Table cells, figure captions and rule side conditions are telegraphic: no articles ("Rebinds variable", not "Rebinds a variable"; "neither list type nor union"). A gloss in apposition after a comma or colon within a cell keeps a leading article, which marks where the gloss begins, and no other: "head, a literal, class or list of length n", not "head, a literal, a class or a list of length n"; "context, a finite map from variables to entries".

## Comments and checklists

- Check a date or time against the clock or the record before stating it, including "yesterday" and "today".
- Code comments: see the coding-conventions skill.
- Checklists and issues: state the task directly ("Move X here; add Y"), no scene-setting.
- Meta-commentary about the document (moves, supersessions) belongs in the issue tracker, never in the text, including inside change markup.
- State the current design and nothing about how it evolved; never contrast it with a superseded design
  ("an earlier design allocated addresses"). When the design changes, delete superseded claims rather than
  annotating them as outdated.
- When reporting the remaining items of a list of tasks or issues, give those items only; do not
  mention items already resolved, removed or deferred, even to explain their absence.

## Structure

- After adding or changing text, reread the whole paragraph around it and check that it still flows: the sentence before the change must lead into it, the sentence after it must follow from it, and an insertion must not interrupt a sequence of sentences on a single topic. Where the paragraph no longer flows, move or reword the surrounding sentences.
- When contrasting two things, frame the sentence around the one dimension of contrast and leave out machinery irrelevant to it (e.g. both maps oriented the same way, so the contrast is join- versus meet-preservation).
- Prefer parallel headings for sibling sections; if two sections share their setup, consider a common parent that states the setup once.
- Mark conjectures as conjectures; do not present a suspicion as a finding.

## LaTeX

- Name a source file after the definitions in it, and rename it when they change. A figure label
  follows the file name.
- A macro is named after its rendering (\baseType for base-type, not \widen), and is renamed when the
  rendered name changes.
- After a build, render each changed page and look at it: no figure, rule, table or definition row may run
  off the page or noticeably into the margin.
- Side conditions of a definition are aligned with one another: all in the condition column, or all on
  their own line under the equation, indented alike. Do not mix the two within a definition, and do not
  leave one condition overfull while the rest align. A bare "otherwise" is the exception: it follows the
  equation on the same line after a `\quad`, in parentheses.

## References in conversation

- Refer to a figure, lemma, definition or section of the specification or paper by name and number in
  the current PDF (the shape-typing figure, Figure 4.13 in the specification). Look the number up in the
  `.aux` of a draft-mode `pdflatex` run; don't guess it.
