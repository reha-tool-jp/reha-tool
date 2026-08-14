import os
import re

directory = 'articles'
# Exclude the 8 files already processed or being processed
exclude = {
    'index.html', 
    'shogai-juyo.html', 'jihi-riha-jisho-riha.html', 'kangokyodo-kazan.html', 'toukatsu-chosei-shitsu.html',
    'ai-riyou-guide.html', 'bedside-reha-gensam.html', 'fim-rida.html', 'jisseki-shisu.html'
}

files = [f for f in os.listdir(directory) if f.endswith('.html') and f not in exclude]

print("Remaining 16 files survey:\n")
for f in sorted(files):
    path = os.path.join(directory, f)
    with open(path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # 1. Check for .site-name a
    site_name_match = re.search(r'<div class="site-name">(.*?)</div>', content)
    has_link = False
    if site_name_match:
        inner = site_name_match.group(1)
        if '<a ' in inner:
            has_link = True
            
    # 2. Check for other unique CSS in header
    style_match = re.search(r'<style>(.*?)</style>', content, flags=re.DOTALL)
    unusual_css = []
    if style_match:
        style_content = style_match.group(1)
        # We expect header { }, header .site-name { }, header h1 { }, and maybe header .site-name a { }
        # Let's find any other header selectors
        header_rules = re.findall(r'header[^\{]*\{[^}]*\}', style_content)
        for rule in header_rules:
            if not any(expected in rule for expected in ['header {', 'header .site-name {', 'header .site-name a {', 'header h1 {']):
                unusual_css.append(rule.strip().split('{')[0].strip())
    
    print(f"■ {f}")
    print(f"  リンク: {'あり (<a>タグ使用)' if has_link else 'なし (テキストのみ)'}")
    print(f"  特殊なheader CSS: {', '.join(unusual_css) if unusual_css else 'なし'}")
    print()
