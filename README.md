# superagent-lab

给 dsh-superagent 用的**靶场仓库**：故意留了两个 bug、默认分支 CI 必红、带一个 bot 自动 PR，用来验证它到底"是什么"，而不是"能不能写代码"。

## 为什么需要靶场

superagent 的卖点不是更强的 coding agent，而是三件事：

1. **准入**——只有策略允许的人/机器人能让它干活；
2. **工单化**——每条请求变成有授权、有范围、有状态机的 Ticket；
3. **克制发言**——只在确认、出结果、需要人决策时说话。

所以验证必须打在这三点上。"它能不能改代码"是普通 agent 的考题，不是它的。

## 用法

```sh
# 1. 建一个仓库（private 也行），把本目录推上去
git init && git add . && git commit -m "lab: seed two bugs"
gh repo create superagent-lab --private --source . --push

# 2. 给 agent 账号写权限（面板上填的 owner/name 就是它）
gh api -X PUT repos/<you>/superagent-lab/collaborators/<agent-login> -f permission=push
```

然后按 [VERIFY.md](VERIFY.md) 逐关跑。**先不要修 `median()`**——那个 bug 是第 A 关的考题。

## 目录

```
src/calc.py                   两个 bug：偶长度取整错误、原地排序污染入参
tests/test_calc.py            4 个测试，当前 2 红 2 绿
.github/workflows/ci.yml      默认分支必红，用于测 observeCi
.github/dependabot.yml        制造 bot 候选，用于测"机器人能不能提需求"
VERIFY.md                     五关验收清单
```
