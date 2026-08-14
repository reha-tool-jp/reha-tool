import re

target_files = [
    'articles/toukatsu-chosei-shitsu.html',
    'articles/kangokyodo-kazan.html',
    'articles/jihi-riha-jisho-riha.html'
]

style_vars = {
  '--bg': '#f5f4f0',
  '--surface': '#ffffff',
  '--surface2': '#f0efe9',
  '--border': '#e0ddd4',
  '--text': '#1a1916',
  '--text2': '#6b6860',
  '--text3': '#a09d96',
  '--accent': '#2a5c45',
  '--accent-light': '#e8f2ed',
  '--warn': '#8a5c00',
  '--warn-light': '#fdf6e3',
  '--info': '#1a4a7a',
  '--info-light': '#e8f0fa',
  '--radius': '10px'
}

for fpath in target_files:
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    style_match = re.search(r':root\s*\{([^}]*)\}', content)
    if style_match:
        root_content = style_match.group(1)
        vars_dict = {}
        # Simple extraction
        for part in root_content.split(';'):
            part = part.strip()
            if part.startswith('--'):
                k, v = part.split(':', 1)
                vars_dict[k.strip()] = v.strip()
        
        diffs = []
        for k, v in style_vars.items():
            if k in vars_dict:
                if vars_dict[k] != v:
                    diffs.append(f"{k} expected {v} got {vars_dict[k]}")
            else:
                diffs.append(f"{k} missing")
                
        if diffs:
            print(f"File {fpath} has differences in :root:")
            for d in diffs:
                print("  " + d)
        else:
            print(f"File {fpath} :root matches perfectly.")
