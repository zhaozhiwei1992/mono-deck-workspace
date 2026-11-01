<script setup lang="ts">
import type { PropType } from 'vue'
import { useDeckText } from 'slidev-theme-base/layoutHelper'

type ColumnItem = { title: string, en?: string, desc?: string }

/**
 * 品牌多列页（对齐 PPT 正文页右侧的「圆点 + 标题 + 英文 + 正文」三列）：
 * 列之间竖细线分隔，每列左侧一条点状引导线，列数由 `columns` 控制（默认 3）。
 */
const props = defineProps({
  frontmatter: { type: Object as PropType<Record<string, unknown>>, default: () => ({}) },
  title: { type: String, default: '' },
  items: { type: Array as PropType<ColumnItem[]>, default: () => [] },
  columns: { type: [String, Number], default: 3 },
})

const text = useDeckText(props)
</script>

<template>
  <div class="slidev-layout brand-columns">
    <h1 v-if="text('title')" class="brand-columns__title">{{ text('title') }}</h1>
    <div v-if="text('title')" class="brand-columns__rule" />

    <slot>
      <div class="brand-columns__grid" :style="{ '--brand-columns': props.columns }">
        <div v-for="(item, idx) in props.items" :key="idx" class="brand-columns__item">
          <span class="brand-columns__dot" />
          <h3 class="brand-columns__item-title">{{ item.title }}</h3>
          <p v-if="item.en" class="brand-columns__item-en">{{ item.en }}</p>
          <p v-if="item.desc" class="brand-columns__item-desc">{{ item.desc }}</p>
        </div>
      </div>
    </slot>
  </div>
</template>
