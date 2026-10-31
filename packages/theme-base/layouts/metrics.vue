<script setup lang="ts">
import type { PropType } from 'vue'
import { useDeckText } from '../layoutHelper'

interface Metric {
  value: string
  label: string
  note?: string
}

const props = defineProps({
  frontmatter: { type: Object as PropType<Record<string, unknown>>, default: () => ({}) },
  title: { type: String, default: '' },
  items: { type: Array as PropType<Metric[]>, default: () => [] },
})

const text = useDeckText(props)
</script>

<template>
  <div class="slidev-layout deck-metrics">
    <h1 v-if="text('title')">{{ text('title') }}</h1>
    <div v-if="text('title')" class="deck-rule" />
    <div v-if="props.items.length" class="deck-metrics__grid">
      <div v-for="(item, idx) in props.items" :key="idx" class="deck-metrics__card">
        <div class="deck-metrics__value">{{ item.value }}</div>
        <div class="deck-metrics__label">{{ item.label }}</div>
        <div v-if="item.note" class="deck-metrics__note">{{ item.note }}</div>
      </div>
    </div>
    <slot />
  </div>
</template>
