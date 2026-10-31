<script setup lang="ts">
import type { PropType } from 'vue'
import { useDeckText } from '../layoutHelper'

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
  <div class="slidev-layout deck-section">
    <div v-if="props.number !== ''" class="deck-section__no">{{ pad(props.number) }}</div>
    <div class="deck-section__inner">
      <slot>
        <div v-if="text('en')" class="deck-section__en">{{ text('en') }}</div>
        <h1>{{ text('title') }}</h1>
        <div class="deck-rule" />
      </slot>
    </div>
  </div>
</template>
