<script setup lang="ts">
import type { PropType } from 'vue'
import { computed } from 'vue'

/**
 * 年份标记（SVG 文本，不是位图）。
 *
 * 为什么不用图片：年份每年变，位图就得每年重出一张；用 SVG `<text>` + 渐变填充，
 * 改年份 = 改一个数字（或干脆不传，自动取当前年），分辨率/暗色/配色都不用管。
 *
 * 注意：这只是**年份标记**，不是 logo。企业标识必须用官方矢量文件（见 README），
 * 不要把年份做进 logo。
 */
const props = defineProps({
  year: { type: [String, Number] as PropType<string | number>, default: '' },
  label: { type: String, default: '' },
})

const text = computed(() => String(props.year || new Date().getFullYear()))
</script>

<template>
  <span class="brand-year">
    <svg class="brand-year__svg" viewBox="0 0 240 96" role="img" :aria-label="text">
      <defs>
        <linearGradient :id="`brand-year-grad-${text}`" x1="0%" y1="0%" x2="100%" y2="0%">
          <stop offset="0%" stop-color="#ffe6b0" />
          <stop offset="100%" stop-color="#f0a24a" />
        </linearGradient>
      </defs>
      <text
        x="50%" y="54%" text-anchor="middle" dominant-baseline="middle"
        class="brand-year__text" :fill="`url(#brand-year-grad-${text})`"
      >{{ text }}</text>
    </svg>
    <span v-if="props.label" class="brand-year__label">{{ props.label }}</span>
  </span>
</template>
