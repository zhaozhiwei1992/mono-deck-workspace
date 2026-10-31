<script setup lang="ts">
const props = defineProps({
  value: { type: [String, Number], required: true },
  unit: { type: String, default: '' },
  label: { type: String, default: '' },
})
</script>

<template>
  <span class="tech-kpi">
    <span class="tech-kpi__value">{{ props.value }}</span>
    <span v-if="props.unit" class="tech-kpi__unit">{{ props.unit }}</span>
    <span v-if="props.label" class="tech-kpi__label">{{ props.label }}</span>
  </span>
</template>
