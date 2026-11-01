<script setup lang="ts">
import type { PropType } from "vue";
import { useDeckText } from "slidev-theme-base/layoutHelper";
import logoHuaqing from "../assets/logo-huaqing.png";
import iconSite from "../assets/deco-ring.png";
import iconAddress from "../assets/deco-ornament.png";
import BrandYear from "./BrandYear.vue";

/**
 * 简洁封面/尾页版式（对齐 PPT 第 14 页「2_标题幻灯片」）：
 *   左对齐文本块（小标 / 主标题 / 副标题 / 英文公司名 / 中文公司名 / 年份·作者·日期）
 *   + 左下角「官网 / 地址」两行（前面各一个 16px 级小图标）。
 *
 * 与旧封面的区别：不再有顶部 logo 条、左侧品牌块、金色徽标——那些是第 1 页的设计，
 * 位置写死、元素多，换年份/换品牌都要重画。这里只有文本，靠底图承载品牌视觉。
 */
const props = defineProps({
  frontmatter: {
    type: Object as PropType<Record<string, unknown>>,
    default: () => ({}),
  },
  eyebrow: { type: String, default: "" },
  title: { type: String, default: "" },
  titleFallback: { type: String, default: "" },
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
  // 右上角标识：默认白色版；写 false 关掉，写路径可换图
  logo: {
    type: [String, Boolean] as PropType<string | boolean>,
    default: true,
  },
});

const text = useDeckText(props);
</script>

<template>
  <div class="brand-simple">
    <img
      v-if="props.logo !== false"
      class="brand-simple__logo"
      :src="typeof props.logo === 'string' ? props.logo : logoHuaqing"
      alt="HUAQING"
    />

    <div class="brand-simple__main">
      <h1>{{ text("title") || props.titleFallback }}</h1>
      <p v-if="text('subtitle')" class="brand-simple__subtitle">
        {{ text("subtitle") }}
      </p>
      <div v-if="text('eyebrow') || text('org')" class="brand-simple__eyebrow">
        {{ text("eyebrow") || text("org") }}
      </div>
      <div v-if="text('orgEn') || text('company')" class="brand-simple__en">
        {{ text("orgEn") || text("company") }}
      </div>
      <div v-if="text('company') && text('orgEn')" class="brand-simple__cn">
        {{ text("company") }}
      </div>
      <div
        v-if="props.year || text('author') || text('date')"
        class="brand-simple__meta"
      >
        <BrandYear
          v-if="props.year"
          :year="props.year === true ? '' : String(props.year)"
          :label="props.yearLabel"
        />
        <span v-if="text('author')">{{ text("author") }}</span>
        <span v-if="text('date')">{{ text("date") }}</span>
      </div>
    </div>

    <div v-if="text('site') || text('address')" class="brand-simple__contact">
      <div v-if="text('site')" class="brand-simple__contact-row">
        <img :src="iconSite" alt="" />
        <span>{{ text("site") }}</span>
      </div>
      <div v-if="text('address')" class="brand-simple__contact-row">
        <img :src="iconAddress" alt="" />
        <span>{{ text("address") }}</span>
      </div>
    </div>
  </div>
</template>
