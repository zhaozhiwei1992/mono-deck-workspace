---
theme: slidev-theme-base
title: 结构层主题自检
layout: cover
eyebrow: 基础主题 / BASE THEME
subtitle: 封面 · 目录 · 章节 · 正文 · 表格 · 指标 · 结束
author: mono-deck-workspace
date: 2026-11-01
org: 内部模板
---

---
layout: agenda
title: 目录
items:
  - 版式清单
  - 排版与组件
  - 表格与指标
  - 结束页
---

---
layout: section
number: 1
en: Layouts
title: 版式清单
---

---
layout: default
---

# 正文页

正文页交给 Slidev 内置 `default` 布局，主题只负责排版与页脚。

## 二级标题带左侧色条

- 列表项一，含 **强调** 文本
- 列表项二

> 引用块用于结论或提示

<DeckCallout type="info" title="组件自检">
DeckCallout 由 theme-base 提供，deck 里无需 import。
</DeckCallout>

<DeckTag variant="accent">TAG</DeckTag>

---
layout: two-cols
---

# 双栏（内置）

左栏内容，验证 core 布局在新主题下的排版。

::right::

右栏内容，验证列间距与字号继承。

---
layout: table
title: 表格页
caption: 示例数据，非真实来源
---

| 指标 | 说明 | 数值 |
| --- | --- | --- |
| 版式数量 | theme-base 提供的布局 | 8 |
| 组件数量 | 全局可用组件 | 5 |
| 覆盖顺序 | theme → addons → deck | 3 层 |

---
layout: metrics
title: 指标页
items:
  - value: '8'
    label: 基础布局
    note: cover/agenda/section/table/metrics/end…
  - value: '5'
    label: 全局组件
    note: Deck* 前缀
  - value: '3'
    label: 覆盖层级
    note: theme/addons/deck
---

---
layout: statement
---

# 一句话结论

---
layout: fact
---

# 42

这是 fact 布局的数值展示

---
layout: quote
---

# “先定结构，再定风格。”

---
layout: end
title: Thank You
contact:
  - mono-deck-workspace
  - slidev-theme-base
---
