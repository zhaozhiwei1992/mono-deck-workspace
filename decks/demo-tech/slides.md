---
theme: slidev-theme-base
addons:
  - slidev-theme-tech
title: demo-tech
layout: cover
eyebrow: 技术场景 / TECH
subtitle: 'theme-base + addons: [slidev-theme-tech]'
author: mono-deck-workspace
date: 2026-11-01
org: 内部模板
---

---
layout: section
number: 1
en: Tech Layouts
title: 技术版式
---

---
layout: tech-code
title: 代码 + 讲解
file: src/main.ts
tag: ts
---

```ts
const stack = {
  theme: 'slidev-theme-base',
  addons: ['slidev-theme-tech'],
}
```

::right::

### 说明

<TechCodeNote label="覆盖顺序">
theme → addons → deck，后者覆盖前者。
</TechCodeNote>

<TechBadge state="ok">覆盖正确</TechBadge>

---
layout: tech-arch
title: 架构示意
caption: 替换成 mermaid / plantuml 即可
---

```text
decks/demo-tech/slides.md
        │  theme / addons
        ▼
slidev-theme-base ──▶ slidev-theme-tech
```

---
layout: tech-compare
title: 方案对比
leftTitle: 复制粘贴
rightTitle: 主题分层
---

- 每份 deck 各改一套
- 样式漂移
- 无法统一升级

::right::

- 结构只在 base 维护
- 场景主题只写差异
- 升级集中在根依赖

---
layout: tech-benchmark
title: 构建耗时
unit: ms
caption: 本机示例数据
---

| 项 | 冷启动 | 构建 |
| --- | ---: | ---: |
| demo-base | 1150 | 8200 |
| demo-tech | 1200 | 8400 |

---
layout: tech-timeline
title: 演进
items:
  - time: 2026-Q4
    title: 第一版
    desc: base + tech
    state: done
  - time: 2027-Q1
    title: 品牌层
    desc: 只改变量
    state: doing
---

---
layout: default
footer: false
---

# 单页关闭页脚

`footer: false` 时页脚不渲染，用于需要整版留白的页面。

---
layout: end
title: Thank You
contact:
  - deck-demo-tech
---
