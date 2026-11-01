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
| `brand-cover` | `title/subtitle/eyebrow/author/date/org/orgEn/company/site/background` | 标题幻灯片（深蓝底 + 金色徽标 + 左品牌块/右标题） |
| `brand-section` | `number/en/title` | 1_正文页-副标题-01（浅底 + 蓝色彩带） |
| `brand-agenda` | `title/items[{no,title,desc}]/panelTitle/panelEn` | 目录（左侧 35.4% 蓝面板 + 右侧 2×2 大序号） |
| `brand-end` | `title/subtitle/address/site/orgEn/background` | 2_标题幻灯片（同封面底 + 口号 + 地址） |
| `brand-columns` | `title/items[{title,en,desc}]/columns` | 正文页右侧「圆点 + 标题 + 英文 + 正文」多列 |
| `brand-steps` | `title/steps[]` + 默认 slot | 正文页底部三档蓝箭头条 |

组件：`BrandChevrons`（`items: ['甲','乙','丙']` 或 `[{title,no}]`），任何布局里都能手写。

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
| `bg-cover.png` | layout「标题幻灯片」整幅底图 1920×1080 | 封面 / 尾页 |
| `band-blue.png` | 章节页 12.145×2.133in 彩带 1822×320 | `brand-section` |
| `logo-mark.png` | 左上角白色书法标识 533×258 | 封面左上 |
| `logo-full.png` | 右上角白色完整 logo 1175×482 | 封面右上 |
| `logo-mark-gold.png` | 封面中部金色徽标 533×258 | 封面 / 尾页 |
| `deco-ring.png` `deco-ornament.png` | 尾页左下装饰 512×512 / 512×476 | 尾页 |

重新生成：

```bash
python3 -m venv /tmp/pptxvenv && /tmp/pptxvenv/bin/pip install python-pptx pillow
/tmp/pptxvenv/bin/python tools/extract-brand-assets.py \
  --pptx ~/Documents/03-华青PPT模板-数字科技-2025-v1.0.pptx \
  --out assets --report /tmp/huaqing-report.md
```

素材来自公司模板，**仅内部使用**，不要随公开仓库分发。
