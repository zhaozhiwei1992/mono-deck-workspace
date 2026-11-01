<script setup lang="ts">
import type { PropType } from 'vue'
import { computed } from 'vue'
import { handleBackground, useDeckText } from 'slidev-theme-base/layoutHelper'
import bgCover from '../assets/bg-cover.png'
import decoOrnament from '../assets/deco-ornament.png'
import decoRing from '../assets/deco-ring.png'
import logoMarkGold from '../assets/logo-mark-gold.png'

/**
 * 品牌结束页（对齐 PPT 「2_标题幻灯片」）：与封面同底 + 金色徽标 + 口号 + 地址/网址。
 * 左下两个装饰（圆环 + 对称纹样）是 PPT 里仅有的两个尾页装饰位图。
 */
const props = defineProps({
  frontmatter: { type: Object as PropType<Record<string, unknown>>, default: () => ({}) },
  title: { type: String, default: '' },
  subtitle: { type: String, default: '' },
  address: { type: String, default: '' },
  site: { type: String, default: '' },
  orgEn: { type: String, default: 'BEIJING TAIJI HUAQING INFORMATION SYSTEM CO., LTD.' },
  background: { type: String, default: '' },
})

const text = useDeckText(props)
const style = computed(() => handleBackground(props.background || bgCover))
</script>

<template>
  <div class="slidev-layout brand-end" :style="style">
    <img class="brand-end__deco" :src="decoOrnament" alt="">
    <img class="brand-end__ring" :src="decoRing" alt="">
    <img class="brand-end__emblem" :src="logoMarkGold" alt="">

    <slot>
      <div class="brand-end__title">{{ text('title', 'Thank You') }}</div>
      <div class="brand-end__en">{{ text('orgEn') }}</div>
      <div v-if="text('subtitle')" class="brand-end__subtitle">{{ text('subtitle') }}</div>
      <div v-if="text('address') || text('site')" class="brand-end__contact">
        <span v-if="text('address')">{{ text('address') }}</span>
        <span v-if="text('site')">{{ text('site') }}</span>
      </div>
    </slot>
  </div>
</template>
