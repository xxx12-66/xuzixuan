---
name: github-push
description: Commit and push this project to the configured GitHub repository. Use when the user says commit, push, 提交, 推送, or 发布到GitHub for this workspace.
---

# GitHub Push

Commit all changes in `d:\VSCode` and push to the configured GitHub remote.

## When to trigger

User asks to commit / push / 提交 / 推送 / 发布 to GitHub (or the configured Gitee remote) for this project.

## Known environment limitation

**This machine blocks outbound TCP port 22.** SSH to `github.com:22` returns "Connection refused". Therefore **GitHub remote MUST use HTTPS** — SSH will always fail here.

- `ssh -T git@github.com` → always fails (port 22 blocked by network)
- `https://github.com`, `https://api.github.com`, `https://raw.githubusercontent.com` → all OK (port 443)

## Repository

| Item | Value |
|------|-------|
| Project root | `d:\VSCode` |
| GitHub remote (primary, HTTPS) | `https://github.com/xxx12-66/xuzixuan.git` |
| GitHub SSH (**NOT usable on this machine**) | `git@github.com:xxx12-66/xuzixuan.git` |
| Gitee remote (origin, HTTPS) | `https://gitee.com/xuzixuan0814/advanced-web-pages.git` |
| Default branch | `master` |
| Git user | `xuzixuan0814 <2062354997@qq.com>` |

## Authentication — GitHub HTTPS

GitHub HTTPS push requires a **Personal Access Token (PAT)** with `repo` scope, not a password.

- If Windows Git Credential Manager is installed and the user has signed in once via a browser popup, subsequent `git push github master` will use the stored credential transparently.
- If the credential manager is NOT available, the first push will prompt the user interactively — tell them to enter their GitHub username as the username, and a PAT (not password) as the password.
- To pre-configure for non-interactive use, ask the user for their PAT once, then run:

```powershell
git remote set-url github https://<USERNAME>:<PAT>@github.com/xxx12-66/xuzixuan.git
# verify
git remote -v
```

Never hardcode a PAT into this file or into the commit history.

## Procedure

Execute these steps in order inside `d:\VSCode`. Use PowerShell-compatible syntax (no bash heredocs).

### 1. Ensure remotes exist

```powershell
git remote -v
# Ensure github uses HTTPS (SSH will NOT work here):
git remote set-url github https://github.com/xxx12-66/xuzixuan.git
# origin (Gitee) should already exist
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

If pushing a fresh empty GitHub repo for the first time and branch is missing on remote, `git push -u github master` may be needed.

### 5. Report back

Print:
- `commit hash` and message
- Which remotes were pushed to
- Any warning (e.g. untracked files skipped, failed remote)

## Troubleshooting

| Symptom | Fix |
|---------|-----|
| `Author identity unknown` | Run `git config user.name "xuzixuan0814"` and `git config user.email "2062354997@qq.com"` inside the repo (local scope only, no `--global`). |
| `ssh: connect to host github.com port 22: Connection refused` | **Expected on this machine.** Switch GitHub remote to HTTPS: `git remote set-url github https://github.com/xxx12-66/xuzixuan.git`. |
| `fatal: Authentication failed` on HTTPS push | Need GitHub PAT. Tell user to create one at https://github.com/settings/tokens (scope: `repo`), then run the push interactively in a normal terminal or provide the PAT to embed once. |
| `failed to push some refs` (non-fast-forward) | **Stop and ask the user.** Do not force push. Explain that the remote has commits we don't have locally and suggest `git pull --rebase github master` followed by push, or let the user choose. |
| `git` not found | Install Git for Windows and ensure it's on PATH. |
| `nothing to commit, working tree clean` | Skip commit, just push. |

## Security notes

- Never commit API keys, `.env`, or `node_modules`. Ensure `.gitignore` covers them.
- Never run `git push --force` unless the user explicitly asks and understands the risk.
- Use repo-local git config (`git config` without `--global`) so the identity stays scoped to this project.
- PAT embedded in remote URL should be rotated if it ever ends up in a commit. Remove it with `git remote set-url github https://github.com/xxx12-66/xuzixuan.git` and reset the credential manager.
