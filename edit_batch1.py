import os
import re

files = [
    'articles/dementia-recovery.html',
    'articles/giren.html',
    'articles/houmon-reha-shogu-kaizen.html',
    'articles/houmon-reha-station.html',
    'articles/ict-8000man.html',
    'articles/kyoumi-chouhyo.html',
    'articles/minashi-tani.html',
    'articles/pt-distribution.html',
    'articles/r8-kaitei-matome.html',
    'articles/seikatsu-chouhyo.html',
    'articles/semegata-yobou-iryo.html',
    'articles/tosho-reha-keikakusho-mokuhyo.html',
    'articles/tug-10m-kijunchi.html',
    'articles/fim-scoring-tips.html',
    'articles/kyujitsu-reha-kazan.html',
    'articles/souki-reha-kazan.html'
]

for filepath in files:
    with open(filepath, 'r', encoding='utf-8', newline='') as f:
        content = f.read()

    # 1. Insert <link> if not present
    link_tag = '<link rel="stylesheet" href="css/style.css">\n<style>'
    if 'css/style.css' not in content:
        content = content.replace('<style>', link_tag, 1)
    
    # 2. Remove :root through .breadcrumb span
    # Because some files might have slightly different formatting (like a:hover, etc.),
    # let's find the position of :root and the position of .breadcrumb span { ... } and slice them out.
    
    # Remove :root
    content = re.sub(r':root\s*\{[^}]*\}', '', content)
    # Remove reset and header and container and breadcrumb (minified style lines)
    content = re.sub(r'\*\s*\{\s*box-sizing:[^}]*\}', '', content)
    content = re.sub(r'body\s*\{[^}]*line-height:\s*1\.8;\s*\}', '', content)
    content = re.sub(r'header\s*\{[^}]*\}', '', content)
    content = re.sub(r'header\s*\.site-name\s*\{[^}]*\}', '', content)
    content = re.sub(r'header\s*\.site-name\s*a\s*\{[^}]*\}', '', content)
    content = re.sub(r'header\s*h1\s*\{[^}]*\}', '', content)
    content = re.sub(r'\.container\s*\{\s*max-width:\s*680px;[^}]*\}', '', content)
    content = re.sub(r'\.breadcrumb\s*\{[^}]*\}', '', content)
    content = re.sub(r'\.breadcrumb\s*a\s*\{[^}]*\}', '', content)
    content = re.sub(r'\.breadcrumb\s*a:hover\s*\{[^}]*\}', '', content)
    content = re.sub(r'\.breadcrumb\s*span\s*\{[^}]*\}', '', content)

    # 3. Remove .footer related
    content = re.sub(r'\.footer\s*\{[^}]*\}', '', content)
    content = re.sub(r'\.footer\s*a\s*\{[^}]*\}', '', content)
    content = re.sub(r'\.footer\s*a:hover\s*\{[^}]*\}', '', content)
    content = re.sub(r'\.footer-sep\s*\{[^}]*\}', '', content)
    
    # 4. Remove .global-nav related
    content = re.sub(r'\.global-nav\s*\{[^}]*\}', '', content)
    content = re.sub(r'\.nav-container\s*\{[^}]*\}', '', content)
    content = re.sub(r'\.nav-container\s*a\s*\{[^}]*\}', '', content)
    content = re.sub(r'\.nav-container\s*a:hover\s*\{[^}]*\}', '', content)
    
    # Clean up excessive empty lines inside <style>
    style_match = re.search(r'<style>(.*?)</style>', content, flags=re.DOTALL)
    if style_match:
        inner_style = style_match.group(1)
        cleaned_style = re.sub(r'\n\s*\n+', '\n', inner_style)
        content = content[:style_match.start(1)] + cleaned_style + content[style_match.end(1):]

    with open(filepath, 'w', encoding='utf-8', newline='') as f:
        f.write(content)
        
print("done")
