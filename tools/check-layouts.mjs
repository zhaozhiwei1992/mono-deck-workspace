#!/usr/bin/env node
/**
 * Slidev 版式体检：逐页检查「溢出、标题行数、页脚、关键元素几何」。
 *
 * 用途：改主题/做品牌层后，用机器代替眼睛确认没有元素跑出版面、标题没炸成多行、
 * 该隐藏页脚的页面真的隐藏了。任何 deck 都能用，不绑定具体主题。
 *
 * 依赖：playwright-chromium（仓库不预装；本机验证时装在 /tmp/pw，见文末）
 *
 * 用法：
 *   pnpm --filter deck-xxx dev            # 另开一个终端，记住端口（默认 3030）
 *   node tools/check-layouts.mjs --url http://localhost:3030 --total 10
 *   node tools/check-layouts.mjs --url http://localhost:3030 --total 10 --dark
 *   node tools/check-layouts.mjs --url ... --selectors ".brand-section__band,.brand-agenda__panel"
 *
 * 退出码：有溢出 = 1（可直接进 CI / pre-commit），无溢出 = 0。
 *
 * 装 playwright（只做一次，不要进仓库依赖）：
 *   mkdir -p /tmp/pw && cd /tmp/pw && npm init -y && npm i playwright-chromium@1
 *   node node_modules/playwright-chromium/install.js
 *   ln -sfn /tmp/pw/node_modules/playwright-chromium <repo>/node_modules/playwright-chromium
 */
import { chromium } from 'playwright-chromium'

function arg(name, fallback) {
  const i = process.argv.indexOf(`--${name}`)
  if (i === -1)
    return fallback
  const v = process.argv[i + 1]
  return v && !v.startsWith('--') ? v : true
}

const base = arg('url', 'http://localhost:3030')
const total = Number(arg('total', 0))
const dark = Boolean(arg('dark', false))
const wait = Number(arg('wait', 500))
const extraSelectors = String(arg('selectors', '')).split(',').map(s => s.trim()).filter(Boolean)

if (!total)
  throw new Error('必须给 --total（总页数）')

const browser = await chromium.launch()
const page = await browser.newPage({ viewport: { width: 1280, height: 720 } })
// dark 只在 deck 的 colorSchema 不是 light 时生效；localStorage 是 Slidev 的官方开关
if (dark)
  await page.addInitScript(() => localStorage.setItem('slidev-color-schema', 'dark'))

const rows = []
for (let i = 1; i <= total; i++) {
  await page.goto('about:blank')
  await page.goto(`${base}/${i}`, { waitUntil: 'networkidle' })
  await page.waitForTimeout(wait)

  rows.push(await page.evaluate(({ i, extraSelectors }) => {
    // Slidev 在 DOM 里同时保留前后页，只有当前页有真实尺寸
    const layouts = [...document.querySelectorAll('.slidev-layout')]
    const layout = layouts.find(el => el.getBoundingClientRect().width > 0) || layouts[0]
    if (!layout)
      return { i, error: '没有 .slidev-layout' }

    const box = el => {
      const b = el.getBoundingClientRect()
      return { x: Math.round(b.x), y: Math.round(b.y), w: Math.round(b.width), h: Math.round(b.height), right: Math.round(b.right), bottom: Math.round(b.bottom) }
    }
    const slide = box(layout)
    const problems = []

    for (const el of layout.querySelectorAll('*')) {
      const cs = getComputedStyle(el)
      if (cs.display === 'none' || cs.visibility === 'hidden')
        continue
      const b = el.getBoundingClientRect()
      if (!b.width || !b.height)
        continue
      const cls = String(el.className || '').slice(0, 46)
      if (b.right > slide.right + 1 || b.bottom > slide.bottom + 1 || b.left < slide.x - 1)
        problems.push(`溢出 <${el.tagName.toLowerCase()} class="${cls}"> right=${Math.round(b.right - slide.x)}/${slide.w} bottom=${Math.round(b.bottom - slide.y)}/${slide.h}`)
      if (!el.children.length && el.scrollWidth > el.clientWidth + 2)
        problems.push(`被裁 <${el.tagName.toLowerCase()} class="${cls}"> scrollW=${el.scrollWidth} clientW=${el.clientWidth}`)
    }

    const h1 = layout.querySelector('h1')
    let heading = null
    if (h1) {
      const range = document.createRange()
      range.selectNodeContents(h1)
      const lines = [...range.getClientRects()].filter(r => r.height > 0).length
      heading = {
        text: h1.textContent.trim().slice(0, 22),
        fs: getComputedStyle(h1).fontSize,
        lines,
        h: Math.round(h1.getBoundingClientRect().height),
      }
      if (lines > 2)
        problems.push(`标题 ${lines} 行：${heading.text}`)
    }

    const footerEl = (layout.closest('.slidev-page') || document).querySelector('.deck-footer')
    const footer = !!footerEl && getComputedStyle(footerEl).display !== 'none' && footerEl.getBoundingClientRect().width > 0

    const extras = {}
    for (const sel of extraSelectors) {
      const el = layout.querySelector(sel)
      extras[sel] = el ? box(el) : null
    }

    return {
      i,
      layout: layout.className.replace('slidev-layout', '').trim() || 'default',
      slide,
      heading,
      footer,
      bg: getComputedStyle(layout).backgroundColor,
      color: getComputedStyle(layout).color,
      extras,
      problems,
    }
  }, { i, extraSelectors }))
}

await browser.close()

const bad = rows.filter(r => r.problems?.length)
for (const r of rows) {
  const h = r.heading ? `h1 ${r.heading.fs} ${r.heading.lines}行` : 'h1 —'
  const extra = Object.entries(r.extras || {})
    .filter(([, v]) => v)
    .map(([k, v]) => `${k}@${Math.round(v.x / r.slide.w * 100)}%,${Math.round(v.y / r.slide.h * 100)}% ${Math.round(v.w / r.slide.w * 100)}%×${Math.round(v.h / r.slide.h * 100)}%`)
    .join(' | ')
  console.log(`p${String(r.i).padStart(2)} ${r.layout.padEnd(26)} ${h}${dark ? `  bg ${r.bg}` : ''}${r.footer ? '  页脚' : ''}${extra ? `  ${extra}` : ''}`)
  for (const p of r.problems || [])
    console.log(`     ! ${p}`)
}
console.log(bad.length ? `\n✗ ${bad.length} 页有问题` : '\n✓ 无溢出')
process.exit(bad.length ? 1 : 0)
