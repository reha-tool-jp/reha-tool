import re

file_path = 'articles/toukatsu-chosei-shitsu.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update <header>
new_header = '''<header>
  <div class="site-name">リハビリ評価・計算ツール｜解説記事</div>
  <h1>リハビリテーション統括調整室とは何か<br>――厚労省に初めて横断調整組織が置かれた日</h1>
</header>'''
content = re.sub(r'<header>\s*<a[^>]*>.*?</a>\s*</header>', new_header, content, flags=re.DOTALL)

# 2. Delete duplicate h1 and subtitle from body
content = re.sub(r'\s*<h1 class="article-title">.*?</h1>\s*<p class="article-subtitle">.*?</p>', '', content, flags=re.DOTALL)

# 3. Delete header a CSS
css_to_remove = r'\s*header a\s*\{[^}]*\}\s*header a:hover\s*\{[^}]*\}'
content = re.sub(css_to_remove, '', content)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("done")
