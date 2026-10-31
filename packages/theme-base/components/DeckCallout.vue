<script setup lang="ts">
import type { PropType } from 'vue'

const props = defineProps({
  type: { type: String as PropType<'info' | 'warn' | 'danger' | 'success'>, default: 'info' },
  title: { type: String, default: '' },
})
</script>

<template>
  <div class="deck-callout" :class="`deck-callout--${props.type}`">
    <div v-if="props.title" class="deck-callout__title">{{ props.title }}</div>
    <slot />
  </div>
</template>
