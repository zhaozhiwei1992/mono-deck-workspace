<script setup lang="ts">
import { computed } from 'vue'
import DeckLogo from '../components/DeckLogo.vue'
import { handleBackground } from '../layoutHelper'

const props = defineProps({
  eyebrow: { type: String, default: '' },
  title: { type: String, default: '' },
  subtitle: { type: String, default: '' },
  author: { type: String, default: '' },
  date: { type: String, default: '' },
  org: { type: String, default: '' },
  logo: { type: String, default: '' },
  background: { type: String, default: '' },
})

const style = computed(() => handleBackground(props.background, true))
</script>

<template>
  <div class="slidev-layout deck-cover" :style="style">
    <div class="deck-cover__bar" />
    <div class="deck-cover__eyebrow">{{ props.eyebrow }}</div>
    <slot>
      <h1>{{ props.title }}</h1>
      <p v-if="props.subtitle" class="deck-cover__subtitle">{{ props.subtitle }}</p>
    </slot>
    <div v-if="props.author || props.date || props.org" class="deck-cover__meta">
      <span v-if="props.author">{{ props.author }}</span>
      <span v-if="props.date">{{ props.date }}</span>
      <span v-if="props.org">{{ props.org }}</span>
    </div>
    <div v-if="props.logo" class="deck-cover__logo">
      <DeckLogo :src="props.logo" :label="props.org" />
    </div>
  </div>
</template>
