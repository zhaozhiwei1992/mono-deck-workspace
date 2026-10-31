<script setup lang="ts">
import type { PropType } from 'vue'

const props = defineProps({
  variant: { type: String as PropType<'default' | 'accent' | 'muted'>, default: 'default' },
})
</script>

<template>
  <span class="deck-tag" :class="`deck-tag--${props.variant}`">
    <slot />
  </span>
</template>
