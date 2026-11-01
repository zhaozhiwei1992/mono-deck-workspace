# 品牌主题 · 华青（从 PPT 模板提取）

`slidev-theme-brand-huaqing` 是**品牌层 addon**：色系 `palette: huaqing` + 6 个 `brand-*` 版式 + 1 个组件 + 7 张从公司模板里提取的位图。

源文件：`~/Documents/03-华青PPT模板-数字科技-2025-v1.0.pptx`（13.333×7.5in，14 页）。
提取脚本：`tools/extract-brand-assets.py`（可重跑，不依赖 `imageN` 文件名）。

**本文件是这个品牌的「实例说明」**（色值、props、素材映射、验收数字）。
接一份新 PPT 的通用流程（原图/CSS 判据、五步、脚本、验收）见
`~/workspace/project-management/开发文档/Slidev多主题工程/02_通用设计/04_品牌层接入流程.org`。

## 用起来

```yaml
---
theme: slidev-theme-base
addons:
  - slidev-theme-brand-huaqing   # 需要技术版式时再加 - slidev-theme-tech
colorSchema: light               # 或 auto / dark
palette: huaqing                 # 不写就还是 base 的 blue
layout: brand-cover
title: 标题
subtitle: 一句话说明
eyebrow: 数字科技 / DIGITAL TECH
author: 解决方案中心
date: 2026-11-01
org: 华青 · HUAQING
orgEn: BEIJING TAIJI HUAQING
company: 北京市太极华青信息系统有限公司
site: 公司官网：www.tjhq.com　云构智慧政府
---
```

deck 的 `package.json`：

```json
{
  "dependencies": {
    "slidev-theme-base": "workspace:*",
    "slidev-theme-brand-huaqing": "workspace:*"
  }
}
```

## 版式

| 版式 | props | 对应 PPT |
| --- | --- | --- |
| `brand-cover` | `title/subtitle/eyebrow/author/date/org/orgEn/company/site/address/year/yearLabel/logo/background` | 位图底 + 右上角白色标识 + 靠左文本块（8%/33% 起）+ 左下官网/地址 |
| `brand-section` | `number/en/title` | 1_正文页-副标题-01（左白→右浅蓝渐变 + 右侧两块斜切浅蓝 + 蓝色彩带） |
| `brand-agenda` | `title/items[{no,title,desc}]/panelTitle/panelEn` | 目录（左侧 35.4% 蓝面板，**标题写在面板里**，右侧 2 列大序号） |
| `brand-end` | `title/titleFallback/subtitle/eyebrow/address/site/orgEn/company/year/yearLabel/logo/background` | 同封面结构，默认口号/地址 |
| `brand-columns` | `title/items[{title,en,desc}]/columns` | 正文页右侧「圆点 + 标题 + 英文 + 正文」多列 |
| `brand-steps` | `title/steps[]` + 默认 slot | 正文页底部三档蓝箭头条 |

组件：

- `BrandChevrons`：箭头条（`items: ['甲','乙','丙']` 或 `[{title,no}]`），任何布局里都能手写
- `BrandYear`：**年份用 SVG 文本**渲染（`year` 不传取当年，`yearLabel` 加副标），替代年度字标位图
- `BrandSimple`：封面/尾页共用的简洁结构，改一处两页同步

封面/尾页默认铺 PPT 原底图 `bg-cover.png`，文本全部**靠左**（与 PPT 第 14 页一致：左边距 8%、标题自 33% 起、左下官网/地址 8.7%）；
不叠任何遮罩阴影。换底图或换纯色就写 `background: <图片路径 | CSS 值>`。年度字标（金色 2025）**不进版式**。

`default` / `two-cols` / `table` / `metrics` 以及 `tech-*` 不重写，直接吃 `palette: huaqing` 的品牌色。

## 自检

```bash
pnpm --filter slidev-theme-brand-huaqing dev     # example.md
pnpm --filter slidev-theme-brand-huaqing build
pnpm --filter deck-demo-brand export             # 需 playwright-chromium
```

## 素材

| 文件 | 来源 | 用途 |
| --- | --- | --- |
| `bg-cover.png` | 「标题幻灯片」整幅底图 1920×1080（画面里带年度字标） | `brand-cover` / `brand-end` 默认底图 |
| `band-blue.png` | 章节页彩带 1822×320 | `brand-section`（页面底是 CSS 渐变 + 2 个 `skewX(-28deg)` 伪元素，不是位图） |
| `logo-huaqing.png` | 华青标识·白色版 1175×482 | 深底（封面/章节/尾页）需要放标时用 |
| `logo-huaqing-color.png` | 华青标识·彩色版 1175×482 | 正文页标题行右上（`default` 页自动带） |
| `deco-ring.png` | 16px 级「官网」小图标 512×512 | 封面/尾页左下 |
| `deco-ornament.png` | 16px 级「地址」小图标 512×476 | 封面/尾页左下 |

### 正文页标题行 logo

PPT 的正文页把彩色标识烤在 4000×2250 底图右上角（实测 left 87.5% / top 7.2% / 宽 7.1%）。
这里不复制底图，改成 `h1::after` 伪元素（`logo-huaqing-color.png`，宽 91px / 高 35px，与标题垂直居中、右边缘落在标题框右边）：

- **任何 `default` 页自动带**，标题再长也不会撞（`h1` 留了 `padding-right: 6.4rem`）
- 单页关掉：frontmatter 写 `class: no-brand-logo`
- 封面/尾页的右上角标识：`logo` prop，默认 `true` 用 `logo-huaqing.png`（白色版），写 `false` 关掉，写路径可换图
- `two-cols` 也带：logo 挂在**右栏标题**（`.col-right h1`）上，落在右栏右边，正好是页面右上角，不会一栏一个
- 右栏没标题的页面就不显示；其他分栏版式（`two-cols-header` 等）暂不带

底图 `bg-cover.png` 是封面专用；正文页不放整页底图。

底图 `bg-cover.png` 是封面专用；正文页不放整页底图。

### 页脚左下角英文名

PPT 正文页左下角还有一行金色 `BEIJING TAIJI HUAQING`（同样烤在底图上）。这里**没有新造元素**，
直接用 base 页脚本来就留着的品牌位 `.deck-footer__brand`，槽位为空时自动补上：

```css
.deck-footer__brand:empty::after {
  content: var(--brand-footer-text, 'BEIJING TAIJI HUAQING');
  font-size: .62rem; letter-spacing: .16em; text-transform: uppercase;
  color: var(--deck-color-muted);    /* 与页码同色，暗色自动跟 */
}
```

- 想换文案：deck 里加 `--brand-footer-text: 'XXX'`（`<style>` 里一行）
- 想关掉整条页脚：该页 frontmatter 写 `footer: false`
- 想换成别的品牌行：该页写 `brand: XXX` 或 `logo: ./x.png`（槽位非空，伪元素自动让位）
- 只影响 `.deck-footer`，不涉及任何版式结构

重新生成：

```bash
python3 -m venv /tmp/pptxvenv && /tmp/pptxvenv/bin/pip install python-pptx pillow
/tmp/pptxvenv/bin/python tools/extract-brand-assets.py \
  --pptx ~/Documents/03-华青PPT模板-数字科技-2025-v1.0.pptx \
  --out assets --report /tmp/huaqing-report.md
```

素材来自公司模板，**仅内部使用**，不要随公开仓库分发。
