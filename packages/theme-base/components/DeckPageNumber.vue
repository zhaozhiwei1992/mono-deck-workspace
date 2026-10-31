<script setup lang="ts">
const props = defineProps({
  current: { type: Number, default: 0 },
  total: { type: Number, default: 0 },
})

function pad(n: number) {
  return String(n).padStart(2, '0')
}
</script>

<template>
  <span class="deck-page-number">{{ pad(props.current) }} / {{ pad(props.total) }}</span>
</template>
