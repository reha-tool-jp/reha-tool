import os
import glob
import re

html_files = glob.glob('articles/*.html')

def extract_selectors_and_vars(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    style_match = re.search(r'<style>(.*?)</style>', content, re.DOTALL)
    if not style_match:
        return {}, [], 0
    
    style_content = style_match.group(1)
    lines = len(style_content.splitlines())
    
    # Extract vars
    vars_dict = {}
    root_match = re.search(r':root\s*\{([^}]*)\}', style_content)
    if root_match:
        for line in root_match.group(1).splitlines():
            line = line.strip()
            if line.startswith('--'):
                parts = line.split(':', 1)
                if len(parts) == 2:
                    vars_dict[parts[0].strip()] = parts[1].split(';')[0].strip()
                    
    # Extract selectors properly using a simple state machine or regex
    # Strip comments
    no_comments = re.sub(r'/\*.*?\*/', '', style_content, flags=re.DOTALL)
    # Find all text before '{'
    blocks = re.findall(r'([^}{]+)\{', no_comments)
    selectors = []
    for b in blocks:
        sel = b.strip().replace('\n', ' ')
        # clean up multiple spaces
        sel = re.sub(r'\s+', ' ', sel)
        if sel and not sel.startswith('@'):
            selectors.extend([s.strip() for s in sel.split(',')])
            
    return vars_dict, selectors, lines

base_vars, base_selectors, base_lines = extract_selectors_and_vars('articles/semegata-yobou-iryo.html')
base_selectors_set = set(base_selectors)

common_candidates = [
    'body', 'header', 'header .site-name', 'header h1', 'header p',
    '.container', '.breadcrumb', '.breadcrumb a', '.breadcrumb span',
    '.global-nav', '.nav-container', '.nav-container a',
    '.author-block', '.author-icon', '.author-info', '.author-name', '.author-desc',
    '.footer', '.footer a', '.footer-sep'
]

file_stats = []
var_discrepancies = []

for f in html_files:
    v, s, l = extract_selectors_and_vars(f)
    s_set = set(s)
    
    # Check variables
    # We care about new template variables: --surface, --surface2, --text2, --text3
    missing_critical = []
    for var in ['--surface', '--surface2', '--text2', '--text3']:
        if var not in v:
            missing_critical.append(var)
    if missing_critical:
        var_discrepancies.append(f"{os.path.basename(f)} is missing: {', '.join(missing_critical)}")
        
    # How many common selectors does it have?
    has_common = [sel for sel in common_candidates if sel in s_set]
    unique_sels = s_set - base_selectors_set
    
    file_stats.append({
        'file': os.path.basename(f),
        'lines': l,
        'common_count': len(has_common),
        'unique_count': len(unique_sels),
        'unique_examples': list(unique_sels)[:5]
    })

print("=== CRITICAL CSS VARIABLES (New Template) ===")
if var_discrepancies:
    for d in var_discrepancies:
        print(d)
else:
    print("All 25 files have --surface, --surface2, --text2, --text3 defined.")

print("\n=== COMMON STRUCTURAL CSS ===")
print("These selectors are found across most files:")
print(", ".join(common_candidates))

print("\n=== LINE COUNTS & SPECIFIC CSS ===")
total_lines = sum(stat['lines'] for stat in file_stats)
print(f"Total lines of CSS across all {len(file_stats)} files: {total_lines}")
print(f"Average lines per file: {total_lines / len(file_stats):.1f}")
print("\nFiles with highest unique CSS selectors:")
for stat in sorted(file_stats, key=lambda x: x['unique_count'], reverse=True)[:10]:
    print(f"  {stat['file']}: {stat['lines']} lines (Common: {stat['common_count']}/{len(common_candidates)}, Unique selectors: {stat['unique_count']})")
    print(f"    Unique examples: {stat['unique_examples']}")

