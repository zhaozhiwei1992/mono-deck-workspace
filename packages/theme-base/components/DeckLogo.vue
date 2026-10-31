<script setup lang="ts">
const props = defineProps({
  src: { type: String, default: '' },
  label: { type: String, default: '' },
})
</script>

<template>
  <span v-if="props.src" class="deck-logo deck-logo--img">
    <img :src="props.src" :alt="props.label || 'logo'">
  </span>
  <span v-else-if="props.label" class="deck-logo deck-logo--text">{{ props.label }}</span>
</template>

<style scoped>
.deck-logo--img {
  display: inline-flex;
  align-items: center;
}

.deck-logo--img img {
  display: block;
  max-height: 2rem;
}

.deck-logo--text {
  font-size: 0.8rem;
  font-weight: 600;
  letter-spacing: 0.08em;
  color: var(--deck-color-primary);
}
</style>
