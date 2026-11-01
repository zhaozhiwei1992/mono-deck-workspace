---
theme: slidev-theme-base
addons:
  - slidev-theme-brand-huaqing
colorSchema: light
palette: huaqing
layout: brand-cover
title: 数字科技 / 类PPT模版
subtitle: 品牌层自检：封面、章节、目录、多列、步骤、结束
eyebrow: HUAQING BRAND
author: mono-deck-workspace
date: 2026-11-01
org: 华青 · HUAQING
orgEn: BEIJING TAIJI HUAQING
company: 北京市太极华青信息系统有限公司
site: 公司官网：www.tjhq.com　云构智慧政府
---

---
layout: brand-agenda
title: 目录
panelTitle: 数字科技 / 模板说明
items:
  - title: 品牌色与材质
    desc: 蓝 / 金 / 浅蓝面板
  - title: 封面与结束
    desc: 位图底 + 金色徽标
  - title: 章节与目录
    desc: 彩带与大序号
  - title: 多列与步骤
    desc: 圆点引导线 + 箭头条
---

---
layout: brand-section
number: 1
en: Brand Tokens
title: 品牌色与材质
---

---
layout: default
---

# 正文页（base 版式 + huaqing 色系）

品牌层不重写 base 的 `default` / `two-cols` / `table` / `metrics`，只换色系与字体：

- 主色 `#025bd9`（对白底 6.00），点缀金 `#c68a2e`（深色前景 6.24）
- 中文 `微软雅黑`，正文 12pt 对应 `--deck-color-fg`
- 面板底 `#e5ecf8` + `1px #025bd9` 描边（见下方 `brand-columns`）

---
layout: brand-columns
title: 三列能力（PPT 正文页右侧那组）
items:
  - title: 私有化部署
    en: PRIVATE DEPLOYMENT
    desc: 十亿～百亿级参数量的行业大模型是目前主流选择，相比千亿级通用模型可明显节省成本。
  - title: 专业定制
    en: DOMAIN TUNING
    desc: 基于开源模型再训练或精调，对模型结构、参数按需调整，适配个性化业务。
  - title: 模型即服务
    en: MAAS
    desc: 以 MaaS 方式交付，屏蔽算力与工程细节，业务只面对接口与效果。
---

---
layout: brand-steps
title: 三步落地（PPT 正文页底部箭头条）
steps:
  - title: 现状盘点
  - title: 试点验证
  - title: 规模推广
---

### 正文区

箭头条是 `BrandChevrons` 组件（纯 CSS `clip-path`），列数任意，4 列以后统一用最深的蓝。
也可以在任何布局里手写 `<BrandChevrons :items="['甲','乙','丙']" />`。

---
layout: two-cols-header
---

# 与 tech 场景层叠加

::left::

```yaml
addons:
  - slidev-theme-tech
  - slidev-theme-brand-huaqing
```

::right::

顺序无所谓（两者互不覆盖），但都必须写在 `addons` 里，`theme` 只能是 base。

---
layout: tech-compare
title: tech 版式也吃品牌色
leftTitle: 只装 base
rightTitle: base + tech + brand
leftTag: default
rightTag: huaqing
---

::right::

`tech-*` 布局只调中性轴，品牌轴仍来自 `palette: huaqing`，所以代码页/对比页自动同色。

---
layout: brand-end
title: 聚力发展　向新出发
address: 北京市朝阳区来广营西路5号诚盈中心7号楼
---
