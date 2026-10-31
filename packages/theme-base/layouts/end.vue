<script setup lang="ts">
import type { PropType } from 'vue'

const props = defineProps({
  title: { type: String, default: 'Thank You' },
  contact: { type: Array as PropType<string[]>, default: () => [] },
})
</script>

<template>
  <div class="slidev-layout deck-end">
    <slot>
      <div class="deck-end__title">{{ props.title }}</div>
      <div v-if="props.contact.length" class="deck-end__contact">
        <span v-for="(line, idx) in props.contact" :key="idx">{{ line }}</span>
      </div>
    </slot>
  </div>
</template>
