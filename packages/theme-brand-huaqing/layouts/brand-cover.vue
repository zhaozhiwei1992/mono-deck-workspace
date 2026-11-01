<script setup lang="ts">
import type { PropType } from "vue";
import { computed } from "vue";
import { handleBackground, useDeckText } from "slidev-theme-base/layoutHelper";
import bgCover from "../assets/bg-cover.png";
import BrandSimple from "../components/BrandSimple.vue";

/**
 * 品牌封面（对齐 PPT 第 14 页「2_标题幻灯片」的简洁版）：
 *   底图 + 左对齐文本块 + 左下角官网/地址。没有 logo 条、没有金色徽标、没有竖线。
 *
 * 为什么不复刻第 1 页：那版元素多、位置写死，且自带年度视觉，换年份/换品牌都要重画。
 */
const props = defineProps({
  frontmatter: {
    type: Object as PropType<Record<string, unknown>>,
    default: () => ({}),
  },
  eyebrow: { type: String, default: "" },
  title: { type: String, default: "" },
  subtitle: { type: String, default: "" },
  author: { type: String, default: "" },
  date: { type: String, default: "" },
  org: { type: String, default: "" },
  orgEn: { type: String, default: "" },
  company: { type: String, default: "" },
  site: { type: String, default: "" },
  address: { type: String, default: "" },
  year: {
    type: [String, Number, Boolean] as PropType<string | number | boolean>,
    default: false,
  },
  yearLabel: { type: String, default: "" },
  logo: {
    type: [String, Boolean] as PropType<string | boolean>,
    default: true,
  },
  background: { type: String, default: "" },
});

const text = useDeckText(props);
const style = computed(() => handleBackground(props.background || bgCover));
</script>

<template>
  <div class="slidev-layout brand-cover" :style="style">
    <BrandSimple
      :frontmatter="props.frontmatter"
      :eyebrow="props.eyebrow"
      :title="text('title')"
      :subtitle="props.subtitle"
      :author="props.author"
      :date="props.date"
      :org="props.org"
      :org-en="props.orgEn"
      :company="props.company"
      :site="props.site"
      :address="props.address"
      :year="props.year"
      :year-label="props.yearLabel"
      :logo="props.logo"
    />
  </div>
</template>
