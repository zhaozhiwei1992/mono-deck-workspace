<script setup lang="ts">
const props = defineProps({
  title: { type: String, default: '' },
  caption: { type: String, default: '' },
})
</script>

<template>
  <div class="slidev-layout deck-table">
    <h1 v-if="props.title">{{ props.title }}</h1>
    <div v-if="props.title" class="deck-rule" />
    <slot />
    <div v-if="props.caption" class="deck-table__caption">{{ props.caption }}</div>
  </div>
</template>
