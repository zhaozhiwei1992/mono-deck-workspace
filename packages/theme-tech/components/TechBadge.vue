<script setup lang="ts">
import type { PropType } from 'vue'

const props = defineProps({
  state: { type: String as PropType<'ok' | 'warn' | 'bad' | 'plain'>, default: 'plain' },
})
</script>

<template>
  <span class="tech-badge" :class="props.state === 'plain' ? '' : `tech-badge--${props.state}`">
    <slot />
  </span>
</template>
