<script setup lang="ts">
import type { PropType } from 'vue'
import { useDeckText } from '../layoutHelper'

const props = defineProps({
  frontmatter: { type: Object as PropType<Record<string, unknown>>, default: () => ({}) },
  title: { type: String, default: 'Thank You' },
  contact: { type: Array as PropType<string[]>, default: () => [] },
})

const text = useDeckText(props)
</script>

<template>
  <div class="slidev-layout deck-end">
    <slot>
      <div class="deck-end__title">{{ text('title', 'Thank You') }}</div>
      <div v-if="props.contact.length" class="deck-end__contact">
        <span v-for="(line, idx) in props.contact" :key="idx">{{ line }}</span>
      </div>
    </slot>
  </div>
</template>
