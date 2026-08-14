import sys

file_path = "C:/Users/SHINSUKE/reha-tool/bi-tool.html"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

old1 = "    @page { size: A4 portrait; margin: 12mm 12mm 12mm 12mm; }"
new1 = "    @page { size: A4 portrait; margin: 8mm 8mm 8mm 8mm; }"
if old1 in content:
    content = content.replace(old1, new1)
else:
    print("Failed 1")
    sys.exit(1)

old2 = """    .info-section { display: none !important; }
    .footer { display: none !important; }
  }"""
new2 = """    .info-section { display: none !important; }
    .footer { display: none !important; }
    .no-print { display: none !important; }
  }"""
old2_rn = old2.replace("\n", "\r\n")
new2_rn = new2.replace("\n", "\r\n")
if old2 in content:
    content = content.replace(old2, new2)
elif old2_rn in content:
    content = content.replace(old2_rn, new2_rn)
else:
    print("Failed 2")
    sys.exit(1)

old3 = """<div class="breadcrumb">
  <a href="./index.html">トップ</a>
  <span>›</span>
  <a href="./index.html#tools">評価ツール</a>
  <span>›</span>
  BI(バーセルインデックス)
</div>"""
new3 = """<div class="breadcrumb no-print">
  <a href="./index.html">トップ</a>
  <span>›</span>
  <a href="./index.html#tools">評価ツール</a>
  <span>›</span>
  BI(バーセルインデックス)
</div>"""
old3_rn = old3.replace("\n", "\r\n")
new3_rn = new3.replace("\n", "\r\n")
if old3 in content:
    content = content.replace(old3, new3)
elif old3_rn in content:
    content = content.replace(old3_rn, new3_rn)
else:
    print("Failed 3")
    sys.exit(1)

old4 = """  <div style="margin-top:40px;border-top:1px solid #e0ddd4;padding-top:32px;">
    <h2 style="font-size:15px;font-weight:700;color:#2a5c45;margin-bottom:10px;">参考文献・出典</h2>"""
new4 = """  <div class="no-print" style="margin-top:40px;border-top:1px solid #e0ddd4;padding-top:32px;">
    <h2 style="font-size:15px;font-weight:700;color:#2a5c45;margin-bottom:10px;">参考文献・出典</h2>"""
old4_rn = old4.replace("\n", "\r\n")
new4_rn = new4.replace("\n", "\r\n")
if old4 in content:
    content = content.replace(old4, new4)
elif old4_rn in content:
    content = content.replace(old4_rn, new4_rn)
else:
    print("Failed 4")
    sys.exit(1)

old5_1 = """  <div class="section-title" style="margin-top: 40px;">関連する解説記事</div>
  <div class="article-list-home">"""
new5_1 = """  <div class="no-print">
  <div class="section-title" style="margin-top: 40px;">関連する解説記事</div>
  <div class="article-list-home">"""
old5_1_rn = old5_1.replace("\n", "\r\n")
new5_1_rn = new5_1.replace("\n", "\r\n")
if old5_1 in content:
    content = content.replace(old5_1, new5_1)
elif old5_1_rn in content:
    content = content.replace(old5_1_rn, new5_1_rn)
else:
    print("Failed 5_1")
    sys.exit(1)

old5_2 = """    <div style="text-align: right; margin-top: 12px; padding-right: 5px; margin-bottom: 24px;">
      <a href="articles/index.html" style="font-size: 14px; color: var(--accent); text-decoration: none; font-weight: bold;">すべての解説記事を見る →</a>
    </div>
  </div>

  <div class="footer" style="margin-top:32px;">"""
new5_2 = """    <div style="text-align: right; margin-top: 12px; padding-right: 5px; margin-bottom: 24px;">
      <a href="articles/index.html" style="font-size: 14px; color: var(--accent); text-decoration: none; font-weight: bold;">すべての解説記事を見る →</a>
    </div>
  </div>
  </div>

  <div class="footer" style="margin-top:32px;">"""
old5_2_rn = old5_2.replace("\n", "\r\n")
new5_2_rn = new5_2.replace("\n", "\r\n")
if old5_2 in content:
    content = content.replace(old5_2, new5_2)
elif old5_2_rn in content:
    content = content.replace(old5_2_rn, new5_2_rn)
else:
    print("Failed 5_2")
    sys.exit(1)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Success")
