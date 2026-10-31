<script setup lang="ts">
/**
 * 页脚：品牌 + 页码
 * - 通过 `@slidev/client` 的公开 composable 取当前页/layout（CLI 内置 alias，主题包无需声明依赖）。
 * - `footer: false` 可单页关闭；默认在封面/章节/结束/中间态布局隐藏。
 */
import type { PropType } from 'vue'
import { useSlideContext } from '@slidev/client'
import { computed } from 'vue'
import DeckLogo from './DeckLogo.vue'
import DeckPageNumber from './DeckPageNumber.vue'

const props = defineProps({
  brand: { type: String, default: '' },
  logo: { type: String, default: '' },
  hideOn: {
    type: Array as PropType<string[]>,
    default: () => ['deck-cover', 'deck-section', 'deck-end', 'cover', 'section', 'end', 'fact', 'statement'],
  },
})

const { $nav, $page, $frontmatter } = useSlideContext()

const layout = computed<string>(() => ($frontmatter.layout as string) || 'default')
const visible = computed(() => {
  if ($frontmatter.footer === false)
    return false
  return !props.hideOn.includes(layout.value)
})
const current = computed(() => $page.value ?? 0)
const total = computed(() => $nav.value?.total ?? 0)
</script>

<template>
  <div v-if="visible" class="deck-footer">
    <div class="deck-footer__brand">
      <DeckLogo :src="logo || $frontmatter.logo" :label="brand || $frontmatter.org" />
    </div>
    <DeckPageNumber :current="current" :total="total" />
  </div>
</template>
