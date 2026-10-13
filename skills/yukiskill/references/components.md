# 控件契约与接入

本指南为 yukiskill 原创，与 Component Gallery Skill 的组件参考方向协作，不包含该项目的源码或参考文件。

先定义控件语义、状态、输入/事件、键盘行为和响应式约束，再搜索实现。优先已有组件系统，React/Vue/Svelte/HTML 各用本栈方案；CSS/Tailwind 不因示例而强制切换。间距沿用已有尺度，布局优先 gap，弹层沿用既有层级。

| 控件 | 验收要点 |
| --- | --- |
| 按钮/开关 | 语义、名称、状态、实际事件、键盘 |
| 表单/选择器 | label、值保留、错误、焦点、手机键盘 |
| Tabs/Accordion | 展开/选中语义、键盘导航、内容可见 |
| Modal/Popover | 关闭与 Escape、焦点返回、背景行为、小屏溢出 |
| 表格/列表 | 长文本、空/加载/错误状态、排序反馈 |
| 动画组件 | reduced-motion、卸载清理、点击和阅读不受影响 |

必要时查 [Component Gallery](https://component.gallery/) 的名称及设计系统参考，再核实选定组件的官方文档。目录链接不代表对应源码允许复制。

已安装 `component-gallery-skill` 时可读取相关规范，之后继续 yukiskill 接入与验证。用户要求安装完整项目时：

```bash
npx skills add nicolas-deyros/component-gallery-skill
```

固定核查版本的 README 声明 MIT，但没有 LICENSE 文件，本包未分发其内容；将来复制前重新核对授权证据。
