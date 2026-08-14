import os

diff_path = 'diff.txt'
artifact_path = 'C:/Users/SHINSUKE/.gemini/antigravity/brain/e0115646-c885-407f-834c-9dd35c611b3d/trial_diff.md'

with open(diff_path, 'r', encoding='utf-8', errors='ignore') as f:
    diff_content = f.read()

artifact_content = f"""# 共通CSS化 試験置換Diff (4ファイル)

以下のDiffは、`ai-riyou-guide.html`, `bedside-reha-gensam.html`, `fim-rida.html`, `jisseki-shisu.html` の4ファイルに対する共通CSS化の試験置換結果です。

```diff
{diff_content}
```
"""

with open(artifact_path, 'w', encoding='utf-8') as f:
    f.write(artifact_content)

print("done")
