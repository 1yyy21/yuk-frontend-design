# 用户指定的 24 个设计资源

用途和接入难度沿用用户清单。地址是检索入口，使用时必须打开具体资源确认当前说明和授权，不能把入口列表视为已安装组件。MotionSites、Norrly、Supahero、Devsnap、FontVS 及六个主要组件站入口在 2026-10-13 已在线定位；其他入口和全部具体资源在实际使用时再核实。

## 可复用控件与动效

| 来源 / 入口 | 适用场景 | 接入方式与难度 |
| --- | --- | --- |
| [UIverse / Uiverse](https://uiverse.io/) | 按钮、开关、输入、卡片、加载状态 | 易：查看具体 HTML/CSS 或组件源码，适配样式和语义 |
| [21st.dev](https://21st.dev/) | React 组件与 AI Prompt | 中：具体组件详情中确认依赖、来源和安装方式 |
| [React Bits](https://reactbits.dev/) | 文字、背景、交互与艺术感 React 动效 | 中：选择适合项目的 JS/TS 与样式变体，按官方说明接入 |
| [Magic UI](https://magicui.design/) | 精致科技感组件与微交互 | 中：检查具体组件的 registry/源码和版本适配 |
| [Animata](https://animata.design/) | 开源动画组件 | 中：查看具体源码、依赖和许可，局部集成 |
| [Aceternity UI](https://ui.aceternity.com/) | 视觉冲击强的动态组件 | 中：区分免费组件与付费内容，按具体官方说明安装 |
| [Devsnap CSS Animations](https://devsnap.me/css-animation-examples) | CSS 动效合集 | 易：追溯具体样例作者与源码，挑选/改造 |
| [CodePen Trending](https://codepen.io/trending) | 可运行前端实验 | 中：追溯原 Pen，核实许可，去除 demo 特有结构与依赖 |
| [Codrops Creative Hub](https://tympanus.net/codrops/) | 前沿动效与实验 | 高：阅读原教程和仓库，提取局部效果并工程化 |
| [OpenProcessing / Particles](https://openprocessing.org/) | 生成艺术和粒子 | 高：Particles 是原清单中的用途关键词，未指定独立站点；按需检索具体实现并核实许可 |
| [three.js](https://threejs.org/) | 网页 3D 和 WebGL | 高：优先现有栈兼容方案；核实官方安装文档及实例生命周期 |

## 整页与视觉参考

| 来源 / 入口 | 适用场景 | 接入方式与难度 |
| --- | --- | --- |
| [MotionSites](https://motionsites.org/) | 整站灵感与 AI Prompt | 易：挑选可访问参考，将视觉语言转成当前项目实现 |
| [Norrly](https://norrly.io/) | 整站灵感与拆解 | 易：查看滚动、配色和排版参考；需要 API 时查官方 [API 文档](https://norrly.io/api-docs) |
| [Dribbble](https://dribbble.com/) | 视觉和版式灵感 | 易：参考层级与布局，不默认复制设计资产 |
| [Supahero](https://supahero.io/) | Hero 首屏灵感 | 易：仅在页面确实需要首屏时参考；入口当前提示已归入 screensdesign |
| [Landingfolio](https://www.landingfolio.com/) | 落地页与商业版式 | 易：参考适合用户产品的局部结构 |

## 图标与动画素材

| 来源 / 入口 | 适用场景 | 接入方式与难度 |
| --- | --- | --- |
| [SVG Repo](https://www.svgrepo.com/) | SVG 图标与矢量素材 | 易：核实具体图标许可，使用现有图标系统或局部 SVG |
| [LottieFiles](https://lottiefiles.com/) | 轻量动画素材 | 易：核实单个素材的使用条件与播放器依赖；适配尺寸和减少动态效果设置 |

## 字体与排版

| 来源 / 入口 | 适用场景 | 接入方式与难度 |
| --- | --- | --- |
| [FontVS：17 款免费打字机字体](https://fontvs.com/zh-Hans/blog/17款免费打字机字体-打造复古与油墨氛围/) | 复古、油墨感专题字体灵感 | 易：追溯每款字体的实际下载源和许可 |
| [Fontshare](https://www.fontshare.com/) | 高质量免费西文字体 | 易：核实字体授权、字重、覆盖字符与网页嵌入方式 |
| [Google Fonts](https://fonts.google.com/) | 开源网页字体 | 易：选择所需字重与子集，按项目方式接入并保留许可 |
| [Fonts In Use](https://fontsinuse.com/) | 真实排版案例档案 | 易：作为排版参考，字体文件需另找合法来源 |
| [Font Squirrel](https://www.fontsquirrel.com/) | 商用免费字体与工具 | 易：查看每款字体许可和 webfont 权限 |
| [Typewolf](https://www.typewolf.com/) | 字体趋势与搭配 | 易：参考搭配，另行核实字体来源与使用条件 |

## 按需求路由

- 表单、按钮、开关、列表和卡片：先现有组件库，再 Uiverse / 21st.dev。
- React 文字、背景和交互动效：React Bits / Magic UI / Animata / Aceternity UI。
- 原生 HTML/CSS 微动效：Uiverse / Devsnap / CodePen；不要为一个按钮引入 React。
- 整页视觉方向：Norrly / MotionSites / Dribbble / Landingfolio；按需补 Supahero。
- 高级视觉实验：Codrops / OpenProcessing / three.js，先评估移动端成本。
- 字体、图标和矢量动画：对应素材分组；需要中文时先确认实际中文字形覆盖。

某站不可访问或候选不适配时，换同用途来源继续任务，不把单站失败等同于整个流程失败。不为了“用了资源”而添加无关视觉效果。
