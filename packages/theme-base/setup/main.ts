import { configs } from '@slidev/client'

/**
 * 把 headmatter 的 `palette` 落成 `<html data-palette="red">`。
 *
 * - 为什么不用官方的 `htmlAttrs: { 'data-palette': red }`：让 deck 只写一行 `palette: red`，
 *   不必记 htmlAttrs 的嵌套写法；两者等价，任选其一。
 * - 为什么用 data 属性而不是 class：暗色由 client 直接 `html.classList.toggle('dark')` 改 DOM
 *   （见 @slidev/client 的 logic/dark.ts），共用 class 属性会互相覆盖。
 *
 * 执行时机：client 在挂载前 await 所有 setup（setup/main.ts 的 setups 循环），所以不会闪色。
 */
export default function setupPalette() {
  const palette = (configs as unknown as Record<string, unknown>).palette
  if (typeof palette === 'string' && palette && typeof document !== 'undefined')
    document.documentElement.dataset.palette = palette
}
