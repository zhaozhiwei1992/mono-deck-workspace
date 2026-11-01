<script setup lang="ts">
import type { PropType } from 'vue'
import { computed } from 'vue'
import { handleBackground, useDeckText } from 'slidev-theme-base/layoutHelper'
import bgCover from '../assets/bg-cover.png'
import logoFull from '../assets/logo-full.png'
import logoMark from '../assets/logo-mark.png'
import logoMarkGold from '../assets/logo-mark-gold.png'

/**
 * 品牌封面（对齐 PPT 「标题幻灯片」版式）：
 *   左上 logo 标识 / 右上完整 logo / 中部左品牌块（金色徽标 + 英文名 + 中文名）/ 右主标题
 *
 * 底图默认用 PPT 里的 1920×1080 品牌渐变位图；`background` 可换成自己的图或纯色。
 */
const props = defineProps({
  frontmatter: { type: Object as PropType<Record<string, unknown>>, default: () => ({}) },
  eyebrow: { type: String, default: '' },
  title: { type: String, default: '' },
  subtitle: { type: String, default: '' },
  author: { type: String, default: '' },
  date: { type: String, default: '' },
  org: { type: String, default: '' },
  orgEn: { type: String, default: '' },
  company: { type: String, default: '' },
  site: { type: String, default: '' },
  background: { type: String, default: '' },
})

const text = useDeckText(props)
const style = computed(() => handleBackground(props.background || bgCover))
</script>

<template>
  <div class="slidev-layout brand-cover" :style="style">
    <header class="brand-cover__top">
      <div class="brand-cover__mark">
        <img :src="logoMark" alt="">
        <span class="brand-cover__org">{{ text('org') }}</span>
      </div>
      <img class="brand-cover__logo" :src="logoFull" alt="HUAQING">
    </header>

    <div class="brand-cover__body">
      <div class="brand-cover__brand">
        <img class="brand-cover__emblem" :src="logoMarkGold" alt="">
        <div class="brand-cover__en">{{ text('orgEn', 'BEIJING TAIJI HUAQING') }}</div>
        <div class="brand-cover__cn">{{ text('company', '北京市太极华青信息系统有限公司') }}</div>
      </div>

      <div class="brand-cover__main">
        <div v-if="text('eyebrow')" class="brand-cover__eyebrow">{{ text('eyebrow') }}</div>
        <slot>
          <h1>{{ text('title') }}</h1>
          <p v-if="text('subtitle')" class="brand-cover__subtitle">{{ text('subtitle') }}</p>
        </slot>
        <div v-if="text('author') || text('date')" class="brand-cover__meta">
          <span v-if="text('author')">{{ text('author') }}</span>
          <span v-if="text('date')">{{ text('date') }}</span>
        </div>
      </div>
    </div>

    <div v-if="text('site')" class="brand-cover__foot">{{ text('site') }}</div>
  </div>
</template>
