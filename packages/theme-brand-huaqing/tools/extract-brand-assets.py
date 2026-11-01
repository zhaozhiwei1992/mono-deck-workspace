#!/usr/bin/env python3
"""从华青 PPT 模板提取品牌素材，并导出可复核的几何/颜色清单。

用途：模板改版后重新生成 assets/ 下的位图，不必手工在 PowerPoint 里另存。

依赖（不要装进系统 python，PEP 668 会拒）：
    python3 -m venv /tmp/pptxvenv
    /tmp/pptxvenv/bin/pip install python-pptx pillow
运行：
    /tmp/pptxvenv/bin/python tools/extract-brand-assets.py \
        --pptx ~/Documents/03-华青PPT模板-数字科技-2025-v1.0.pptx \
        --out assets --raw assets/_raw --report /tmp/huaqing-report.md

产出（assets/）：
    bg-cover.png        封面/尾页整幅底图（深蓝渐变 + 光效），16:9
    band-blue.png       章节页蓝色彩带（12.145×2.133in 原位图）
    logo-mark.png       白色书法标识（左上角用小图）
    logo-full.png       白色「华青 HUAQING」完整 logo（右上角）
    logo-mark-gold.png  金色徽标（封面中部 / 尾页）
    deco-ring.png       尾页左下圆环
    deco-ornament.png   尾页左下对称纹样
    _raw/               ppt/media 全量原图，便于回溯

脚本不写死文件名（image1/image16…），而是按「占版面的比例 + 宽高比 + 颜色」认图，
所以模板小改版后仍能跑；真换了版式请先看 --report 输出的清单再调阈值。
"""
from __future__ import annotations

import argparse
import io
import sys
from pathlib import Path

from PIL import Image
from pptx import Presentation

# 认定阈值：以版面比例为准，避免依赖 media 文件名
FULLBLEED = 0.985        # 宽/高都 ≥ 版面的 98.5% 视为整幅底图
BAND_W, BAND_H = 0.90, 0.26   # 彩带：宽 ≈ 91%、高 ≈ 28%
ASPECT_TOL = 0.06        # 宽高比容差（相对误差）

EMU_PER_INCH = 914400


def ratio(v, base):
    return (v / base) if v is not None and base else 0.0


def walk(shapes):
    """递归展开组合，产出所有 shape。"""
    for sh in shapes:
        yield sh
        if sh.shape_type == 6:  # GROUP
            yield from walk(sh.shapes)


def pictures(container, slide_w, slide_h):
    out = []
    for sh in walk(container.shapes):
        if sh.shape_type != 13:  # PICTURE
            continue
        try:
            blob = sh.image.blob
            im = Image.open(io.BytesIO(blob))
        except Exception:
            continue
        out.append({
            'name': sh.name,
            'w': ratio(sh.width, slide_w),
            'h': ratio(sh.height, slide_h),
            'left': ratio(sh.left, slide_w),
            'top': ratio(sh.top, slide_h),
            'px': im.size,
            'image': im,
            'blob': blob,
            'ext': (im.format or 'png').lower().replace('jpeg', 'jpg'),
        })
    return out


def near(value, target, tol=ASPECT_TOL):
    return abs(value - target) <= target * tol


def mean_rgb(im):
    # 缩到 64×64 再统计：够区分白/金，且避开 Pillow 13 的 getdata 弃用
    rgba = im.convert('RGBA').resize((64, 64))
    px = [tuple(rgba.getpixel((x, y))) for y in range(64) for x in range(64)]
    px = [p for p in px if p[3] > 200]
    if not px:
        return (0, 0, 0)
    n = len(px)
    return tuple(sum(p[i] for p in px) // n for i in range(3))


def pick_logo(pics, aspect, want_dark):
    """按宽高比找 logo，再用平均色区分白色/金色。"""
    cands = [p for p in pics if near(p['px'][0] / p['px'][1], aspect, 0.08)]
    if not cands:
        return None
    scored = []
    for p in cands:
        r, g, b = mean_rgb(p['image'])
        warm = r > g > b and (r - b) > 40          # 金色：R>G>B 且差距明显
        scored.append((warm == want_dark, p['px'][0] * p['px'][1], p))
    scored.sort(key=lambda t: (t[0], t[1]), reverse=True)
    return scored[0][2]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument('--pptx', required=True, type=Path)
    ap.add_argument('--out', required=True, type=Path)
    ap.add_argument('--raw', type=Path, default=None, help='原始 media 输出目录（默认 <out>/_raw）')
    ap.add_argument('--report', type=Path, default=None, help='输出 markdown 清单')
    args = ap.parse_args()

    if not args.pptx.exists():
        print(f'找不到 pptx: {args.pptx}', file=sys.stderr)
        return 2

    prs = Presentation(str(args.pptx))
    sw, sh = prs.slide_width, prs.slide_height
    args.out.mkdir(parents=True, exist_ok=True)
    raw = args.raw or (args.out / '_raw')
    raw.mkdir(parents=True, exist_ok=True)

    report = [f'# {args.pptx.name} 结构与素材清单', '',
              f'- 尺寸：{sw / EMU_PER_INCH:.3f} × {sh / EMU_PER_INCH:.3f} in（{len(prs.slides)} 页）', '']

    # 1) 原始 media 全量导出（只用于回溯）
    seen = set()
    for i, slide in enumerate(prs.slides, 1):
        for p in pictures(slide, sw, sh):
            key = (p['ext'], len(p['blob']))
            if key in seen:
                continue
            seen.add(key)
            (raw / f'slide{i:02d}-{p["name"].replace(" ", "_")}.{p["ext"]}').write_bytes(p['blob'])

    # 2) 按版面角色认图
    layout_pics = []
    for lay in prs.slide_layouts:
        layout_pics.extend(pictures(lay, sw, sh))
    slide_pics = []
    for i, slide in enumerate(prs.slides, 1):
        for p in pictures(slide, sw, sh):
            p['slide'] = i
            slide_pics.append(p)

    writes: dict[str, dict] = {}

    def take(target, pic):
        if pic is None:
            return
        im = pic['image']
        if target.endswith('.png'):
            out = im.convert('RGBA') if im.mode == 'RGBA' else im.convert('RGB')
            out.save(args.out / target, optimize=True)
        else:
            im.save(args.out / target)
        writes[target] = pic

    # 封面/尾页底图：layout 里 16:9 的整幅图（标题幻灯片）
    covers = [p for p in layout_pics if p['w'] >= FULLBLEED and p['h'] >= FULLBLEED]
    take('bg-cover.png', covers[0] if covers else None)

    # 章节页彩带：某页上 91%×28% 的图
    bands = [p for p in slide_pics if near(p['w'], BAND_W, 0.05) and near(p['h'], BAND_H, 0.12)]
    take('band-blue.png', bands[0] if bands else None)

    # logo：533×258（2.07:1）与 1175×482（2.44:1）
    take('logo-mark.png', pick_logo(layout_pics + slide_pics, 533 / 258, want_dark=False))
    take('logo-full.png', pick_logo(layout_pics + slide_pics, 1175 / 482, want_dark=False))
    take('logo-mark-gold.png', pick_logo(layout_pics + slide_pics, 533 / 258, want_dark=True))

    # 尾页装饰：512×512 圆环、512×476 纹样
    squares = [p for p in slide_pics if near(p['px'][1], p['px'][0], 0.02)]
    take('deco-ring.png', squares[0] if squares else None)
    rects = [p for p in slide_pics if near(p['px'][1], p['px'][0] * 0.93, 0.03)]
    take('deco-ornament.png', rects[0] if rects else None)

    report += ['## 输出', '', '| 文件 | 来源页/版式 | 版面占比（w×h） | 像素 |', '| --- | --- | --- | --- |']
    for name, p in writes.items():
        src = f"slide {p['slide']}" if 'slide' in p else 'layout'
        report.append(f"| {name} | {src} / {p['name']} | {p['w']:.3f} × {p['h']:.3f} | {p['px'][0]}×{p['px'][1]} |")
    missing = [n for n in ('bg-cover.png', 'band-blue.png', 'logo-mark.png', 'logo-full.png',
                           'logo-mark-gold.png', 'deco-ring.png', 'deco-ornament.png') if n not in writes]
    if missing:
        report += ['', f'> 未识别：{", ".join(missing)}（模板改版后请调阈值或手工另存）', '']

    # 3) 版式几何 + 实色清单（用于核对 brand.css 里的坐标与色值）
    report += ['', '## 版式几何', '', '| slide | layout | 形状 | 位置（占版面） | 尺寸（占版面） |', '| --- | --- | --- | --- | --- |']
    for i, slide in enumerate(prs.slides, 1):
        for p in pictures(slide, sw, sh):
            report.append(f"| {i} | {slide.slide_layout.name} | 图片 {p['name']} | "
                          f"{p['left']:.3f}, {p['top']:.3f} | {p['w']:.3f}×{p['h']:.3f} |")

    if args.report:
        args.report.parent.mkdir(parents=True, exist_ok=True)
        args.report.write_text('\n'.join(report), encoding='utf8')
        print(f'report → {args.report}')
    print(f'assets  → {args.out}')
    return 0 if not missing else 1


if __name__ == '__main__':
    raise SystemExit(main())
