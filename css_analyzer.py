import os
import glob
import re
from collections import defaultdict

html_files = glob.glob('articles/*.html')

results = {}
root_vars_per_file = {}
selectors_per_file = {}
style_lengths = {}

for f in html_files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    style_match = re.search(r'<style>(.*?)</style>', content, re.DOTALL)
    if style_match:
        style_content = style_match.group(1)
        style_lengths[f] = len(style_content.splitlines())
        
        # Extract root vars
        root_match = re.search(r':root\s*\{([^}]*)\}', style_content)
        vars_dict = {}
        if root_match:
            vars_content = root_match.group(1)
            for line in vars_content.splitlines():
                line = line.strip()
                if line.startswith('--'):
                    parts = line.split(':', 1)
                    if len(parts) == 2:
                        var_name = parts[0].strip()
                        var_value = parts[1].split(';')[0].strip()
                        vars_dict[var_name] = var_value
        root_vars_per_file[f] = vars_dict
        
        # Extract selectors roughly (just looking at lines ending with '{' or containing '{'
        selectors = []
        # Basic regex for CSS selectors: not inside {} and ends before {
        # This is very rough but gives an idea
        # Remove comments first
        no_comments = re.sub(r'/\*.*?\*/', '', style_content, flags=re.DOTALL)
        # Find all blocks
        blocks = re.findall(r'([^{]+)\s*\{', no_comments)
        for b in blocks:
            sel = b.strip().replace('\n', ' ')
            if sel and not sel.startswith('@'):
                selectors.append(sel)
        selectors_per_file[f] = set(selectors)
    else:
        style_lengths[f] = 0
        root_vars_per_file[f] = {}
        selectors_per_file[f] = set()

# Analysis of root vars
all_var_names = set()
for f, vars in root_vars_per_file.items():
    all_var_names.update(vars.keys())

var_values_across_files = defaultdict(set)
for f, vars in root_vars_per_file.items():
    for var in all_var_names:
        val = vars.get(var, "MISSING")
        var_values_across_files[var].add(val)

print("=== ROOT VARIABLES ===")
inconsistent_vars = {v: vals for v, vals in var_values_across_files.items() if len(vals) > 1}
if inconsistent_vars:
    print("Inconsistent variables found:")
    for v, vals in inconsistent_vars.items():
        print(f"  {v}: {vals}")
else:
    print("All root variables are consistent across files (or consistently missing).")

missing_report = defaultdict(list)
for f, vars in root_vars_per_file.items():
    for var in all_var_names:
        if var not in vars:
            missing_report[f].append(var)
if missing_report:
    print("\nFiles missing some variables:")
    for f, missing in missing_report.items():
        print(f"  {os.path.basename(f)}: missing {len(missing)} vars")
        if len(missing) < 5:
            print(f"    {missing}")

# Analysis of selectors (Common vs Specific)
selector_counts = defaultdict(int)
for f, sels in selectors_per_file.items():
    for s in sels:
        selector_counts[s] += 1

common_selectors = {s for s, c in selector_counts.items() if c >= len(html_files) * 0.8} # Present in 80%+ files
print(f"\n=== SELECTORS ===")
print(f"Found {len(common_selectors)} common selectors.")
print("Some common selectors: ", list(common_selectors)[:10])

# Estimate lines of code
total_lines = 0
for f, length in style_lengths.items():
    total_lines += length
avg_lines = total_lines / len(html_files) if html_files else 0

print(f"\n=== LINE COUNTS ===")
print(f"Total HTML files: {len(html_files)}")
print(f"Average <style> length: {avg_lines:.1f} lines")
print(f"Min length: {min(style_lengths.values())}")
print(f"Max length: {max(style_lengths.values())}")

# Check specific files
print("\nFiles with most CSS (potential unique components):")
sorted_files = sorted(style_lengths.items(), key=lambda x: x[1], reverse=True)
for f, length in sorted_files[:5]:
    print(f"  {os.path.basename(f)}: {length} lines")
