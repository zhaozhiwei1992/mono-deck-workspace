<script setup lang="ts">
const props = defineProps({
  title: { type: String, default: '' },
  file: { type: String, default: '' },
  tag: { type: String, default: '' },
})
</script>

<template>
  <div class="slidev-layout tech-code">
    <div class="tech-code__head">
      <h3 v-if="props.title" class="tech-code__title">{{ props.title }}</h3>
      <span v-if="props.tag" class="tech-badge">{{ props.tag }}</span>
      <span v-if="props.file" class="tech-code__file">{{ props.file }}</span>
    </div>
    <div class="tech-code__main">
      <slot />
    </div>
    <div class="tech-code__aside">
      <slot name="right" />
    </div>
  </div>
</template>
