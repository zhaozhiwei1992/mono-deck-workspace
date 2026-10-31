<script setup lang="ts">
import type { PropType } from 'vue'
import { useDeckText } from '../layoutHelper'

type AgendaItem = string | { title: string, desc?: string }

const props = defineProps({
  frontmatter: { type: Object as PropType<Record<string, unknown>>, default: () => ({}) },
  title: { type: String, default: '目录' },
  en: { type: String, default: 'CONTENTS' },
  items: { type: Array as PropType<AgendaItem[]>, default: () => [] },
})

const text = useDeckText(props)

function normalize(item: AgendaItem) {
  return typeof item === 'string' ? { title: item, desc: '' } : { title: item.title, desc: item.desc || '' }
}
</script>

<template>
  <div class="slidev-layout deck-agenda">
    <h1>{{ text('title', '目录') }}</h1>
    <div class="deck-rule" />
    <slot>
      <div class="deck-agenda__grid">
        <div v-for="(item, idx) in props.items" :key="idx" class="deck-agenda__item">
          <span class="deck-agenda__no">{{ String(idx + 1).padStart(2, '0') }}</span>
          <span>
            <span class="deck-agenda__title">{{ normalize(item).title }}</span>
            <span v-if="normalize(item).desc" class="deck-agenda__desc"> · {{ normalize(item).desc }}</span>
          </span>
        </div>
      </div>
    </slot>
  </div>
</template>
