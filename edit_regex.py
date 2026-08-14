import re

file_path = 'articles/shogai-juyo.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# We need to replace the start of the style tag up to '.breadcrumb span { margin: 0 6px; }'
pattern1 = r'<style>\s*:root\s*\{.*?.breadcrumb span \{ margin: 0 6px; \}'
replacement1 = '<link rel="stylesheet" href="css/style.css">\n<style>'
content = re.sub(pattern1, replacement1, content, flags=re.DOTALL)

# We need to replace from '.footer {' to '</style>'
pattern2 = r'\.footer\s*\{.*?\}</style>'
replacement2 = '</style>'
content = re.sub(pattern2, replacement2, content, flags=re.DOTALL)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
print("Done")
