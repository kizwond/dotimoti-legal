#!/usr/bin/env python3
"""Render the seven approved offline policy mirrors. No network or user data."""
import argparse
import html
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BASE = 'https://kizwond.github.io/dotimoti-legal/dotidoit/privacy/'
LANGUAGES = [
    ('ko', '', '한국어', '개인정보처리방침', '시행일: 2026년 11월 10일'),
    ('en', 'en/', 'English', 'Privacy Policy', 'Effective November 10, 2026'),
    ('ja', 'ja/', '日本語', 'プライバシーポリシー', '施行日：2026年11月10日'),
    ('zh-Hans', 'zh-hans/', '简体中文', '隐私政策', '生效日期：2026年11月10日'),
    ('zh-Hant', 'zh-hant/', '繁體中文', '隱私權政策', '生效日期：2026年11月10日'),
    ('es', 'es/', 'Español', 'Política de privacidad', 'En vigor desde el 10 de noviembre de 2026'),
    ('vi', 'vi/', 'Tiếng Việt', 'Chính sách quyền riêng tư', 'Có hiệu lực ngày 10 tháng 11 năm 2026'),
]
LANGUAGE_LABELS = {'ko':'언어','en':'Language','ja':'言語','zh-Hans':'语言','zh-Hant':'語言','es':'Idioma','vi':'Ngôn ngữ'}
NOTICES = {
    'ko': '광고가 포함된 도티두잇 버전에 적용되는 방침입니다. 기존 광고 없는 버전은 광고 SDK를 포함하지 않습니다.',
    'en': 'This policy covers DotiDoit versions with advertising. Existing ad-free versions do not include the advertising SDK.',
    'ja': '広告を含むDotiDoitの版に適用されるポリシーです。既存の広告なしの版には広告SDKは含まれません。',
    'zh-Hans': '本政策适用于包含广告的DotiDoit版本。现有无广告版本不包含广告SDK。',
    'zh-Hant': '本政策適用於包含廣告的DotiDoit版本。現有無廣告版本不包含廣告SDK。',
    'es': 'Esta política cubre las versiones de DotiDoit con publicidad. Las versiones existentes sin anuncios no incluyen el SDK publicitario.',
    'vi': 'Chính sách này áp dụng cho các phiên bản DotiDoit có quảng cáo. Các phiên bản không quảng cáo hiện có không chứa SDK quảng cáo.',
}
e = html.escape

def article(code, sections):
    assert len(sections) == 15, (code, 'expected fifteen sections')
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
</style></head><body><main><header><p class="muted">DotiDoit · opensky</p><h1>{e(title)}</h1><p>{e(effective)}</p><p>{e(NOTICES[code])}</p><nav aria-label="{e(LANGUAGE_LABELS[code])}">{nav}</nav></header>
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
    print('Verified seven policies, 15 sections each, and legacy root anchors' if args.check else 'Rendered seven policies')

if __name__ == '__main__': main()
