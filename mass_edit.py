import os
import re

tools = [
    'balance-tool.html', 'bi-tool.html', 'fim-tool.html', 'hdsr-tool.html',
    'kihon-checklist.html', 'kyoumi-tool.html', 'santei-tool.html',
    'seikatsu-tool.html', 'walk-tool.html'
]

articles_dir = 'articles'
articles = [os.path.join(articles_dir, f) for f in os.listdir(articles_dir) if f.endswith('.html') and f != 'index.html']

all_files = tools + articles

for filepath in all_files:
    if not os.path.exists(filepath):
        print(f"Skipping {filepath}, not found")
        continue

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Update Global Nav
    nav_search = '<a href="/#tools">評価ツール</a>'
    nav_replace = '<a href="/#tools">評価ツール</a>\n    <a href="/about.html">このサイトについて</a>'
    if nav_search in content and nav_replace not in content:
        content = content.replace(nav_search, nav_replace)

    # Calculate relative path to about.html
    rel_path = '../about.html' if filepath.startswith('articles') else 'about.html'

    top_block = f'''
<div style="font-size:13px;color:var(--text2);margin-bottom:16px;padding-bottom:12px;border-bottom:1px solid var(--border);">
執筆・監修：理学療法士（臨床25年目）・認知症ケア専門士　|　<a href="{rel_path}" style="color:var(--accent);font-weight:700;text-decoration:none;">運営者について →</a>
</div>
'''

    bottom_block = f'''
<div style="background:var(--surface);border:1px solid var(--border);border-radius:var(--radius);padding:16px 20px;margin:24px 0;font-size:14px;color:var(--text2);line-height:1.8;">
この記事は、理学療法士（臨床25年目・認知症ケア専門士、病院リハビリテーション科長として勤務）が、臨床経験と厚生労働省等の一次資料をもとに執筆・監修しています。<br>
経歴の詳細はこちら → <a href="{rel_path}" style="color:var(--accent);font-weight:700;text-decoration:none;">運営者について</a>
</div>
'''

    # 2. Insert Top Block
    # Look for </header> and insert after the breadcrumb or inside container.
    # A safe place is right before <div class="article-body"> OR right after <div class="breadcrumb">...</div>.
    # Some tool pages might not have article-body.
    # Let's insert it immediately after the breadcrumb closing div.
    # Breadcrumb format: <div class="breadcrumb"> ... </div>
    # Using regex to find the breadcrumb div and insert after it.
    if top_block.strip() not in content:
        breadcrumb_match = re.search(r'(<div class="breadcrumb">.*?</div>)', content, flags=re.DOTALL)
        if breadcrumb_match:
            content = content[:breadcrumb_match.end()] + "\n" + top_block.strip() + "\n" + content[breadcrumb_match.end():]
        else:
            print(f"Breadcrumb not found in {filepath}!")

    # 3. Insert Bottom Block
    if bottom_block.strip() not in content:
        # Find the earliest of: <div class="references">, <div class="related-section">, <div class="footer">
        refs_idx = content.find('<div class="references">')
        related_idx = content.find('<div class="related-section">')
        footer_idx = content.find('<div class="footer">')
        
        candidates = [idx for idx in [refs_idx, related_idx, footer_idx] if idx != -1]
        if candidates:
            insert_idx = min(candidates)
            content = content[:insert_idx] + bottom_block.strip() + "\n\n  " + content[insert_idx:]
        else:
            print(f"Could not find insertion point for bottom block in {filepath}!")

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Done")
