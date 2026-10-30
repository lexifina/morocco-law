import re, json, hashlib, pymupdf, os
HERE = os.path.dirname(os.path.abspath(__file__))
PDF = os.path.join(HERE, '.cache', 'adala_constitution.pdf')
sha = hashlib.sha256(open(PDF,'rb').read()).hexdigest()
d = pymupdf.open(PDF)
blocks = []
for p in d:
    for b in sorted(p.get_text('blocks'), key=lambda b: (round(b[1]), b[0])):
        t = b[4].replace('\xa0', ' ').replace('', '').replace('', '')
        t = re.sub(r'\s*\n\s*', ' ', t); t = re.sub(r' +', ' ', t).strip()
        if not t or re.fullmatch(r'-\s*\d+\s*-', t): continue
        blocks.append(t)
# merge blocks split by a page break: previous does not end a sentence and next starts lowercase
merged = []
for t in blocks:
    if merged and not re.search(r'[.;:!?»)]$', merged[-1]) and t[:1].islower() and not re.match(r'^(Article|TITRE)', merged[-1]):
        merged[-1] += ' ' + t
    else: merged.append(t)
start = next(i for i,t in enumerate(merged) if t.startswith('Préambule') or t.upper() == 'PREAMBULE' or t.upper() == 'PRÉAMBULE')
pre_blocks = merged[:start]
body = merged[start:]
units = {}
cur = 'preambule'; label = 'Préambule'
texts = {cur: []}
labels = {cur: (label, 'preamble')}
order = [cur]
for t in body[1:]:
    m = re.fullmatch(r'Article (premier|\d+)', t)
    if m:
        n = 1 if m.group(1) == 'premier' else int(m.group(1))
        cur = 'art-%03d' % n; texts[cur] = []; labels[cur] = ('Article %s' % ('premier' if n == 1 else n), 'art'); order.append(cur)
    elif re.match(r'^TITRE ', t) or re.match(r'^TITRE', t):
        # structural heading: skip (also skip a continuation line)
        continue
    elif t.isupper() and len(t) < 80 and cur != 'preambule':
        continue
    else:
        texts[cur].append(t)
for k in order:
    lab, kind = labels[k]
    head = lab
    units[k] = {'label': lab, 'kind': kind, 'text': '# %s\n' % head + '\n'.join(texts[k]) + '\n'}
nums = [int(k[4:]) for k in order if k.startswith('art-')]
assert nums == list(range(1, 181)), nums
# dahir of promulgation
dahir = [t for t in pre_blocks if t.strip()]
print(len(units)); print(units['art-006']['text'][:600]); print(units['preambule']['text'][:300])
URL = 'https://adala.justice.gov.ma/'
corpus = {
 'country': {'code':'MA','name':'Morocco','slug':'morocco','lang':'fr','tz':'Africa/Casablanca','future_branch':'futur',
   'publisher': {'name':'Ministère de la Justice du Royaume du Maroc (Adala)','email':'adala@justice.gov.ma.invalid'},
   'default_in_force_rule': {'text':'The Constitution of 2011 took effect on publication in the Bulletin officiel n° 5964 bis of 30 July 2011, as promulgated by Dahir n° 1-11-91','source':'https://adala.justice.gov.ma/'},
   'licence_note':'Texte de la Constitution du Royaume du Maroc, version française publiée par le Ministère de la Justice (adala.justice.gov.ma).'},
 'sources':[{'name':'Ministère de la Justice, portail Adala (La Constitution, version française)','url':URL,'retrieved':'2026-10-28','requests':1,'licence':'Official text of the Constitution published by the Moroccan Ministry of Justice; no licence statement found','notes':'58-page text-layer PDF, French version of the Constitution promulgated by Dahir n° 1-11-91 of 29 July 2011. The Arabic text is the authoritative one.'}],
 'laws': {'dahir-1-11-91': {'label':'Dahir n° 1-11-91','title':'Dahir n° 1-11-91 du 27 chaabane 1432 (29 juillet 2011) portant promulgation du texte de la Constitution','kind':'decree','enacted':'2011-07-29','published':'2011-07-30','url':URL,'temporary_until':None,'restores':None,'note':None}},
 'acts':[{'slug':'constitution','short':'Const.','title':'Constitution du Royaume du Maroc (2011)','url':URL,'first_law':'dahir-1-11-91','earlier_laws':[],
   'versions':[{'from':'2011-07-30','source_url':URL,'sha256':sha,'units':units,'credits':{},'note':'The Constitution as adopted by referendum on 1 July 2011 and promulgated on 29 July 2011; it has not been amended since. French version published by the Ministry of Justice.'}]}],
 'applies':[],
 'decisions':['The Constitution has no later amendment, so the repository holds one version, the Constitution as promulgated, dated 2011-07-30, the day it appeared in the Bulletin officiel (n° 5964 bis); the dahir of promulgation is dated 2011-07-29.',
   'The French text is used because the Ministry of Justice portal publishes it as a text-layer PDF; the Arabic text is the authoritative one and was not available as text.',
   'Page numbers and title headings (TITRE ...) were removed; the promulgation dahir is not a unit.'],
 'ai_use':['none']}
json.dump(corpus, open(os.path.join(HERE,'corpus.json'),'w',encoding='utf-8'), ensure_ascii=False, indent=1)
