# Git + Worktree 协作实验

用最小练习项目验证 GitHub 上的任务隔离、PR、CI、人工评审、冲突处理、Squash Merge 和清理流程。

## 当前阶段

已准备通用项目配置。尚未添加 Python 脚手架、业务代码或 GitHub Actions CI。

## 协作分工

Codex 负责开发和展示验证证据；用户负责评审。CI 通过且用户明确授权后，Codex 才执行 Squash Merge。

## 实验顺序

1. 在桌面初始化 main、项目规则和 GitHub 公开仓库。
2. 在独立任务分支和 Worktree 中添加 Python 命令行基础、pytest、Ruff 和 CI，创建基础 PR。
3. 基础 PR 经用户评审授权合并后，从同一 main 开展单词统计和文本转换两个任务。
4. 演示 CI 失败与修复、原 PR 迭代、主线同步及可控冲突。
5. 用户逐个评审授权合并，验证主线结果并清理任务资源。

基础设施 PR 首次引入 CI，必须等该 PR 的 CI 实际通过后才提交合并审批。当前初始化提交不是功能 PR，不声称已通过 CI。

## 验证

初始化：检查 git status、git branch --show-current、git remote -v 和首次推送结果。
后续代码阶段：计划使用 uv run ruff check .、uv run pytest，具体配置随基础 PR 添加。

## 依据

- [个人项目初始化 SOP（Codex）](https://xcndtmrh4n6z.feishu.cn/wiki/RrzKwGfzUiU2hMkhTJzcs2hLngh)
- [Git + Worktree 协作规范 SOP V0.3](https://xcndtmrh4n6z.feishu.cn/wiki/ORfywhGPiixpsMkzfZUc6nYOnwc)
