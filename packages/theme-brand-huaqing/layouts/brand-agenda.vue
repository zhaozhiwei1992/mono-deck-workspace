<script setup lang="ts">
import type { PropType } from 'vue'
import { useDeckText } from 'slidev-theme-base/layoutHelper'

type AgendaItem = string | { no?: string | number, title: string, desc?: string }

/**
 * 品牌目录页（对齐 PPT 「目录」版式）：左侧 35.4% 宽的蓝色面板 + 右侧 2×2 大序号条目。
 * 面板用 CSS 渐变 + 径向高光重建（PPT 里是位图），因此条目数量可变、暗色下不刺眼。
 */
const props = defineProps({
  frontmatter: { type: Object as PropType<Record<string, unknown>>, default: () => ({}) },
  title: { type: String, default: '' },
  items: { type: Array as PropType<AgendaItem[]>, default: () => [] },
  panelTitle: { type: String, default: '' },
  panelEn: { type: String, default: 'CONTENTS' },
})

const text = useDeckText(props)

function normalize(item: AgendaItem, idx: number) {
  const item0 = typeof item === 'string' ? { title: item } : item
  const no = item0.no === undefined ? String(idx + 1).padStart(2, '0') : String(item0.no)
  return { no, title: item0.title, desc: item0.desc || '' }
}
</script>

<template>
  <div class="slidev-layout brand-agenda">
    <div class="brand-agenda__panel">
      <div class="brand-agenda__panel-en">{{ props.panelEn }}</div>
      <div v-if="text('panelTitle')" class="brand-agenda__panel-title">{{ text('panelTitle') }}</div>
    </div>

    <h1 v-if="text('title')" class="brand-agenda__title">{{ text('title') }}</h1>

    <slot>
      <div class="brand-agenda__grid">
        <div v-for="(item, idx) in props.items" :key="idx" class="brand-agenda__item">
          <span class="brand-agenda__no">{{ normalize(item, idx).no }}</span>
          <span class="brand-agenda__text">
            <span class="brand-agenda__item-title">{{ normalize(item, idx).title }}</span>
            <span v-if="normalize(item, idx).desc" class="brand-agenda__item-desc">{{ normalize(item, idx).desc }}</span>
          </span>
        </div>
      </div>
    </slot>
  </div>
</template>
