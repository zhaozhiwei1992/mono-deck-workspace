<script setup lang="ts">
const props = defineProps({
  title: { type: String, default: '' },
  unit: { type: String, default: '' },
  caption: { type: String, default: '' },
})
</script>

<template>
  <div class="slidev-layout tech-benchmark">
    <h1 v-if="props.title">
      {{ props.title }}<span v-if="props.unit" class="tech-benchmark__unit">单位：{{ props.unit }}</span>
    </h1>
    <div v-if="props.title" class="deck-rule" />
    <slot />
    <div v-if="props.caption" class="deck-table__caption">{{ props.caption }}</div>
  </div>
</template>
