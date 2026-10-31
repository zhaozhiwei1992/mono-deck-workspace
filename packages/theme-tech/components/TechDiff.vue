<script setup lang="ts">
import type { PropType } from 'vue'

interface DiffLine {
  type: 'add' | 'del' | 'ctx'
  text: string
}

const props = defineProps({
  lines: { type: Array as PropType<DiffLine[]>, default: () => [] },
})

function prefix(type: DiffLine['type']) {
  return type === 'add' ? '+' : type === 'del' ? '-' : ' '
}
</script>

<template>
  <div class="tech-diff">
    <div
      v-for="(line, idx) in props.lines"
      :key="idx"
      :class="line.type === 'ctx' ? '' : `tech-diff__line--${line.type}`"
    >
      {{ prefix(line.type) }} {{ line.text }}
    </div>
  </div>
</template>
