# mono-deck-workspace

用来做演示文档工作，技术人员可用来替代ppt。基于Slidev 进行多主题 / 多 deck 工作区设计。

注: 纯小白不要入坑，等以后优化再考虑。

## 结构

```
packages/
  theme-base/           slidev-theme-base          结构层：版式 + 排版 + token（唯一 theme）
  theme-tech/           slidev-theme-tech          场景层：tech-* 版式与组件（以 addons 叠加）
  theme-brand-huaqing/  slidev-theme-brand-huaqing 品牌层：华青色系 huaqing + brand-* 版式 + 提取素材
decks/
  _template/    新 deck 复制起点
  demo-base/    只用 theme-base 的验证 deck
  demo-tech/    base + tech 的验证 deck（含 deck 级变量覆盖）
  demo-brand/   base + tech + brand 的验证 deck（公司模板风格）
  _private/     私有 deck 容器（独立 git 仓库，主仓忽略，见下文）
```

包名即引用名，不走 scope、不发布 npm，一律 `workspace:*` 软链。

## 核心规则（顺序决定一切）

加载顺序（Slidev 53）：

```
Slidev 内置  →  theme  →  addons[0]  →  addons[1]  →  deck 本地
```

**后者覆盖前者**（布局按文件名、样式按 import 顺序）。所以：

- 结构层必须是 `theme`
- 场景层 / 品牌层必须是 `addons`（按数组顺序叠加；tech 与 brand 互不覆盖，先后随意）
- 单个 deck 的临时覆盖放 `decks/<name>/`

反例：`theme: slidev-theme-tech` + `addons: [slidev-theme-base]` 会让 base 反过来压掉 tech，不要这么写。

## 如何创建一份演示文档

```bash
cp -r decks/_template decks/my-deck
# 修改 package.json 的 name（deck-my-deck）与 dependencies
```

`slides.md`

```yaml
---
theme: slidev-theme-base
addons: []                       # 技术类：['slidev-theme-tech']
layout: cover
title: 标题
subtitle: 副标
author: 演讲人
date: 2026-11-01
org: 组织
---
```

```bash
pnpm install
pnpm --filter deck-my-deck dev       # http://localhost:3030
pnpm --filter deck-my-deck build
pnpm --filter deck-my-deck export
```

`decks/<name>/` 内可选目录（仅本 deck 生效）：`components/ layouts/ setup/ styles/ public/`。

## 私有 deck（不进公开仓库）

私有 / 客户 / 内部内容放 `decks/_private/`，它本身是一个**独立的 git 仓库**，已被根 `.gitignore` 忽略：

```
decks/
  _template/           公开
  demo-base/           公开
  demo-tech/           公开
  _private/            ← 独立 git 仓库（.git 在这一层），主仓忽略整个目录
    client-a/          deck-client-a
    internal-2026/     deck-internal-2026
```

新建一份私有 deck（公开仓里**零改动**）：

```bash
cp -r decks/_template decks/_private/client-a
# 改 decks/_private/client-a/package.json 的 name 为 deck-client-a
pnpm install
pnpm --filter deck-client-a dev
```

版本控制走它自己的仓库：

```bash
cd decks/_private
git add . && git commit -m "feat: 初始 client-a"
git remote add origin git@github.com:<you>/deck-private.git   # 私有仓库
git push -u origin main
```

## 工具

| 脚本 | 用途 | 依赖 |
|---|---|---|
| `tools/pptx-inspect.py` | 盘点任意 pptx：版式、形状几何（占版面 %）、填充、图片清单与「原图/CSS」初判 | `python-pptx` + `pillow`（venv） |
| `tools/check-layouts.mjs` | 逐页体检 Slidev deck：溢出、标题行数、页脚、关键元素百分比；有溢出退出码 1 | `playwright-chromium`（临时装，见脚本注释） |

接一份新 PPT 做品牌层的完整流程（判据、五步、验收、坑）见项目文档
`02_通用设计/04_品牌层接入流程.org`。

## 常用脚本

| 命令 | 作用 |
|---|---|
| `pnpm dev:base` / `pnpm dev:tech` / `pnpm dev:brand` | 主题自检（`packages/*/example.md`） |
| `pnpm dev:demo-base` / `pnpm dev:demo-tech` / `pnpm dev:demo-brand` | 验证 deck |
| `pnpm build:base` / `pnpm build:tech` / `pnpm build:brand` | 主题自检构建 |
| `pnpm build:all` | 所有 deck 构建 |
| `pnpm --filter <pkg> export` | 导出（需先装 `playwright-chromium`） |

## 主题能力

### theme-base

| 布局 | 说明 |
|---|---|
| `cover` | `eyebrow/subtitle/author/date/org/logo/background` |
| `agenda` | `title/items`（string 或 `{title,desc}`） |
| `section` | `number/en/title` |
| `table` | `title/caption` + 正文表格 |
| `metrics` | `title/items[{value,label,note}]` |
| `end` | `title/contact[]` |
| `intro/statement/fact/quote` | 复用内置布局 + 主题排版 |
| `default/two-cols/two-cols-header/image*/iframe*/full/none/center` | 不重写，直接用内置 |

组件（全局可用，无需 import）：`DeckLogo` `DeckFooter` `DeckPageNumber` `DeckTag` `DeckCallout`。

页脚：`slide-bottom.vue` 自动挂载，封面/章节/结束等布局自动隐藏；单页关闭用 `footer: false`。

### theme-tech

| 布局 | props |
|---|---|
| `tech-code` | `title/file/tag` + 左代码（默认 slot）+ 右讲解（`::right::`） |
| `tech-arch` | `title/caption` + 图形 slot + `::aside::` |
| `tech-compare` | `title/leftTitle/rightTitle/leftTag/rightTag` + `::right::` |
| `tech-benchmark` | `title/unit/caption` + 表格 |
| `tech-timeline` | `title/items[{time,title,desc,state}]` |

组件：`TechBadge` `TechCodeNote` `TechDiff` `TechKpi`（**带前缀**，避免与 base 同名）。

### theme-brand-huaqing（品牌层）

从公司 PPT 模板（`03-华青PPT模板-数字科技-2025-v1.0.pptx`）提取：品牌色系 `huaqing` + 品牌页版式 + 7 张位图。

| 布局 | props |
|---|---|
| `brand-cover` | `title/subtitle/eyebrow/author/date/org/orgEn/company/site/background` |
| `brand-section` | `number/en/title` |
| `brand-agenda` | `title/items[{no,title,desc}]/panelTitle/panelEn` |
| `brand-end` | `title/subtitle/address/site/orgEn/background` |
| `brand-columns` | `title/items[{title,en,desc}]/columns` |
| `brand-steps` | `title/steps[]` + 正文 |

组件：`BrandChevrons`（底部箭头条）。

用法（`palette: huaqing` 是品牌层的色系名）：

```yaml
---
theme: slidev-theme-base
addons: [slidev-theme-tech, slidev-theme-brand-huaqing]
palette: huaqing
layout: brand-cover
---
```

为什么封面/尾页用位图、正文页用 CSS，以及颜色/字号/坐标的对照表见
`packages/theme-brand-huaqing/README.md`；接新 PPT 的通用流程见项目文档 `02_通用设计/04_品牌层接入流程.org`。

## 改风格（不要新建主题包）

### 换色系：只在 frontmatter 里选值

```yaml
---
theme: slidev-theme-base
addons: [slidev-theme-tech]
colorSchema: auto        # auto（跟随系统/可切换）| light | dark
palette: red             # 不写 = blue（默认）；可选 red / teal / graphite / huaqing（需装品牌层）
---
```

- `colorSchema` 是 Slidev 官方字段，只负责亮/暗；`palette` 是本项目字段，只负责品牌色，两者正交
- `palette` 由 `packages/theme-base/setup/main.ts` 落到 `<html data-palette>`，样式按属性选择
- 等价的纯官方写法（不想依赖主题里的 setup）：在 headmatter 写 `htmlAttrs: { 'data-palette': red }` 代替 `palette: red`

### 单份 / 品牌覆盖（第 4 层）

三处按优先级从低到高：

1. `packages/theme-base/styles/tokens.css` —— 默认值（= blue 色系 + 中性轴）
2. `packages/theme-base/styles/palettes.css` —— 色系
3. `decks/<name>/styles/index.css` —— 单份 / 品牌覆盖

```css
:root {
  --deck-color-primary: #0f766e;
  --deck-color-accent: #f59e0b;
}
```
