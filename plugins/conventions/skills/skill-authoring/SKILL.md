---
name: skill-authoring
description: Conventions for writing and revising skills. Use whenever creating or editing a skill.
---

# Skill authoring

Load the technical-authoring and coding-conventions skills first; their rules on brevity, telegraphic style
and comments apply to skills and are not repeated here.

- Avoid history in a rule, such as an account of how the rule arose or the case that prompted it.
- Decisions do not become rules. A choice made for one formalisation, codebase or document is recorded
  there; a skill gains the rule behind it only when the rule holds in every case the skill covers.
- Avoid facts the repository already records, such as identifiers or file layout.
- A rule goes in the most general skill whose every case it fits; refer to another skill rather than
  restate its rules.
- Avoid project-specific details in a shared skill.
- Identified pitfalls don't become skills; by default add to the skill only on request.
- Before adding a rule, check the skill and the skills it loads for one that already covers it.
- Avoid positive overspecification; concentrate on antipatterns.
- A rule names the problem, with an example of it; it does not prescribe the rewrite.
- State the rule, without its reason or the failure it prevents.
- Prefer "avoid" to "never" in a rule ("Avoid amending a commit", not "Never amend a commit").
