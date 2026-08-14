import os

file_path = 'articles/shogai-juyo.html'
with open(file_path, 'r', encoding='utf-8', newline='') as f:
    lines = f.readlines()

new_lines = []
skip = False
for i, line in enumerate(lines):
    if line.strip() == '<style>':
        # Start of style block
        new_lines.append('<link rel="stylesheet" href="css/style.css">\n')
        new_lines.append('<style>\n')
        skip = True
        continue
    
    if skip and line.strip() == '.breadcrumb span { margin: 0 6px; }':
        skip = False
        continue
        
    if skip:
        continue
        
    if line.strip() == '.footer { text-align: center; font-size: 12px; color: var(--text3); margin-top: 40px; line-height: 2.2; }':
        skip = True
        continue
        
    if skip and line.strip() == '.nav-container a:hover { background: var(--accent-light); color: var(--accent); }</style>':
        skip = False
        new_lines.append('</style>\n')
        continue
        
    if skip:
        continue
        
    new_lines.append(line)

with open(file_path, 'w', encoding='utf-8', newline='') as f:
    f.writelines(new_lines)
