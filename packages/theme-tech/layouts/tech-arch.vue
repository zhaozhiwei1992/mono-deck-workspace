<script setup lang="ts">
import type { PropType } from 'vue'
import { useDeckText } from 'slidev-theme-base/layoutHelper'

const props = defineProps({
  frontmatter: { type: Object as PropType<Record<string, unknown>>, default: () => ({}) },
  title: { type: String, default: '' },
  caption: { type: String, default: '' },
})

const text = useDeckText(props)
</script>

<template>
  <div class="slidev-layout tech-arch">
    <div>
      <h1 v-if="text('title')">{{ text('title') }}</h1>
      <div v-if="text('title')" class="deck-rule" />
    </div>
    <div class="tech-arch__figure">
      <slot />
    </div>
    <div v-if="props.caption || $slots.aside" class="tech-arch__caption">
      <slot name="aside">{{ props.caption }}</slot>
    </div>
  </div>
</template>
