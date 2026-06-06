import os, glob

# 全HTMLファイルを処理
files = glob.glob('**/*.html', recursive=True) + glob.glob('*.html')
files = list(set(files))

for filepath in files:
    with open(filepath, 'rb') as f:
        data = f.read()
    try:
        text = data.decode('utf-8')
        new_text = text.replace('/reha-tool/', '/')
        if new_text != text:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_text)
            print('Fixed: ' + filepath)
    except Exception as e:
        print('Error ' + filepath + ': ' + str(e))

# service-worker.js
with open('service-worker.js', 'rb') as f:
    data = f.read()
text = data.decode('utf-8')
new_text = text.replace('/reha-tool/', '/')
with open('service-worker.js', 'w', encoding='utf-8') as f:
    f.write(new_text)
print('Fixed: service-worker.js')

# sitemap.xml
with open('sitemap.xml', 'rb') as f:
    data = f.read()
text = data.decode('utf-8')
new_text = text.replace('reha-tool-jp.github.io/reha-tool', 'reha-tool.jp')
with open('sitemap.xml', 'w', encoding='utf-8') as f:
    f.write(new_text)
print('Fixed: sitemap.xml')

print('全て完了しました')
