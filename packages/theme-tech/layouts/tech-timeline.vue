<script setup lang="ts">
import type { PropType } from 'vue'

interface Milestone {
  time: string
  title: string
  desc?: string
  state?: 'done' | 'doing' | 'todo'
}

const props = defineProps({
  title: { type: String, default: '' },
  items: { type: Array as PropType<Milestone[]>, default: () => [] },
})
</script>

<template>
  <div class="slidev-layout tech-timeline">
    <h1 v-if="props.title">{{ props.title }}</h1>
    <div v-if="props.title" class="deck-rule" />
    <div class="tech-timeline__track">
      <div
        v-for="(item, idx) in props.items"
        :key="idx"
        class="tech-timeline__node"
        :class="`tech-timeline__node--${item.state || 'todo'}`"
      >
        <span class="tech-timeline__dot" />
        <div class="tech-timeline__time">{{ item.time }}</div>
        <div class="tech-timeline__title">{{ item.title }}</div>
        <div v-if="item.desc" class="tech-timeline__desc">{{ item.desc }}</div>
      </div>
    </div>
    <slot />
  </div>
</template>
