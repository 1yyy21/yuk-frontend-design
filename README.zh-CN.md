# yukiskill — 前端设计与 UI 组件发现技能

**自动寻找合适的 UI，接入项目，验证效果。**

[English](README.md) · [技能正文](skills/yukiskill/SKILL.md) · [24 个资源网站](skills/yukiskill/references/sources.md) · [MIT 许可证](LICENSE)

yukiskill 是一个用于前端设计开发的 Agent Skill。它将 24 个设计资源网站整合成可执行的工作流：识别项目技术栈，搜索适用的控件、动画、UI、图标和字体，筛选兼容的实现，安装接入，并检查实际页面效果。

适用于**前端设计、UI/UX 美化、UI 组件搜集、控件安装、CSS 动画、React 动效、Tailwind CSS 适配、网页设计灵感、图标与字体选用**。采用 Agent Skills 格式，可通过 Codex、Claude Code、Cursor 等编码 Agent 各自支持的技能安装流程使用。

## 安装

**v0.2.0 整合版**：统一编排资源发现、离线设计检索、控件规范、安装接入与页面验证。内置经过授权的上游材料与原创适配，固定版本与分工见[整合说明](skills/yukiskill/references/integrations.md)。

通过 [Skills CLI](https://github.com/vercel-labs/skills) 安装：

```bash
npx skills add 1yyy21/yukiskill --skill yukiskill
```

全局安装到 Codex：

```bash
npx skills add 1yyy21/yukiskill --skill yukiskill --agent codex --global
```

也可以克隆仓库，将 `skills/yukiskill` 整个目录复制到你的 Agent 技能目录。Codex 使用 `$CODEX_HOME/skills`，未设置时使用 `~/.codex/skills`。其他 Agent 的加载规则以其文档为准。

## 使用示例

在 Codex 中可以输入 `$yukiskill` 显式调用；支持自动选用技能的环境中，也会在相关前端任务里被选择。

```text
用 $yukiskill 美化这个 React 设置页面。
找合适的开关、卡片和轻量动效，沿用当前配色，接入后检查手机布局。
```

```text
用 $yukiskill 给这个原生 HTML 页面增加加载动画。
保留结构，优先用 CSS，不引入新的框架。
```

```text
用 $yukiskill 为这个仪表盘做一个独立预览。
先展示新风格，确认后再改正式源码。
```

## 工作方式

| 步骤 | 实际工作 |
| --- | --- |
| 识别 | 阅读项目约定、技术栈、依赖与已有组件 |
| 搜索 | 按任务选择相关资源，查看官方页面与具体组件 |
| 筛选 | 比较视觉、兼容性、依赖成本和复用许可 |
| 接入 | 在用户授权范围内安装所选依赖或适配源码 |
| 验证 | 检查构建、交互、响应式和实际动效 |
| 记录 | 登记来源、版本、授权证据与验证结果 |

资源覆盖 Uiverse、21st.dev、React Bits、Magic UI、Animata、Aceternity UI、Codrops、CodePen、three.js，以及整页灵感、图标、Lottie 与字体网站。完整清单见[资源目录](skills/yukiskill/references/sources.md)。

## 怎么搜索同类 Skill

在 [Skills 目录](https://skills.sh/) 或 Skills CLI 中，英文任务关键词通常更方便定位对应技能：

| 想找什么 | 建议关键词 |
| --- | --- |
| 前端设计与界面美化 | `frontend-design`、`ui-ux`、`web-design` |
| 搜集资源并接入项目 | `design-resources`、`design-resource-library`、`ui-components`、`component-library` |
| 控件动画与动态组件 | `css-animation`、`react-bits`、`magic-ui`、`aceternity-ui`、`uiverse` |
| 特定 Agent 技能 | `agent-skills`、`codex-skills`、`claude-code-skills` |

```bash
npx skills find frontend-design
npx skills find design-resources
npx skills find ui-components
npx skills find react-bits
```

在 GitHub 搜索仓库时，可用 `topic:agent-skills frontend`、`topic:frontend-design skill` 或 `"design-resource-library"`。中文可搜索“前端设计 skill”“UI 组件 skill”“动效技能”“设计资源 skill”。直接找本项目则搜索 `yukiskill`，或使用上方安装命令。

本项目侧重“资源发现 → 筛选 → 安装接入 → 验证”。视觉设计指导、设计系统规范和 UI 审查也属于邻近品类，但工作内容不完全相同。新仓库进入搜索索引和第三方目录可能需要时间；关键词不保证排名或收录。

## 使用条件

- 运行环境需要支持 `SKILL.md`，并具备联网搜索和项目文件编辑能力。安装依赖还需要命令执行和项目包管理器。
- 这是带离线设计检索工具的 Agent 技能；只安装实际选中的组件依赖。离线工具需要 Python 3.10+，其他流程无需 Python。
- 优先复用已有组件，尊重用户对预览、安装和修改范围的要求。
- 保留键盘、焦点、移动端、安全区域及减少动态效果设置。
- 付费资源、上线部署、外部发布分别遵循用户授权。
- 第三方素材和代码使用各自许可证；本仓库 MIT 不覆盖链接网站的素材。
- 浏览器工具不可用时，明确报告视觉验证尚未完成。

## 参与维护

内置 Design Resource Library 资源目录、UI UX Pro Max 检索引擎与数据、Impeccable 设计质量指南；通过原创控件指南与 Component Gallery Skill 可选协作。未打包完整上游运行时或 hooks。

```bash
python skills/yukiskill/scripts/design-search.py "keyboard focus" --domain ux --json
python skills/yukiskill/scripts/design-search.py "form validation" --stack react --json
```

欢迎提交资源链接修正、框架适配经验与真实使用案例。参见 [CONTRIBUTING.md](CONTRIBUTING.md)。

```bash
python -m pip install -r requirements-dev.txt
python scripts/validate.py
```

## 致谢与许可证

仓库结构参考 [anthropics/skills](https://github.com/anthropics/skills)、[vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) 和 [Agent Skills 格式](https://agentskills.io/)。本项目独立维护。

原创内容采用 [MIT](LICENSE)；内置上游文件保留 MIT / Apache-2.0 原许可。见 [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md)。
