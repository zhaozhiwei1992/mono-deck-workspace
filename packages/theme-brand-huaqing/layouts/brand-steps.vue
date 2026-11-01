<script setup lang="ts">
import type { PropType } from 'vue'
import { useDeckText } from 'slidev-theme-base/layoutHelper'
import BrandChevrons from '../components/BrandChevrons.vue'

type StepItem = string | { title: string, no?: string | number }

/**
 * 品牌步骤页（对齐 PPT 正文页底部箭头条）：标题 + 正文 slot + 底部 BrandChevrons。
 */
const props = defineProps({
  frontmatter: { type: Object as PropType<Record<string, unknown>>, default: () => ({}) },
  title: { type: String, default: '' },
  steps: { type: Array as PropType<StepItem[]>, default: () => [] },
})

const text = useDeckText(props)
</script>

<template>
  <div class="slidev-layout brand-steps">
    <h1 v-if="text('title')" class="brand-steps__title">{{ text('title') }}</h1>
    <div v-if="text('title')" class="brand-steps__rule" />
    <div class="brand-steps__body">
      <slot />
    </div>
    <BrandChevrons v-if="props.steps.length" :items="props.steps" />
  </div>
</template>
