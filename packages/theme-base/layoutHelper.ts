// vendored from @slidev/theme-default@0.25.0 (MIT, (c) Anthony Fu) — modified
import type { CSSProperties } from 'vue'

/**
 * Resolve urls from frontmatter and append with the base url
 */
export function resolveAssetUrl(url: string) {
  if (url.startsWith('/'))
    return import.meta.env.BASE_URL + url.slice(1)
  return url
}

export interface DeckFrontmatter {
  [key: string]: unknown
}

/**
 * 布局取文本的统一入口。
 *
 * Slidev 会把保留字段从布局 props 里剔除（`title` 每页都剔，`author` 等 headmatter 字段
 * 在首页剔除，见 @slidev/client 的 `frontmatterToProps`），所以这类字段只能从 Slidev
 * 透传的 `frontmatter` prop 上取；非保留字段仍然可以直接读 props。
 */
export function useDeckText<T extends object>(props: T & { frontmatter?: DeckFrontmatter }) {
  return (key: string, fallback = ''): string => {
    const frontmatter = props.frontmatter || {}
    const value = frontmatter[key] ?? (props as unknown as DeckFrontmatter)[key]
    return typeof value === 'string' && value ? value : fallback
  }
}

export function handleBackground(background?: string, dim = false, backgroundSize = 'cover'): CSSProperties {
  const isColor = background && (background[0] === '#' || background.startsWith('rgb'))

  const style: CSSProperties = {
    background: isColor ? background : undefined,
    color: (background && !isColor) ? 'white' : undefined,
    backgroundImage: isColor
      ? undefined
      : background
        ? dim
          ? `linear-gradient(#0005, #0008), url(${resolveAssetUrl(background)})`
          : `url("${resolveAssetUrl(background)}")`
        : undefined,
    backgroundRepeat: 'no-repeat',
    backgroundPosition: 'center',
    backgroundSize,
  }

  if (!style.background)
    delete style.background

  return style
}
