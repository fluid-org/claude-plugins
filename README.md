# claude-plugins

Claude Code plugins for fluid-org and pure-py repositories.

## conventions

Skills for code (`coding-conventions`, `agda-implementor`, `spec-implementor`), prose
(`technical-authoring`) and Git and GitHub (`github`), invoked as `conventions:<skill>`.

A project enables the plugin in its checked-in `.claude/settings.json`; Claude Code then offers to install
it when the project is opened. To use it in every project:

```
claude plugin marketplace add fluid-org/claude-plugins
claude plugin install conventions@fluid-org
```

## Editing the skills

Register a local checkout as the marketplace, so that sessions read the skills from the checkout and an
edit takes effect at the next session or after `/reload-plugins`:

```
claude plugin marketplace add ~/Repo/fluid-org/claude-plugins
```

Commit and push to `main` to publish an edit. Run `claude plugin validate .` after changing a manifest.
