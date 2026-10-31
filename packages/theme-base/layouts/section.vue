<script setup lang="ts">
const props = defineProps({
  number: { type: [String, Number], default: '' },
  en: { type: String, default: '' },
  title: { type: String, default: '' },
})

function pad(n: string | number) {
  if (n === '')
    return ''
  const num = Number(n)
  return Number.isNaN(num) ? String(n) : String(num).padStart(2, '0')
}
</script>

<template>
  <div class="slidev-layout deck-section">
    <div v-if="props.number !== ''" class="deck-section__no">{{ pad(props.number) }}</div>
    <div class="deck-section__inner">
      <slot>
        <div v-if="props.en" class="deck-section__en">{{ props.en }}</div>
        <h1>{{ props.title }}</h1>
        <div class="deck-rule" />
      </slot>
    </div>
  </div>
</template>
