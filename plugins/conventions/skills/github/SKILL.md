---
name: github
description: Conventions for commits, GitHub issues, pull requests, the project board and meeting issues, including a terse writing style for titles, commit messages and bullet lists. Use whenever committing or working with GitHub issues or pull requests.
---

# Git and GitHub conventions

## Terse style

Commit messages, issue and pull request titles and bulleted lists are telegraphic, as defined in the
technical-authoring skill. In addition:

- Titles and task-list items are noun phrases naming the thing rather than the action ("Syntax of types", not "Define the syntax of types")
- Where a noun phrase would need a participle ("Maybe replaced by Optional"), use the imperative ("Replace Maybe by Optional")
- No repository name in a title
- Commit message a subject line only, succinctly describing the change as an imperative or noun phrase; no body
- Names of workflows, jobs and steps in GitHub Actions likewise: a noun phrase for a workflow or job, the
  imperative for a step

## Commits

- Always work on a branch, for the current issue when there is one, since new work does not need an issue; never commit directly to the default branch, except for skill fixes, which go directly to `main`, and, in a repository with milestone branches, minor docs, process changes and trivial fixes, which go directly on the current milestone branch
- Name the branch after the issue, number first (`247-syntax`), or after the work when there is no issue (`min-max`); when a feature branch for the issue collects the work of several subtasks, name the feature branch after the issue and each sub-branch off it after its subtask
- While a branch is checked out, all work goes on it, related to its purpose or not; a new branch only when asked for
- Work in the existing local clone, on the branch checked out there; a worktree only when asked for, or when another session is modifying
  the clone
- Always commit, unless specifically instructed otherwise; push only when asked, a new branch with `-u` to set up tracking
- Every push starts CI, so push once a unit of work is complete, not after each commit; while the user reviews
  an open pull request on GitHub, push each commit made in response
- A small change made across several repositories (Claude settings, a `CLAUDE.md` line) goes on the branch active in the local checkout, or on `main` without a suitable checkout; no fresh branches or clones for it
- Never leave uncommitted changes in the working tree, including changes not made in the session; commit them, or add generated files to `.gitignore` (and untrack any already committed)
- Never add entries to `.git/info/exclude`
- Fix a committed mistake with a new commit; never amend, and never `git stash`
- A mechanical change (a move, a mass deletion, an import of files from elsewhere, regenerated output) is a
  separate commit, first on the branch where possible, with "(mechanical)" ending its subject; the reviewer
  then reads the other commits as a range in the web interface
- Commits by Claude are authored by the bot account named in the user's configuration, with no attribution trailer (`Co-Authored-By`) or session link, whatever the harness suggests
- After committing, do not report the commit message back or summarise the commit
- After pushing, check the CI run for the branch and diagnose any failure; the coding-conventions skill says when to report the run

## Permissions

- When an action is refused for lack of permission, stop and report it; never work around the refusal
  with another account, token or bypass flag
- Destructive or organisation-wide changes need explicit approval: project board fields, branch
  protection, organisation settings, and any mutation that replaces rather than appends data
- A bulk operation of more than a few hundred API requests, such as deleting workflow runs one by one,
  needs explicit confirmation, with the request count stated against the hourly rate limit shared by every
  session using the token; once confirmed, throttle it and run a single instance

## Referring to an issue, pull request or branch

- Give its number, title and URL: #181, Classes for built-in types,
  https://github.com/OWNER/REPO/issues/181; likewise for a pull request, with its `pull` URL
- A branch by name and URL: `247-syntax`, https://github.com/OWNER/REPO/tree/247-syntax

## Issues

- Prose in bodies and comments follows the technical-authoring skill
- Before starting work on an issue, assign it to the user and to the account you run as (`gh api user --jq .login`)
- Check with the user before creating an issue, unless explicitly instructed to create one
- A new issue goes on the project board with a Status (`Proposed` for new work) and, in fluid, an Aspect; set Type, labels and milestone when appropriate
- Add content to an issue (body, comment, closing comment) only when asked; otherwise create, edit or close it and nothing more
- Delete a duplicate issue rather than close it, unless a third party created it
- A subtask of an issue is a line in the task list of its body, not a GitHub sub-issue, unless a sub-issue or new issue is asked for
- A sub-issue appears in neither the task list nor the **See also** paragraph of its parent, and the parent in neither of the sub-issue's; the sub-issue relation records the link
- Re-read a body from GitHub before editing it; never edit from a copy
- Keep checklist items in the body updated as the work completes: open items stay in the task list; a
  checked item moves to a `## Done/dropped` section before **See also**, by default nested under plain bullets that
  repeat its ancestors in the task list, with a dropped item struck through (`- [x] ~~item~~`); once no open
  item remains, the heading goes and the checked items stand as the task list
- Do not hard-wrap paragraphs in a body; omit the language tag on a code fence rather than guess it
- Keep a body as simple as possible: paragraphs, the task list, tables where they serve and **See also**, with no other headings or structure, except `###` subheadings dividing a task list that covers several kinds of work, and `####` subheadings dividing a `###` section in the same way; meeting issues excepted
- Keep a body minimal: a line or two of context and the task items, each naming the code or text it concerns; no account of how the problem was found or of the course of the discussion behind it
- Use existing labels; give a new label no description
- An issue body describes the repository as it stands or will stand: no branch names, pull request numbers or interim states of the code; refer to pending work by its issue
- Link an external resource inline where the body mentions it, rather than in a **See also** paragraph
- When an issue references other issues, end with a **See also** paragraph:

  ```
  ## See also

  - #36
  - #50
  ```

- In a bullet list, link another issue as bare `#N`, which GitHub renders with its title; within the text of a task item, link it with descriptive text (`[first three models](URL)`) instead, since the rendered title would interrupt the item

## Escalation

- When the best approach isn't obvious, comment on the issue with the options and a recommendation,
  set its Status to `Awaiting Decision`, and move to other work

## Project board

- To read or set an issue's board Status, query the `projectItems` of the issue (in fluid,
  `script/issue-status.sh <issue> [Status]`, which also adds an absent issue to the board); never
  `gh project item-list`, which fetches the whole board and trips the GraphQL rate limit
- Closing an issue does not change its Status; set `Done` or `Rejected` explicitly
- After changing board state, verify the project view

## Pull requests

- Open a pull request only when asked to submit the branch for review; otherwise report the branch
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
  `{"env": {"GH_TOKEN": "<fine-grained-pat>"}}`; the token needs read and write on pull requests and
  issues, and read, write and admin on organisation projects
- Never run `gh auth refresh` or `gh auth login` without `--with-token`, which replaces the
  fine-grained PAT with an OAuth token that lacks private repository access
