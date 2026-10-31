<script setup lang="ts">
import type { PropType } from 'vue'
import { useDeckText } from '../layoutHelper'

const props = defineProps({
  frontmatter: { type: Object as PropType<Record<string, unknown>>, default: () => ({}) },
  title: { type: String, default: '' },
  caption: { type: String, default: '' },
})

const text = useDeckText(props)
</script>

<template>
  <div class="slidev-layout deck-table">
    <h1 v-if="text('title')">{{ text('title') }}</h1>
    <div v-if="text('title')" class="deck-rule" />
    <slot />
    <div v-if="props.caption" class="deck-table__caption">{{ props.caption }}</div>
  </div>
</template>
