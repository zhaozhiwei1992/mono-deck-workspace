---
theme: slidev-theme-base
addons:
  - slidev-theme-tech
  - slidev-theme-brand-huaqing
colorSchema: light
palette: huaqing
layout: brand-cover
title: 行业大模型落地实践
subtitle: 私有化部署 · 专业定制 · 模型即服务
eyebrow: 数字科技 / DIGITAL TECH
author: 解决方案中心
date: 2026-11-01
org: 华青 · HUAQING
orgEn: BEIJING TAIJI HUAQING
company: 北京市太极华青信息系统有限公司
site: 公司官网：www.tjhq.com　云构智慧政府
---

---
layout: brand-agenda
title: 目录
panelTitle: 从模型选型到业务落地
items:
  - title: 背景与目标
    desc: 为什么需要行业大模型
  - title: 技术路径
    desc: 私有化 / 精调 / MaaS
  - title: 场景验证
    desc: 智能填单与合规判定
  - title: 落地节奏
    desc: 试点到规模推广
---

---
layout: brand-section
number: 1
en: Background
title: 背景与目标
---

---
layout: default
---

# 通用大模型与行业大模型

- **通用大模型**：千亿级以上参数，能力强，但成本高、数据出域
- **行业大模型**：十亿～百亿级参数，在开源模型上再训练或精调
- **本地方案**：全量私有化部署，数据不出机房，成本可控

> 结论：政企场景优先选择「行业大模型 + 私有化部署」，用 MaaS 方式交付。

---
layout: brand-columns
title: 三条技术路径
items:
  - title: 可私有化部署
    en: PRIVATE DEPLOYMENT
    desc: 高性价比。行业大模型在较小参数量模型基础上再训练，十亿～百亿级参数即可达到较好效果，相比千亿级通用模型明显节省成本。
  - title: 可专业定制
    en: DOMAIN TUNING
    desc: 基于开源模型开发，可对模型结构、参数按需调整，更好地适配个性化的应用需要。
  - title: 模型即服务
    en: MAAS
    desc: 以 MaaS 方式交付，屏蔽算力与工程细节，业务侧只面对接口与效果指标。
---

---
layout: two-cols-header
---

# 与传统方案的差异

::left::

### 传统规则引擎

- 规则由人维护，覆盖长尾成本高
- 表单结构变更即失效
- 无自然语言理解能力

::right::

### 行业大模型

- 从表单结构与制度文本中学习
- 结构变更靠重新对齐，不重写规则
- 支持自然语言填报与解释

---
layout: tech-compare
title: 两种交付形态
leftTitle: 私有化一体机
rightTitle: 云端 MaaS
leftTag: 政企
rightTag: 中小
---

- 全量私有化，数据不出机房
- 一次性买断算力，无按量费用
- 需要自有运维与显卡资源

::right::

`tech-*` 版式来自 `slidev-theme-tech`，只调中性轴，品牌轴仍由 `palette: huaqing` 提供，因此和品牌页同色。

---
layout: brand-steps
title: 落地节奏
steps:
  - title: 现状盘点
  - title: 单场景试点
  - title: 规模推广
---

### 三个里程碑

1. **现状盘点（2 周）**：梳理表单、制度、接口，确定试点场景
2. **单场景试点（6 周）**：智能填单跑通，人工对比验收
3. **规模推广（1 季度）**：沉淀工具与技能，复制到其他业务

---
layout: metrics
title: 试点结果
items:
  - value: '92%'
    label: 字段识别准确率
    note: 结构化表单抽取
  - value: '-64%'
    label: 平均填报耗时
    note: 与人工填报对比
  - value: '3'
    label: 已接入业务系统
    note: 表单 / 制度 / 预算
---

---
layout: brand-end
title: 聚力发展　向新出发
address: 北京市朝阳区来广营西路5号诚盈中心7号楼
site: 官方网址：www.tjhq.com
---
