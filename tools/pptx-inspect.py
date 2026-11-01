#!/usr/bin/env python3
"""盘点任意 pptx：版式、形状几何（占版面%）、填充、图片清单与「该不该用位图」的初判。

用途：接到一份新 PPT 时，先跑这个，再决定「哪些页用原图、哪些页用 CSS、要做几个 layout」。
不做命名判断、不写死任何模板的名字——只给事实和启发式建议。

依赖（系统 python 受 PEP 668 管理，必须用 venv）：
    python3 -m venv /tmp/pptxvenv
    /tmp/pptxvenv/bin/pip install python-pptx pillow
运行：
    /tmp/pptxvenv/bin/python tools/pptx-inspect.py deck.pptx --out /tmp/report.md [--with-text]

读法（详见 02_通用设计/04_品牌层接入流程.org）：
- coverage ≈ 1.0 的图 → 整页底图候选，通常「保留原图」
- coverage 0.05~0.4 且宽高比 != 1 的图 → 彩带 / 面板 / 装饰，按「能否用 CSS 还原」取舍
- smooth 很小（相邻像素平均梯度 < 0.5）→ 基本是渐变/纯色，CSS 可无损重画
- smooth 大（> 2）→ 有纹理/照片，用原图
"""
from __future__ import annotations

import argparse
import hashlib
import io
import sys
from pathlib import Path

from PIL import Image
from pptx import Presentation

EMU_PER_INCH = 914400
TYPE_NAMES = {1: 'AUTO', 3: 'CHART', 5: 'FREEFORM', 6: 'GROUP', 9: 'LINE', 13: 'PICTURE', 14: 'PLACEHOLDER', 17: 'TEXTBOX'}


def pct(v, base):
    return 0.0 if v is None or not base else v / base


def walk(shapes):
    for sh in shapes:
        yield sh
        if sh.shape_type == 6:
            yield from walk(sh.shapes)


def fill_desc(shape):
    try:
        f = shape.fill
        t = f.type
    except Exception:
        return ''
    if t is None:
        return ''
    s = str(t)
    if s.startswith('SOLID'):
        try:
            c = f.fore_color
            return f'#{c.rgb}' if c.type == 1 else f'theme:{c.theme_color}'
        except Exception:
            return 'solid'
    if s.startswith('GRADIENT'):
        stops = []
        try:
            for st in f.gradient_stops:
                try:
                    stops.append(f'{st.position:.2f}:{getattr(st.color, "rgb", None)}')
                except Exception:
                    stops.append('?')
            ang = f.gradient_angle
        except Exception:
            ang = '?'
        return f'grad({ang}) ' + ' | '.join(stops)
    if s.startswith('PICTURE'):
        return 'picture-fill'
    return s


def line_desc(shape):
    try:
        ln = shape.line
        if not ln.fill.type:
            return ''
        c = ln.color
        col = f'#{c.rgb}' if c.type == 1 else f'theme:{c.theme_color}'
        return f'line {col} {ln.width.pt if ln.width else "?"}pt'
    except Exception:
        return ''


def flatten(im, bg=(128, 128, 128)):
    """透明图先压到中灰上再做统计，否则「白 logo + 透明底」会被当成纯色。"""
    if im.mode in ('RGBA', 'LA', 'P'):
        im = im.convert('RGBA')
        canvas = Image.new('RGB', im.size, bg)
        canvas.paste(im, mask=im.split()[-1])
        return canvas
    return im.convert('RGB')


def smoothness(im):
    """相邻像素平均绝对差：越小越像纯色/渐变。"""
    g = flatten(im).convert('L').resize((160, 160))
    px = list(g.tobytes())
    w = 160
    dx = sum(abs(px[y * w + x] - px[y * w + x + 1]) for y in range(160) for x in range(w - 1)) / (160 * 159)
    return dx


def hint_for(cov, sm, aspect):
    """位图/CSS 初判：先看它占版面多大（角色），再看它有多「不光滑」（可否用 CSS 还原）。"""
    if cov > .9:
        return '整页底图但近乎纯色：CSS 可重画（省体积、能跟暗色）' if sm < .5 else '整页底图：保留原图'
    if cov >= .05:
        if sm < .5:
            return '彩带/面板，纯渐变：CSS 重画'
        if sm < 1.5:
            return '彩带/面板，轻纹理：CSS 渐变可近似'
        return '彩带/面板，有纹理：保留原图'
    if 0.8 <= aspect <= 3.2:
        return '标识/图标：保留原图（要矢量得另行矢量化）'
    return '装饰件：CSS 可近似' if sm < 1.5 else '装饰件：保留原图'


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument('pptx', type=Path)
    ap.add_argument('--out', type=Path, default=None, help='markdown 输出（默认 stdout）')
    ap.add_argument('--with-text', action='store_true', help='额外打印每段文字的字号/字体（多数情况不需要）')
    ap.add_argument('--raw', type=Path, default=None, help='把 media 原图导出到这个目录')
    args = ap.parse_args()

    if not args.pptx.exists():
        print(f'找不到 {args.pptx}', file=sys.stderr)
        return 2

    prs = Presentation(str(args.pptx))
    sw, sh = prs.slide_width, prs.slide_height
    out: list[str] = []
    A = out.append

    A(f'# {args.pptx.name}')
    A('')
    A(f'- 版面：{sw / EMU_PER_INCH:.3f} × {sh / EMU_PER_INCH:.3f} in'
      f'（{sw / 914400 * 96:.0f} × {sh / 914400 * 96:.0f} px @96dpi，宽高比 {sw / sh:.3f}）')
    A(f'- 页数：{len(prs.slides)}；版式：{len(prs.slide_layouts)}')
    A('')
    A('## 版式清单')
    A('')
    A('| # | 版式名 | 形状数 | 图片数 | 备注 |')
    A('| --- | --- | --- | --- | --- |')
    for i, lay in enumerate(prs.slide_layouts, 1):
        shapes = list(walk(lay.shapes))
        pics = [s for s in shapes if s.shape_type == 13]
        full = [p for p in pics if pct(p.width, sw) > .95 and pct(p.height, sh) > .95]
        note = '含整页底图' if full else ('含图' if pics else '—')
        A(f'| {i} | {lay.name} | {len(shapes)} | {len(pics)} | {note} |')

    A('')
    A('## 每页形状（坐标/尺寸为占版面比例）')
    for i, slide in enumerate(prs.slides, 1):
        A('')
        A(f'### slide {i} — {slide.slide_layout.name}')
        A('')
        A('| 类型 | 名称 | x,y,w,h | 填充 | 文字 |')
        A('| --- | --- | --- | --- | --- |')
        for s in walk(slide.shapes):
            text = ''
            if getattr(s, 'has_text_frame', False):
                text = ' / '.join(p.text for p in s.text_frame.paragraphs if p.text.strip())[:48].replace('|', '/')
                if args.with_text and text:
                    sizes = sorted({round(r.font.size.pt, 1) for p in s.text_frame.paragraphs for r in p.runs if r.font.size})
                    text += f' ⟨{sizes}pt⟩' if sizes else ''
            geo = f'{pct(s.left, sw):.3f},{pct(s.top, sh):.3f},{pct(s.width, sw):.3f},{pct(s.height, sh):.3f}'
            fill = ' '.join(x for x in (fill_desc(s), line_desc(s)) if x)
            A(f"| {TYPE_NAMES.get(s.shape_type, s.shape_type)} | {s.name} | {geo} | {fill} | {text} |")

    # 图片清单（按内容去重）
    A('')
    A('## 图片清单（去重，按版面覆盖率排序）')
    A('')
    A('| 像素 | 宽高比 | 最大覆盖率 | 平滑度 | 平均色 | 出现位置 | 初判 |')
    A('| --- | --- | --- | --- | --- | --- | --- |')
    seen: dict[tuple, dict] = {}
    raw = args.raw
    if raw:
        raw.mkdir(parents=True, exist_ok=True)
    containers = [(f'L{n}', lay) for n, lay in enumerate(prs.slide_layouts, 1)]
    containers += [(f's{n}', sl) for n, sl in enumerate(prs.slides, 1)]
    for label, container in containers:
        for s in walk(container.shapes):
            if s.shape_type != 13:
                continue
            try:
                blob = s.image.blob
                im = Image.open(io.BytesIO(blob))
            except Exception:
                continue
            key = hashlib.md5(blob).hexdigest()
            cov = pct(s.width, sw) * pct(s.height, sh)
            rec = seen.setdefault(key, {'im': im, 'cov': 0.0, 'where': []})
            rec['cov'] = max(rec['cov'], cov)
            if len(rec['where']) < 4 and label not in rec['where']:
                rec['where'].append(label)
            if raw:
                (raw / f'image-{im.size[0]}x{im.size[1]}-{len(blob)}.{ (im.format or "png").lower() }').write_bytes(blob)
    for rec in sorted(seen.values(), key=lambda r: -r['cov']):
        im = rec['im']
        sm = smoothness(im)
        rgb = flatten(im).resize((1, 1)).getpixel((0, 0))
        hint = hint_for(rec['cov'], sm, im.size[0] / im.size[1])
        A(f"| {im.size[0]}×{im.size[1]} | {im.size[0] / im.size[1]:.2f} | {rec['cov']:.2f} | {sm:.2f} "
          f"| #{rgb[0]:02x}{rgb[1]:02x}{rgb[2]:02x} | {' '.join(rec['where'])} | {hint} |")

    if args.out:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text('\n'.join(out) + '\n', encoding='utf8')
        print(f'→ {args.out}')
    else:
        print('\n'.join(out))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
