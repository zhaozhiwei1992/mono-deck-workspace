<script setup lang="ts">
import type { PropType } from 'vue'
import { computed } from 'vue'
import DeckLogo from '../components/DeckLogo.vue'
import { handleBackground, useDeckText } from '../layoutHelper'

const props = defineProps({
  frontmatter: { type: Object as PropType<Record<string, unknown>>, default: () => ({}) },
  eyebrow: { type: String, default: '' },
  title: { type: String, default: '' },
  subtitle: { type: String, default: '' },
  author: { type: String, default: '' },
  date: { type: String, default: '' },
  org: { type: String, default: '' },
  logo: { type: String, default: '' },
  background: { type: String, default: '' },
})

const text = useDeckText(props)
const style = computed(() => handleBackground(props.background, true))
</script>

<template>
  <div class="slidev-layout deck-cover" :style="style">
    <div class="deck-cover__bar" />
    <div class="deck-cover__eyebrow">{{ text('eyebrow') }}</div>
    <slot>
      <h1>{{ text('title') }}</h1>
      <p v-if="text('subtitle')" class="deck-cover__subtitle">{{ text('subtitle') }}</p>
    </slot>
    <div v-if="text('author') || text('date') || text('org')" class="deck-cover__meta">
      <span v-if="text('author')">{{ text('author') }}</span>
      <span v-if="text('date')">{{ text('date') }}</span>
      <span v-if="text('org')">{{ text('org') }}</span>
    </div>
    <div v-if="text('logo')" class="deck-cover__logo">
      <DeckLogo :src="text('logo')" :label="text('org')" />
    </div>
  </div>
</template>
