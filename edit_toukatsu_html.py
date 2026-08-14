import re

file_path = 'articles/toukatsu-chosei-shitsu.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace HTML classes to match common CSS
content = content.replace('<header class="site-header">', '<header>')
content = content.replace('<footer class="site-footer">', '<div class="footer">')
content = content.replace('</footer>', '</div>')

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("HTML classes updated.")
