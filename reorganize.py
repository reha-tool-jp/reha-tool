import re
import sys

with open('articles/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

header_end = html.find('<div class="section-title">')
footer_start = html.find('<div class="footer">')

if header_end == -1 or footer_start == -1:
    print('Could not find header or footer')
    sys.exit(1)

header = html[:header_end]
footer = html[footer_start:]
middle = html[header_end:footer_start]

cards = {}
pattern = re.compile(r'(<a class="article-card"\s+href="(.*?)">.*?</a>)', re.DOTALL)
for match in pattern.finditer(middle):
    card_html = match.group(1)
    filename = match.group(2)
    cards[filename] = card_html

if len(cards) != 24:
    print(f'Error: Found {len(cards)} cards, expected 24')
    sys.exit(1)

layout = [
    ('診療報酬改定(医療保険)', [
        'r8-kaitei-matome.html',
        'souki-reha-kazan.html',
        'kyujitsu-reha-kazan.html',
        'bedside-reha-gensam.html',
        'minashi-tani.html',
        'jisseki-shisu.html',
        'kangokyodo-kazan.html',
        'ict-8000man.html',
        'fim-scoring-tips.html',
        'fim-rida.html'
    ]),
    ('介護報酬改定(介護保険)', [
        'tosho-reha-keikakusho-mokuhyo.html',
        'houmon-reha-shogu-kaizen.html',
        'houmon-reha-station.html',
        'seikatsu-chouhyo.html',
        'kyoumi-chouhyo.html'
    ]),
    ('その他', [
        'semegata-yobou-iryo.html',
        'ai-riyou-guide.html',
        'pt-distribution.html',
        'jihi-riha-jisho-riha.html',
        'shogai-juyo.html',
        'tug-10m-kijunchi.html',
        'dementia-recovery.html',
        'toukatsu-chosei-shitsu.html',
        'giren.html'
    ])
]

new_middle = ''
for title, filenames in layout:
    new_middle += f'  <div class="section-title">{title}</div>\n\n'
    for fname in filenames:
        if fname not in cards:
            print(f'Error: Card for {fname} not found!')
            sys.exit(1)
        new_middle += cards[fname] + '\n\n'

new_html = header + new_middle + footer

with open('articles/index.html', 'w', encoding='utf-8') as f:
    f.write(new_html)

print('Reorganization complete!')
