import os
import re

directory = 'articles'
exclude = {'index.html', 'shogai-juyo.html', 'jihi-riha-jisho-riha.html', 'kangokyodo-kazan.html', 'toukatsu-chosei-shitsu.html'}
files = [f for f in os.listdir(directory) if f.endswith('.html') and f not in exclude]

standard_vars = {
    '--bg': '#f5f4f0',
    '--surface': '#ffffff',
    '--surface2': '#f0efe9',
    '--border': '#e0ddd4',
    '--text': '#1a1916',
    '--text2': '#6b6860',
    '--text3': '#a09d96',
    '--accent': '#2a5c45',
    '--accent-light': '#e8f2ed',
    '--warn': '#8a5c00',
    '--warn-light': '#fdf6e3',
    '--info': '#1a4a7a',
    '--info-light': '#e8f0fa',
    '--radius': '10px'
}

with open('analysis.txt', 'w', encoding='utf-8') as out:
    for f in sorted(files):
        path = os.path.join(directory, f)
        with open(path, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # 1. :root variables
        root_match = re.search(r':root\s*\{([^}]*)\}', content)
        vars_dict = {}
        if root_match:
            root_content = root_match.group(1)
            for part in root_content.split(';'):
                part = part.strip()
                if part.startswith('--'):
                    if ':' in part:
                        k, v = part.split(':', 1)
                        vars_dict[k.strip()] = v.strip()
        
        # 2. --info missing
        has_info = '--info' in vars_dict and '--info-light' in vars_dict
        
        # 3. Custom colors
        custom_colors = []
        for k, v in vars_dict.items():
            if k in standard_vars and v.lower() != standard_vars[k].lower():
                custom_colors.append(f"{k}: {v}")
        
        # 4. .site-header / .site-footer
        has_site_header = '.site-header' in content
        has_site_footer = '.site-footer' in content
        header_info = []
        if has_site_header: header_info.append(".site-header")
        else: header_info.append("<header>")
        
        if has_site_footer: header_info.append(".site-footer")
        else: header_info.append("<footer>/none")
        
        # 5. .article-container or unique max-width
        container_matches = re.findall(r'\.([a-zA-Z0-9_-]*container[a-zA-Z0-9_-]*)\s*\{[^}]*max-width:\s*([^;]+);', content)
        unique_containers = []
        for match in container_matches:
            cls_name, width = match
            if cls_name != 'container' and cls_name != 'nav-container':
                unique_containers.append(f".{cls_name} ({width})")
                
        # 6. <h1 class="article-title">
        has_article_title = '<h1 class="article-title">' in content
        
        out.write(f"■ {f}\n")
        out.write(f"  --info/info-light定義: {'あり' if has_info else 'なし'}\n")
        out.write(f"  独自:rootカラー: {', '.join(custom_colors) if custom_colors else 'なし (標準一致)'}\n")
        out.write(f"  ヘッダー/フッター実装: {' / '.join(header_info)}\n")
        out.write(f"  独自コンテナ: {', '.join(unique_containers) if unique_containers else 'なし (通常の.container等)'}\n")
        out.write(f"  <h1 class=\"article-title\">: {'あり' if has_article_title else 'なし'}\n")
        out.write("\n")
