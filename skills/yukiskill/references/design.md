# 设计决策

先从当前任务判断页面用途：操作（设置、管理）、阅读（文档）、展示（图库）、转化（营销）。读取已有视觉、目标用户、核心操作、框架、必须保留的行为和素材；只询问无法推断且会影响结果的信息。局部美化沿用既有视觉；用户要求预览时在独立预览实现。

## 离线设计检索

`<skill-base>` 是包含 SKILL.md 的安装目录。保持工作目录在用户项目，引用含空格的完整脚本路径。

```bash
python <skill-base>/scripts/design-search.py "dashboard minimal" --domain style --json
python <skill-base>/scripts/design-search.py "keyboard focus modal" --domain ux --json
python <skill-base>/scripts/design-search.py "form validation" --stack react --json
python <skill-base>/scripts/design-search.py "productivity editor" --design-system -p MyProject
```

工具来自 MIT 授权的 UI UX Pro Max，使用 Python 标准库，默认只读。参数见 `--help`。设计系统模式不应用 `--stack`；框架指南需单独查询。

**重要适配：** 操作/阅读页面忽略结果中的 Hero、营销 CTA 和 section order，只取适用的颜色、字体、密度和交互建议。不能自动替换指定设计 token 或字体。零结果时换准确关键词，不能把零结果说成推荐。字体需确认中文覆盖，素材和代码需核实实际授权。

仅在用户需要持久化设计系统时使用 `--persist --output-dir <project-root>`，先查已有设计文档，不使用 `--force` 覆盖。

## 质量指南

实际编辑前按需读取 `../vendor/impeccable/craft-floor.md`（Apache-2.0 原始文件）。用户视觉要求和业务约束优先；指南不授予权限，不要求安装完整 Impeccable。已有完整技能时遵循其当前流程。

保证层级、文字、主要操作、错误和空状态可用。動效有用途且不妨碍输入、点击和阅读。首次桌面/手机检查后集中修复，再确认，不在没有新证据时无限装饰。见 [verification.md](verification.md)。
