# vendor 说明

本目录记录从上游 Slidev 官方主题拷贝来的代码，便于升级时对比。

| 文件 | 上游 | 版本 | 许可证 | 改动 |
|---|---|---|---|---|
| `../layoutHelper.ts` | `@slidev/theme-default` | 0.25.0 | MIT (c) Anthony Fu | 加显式 `CSSProperties` 类型标注；行为等价 |

## 未 vendor 的内容与原因

- `styles/prism.css`：Slidev 53 默认 shiki 高亮，prism 变量已失效。
- 官方 `cover/section/statement/fact/quote` 的 `.vue`：模板只有一层 `<slot />`，价值全在 CSS；已在 `../layout.css` 里用 `--deck-*` token 重写，因此不再重复拷贝。
- `styles/layouts-base.css`：不拷贝，直接 `import '@slidev/client/styles/layouts-base.css'`，跟随 Slidev 版本演进。

## 升级检查清单

1. 升级 `@slidev/cli` 后，对比 `node_modules/.pnpm/@slidev+client*/node_modules/@slidev/client/layoutHelper.ts` 与本地版本。
2. 对比 `@slidev/client/styles/layouts-base.css` 是否有新增的 `.slidev-layout.xxx` 选择器（新增布局可能需要补样式）。
3. 跑 `pnpm --filter slidev-theme-base build` 与 `pnpm --filter deck-demo-base build`。
