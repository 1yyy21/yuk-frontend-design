# yukiskill

**自动寻找合适的 UI，接入项目，验证效果。**

[English](README.md) · [技能正文](skills/yukiskill/SKILL.md) · [24 个资源网站](skills/yukiskill/references/sources.md) · [MIT 许可证](LICENSE)

yukiskill 是一个用于前端设计开发的 Agent Skill。它将 24 个设计资源网站整合成可执行的工作流：识别项目技术栈，搜索适用的控件、动画、UI、图标和字体，筛选兼容的实现，安装接入，并检查实际页面效果。

## 安装

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

## 使用条件

- 运行环境需要支持 `SKILL.md`，并具备联网搜索和项目文件编辑能力。安装依赖还需要命令执行和项目包管理器。
- 这是指导 Agent 工作的技能，不是独立爬虫、后台服务或组件素材包。只安装本次实际选中的依赖。
- 优先复用已有组件，尊重用户对预览、安装和修改范围的要求。
- 保留键盘、焦点、移动端、安全区域及减少动态效果设置。
- 付费资源、上线部署、外部发布分别遵循用户授权。
- 第三方素材和代码使用各自许可证；本仓库 MIT 不覆盖链接网站的素材。
- 浏览器工具不可用时，明确报告视觉验证尚未完成。

## 参与维护

欢迎提交资源链接修正、框架适配经验与真实使用案例。参见 [CONTRIBUTING.md](CONTRIBUTING.md)。

```bash
python -m pip install -r requirements-dev.txt
python scripts/validate.py
```

## 致谢与许可证

仓库结构参考 [anthropics/skills](https://github.com/anthropics/skills)、[vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) 和 [Agent Skills 格式](https://agentskills.io/)。本项目独立维护。

本仓库采用 [MIT](LICENSE) 许可证；外部资源说明见 [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md)。
