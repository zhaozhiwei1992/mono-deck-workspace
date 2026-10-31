---
theme: slidev-theme-base
title: demo-base
layout: cover
eyebrow: 结构层 / BASE
subtitle: 只用 theme-base，验证基础版式与页脚
author: mono-deck-workspace
date: 2026-11-01
org: 内部模板
---

---
layout: agenda
title: 目录
items:
  - 版式验证
  - 组件验证
  - 结束
---

---
layout: section
number: 1
en: Layouts
title: 版式验证
---

---
layout: default
---

# 正文页

正文页用 Slidev 内置 `default` 布局，主题只叠加排版与页脚。

## 二级标题

- 列表项
- 含 **强调** 的列表项

> 引用块用于放结论

<DeckCallout type="success" title="组件">
DeckCallout / DeckTag 无需 import 即可使用。
</DeckCallout>

<DeckTag variant="accent">demo</DeckTag>

---
layout: two-cols
---

# 双栏

左栏（内置布局）

::right::

右栏（内置布局）

---
layout: table
title: 表格页
caption: 示例数据
---

| 项 | 值 |
| --- | --- |
| 主题 | slidev-theme-base |
| 层级 | 结构层 |

---
layout: metrics
title: 指标页
items:
  - value: '1'
    label: theme 包
    note: slidev-theme-base
  - value: '5'
    label: 组件
    note: Deck* 前缀
---

---
layout: end
title: Thank You
contact:
  - deck-demo-base
---
