<script setup lang="ts">
const props = defineProps({
  title: { type: String, default: '' },
  caption: { type: String, default: '' },
})
</script>

<template>
  <div class="slidev-layout tech-arch">
    <div>
      <h1 v-if="props.title">{{ props.title }}</h1>
      <div v-if="props.title" class="deck-rule" />
    </div>
    <div class="tech-arch__figure">
      <slot />
    </div>
    <div v-if="props.caption || $slots.aside" class="tech-arch__caption">
      <slot name="aside">{{ props.caption }}</slot>
    </div>
  </div>
</template>
