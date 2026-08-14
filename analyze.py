import os
import re

files = [
    "hdsr-tool.html",
    "walk-tool.html",
    "bi-tool.html",
    "balance-tool.html",
    "santei-tool.html",
    "kihon-checklist.html",
    "kyoumi-tool.html",
    "seikatsu-tool.html"
]

base_dir = "C:/Users/SHINSUKE/reha-tool"

def strip_tags(html):
    # Remove script and style elements
    html = re.sub(r'<(script|style)[^>]*>.*?</\1>', '', html, flags=re.DOTALL)
    # Remove HTML comments
    html = re.sub(r'<!--.*?-->', '', html, flags=re.DOTALL)
    # Remove tags
    text = re.sub(r'<[^>]+>', ' ', html)
    # Remove extra whitespace
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def parse_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        return {"error": str(e)}

    # Extract body
    body_match = re.search(r'<body[^>]*>(.*?)</body>', content, flags=re.DOTALL)
    if body_match:
        body_content = body_match.group(1)
    else:
        body_content = content

    # Total body text length
    body_text = strip_tags(body_content)
    total_body_len = len(body_text.replace(' ', '')) # count characters excluding spaces

    # Find sections by looking for <h2> tags or specific div structures.
    # Most articles are wrapped in <div style="margin-bottom:28px;"> ... <h2>...</h2> ... </div>
    # Let's just find all <h2> and get the text until the next <h2> or end of body.
    h2_splits = re.split(r'(<h2[^>]*>.*?</h2>)', body_content, flags=re.DOTALL)
    
    sections = []
    # h2_splits[0] is before first h2
    for i in range(1, len(h2_splits), 2):
        h2_tag = h2_splits[i]
        h2_text = strip_tags(h2_tag)
        content_after = h2_splits[i+1]
        
        # Stop at the next </div> that closes the container? 
        # Actually splitting by h2 is an approximation. Let's just take the text up to the next h2.
        section_text = strip_tags(content_after)
        
        # Count FAQs (number of <details> in this section)
        faq_count = len(re.findall(r'<details[^>]*>', content_after))
        
        sections.append({
            "title": h2_text,
            "text_len": len(section_text.replace(' ', '')),
            "faq_count": faq_count
        })

    return {
        "total_body_len": total_body_len,
        "sections": sections
    }

for filename in files:
    filepath = os.path.join(base_dir, filename)
    data = parse_file(filepath)
    print(f"--- {filename} ---")
    print(f"Total Body Char Count: {data.get('total_body_len')}")
    for sec in data.get("sections", []):
        print(f"  H2: {sec['title']} (Text length: {sec['text_len']}, FAQs: {sec['faq_count']})")
    print("\n")
