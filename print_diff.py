import subprocess

result = subprocess.run(['git', 'diff', 'articles/index.html'], capture_output=True)
with open('diff_clean.txt', 'wb') as f:
    f.write(result.stdout)
