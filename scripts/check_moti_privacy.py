#!/usr/bin/env python3
"""Compare public article text to runtime exports and verify direct, app-specific language links."""
import json
from html.parser import HTMLParser
from build_privacy import ROOT,LANGUAGES,render as render_doit
from build_moti_privacy import render as render_moti,BASE

class Articles(HTMLParser):
    def __init__(self):super().__init__();self.current=None;self.section=None;self.capture=None;self.parts=[];self.articles={};self.links=[]
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if tag=='a':self.links.append(a)
        if tag=='article':self.current=a['id'];self.articles[self.current]=[]
        if self.current and tag=='section':self.section={'title':'','paragraphs':[],'bullets':[]}
        if self.section is not None and tag in ('h2','p','li'):self.capture=tag;self.parts=[]
    def handle_data(self,data):
        if self.capture:self.parts.append(data)
    def handle_endtag(self,tag):
        if tag==self.capture:
            t=''.join(self.parts)
            if tag=='h2':self.section['title']=t
            else:self.section['paragraphs' if tag=='p' else 'bullets'].append(t)
            self.capture=None
        if tag=='section' and self.section is not None:self.articles[self.current].append(self.section);self.section=None
        if tag=='article':self.current=None

sources={code:json.loads((ROOT/'policy'/f'{code}.json').read_text()) for code,*_ in LANGUAGES}
for language in LANGUAGES:
    code,path,*_=language
    for app in ['dotidoit','dotimoti']:
        raw=(ROOT/app/'privacy'/path/'index.html').read_text();parser=Articles();parser.feed(raw)
        if code=='ko':assert '공인미션' not in raw and '공식미션' in raw,(app,'obsolete official-mission wording')
        if app=='dotimoti':
            source=json.loads((ROOT/'policy/dotimoti'/f'{code}.json').read_text())
            assert raw==render_moti(language,source)
            assert parser.articles[code]==source['sections'],(code,'Moti text drift')
            assert source['publicUrl']==BASE+path and isinstance(source['versionCode'], int) and source['versionCode'] > 0
            assert not any('ZIP' in s for s in source['sections'][8]['paragraphs'])
            assert source['deletionUrl'] in [a.get('href') for a in parser.links]
        else:
            assert raw==render_doit(language,sources)
            assert parser.articles[code]==sources[code],(code,'Doit policy changed')
            if code=='ko':assert parser.articles['en']==sources['en']
        for target in ['dotidoit','dotimoti']:
            url=f'https://kizwond.github.io/dotimoti-legal/{target}/privacy/{path}'
            assert url in [a.get('href') for a in parser.links],(app,code,target)
        assert '<script' not in raw
print('PASS 7 Moti runtime articles + 7 unchanged Doit articles, direct app/language navigation, legacy root English and deletion links')
