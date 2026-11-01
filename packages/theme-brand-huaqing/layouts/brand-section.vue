<script setup lang="ts">
import type { PropType } from 'vue'
import { useDeckText } from 'slidev-theme-base/layoutHelper'

/**
 * 品牌章节页（对齐 PPT 「1_正文页-副标题-01」）：浅底 + 蓝色彩带 + 白字标题。
 * 彩带位置按 PPT 原始坐标固定（left 0 / top 33.3% / 宽 91.1% / 高 28.4%），标题落在彩带内。
 */
const props = defineProps({
  frontmatter: { type: Object as PropType<Record<string, unknown>>, default: () => ({}) },
  number: { type: [String, Number], default: '' },
  en: { type: String, default: '' },
  title: { type: String, default: '' },
})

const text = useDeckText(props)

function pad(n: string | number) {
  if (n === '')
    return ''
  const num = Number(n)
  return Number.isNaN(num) ? String(n) : String(num).padStart(2, '0')
}
</script>

<template>
  <div class="slidev-layout brand-section">
    <div class="brand-section__band" />
    <div class="brand-section__inner">
      <slot>
        <div v-if="props.number !== ''" class="brand-section__no">{{ pad(props.number) }}</div>
        <h1>{{ text('title') }}</h1>
        <div v-if="text('en')" class="brand-section__en">{{ text('en') }}</div>
        <div class="brand-section__rule" />
      </slot>
    </div>
  </div>
</template>
