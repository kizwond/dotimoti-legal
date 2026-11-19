#!/usr/bin/env python3
"""Render public Moti policies exported from the actual Android runtime; no duplicate translations."""
import argparse,json,re
from pathlib import Path
from build_privacy import ROOT,LANGUAGES,LANGUAGE_LABELS,article,app_navigation,e
BASE='https://kizwond.github.io/dotimoti-legal/dotimoti/privacy/'

def render(language, source):
    code,path,name,title,_=language
    assert source['language']==code and source['publicUrl']==BASE+path
    assert re.fullmatch(r'\d{4}-\d{2}-\d{2}',source['effectiveDate'])
    assert len(source['sections'])==20
    nav=''.join(f'<a href="{BASE}{p}" lang="{c}" hreflang="{c}"'+(' aria-current="page"' if c==code else '')+f'>{e(n)}</a>' for c,p,n,_,_ in LANGUAGES)
    alternates=''.join(f'<link rel="alternate" hreflang="{c}" href="{BASE}{p}">' for c,p,_,_,_ in LANGUAGES)
    content=article(code,source['sections'],expected=20)
    return f'''<!doctype html>
<html lang="{code}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>DotiMoti · {e(title)}</title><link rel="canonical" href="{BASE}{path}">{alternates}
<link rel="alternate" hreflang="x-default" href="{BASE}">
<style>
*{{box-sizing:border-box}}body{{margin:0;background:#f5f8fb;color:#183444;font-family:system-ui,-apple-system,"Segoe UI",sans-serif;line-height:1.8;overflow-wrap:anywhere}}main{{max-width:920px;margin:auto;padding:32px 20px 64px}}header{{border-bottom:1px solid #d7e1e9;padding-bottom:24px}}h1{{font-size:clamp(28px,6vw,44px);line-height:1.25;letter-spacing:-.03em}}h2{{font-size:22px;margin:32px 0 12px;line-height:1.45}}p,li{{font-size:16px}}p{{margin:0 0 14px}}ul{{padding-left:22px}}nav{{display:flex;flex-wrap:wrap;gap:8px 16px;margin:12px 0}}a{{color:#285575}}a[aria-current]{{font-weight:800;text-decoration-thickness:3px;text-underline-offset:6px}}.muted,footer{{color:#536b7c}}footer{{border-top:1px solid #d7e1e9;margin-top:40px;padding-top:20px}}a:focus-visible{{outline:3px solid #f47a2b;outline-offset:4px}}
</style></head><body><main><header><p class="muted">DotiMoti · opensky</p><h1>{e(title)}</h1><p><time datetime="{source['effectiveDate']}">{source['effectiveDate']}</time></p><p class="muted">DotiMoti · Play: com.opensky.dotimoti · Preview: com.dotimoti.app.next</p>{app_navigation('dotimoti',path)}<nav aria-label="{e(LANGUAGE_LABELS[code])}">{nav}</nav></header>
{content}
<footer><p>© opensky · <a href="mailto:eonseok.yoon@opensky.co.kr">eonseok.yoon@opensky.co.kr</a></p><a href="{e(source['deletionUrl'])}">{e(source['deletionLabel'])}</a> · <a href="https://kizwond.github.io/dotimoti-legal/dotimoti/child-safety/">Child Safety · 아동 안전 기준</a></footer></main></body></html>
'''

def main():
    p=argparse.ArgumentParser();p.add_argument('--check',action='store_true');args=p.parse_args()
    for language in LANGUAGES:
        source=json.loads((ROOT/'policy/dotimoti'/f'{language[0]}.json').read_text())
        target=ROOT/'dotimoti/privacy'/language[1]/'index.html';rendered=render(language,source)
        if args.check:assert target.read_text()==rendered,str(target)+' is stale'
        else:target.parent.mkdir(parents=True,exist_ok=True);target.write_text(rendered)
    print('Moti: verified 7 runtime policies' if args.check else 'Moti: rendered 7 runtime policies')
if __name__=='__main__':main()
