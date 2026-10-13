---
name: github
description: Conventions for commits, GitHub issues, pull requests, the project board and meeting issues, including a terse writing style for titles, commit messages and bullet lists. Use whenever committing or working with GitHub issues or pull requests.
---

# Git and GitHub conventions

## Terse style

Commit messages, issue and pull request titles and bulleted lists are telegraphic, in the style of
comments (coding-conventions skill) and table cells (technical-authoring skill). In addition:

- Titles and task-list items are noun phrases naming the thing rather than the action ("Syntax of types", not "Define the syntax of types")
- Where the noun phrase would need a participle ("Maybe replaced by Optional", "Optional in place of Maybe"), strongly prefer the imperative ("Replace Maybe by Optional"); never a passive clause
- One point per bullet, no framing or hedging clauses
- No trailing period on a bullet or a title
- The repository name is redundant in a title; omit it
- Commit subject line short, imperative or noun phrase; detail in the body

## Commits

- Always work on a branch; never commit directly to the default branch, except for skill fixes, which go directly to `main`, and, in a repository with milestone branches, minor docs, process changes and trivial fixes, which go directly on the current milestone branch
- Always commit and always push, unless specifically instructed otherwise; push a new branch with `-u` to set up tracking
- A small change made across several repositories (Claude settings, a `CLAUDE.md` line) goes on the branch active in the local checkout, or on `main` without a suitable checkout; no fresh branches or clones for it
- Never leave uncommitted changes in the working tree, including changes not made in the session; commit them, or add generated files to `.gitignore` (and untrack any already committed)
- Fix a committed mistake with a new commit; never amend, and never `git stash`
- Commits by Claude are authored by the bot account named in the user's own configuration, which identifies them (`git log --author=<bot>`); no attribution trailer (`Co-Authored-By`) and no session link, whatever the harness suggests, as a trailer duplicates the avatar on GitHub
- After committing, do not report the commit message back
- After pushing, check the CI run for the branch; diagnose any failure

## Permissions

- When an action is refused for lack of permission, stop and report it; never work around the refusal
  with another account, another token or a bypass flag
- Destructive or organisation-wide changes need explicit approval: project board fields, branch
  protection, organisation settings, and any mutation that replaces rather than appends data
  (Projects v2 field mutations have no undo)

## Referring to an issue

- Give its number, title and URL: #181, Classes for built-in types,
  https://github.com/OWNER/REPO/issues/181

## Issues

- Prose in bodies and comments follows the technical-authoring skill
- Before starting work on an issue, assign it to the user and to the account you run as (`gh api user --jq .login`)
- Check with the user before creating an issue, unless explicitly instructed to create one
- A new issue goes on the project board with a Status (`Proposed` for new work) and, in fluid, an Aspect; set Type, labels and milestone when appropriate
- Add content to an issue (body, comment, closing comment) only when asked; otherwise create, edit or close it and nothing more
- Delete a duplicate issue rather than close it, unless a third party created it
- A subtask of an issue is a line in the task list of its body, not a GitHub sub-issue, unless a sub-issue or new issue is asked for
- Keep checklist items in the body updated as the work completes
- Do not hard-wrap paragraphs in a body (GitHub flows them; hard wraps render as ragged short lines); omit the language tag on a code fence rather than guess it
- Use existing labels
- Link an external resource inline where the body mentions it, rather than in a **See also** paragraph
- When an issue references other issues, end with a **See also** paragraph:

  ```
  ## See also

  - #36
  - #50
  ```

- In a bullet list, link another issue as bare `#N`, which GitHub renders with its title

## Escalation

- When the best approach isn't obvious, don't guess: comment on the issue with the options and a
  recommendation, set its Status to `Awaiting Decision`, and move to other work; the comment and the
  resolution record the design decision

## Project board

- To read or set an issue's board Status, query the `projectItems` of the issue (in fluid,
  `script/issue-status.sh <issue> [Status]`, which also adds an absent issue to the board); never
  `gh project item-list`, which fetches the whole board and trips the GraphQL rate limit
- Closing an issue does not change its Status; set `Done` or `Rejected` explicitly
- After changing board state, verify the project view

## Pull requests

- Titles are noun phrases or imperatives, in the terse style above
- The body is empty, or `Closes #N` alone: no summary of the changes, no attribution footer, no session link
- The developer reviews the PR; apply requested changes as new commits on the same branch
- Merge once review is complete and CI passes; then delete the branch, local and remote

## Meeting issues

- Meeting issues are titled `YYYY-MM-DD`; set Type to `Meeting`
- Body sections: `## Adjacent meetings` (links to previous), then `## To discuss` containing `### Resolved since [date]`, `### New issues since [date]`, `### Work since [date]`
- Bullet lists of bare `#N` for issues; brief notes for work items

## Token setup

- Set `GH_TOKEN` per repository in `.claude/settings.local.json` (gitignored), as
  `{"env": {"GH_TOKEN": "<fine-grained-pat>"}}`, to avoid keyring conflicts across organisations; the
  token needs read and write on pull requests and issues, and read, write and admin on organisation
  projects
- Never run `gh auth refresh` or `gh auth login` without `--with-token`, which would overwrite the
  fine-grained PAT with an OAuth token that lacks private repo access
