import re

file_path = 'articles/kangokyodo-kazan.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add variables to :root
# Find where --warn-light is, and append --info and --info-light
if '--info:' not in content:
    content = content.replace(
        '--warn-light: #fdf6e3;',
        '--warn-light: #fdf6e3;\n  --info: #1a4a7a;\n  --info-light: #e8f0fa;'
    )

# 2. Add <link> and remove common CSS
pattern1 = r'<style>\s*:root\s*\{.*?.breadcrumb span \{ margin: 0 6px; \}'
replacement1 = '<link rel="stylesheet" href="css/style.css">\n<style>'
content = re.sub(pattern1, replacement1, content, flags=re.DOTALL)

# Replace the bottom part (footer + global-nav)
pattern2 = r'\.footer\s*\{.*?\}</style>'
replacement2 = '</style>'
content = re.sub(pattern2, replacement2, content, flags=re.DOTALL)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

with open(file_path, 'rb') as f:
    c = f.read()
c = c.replace(b'\r\r\n', b'\r\n')
with open(file_path, 'wb') as f:
    f.write(c)

print("kangokyodo-kazan.html updated.")
