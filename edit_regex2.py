import re

file_path = 'articles/jihi-riha-jisho-riha.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the top part
pattern1 = r'<style>\s*:root\s*\{.*?.breadcrumb span \{ margin: 0 6px; \}'
replacement1 = '<link rel="stylesheet" href="css/style.css">\n<style>'
content = re.sub(pattern1, replacement1, content, flags=re.DOTALL)

# Replace the bottom part
pattern2 = r'\.footer\s*\{.*?\}</style>'
replacement2 = '</style>'
content = re.sub(pattern2, replacement2, content, flags=re.DOTALL)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

# Fix CRLF
with open(file_path, 'rb') as f:
    content = f.read()
content = content.replace(b'\r\r\n', b'\r\n')
content = content.replace(b'\r\n', b'\n')
with open(file_path, 'wb') as f:
    f.write(content)
print("Done")
