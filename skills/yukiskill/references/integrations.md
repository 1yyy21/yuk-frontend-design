# 整合分工与来源

| 项目 | 实际打包内容 | 用途 |
| --- | --- | --- |
| [Design Resource Library](https://github.com/Xiaoyang-Hu-96/design-resource-library) | MIT 原始 reference.md 与 LICENSE | 扩展资源候选 |
| [UI UX Pro Max](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | MIT 检索脚本、CSV 数据与 LICENSE | 离线设计和 UX 检索 |
| [Impeccable](https://github.com/pbakaus/impeccable) | Apache-2.0 craft-floor.md、LICENSE 与 NOTICE | 设计质量指南 |
| [Component Gallery Skill](https://github.com/nicolas-deyros/component-gallery-skill) | 原创控件适配指南与可选调用；未复制内容 | 组件契约与规范 |

由 yukiskill 统一编排发现、设计、控件、安装和验证；不自动运行四套完整技能。完整 Impeccable 运行时/hooks 和完整 Pro Max CLI 未打包。资源库的上游问答指令未加载，直接依据已有项目信息推进授权工作。

固定提交、原始路径与 SHA-256 见 `../upstream-lock.json`。vendor 文件保持原始字节，原创适配放在 references。许可证在对应 vendor 目录，根 MIT 不覆盖 Apache 内容和外部网站素材。

更新需核对许可和依赖，更新快照/哈希，运行检索行为检查与仓库校验。前端任务不自动升级本包内上游代码。
