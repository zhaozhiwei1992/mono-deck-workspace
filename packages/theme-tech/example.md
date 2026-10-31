---
theme: slidev-theme-base
# 相对 addon 以「本包的父目录」为基准解析，故写作 ./theme-tech。
# 用包名 slidev-theme-tech 只在 deck（有 node_modules 链接）里可用。
addons:
  - ./theme-tech
title: theme-tech 自检
layout: cover
eyebrow: 技术场景 / TECH THEME
subtitle: 代码 · 架构 · 对比 · 指标 · 演进
author: mono-deck-workspace
date: 2026-11-01
org: 场景层自检
---

---
layout: tech-code
title: 代码 + 讲解
file: src/example.ts
tag: shiki
---

```ts
export function greet(name: string) {
  return `Hello, ${name}`
}
```

::right::

### 要点

<TechCodeNote label="为什么">
左侧代码区宽度 1.4fr，右侧讲解 1fr，长代码自动内部滚动。
</TechCodeNote>

<TechBadge state="ok">已支持行高亮</TechBadge>

---
layout: tech-arch
title: 架构页
caption: 占位示意，替换为 mermaid / plantuml / 手绘图
---

```text
┌──────────┐     ┌──────────┐     ┌──────────┐
│  decks   │────▶│ themes   │────▶│  build   │
└──────────┘     └──────────┘     └──────────┘
```

---
layout: tech-compare
title: 方案对比
leftTitle: 现状
rightTitle: 方案
leftTag: before
rightTag: after
---

- 主题散落在各 deck
- 样式靠复制粘贴
- 升级 slidev 后全崩

::right::

- theme-base 统一结构
- 场景主题只写差异
- 版本集中在根 package.json

---
layout: tech-benchmark
title: 指标对比
unit: ms
caption: 示例数据
---

| 方案 | 冷启动 | 构建 | 导出 PDF |
| --- | ---: | ---: | ---: |
| 单工程 | 1200 | 8400 | 22000 |
| monorepo | 1100 | 8100 | 21800 |

---
layout: default
---

# 组件自检

<TechKpi value="42" unit="ms" label="P95 延迟" />

<TechDiff
  :lines="[
    { type: 'ctx', text: 'const theme = resolve()' },
    { type: 'del', text: '// string keys, 易错' },
    { type: 'add', text: '// useSlideContext()' },
  ]"
/>

---
layout: tech-timeline
title: 演进路线
items:
  - time: 2026-Q4
    title: 第一版
    desc: base + tech 可跑通
    state: done
  - time: 2027-Q1
    title: 场景扩展
    desc: finance / medical
    state: doing
  - time: 2027-Q2
    title: 品牌层
    desc: 变量覆盖 + logo
    state: todo
---

---
layout: end
title: Thank You
contact:
  - slidev-theme-tech
---
