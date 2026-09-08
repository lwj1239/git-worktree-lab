# Git + Worktree 协作实验

用最小 Python 命令行文本工具验证 GitHub 上的任务隔离、PR、CI、人工评审、冲突处理、Squash Merge 和清理流程。

## 当前阶段

基础程序提供命令入口、帮助信息、pytest 测试和 GitHub Actions CI 配置。功能开发及后续协作环节尚待执行；配置存在不代表流程已验证。

当前功能：帮助信息、大写转换

## 安装

需要 Git 和 uv。项目使用 Python 3.12，依赖版本记录在 `uv.lock` 中。

```powershell
git clone https://github.com/lwj1239/git-worktree-lab.git
cd git-worktree-lab
uv sync --locked
```

已有仓库直接在对应任务 Worktree 中执行 `uv sync --locked`，无需重新克隆或初始化。uv 会在需要时获取 Python 并创建 `.venv`。

Windows 如继承了 `SSLKEYLOGFILE`，可在运行 uv 前仅清除当前终端进程的变量：

```powershell
Remove-Item Env:SSLKEYLOGFILE -ErrorAction SilentlyContinue
```

这不会修改 User/Machine 级变量，TLS 验证仍然开启。

## 运行

```powershell
uv run git-worktree-lab
uv run git-worktree-lab --help
```

两种方式均显示帮助并成功退出，也支持 `-h`。未知参数会报错并以状态码 2 退出。不需要数据库、Web 服务或部署。

使用 `upper` 子命令按 Python `str.upper()` 语义转换文本，空字符串输出空行：

```powershell
uv run git-worktree-lab upper "Hello"
# 输出：HELLO
```

## 检查与测试

```powershell
uv sync --locked
uv run ruff check .
uv run pytest
```

测试实际调用安装后的命令入口，覆盖无参数、`--help`、`-h`、未知参数，以及大写转换的空字符串、混合大小写、Unicode 转换和缺失文本参数。

GitHub Actions 在指向 `main` 的 PR 和 `main` 的 push 时执行上述三个命令，使用 Python 3.12、uv 0.9.25，仅授予 `contents: read` 权限。本地检查通过后仍需查看对应最新提交的远程 CI 结果。

## 协作分工

Codex 负责开发和展示验证证据；用户负责评审。主 Worktree 固定保持 `main`，只用于同步、查看和管理。每个任务使用独立分支、Worktree 和 PR；评审修改继续更新原分支和原 PR。

## 实验步骤

1. 基础任务：在 `chore/project-foundation` 和独立 Worktree 中添加命令入口、测试及 CI；提交、推送并创建 PR，确认最新提交的 CI 结果后交给用户评审。
2. 用户明确评审通过并授权后，Squash Merge 基础 PR，再同步主线和清理该任务。
3. 从同一个最新 `main` 提交创建 `feat/word-count` 和 `feat/text-case` 两个独立 Worktree，记录共同起点，分别创建 PR，保持两个任务同时进行。
4. 单词统计任务先用 `text.split(" ")` 演示连续空白测试失败，记录本地及远程 CI 的实际失败；在同一个 PR 改为 `text.split()`，保留测试要求，再确认最新 CI 通过。
5. 两个功能任务分别修改上面的“当前功能”一行，以便观察后续合并冲突。用户评审授权且最新 CI 通过后，Squash Merge 单词统计任务。
6. 在文本转换任务 Worktree 执行 `git fetch origin`、`git merge origin/main`，记录实际冲突并解决，保留两个功能及文档；重新检查、测试、推送并确认 CI。若没有出现冲突，如实调查和记录。
7. 用户再次评审并明确授权后，Squash Merge 文本转换 PR。不得自动合并或绕过失败 CI。
8. 每次合并后确认 PR 已合并、工作区干净且没有未推送或需保留的工作，再删除对应远程分支、同步主 Worktree 的 `main`、用 `git worktree remove` 删除任务 Worktree，最后删除对应本地分支。Squash 导致 `git branch -d` 拒绝时，先核实工作已保存及 PR 合并状态，才对该确切分支使用 `-D`。
9. 最终检查两个功能、主线本地测试与远程 CI、三个 PR 的授权合并记录及逻辑提交、任务资源清理和干净工作区。总结引用实际 PR、提交及 CI 记录，不声称验证了多真人或多 Agent 同时运行。

## 依据

- [个人项目初始化 SOP（Codex）](https://xcndtmrh4n6z.feishu.cn/wiki/RrzKwGfzUiU2hMkhTJzcs2hLngh)
- [Git + Worktree 协作规范 SOP V0.3](https://xcndtmrh4n6z.feishu.cn/wiki/ORfywhGPiixpsMkzfZUc6nYOnwc)
