---
name: github-push
description: Commit and push this project to the configured GitHub repository. Use when the user says commit, push, 提交, 推送, or 发布到GitHub for this workspace.
---

# GitHub Push

Commit all changes in `d:\VSCode` and push to the configured GitHub remote.

## When to trigger

User asks to commit / push / 提交 / 推送 / 发布 to GitHub (or the configured Gitee remote) for this project.

## Repository

| Item | Value |
|------|-------|
| Project root | `d:\VSCode` |
| GitHub SSH | `git@github.com:xxx12-66/xuzixuan.git` |
| GitHub HTTPS | `https://github.com/xxx12-66/xuzixuan.git` |
| Gitee HTTPS (origin) | `https://gitee.com/xuzixuan0814/advanced-web-pages.git` |
| Default branch | `master` |
| Git user | `xuzixuan0814 <2062354997@qq.com>` |

## Procedure

Execute these steps in order inside `d:\VSCode`. Use PowerShell-compatible syntax (no bash heredocs).

### 1. Ensure remotes exist

```powershell
git remote -v
# If no github remote, add it:
git remote add github git@github.com:xxx12-66/xuzixuan.git
```

If `github` already exists but points elsewhere, update it:
```powershell
git remote set-url github git@github.com:xxx12-66/xuzixuan.git
```

### 2. Stage everything

```powershell
git add -A
```

### 3. Commit — one-line message via `-m` only (PowerShell-safe)

```powershell
git commit -m "feat: <describe what changed>"
```

Rules for the message:
- If the user gives a specific message, use it verbatim.
- Otherwise generate a concise conventional-commit style message summarising the change.
- Never use bash heredocs (`<<'EOF'`) in PowerShell.
- If there are no staged changes, skip commit and go straight to push.

### 4. Push

Push to **both** remotes so Gitee stays in sync and GitHub mirrors:

```powershell
git push origin master
git push github master
```

If pushing a fresh empty GitHub repo for the first time and SSH auth succeeds but branch is missing on remote, `git push -u github master` may be needed.

### 5. Report back

Print:
- `commit hash` and message
- Which remotes were pushed to
- Any warning (e.g. untracked files skipped, failed remote)

## Troubleshooting

| Symptom | Fix |
|---------|-----|
| `Author identity unknown` | Run `git config user.name "xuzixuan0814"` and `git config user.email "2062354997@qq.com"` inside the repo (local scope only, no `--global`). |
| `Permission denied (publickey)` on GitHub | Remind user that SSH key needs to be added to https://github.com/settings/keys or ask them to run `ssh -T git@github.com` once in a terminal. |
| `failed to push some refs` (non-fast-forward) | **Stop and ask the user.** Do not force push. Explain that the remote has commits we don't have locally and suggest `git pull --rebase github master` followed by push, or let the user choose. |
| `git` not found | Environment issue — tell user to install Git for Windows and ensure it's on PATH. |
| `nothing to commit, working tree clean` | Skip commit, just push. |

## Security notes

- Never commit API keys, `.env`, or `node_modules`. Ensure `.gitignore` covers them.
- Never run `git push --force` unless the user explicitly asks and understands the risk.
- Use repo-local git config (`git config` without `--global`) so the identity stays scoped to this project.
