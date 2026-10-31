<script setup lang="ts">
import type { PropType } from 'vue'
import { useDeckText } from 'slidev-theme-base/layoutHelper'

const props = defineProps({
  frontmatter: { type: Object as PropType<Record<string, unknown>>, default: () => ({}) },
  title: { type: String, default: '' },
  leftTitle: { type: String, default: '现状' },
  rightTitle: { type: String, default: '方案' },
  leftTag: { type: String, default: 'before' },
  rightTag: { type: String, default: 'after' },
})

const text = useDeckText(props)
</script>

<template>
  <div class="slidev-layout tech-compare">
    <div class="tech-compare__head">
      <h3 class="tech-code__title">{{ text('title') }}</h3>
    </div>
    <div class="tech-compare__col tech-compare__col--left">
      <div class="tech-code__head">
        <strong>{{ props.leftTitle }}</strong>
        <span class="tech-badge tech-badge--bad">{{ props.leftTag }}</span>
      </div>
      <slot />
    </div>
    <div class="tech-compare__col tech-compare__col--right">
      <div class="tech-code__head">
        <strong>{{ props.rightTitle }}</strong>
        <span class="tech-badge tech-badge--ok">{{ props.rightTag }}</span>
      </div>
      <slot name="right" />
    </div>
  </div>
</template>
