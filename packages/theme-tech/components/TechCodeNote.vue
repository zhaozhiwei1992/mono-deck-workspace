<script setup lang="ts">
defineProps({
  label: { type: String, default: '' },
})
</script>

<template>
  <div class="tech-code-note">
    <strong v-if="label">{{ label }}：</strong><slot />
  </div>
</template>
