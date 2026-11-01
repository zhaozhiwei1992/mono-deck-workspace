# 品牌主题 · 华青

`slidev-theme-brand-huaqing` 是挂在 `slidev-theme-base` 上的**品牌层 addon**：提供 `palette: huaqing` 色系、6 个 `brand-*` 版式、3 个组件和 6 张从公司模板提取的素材。

- 源模板：`~/Documents/03-华青PPT模板-数字科技-2025-v1.0.pptx`
- 设计取舍（为什么用位图、为什么用 CSS、怎么从 PPT 量出来、验收数字）：见项目笔记
  `~/workspace/project-management/开发文档/Slidev多主题工程/02_通用设计/04_品牌层接入流程.org`

## 安装

```json
// deck/package.json
{
  "dependencies": {
    "slidev-theme-base": "workspace:*",
    "slidev-theme-brand-huaqing": "workspace:*"
  }
}
```

## 用法

```yaml
---
theme: slidev-theme-base
addons:
  - slidev-theme-brand-huaqing    # 需要 tech 版式再加 - slidev-theme-tech
palette: huaqing                  # 不写还是 base 的 blue
colorSchema: light                # 或 auto / dark
layout: brand-cover
title: 一体化 AI 中台 harness 工程设计
subtitle: 一句话说明
eyebrow: 数字科技 / DIGITAL TECH
author: 赵志伟
date: 2026-11-12
org: 财政研发中心
orgEn: BEIJING TAIJI HUAQING
company: 北京市太极华青信息系统有限公司
site: 公司官网：www.tjhq.com
address: 北京市朝阳区来广营西路 5 号诚盈中心 7 号楼
year: true                        # 可选：右上角年份（SVG 文本，自动取当年）
yearLabel: DIGITAL TECH
logo: true                        # 可选：右上角白色标识，默认就带；false 关闭
---
```

## 版式

| 版式 | 主要 props | 样子 |
| --- | --- | --- |
| `brand-cover` | `title/subtitle/eyebrow/author/date/org/orgEn/company/site/address/year/yearLabel/logo/background` | 深蓝底图 + 右上白色标识 + 靠左文本块 + 左下官网/地址 |
| `brand-end` | 同上，另有 `titleFallback` | 与封面同结构，默认口号/地址 |
| `brand-section` | `number/en/title` | 左白→右浅蓝渐变 + 右侧斜切块 + 蓝色彩带（标题落在彩带内） |
| `brand-agenda` | `title/items[{no,title,desc}]/panelTitle/panelEn` | 左侧蓝面板（**标题写在面板里**）+ 右侧 2 列大序号 |
| `brand-columns` | `title/items[{title,en,desc}]/columns` | 多列：圆点引导线 + 标题 + 英文 + 正文 |
| `brand-steps` | `title/steps[]` + 默认 slot | 标题 + 正文 + 底部箭头条 |

`default` / `two-cols` / `table` / `metrics` / `tech-*` 不重写，直接吃 `palette: huaqing` 的颜色。

## 内容页自动行为

用 `palette: huaqing` 后，普通内容页自动带两个品牌元素，不需要每页写：

| 行为 | 落在哪 | 关掉 |
| --- | --- | --- |
| 标题行右上角彩色标识（91×35） | `.slidev-layout.default h1`、`two-cols` 的右栏标题 | 该页 frontmatter 写 `class: no-brand-logo` |
| 页脚左下角 `BEIJING TAIJI HUAQING` | base 页脚品牌位 `.deck-footer__brand` | 该页 `footer: false`；或写 `brand:` / `logo:` 换成自己的 |

- 换页脚文案：deck 里加 `--brand-footer-text: 'XXX'`
- `two-cols` 的标识挂在右栏标题上；右栏没标题就不显示；`two-cols-header` 等其他分栏版式暂不带
- 页脚那行颜色跟页码一致（`--deck-color-muted`）

## 组件

| 组件 | 用法 |
| --- | --- |
| `BrandChevrons` | `<BrandChevrons :items="['需求','设计','开发']" />`，也接受 `[{title,no}]` |
| `BrandYear` | `<BrandYear year-label="DIGITAL TECH" />`，不传 `year` 取当年 |
| `BrandSimple` | 封面/尾页共用的结构，一般不用直接写 |

## 素材

| 文件 | 内容 | 用在哪 |
| --- | --- | --- |
| `bg-cover.png` | 深蓝整幅底图 1920×1080 | `brand-cover` / `brand-end` 默认底图 |
| `band-blue.png` | 蓝色彩带 1822×320 | `brand-section` |
| `logo-huaqing.png` | 标识·白色版 1175×482 | 封面/尾页右上角 |
| `logo-huaqing-color.png` | 标识·彩色版 1175×482 | 内容页标题行右上角 |
| `deco-ring.png` | 官网小图标 | 封面/尾页左下 |
| `deco-ornament.png` | 地址小图标 | 封面/尾页左下 |

素材来自公司模板，**仅内部使用**，不要随公开仓库分发。

## 命令

```bash
pnpm --filter slidev-theme-brand-huaqing dev      # 看 example.md
pnpm --filter slidev-theme-brand-huaqing build
pnpm --filter deck-demo-brand export              # 需 playwright-chromium
```

重新从 PPT 提取素材（会覆盖 `assets/`，产出与本次一致）：

```bash
python3 -m venv /tmp/pptxvenv && /tmp/pptxvenv/bin/pip install python-pptx pillow
/tmp/pptxvenv/bin/python tools/extract-brand-assets.py \
  --pptx ~/Documents/03-华青PPT模板-数字科技-2025-v1.0.pptx \
  --out assets --report /tmp/huaqing-report.md
```
