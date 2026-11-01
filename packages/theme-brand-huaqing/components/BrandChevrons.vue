<script setup lang="ts">
import type { PropType } from 'vue'

type ChevronItem = string | { title: string, no?: string | number }

/**
 * 底部箭头步骤条（对齐 PPT 正文页底部三条蓝箭头，颜色依次加深）。
 * 纯 CSS clip-path 绘制，可任意列数（4 列以后统一用最深的蓝）。
 */
const props = defineProps({
  items: { type: Array as PropType<ChevronItem[]>, default: () => [] },
})

function normalize(item: ChevronItem, idx: number) {
  const item0 = typeof item === 'string' ? { title: item } : item
  const no = item0.no === undefined ? String(idx + 1).padStart(2, '0') : String(item0.no)
  return { no, title: item0.title }
}
</script>

<template>
  <div class="brand-chevrons">
    <div
      v-for="(item, idx) in props.items"
      :key="idx"
      class="brand-chevrons__item"
      :class="`brand-chevrons__item--${idx + 1}`"
    >
      <span class="brand-chevrons__no">{{ normalize(item, idx).no }}</span>
      <span class="brand-chevrons__title">{{ normalize(item, idx).title }}</span>
    </div>
  </div>
</template>
