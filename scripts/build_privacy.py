#!/usr/bin/env python3
"""Render the seven approved offline policy mirrors. No network or user data."""
import argparse
import html
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BASE = 'https://kizwond.github.io/dotimoti-legal/dotidoit/privacy/'
LANGUAGES = [
    ('ko', '', '한국어', '개인정보처리방침', '시행일: 2026년 11월 2일'),
    ('en', 'en/', 'English', 'Privacy Policy', 'Effective November 2, 2026'),
    ('ja', 'ja/', '日本語', 'プライバシーポリシー', '施行日：2026年11月2日'),
    ('zh-Hans', 'zh-hans/', '简体中文', '隐私政策', '生效日期：2026年11月2日'),
    ('zh-Hant', 'zh-hant/', '繁體中文', '隱私權政策', '生效日期：2026年11月2日'),
    ('es', 'es/', 'Español', 'Política de privacidad', 'En vigor desde el 2 de noviembre de 2026'),
    ('vi', 'vi/', 'Tiếng Việt', 'Chính sách quyền riêng tư', 'Có hiệu lực ngày 2 tháng 11 năm 2026'),
]
LANGUAGE_LABELS = {'ko':'언어','en':'Language','ja':'言語','zh-Hans':'语言','zh-Hant':'語言','es':'Idioma','vi':'Ngôn ngữ'}
e = html.escape

def article(code, sections):
    assert len(sections) == 14, (code, 'expected fourteen sections')
    result = f'<article id="{code}" lang="{code}">'
    for section in sections:
        result += '<section><h2>' + e(section['title']) + '</h2>'
        result += ''.join('<p>' + e(p) + '</p>' for p in section['paragraphs'])
        if section['bullets']:
            result += '<ul>' + ''.join('<li>' + e(p) + '</li>' for p in section['bullets']) + '</ul>'
        result += '</section>\n'
    return result + '</article>'

def render(language, sources):
    code, path, name, title, effective = language
    nav = ''.join(f'<a href="{BASE}{p}" lang="{c}" hreflang="{c}"' + (' aria-current="page"' if c == code else '') + f'>{e(n)}</a>' for c,p,n,_,_ in LANGUAGES)
    alternates = ''.join(f'<link rel="alternate" hreflang="{c}" href="{BASE}{p}">' for c,p,_,_,_ in LANGUAGES)
    content = article(code, sources[code])
    # Preserve the historic root #ko and #en anchors used by existing installations/bookmarks.
    if code == 'ko':
        content += '<div class="divider"><h2>English · Privacy Policy</h2></div>' + article('en', sources['en'])
    return f'''<!doctype html>
<html lang="{code}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>DotiDoit · {e(title)}</title><link rel="canonical" href="{BASE}{path}">{alternates}
<link rel="alternate" hreflang="x-default" href="{BASE}">
<style>
*{{box-sizing:border-box}}body{{margin:0;background:#fbfdfc;color:#17202f;font-family:system-ui,-apple-system,"Segoe UI",sans-serif;line-height:1.75;overflow-wrap:anywhere}}main{{max-width:920px;margin:auto;padding:40px 20px 72px}}header,footer{{border-bottom:1px solid #e4e7ec;padding-bottom:24px;margin-bottom:28px}}h1{{font-size:clamp(30px,6vw,54px);line-height:1.2;letter-spacing:-.03em}}h2{{font-size:24px;margin:32px 0 12px;line-height:1.4}}p,li{{font-size:16px}}p{{margin:0 0 14px}}ul{{padding-left:22px}}nav{{display:flex;flex-wrap:wrap;gap:8px 16px}}a{{color:#115e59}}a[aria-current]{{font-weight:800}}.muted,footer{{color:#667085}}.divider{{border-top:1px solid #e4e7ec;margin-top:52px;padding-top:20px}}footer{{border-top:1px solid #e4e7ec;border-bottom:0;margin-top:40px;padding-top:20px}}
</style></head><body><main><header><p class="muted">DotiDoit · opensky</p><h1>{e(title)}</h1><p>{e(effective)}</p><nav aria-label="{e(LANGUAGE_LABELS[code])}">{nav}</nav></header>
{content}
<footer>© opensky · <a href="mailto:eonseok.yoon@opensky.co.kr">eonseok.yoon@opensky.co.kr</a></footer></main></body></html>
'''

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    sources = {code: json.loads((ROOT/'policy'/f'{code}.json').read_text()) for code,_,_,_,_ in LANGUAGES}
    for language in LANGUAGES:
        output = ROOT/'dotidoit/privacy'/language[1]/'index.html'
        rendered = render(language, sources)
        if args.check:
            assert output.read_text() == rendered, str(output) + ' is out of date'
        else:
            output.parent.mkdir(parents=True, exist_ok=True)
            output.write_text(rendered)
    print('Verified seven policies, 14 sections each, and legacy root anchors' if args.check else 'Rendered seven policies')

if __name__ == '__main__': main()
