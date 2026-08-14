import os
import re

files = [
    'fim-rida.html',
    'fim-scoring-tips.html',
    'jisseki-shisu.html',
    'kyujitsu-reha-kazan.html',
    'souki-reha-kazan.html',
    'tosho-reha-keikakusho-mokuhyo.html'
]

directory = 'articles'

print("Analyzing body h1 implementation in the 6 files...\n")
for f in files:
    path = os.path.join(directory, f)
    with open(path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Extract the <style> block
    style_match = re.search(r'<style>(.*?)</style>', content, flags=re.DOTALL)
    style_content = style_match.group(1) if style_match else ""
    
    # We want to find the first <h1> or similar that appears AFTER the <header> block.
    # The header block usually ends with </header>
    body_content = ""
    header_end = content.find('</header>')
    if header_end != -1:
        body_content = content[header_end + 9:]
    else:
        body_content = content
        
    # Find h1 in the body
    h1_match = re.search(r'<h1([^>]*)>(.*?)</h1>', body_content, flags=re.DOTALL)
    if h1_match:
        attrs = h1_match.group(1).strip()
        h1_text = h1_match.group(2).strip()
        print(f"■ {f}")
        print(f"  Body H1 tag: <h1 {attrs}>" if attrs else "  Body H1 tag: <h1>")
        # Check if there is specific CSS for h1 in the <style> block, other than header h1
        # E.g. h1 { ... } or .article-title { ... }
        h1_css = re.findall(r'[^a-zA-Z0-9_-]h1\s*\{[^}]*\}', style_content)
        # Check .article-title in CSS
        article_title_css = re.findall(r'\.article-title\s*\{[^}]*\}', style_content)
        print(f"  CSS for h1: {h1_css}")
        print(f"  CSS for .article-title: {article_title_css}")
    else:
        print(f"■ {f}")
        print("  NO h1 found in body.")
    print("-" * 50)
