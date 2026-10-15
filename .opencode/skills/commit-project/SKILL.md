---
name: commit-project
description: Use when the user asks to 提交项目, 提交代码, commit and push, 推送项目, 上传到 gitee, or sync the current project to the Gitee remote. Commits all changes and pushes the current project to https://gitee.com/xuzixuan0814/advanced-web-pages.
---

# 提交项目 (Commit & Push to Gitee)

Commit all current changes and push the project to the Gitee remote:
`https://gitee.com/xuzixuan0814/advanced-web-pages`

## Steps

1. Confirm `git` is available and the working directory is a repo:

   ```powershell
   git rev-parse --is-inside-work-tree
   ```

2. If it is not a repo, initialize it and set the remote:

   ```powershell
   git init
   git remote add origin https://gitee.com/xuzixuan0814/advanced-web-pages.git
   ```

3. Ensure the remote points at the Gitee URL (add if missing, fix if wrong):

   ```powershell
   git remote get-url origin
   git remote set-url origin https://gitee.com/xuzixuan0814/advanced-web-pages.git
   ```

4. Stage everything and review what will be committed:

   ```powershell
   git add -A
   git status
   ```

5. Commit with a concise message describing the changes. If the user supplied
   a message, use it verbatim; otherwise write one that matches the changes:

   ```powershell
   git commit -m "<message>"
   ```

6. Push to the Gitee remote (set upstream on first push):

   ```powershell
   git push -u origin master
   ```

   If the branch is `main` instead of `master`, push that branch instead.

## Notes

- Never force-push unless the user explicitly asks.
- If `git` is not recognized, tell the user to install Git or add it to `PATH`
  before retrying.
- If the push is rejected (non-fast-forward), fetch and reconcile first:
  `git pull --rebase origin <branch>` then push again.
