<script setup lang="ts">
import type { PropType } from 'vue'
import { useDeckText } from 'slidev-theme-base/layoutHelper'

const props = defineProps({
  frontmatter: { type: Object as PropType<Record<string, unknown>>, default: () => ({}) },
  title: { type: String, default: '' },
  file: { type: String, default: '' },
  tag: { type: String, default: '' },
})

const text = useDeckText(props)
</script>

<template>
  <div class="slidev-layout tech-code">
    <div class="tech-code__head">
      <h3 v-if="text('title')" class="tech-code__title">{{ text('title') }}</h3>
      <span v-if="props.tag" class="tech-badge">{{ props.tag }}</span>
      <span v-if="props.file" class="tech-code__file">{{ props.file }}</span>
    </div>
    <div class="tech-code__main">
      <slot />
    </div>
    <div class="tech-code__aside">
      <slot name="right" />
    </div>
  </div>
</template>
