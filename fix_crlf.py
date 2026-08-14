import re
file_path = 'articles/shogai-juyo.html'
with open(file_path, 'rb') as f:
    content = f.read()

# Replace \r\r\n with \r\n
content = content.replace(b'\r\r\n', b'\r\n')
# Also just to be safe, replace \r\n\r\n with \r\n where there were single newlines
# Actually let's just make it \n and then let git handle it.
content = content.replace(b'\r\n', b'\n')

with open(file_path, 'wb') as f:
    f.write(content)
