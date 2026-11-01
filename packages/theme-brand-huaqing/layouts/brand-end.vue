<script setup lang="ts">
import type { PropType } from "vue";
import { computed } from "vue";
import { handleBackground, useDeckText } from "slidev-theme-base/layoutHelper";
import bgCover from "../assets/bg-cover.png";
import BrandSimple from "../components/BrandSimple.vue";

/**
 * 品牌结束页：与封面同一套简洁结构（PPT 第 14 页本就是「尾页式封面」），
 * 只把默认值换成口号/地址，避免两套版式各写一遍。
 */
const props = defineProps({
  frontmatter: {
    type: Object as PropType<Record<string, unknown>>,
    default: () => ({}),
  },
  title: { type: String, default: "" },
  titleFallback: { type: String, default: "Thank You" },
  subtitle: { type: String, default: "" },
  eyebrow: { type: String, default: "" },
  orgEn: { type: String, default: "" },
  company: { type: String, default: "" },
  address: { type: String, default: "" },
  site: { type: String, default: "" },
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
  <div class="slidev-layout brand-end" :style="style">
    <BrandSimple
      :frontmatter="props.frontmatter"
      :eyebrow="props.eyebrow"
      :title="text('title')"
      :title-fallback="props.titleFallback"
      :subtitle="props.subtitle"
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
