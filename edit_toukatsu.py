import re

file_path = 'articles/toukatsu-chosei-shitsu.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Add <link ...> right before <style>
if '<link rel="stylesheet" href="css/style.css">' not in content:
    content = content.replace('<style>', '<link rel="stylesheet" href="css/style.css">\n<style>')

# Now we need to remove the structural CSS blocks from the <style> tag.
# Let's use regex to remove them based on their comments or selectors.

# Remove:
# * { box-sizing: border-box; margin: 0; padding: 0; }
content = re.sub(r'\*\s*\{\s*box-sizing:\s*border-box;\s*margin:\s*0;\s*padding:\s*0;\s*\}', '', content)

# Remove body { ... }
content = re.sub(r'body\s*\{[^}]*\}', '', content)

# Remove .site-header { ... } and .site-header a { ... } and .site-header a:hover { ... }
content = re.sub(r'/\*\s*ヘッダー\s*\*/\s*\.site-header\s*\{[^}]*\}\s*\.site-header\s*a\s*\{[^}]*\}\s*\.site-header\s*a:hover\s*\{[^}]*\}', '', content)

# Remove .breadcrumb and related
content = re.sub(r'/\*\s*パンくず\s*\*/\s*\.breadcrumb\s*\{[^}]*\}\s*\.breadcrumb\s*a\s*\{[^}]*\}\s*\.breadcrumb\s*a:hover\s*\{[^}]*\}\s*\.breadcrumb\s*span\s*\{[^}]*\}', '', content)

# Remove .site-footer and related
content = re.sub(r'/\*\s*フッター\s*\*/\s*\.site-footer\s*\{[^}]*\}\s*\.site-footer\s*a\s*\{[^}]*\}', '', content)

# Remove .global-nav and .nav-container ...
content = re.sub(r'\.global-nav\s*\{[^}]*\}\s*\.nav-container\s*\{[^}]*\}\s*\.nav-container\s*a\s*\{[^}]*\}\s*\.nav-container\s*a:hover\s*\{[^}]*\}', '', content)

# Fix CRLF issues if they were introduced
with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

with open(file_path, 'rb') as f:
    c = f.read()
c = c.replace(b'\r\r\n', b'\r\n')
with open(file_path, 'wb') as f:
    f.write(c)

print("toukatsu-chosei-shitsu.html updated.")
