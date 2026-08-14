with open("articles/kangokyodo-kazan.html", "r", encoding="utf-8") as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if "こうした現場の懸念を受け、三療法士協会（PT・OT・ST協会）は看護・多職種協働加算の実践指針を公表しました。" in line:
        lines[i] = line.replace("こうした現場の懸念を受け、三療法士協会（PT・OT・ST協会）は看護・多職種協働加算の実践指針を公表しました。", "こうした現場の懸念を受け、リハビリテーション専門職団体協議会（日本理学療法士協会・日本作業療法士協会・日本言語聴覚士協会の3団体）は、令和8年4月に看護・多職種協働加算に関する実践指針を公表しました。")
    if "「3療法士は恒常的な介護業務や生活介助を担うものではない」" in line:
        lines[i] = line.replace("「3療法士は恒常的な介護業務や生活介助を担うものではない」", "「３療法士は、恒常的な介護業務や生活介助・援助業務を担うものではない」")
    if "出典：日本作業療法士協会 実践指針（2024年）" in line:
        lines[i] = line.replace("出典：日本作業療法士協会 実践指針（2024年）", "出典：理学療法士・作業療法士・言語聴覚士が専門性を発揮して病棟において協働する体制（看護・多職種協働加算）の実践指針（リハビリテーション専門職団体協議会、令和8年4月）")
    if "リハ職が病棟に出ていくこと自体は、患者にとっても有益です。問題はその中身です。専門家としての視点・判断・介入を持ち込むことが、リハビリテーション専門職としての存在意義につながります。" in line:
        lines[i] = line + """
    <div style="margin-top:40px;border-top:1px solid #e0ddd4;padding-top:32px;">
      <h2 style="font-size:15px;font-weight:700;color:#2a5c45;margin-bottom:10px;">参考文献・出典</h2>
      <ul style="font-size:13px;color:#6b6860;line-height:1.8;padding-left:1.5em;margin-bottom:0;">
        <li>理学療法士・作業療法士・言語聴覚士が専門性を発揮して病棟において協働する体制（看護・多職種協働加算）の実践指針（リハビリテーション専門職団体協議会、令和8年4月）<br>
          <a href="https://www.jaot.or.jp/document/dl/c176fa63c65f40b46d7813a8645655e3/" target="_blank" rel="noopener" style="font-size:12px;color:var(--accent);">https://www.jaot.or.jp/document/dl/c176fa63c65f40b46d7813a8645655e3/</a></li>
      </ul>
      <p style="font-size:13px;color:#888;margin-top:12px;">※本記事は臨床経験と公開資料をもとに作成しています。評価・運用は最新の通知や所属施設のルールをご確認ください。</p>
    </div>
"""

with open("articles/kangokyodo-kazan.html", "w", encoding="utf-8") as f:
    f.writelines(lines)

print("Replacement complete.")
