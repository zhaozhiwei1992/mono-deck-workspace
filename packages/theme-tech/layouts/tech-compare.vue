<script setup lang="ts">
const props = defineProps({
  title: { type: String, default: '' },
  leftTitle: { type: String, default: '现状' },
  rightTitle: { type: String, default: '方案' },
  leftTag: { type: String, default: 'before' },
  rightTag: { type: String, default: 'after' },
})
</script>

<template>
  <div class="slidev-layout tech-compare">
    <div class="tech-compare__head">
      <h3 class="tech-code__title">{{ props.title }}</h3>
    </div>
    <div class="tech-compare__col tech-compare__col--left">
      <div class="tech-code__head">
        <strong>{{ props.leftTitle }}</strong>
        <span class="tech-badge tech-badge--bad">{{ props.leftTag }}</span>
      </div>
      <slot />
    </div>
    <div class="tech-compare__col tech-compare__col--right">
      <div class="tech-code__head">
        <strong>{{ props.rightTitle }}</strong>
        <span class="tech-badge tech-badge--ok">{{ props.rightTag }}</span>
      </div>
      <slot name="right" />
    </div>
  </div>
</template>
