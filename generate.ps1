$css = @"
.global-nav {
  background: var(--surface, #f5f4f0); border-bottom: 1px solid var(--border, #ddd);
  position: sticky; top: 0; z-index: 100;
}
.nav-container {
  max-width: 680px; margin: 0 auto;
  display: flex; gap: 12px; padding: 12px 20px;
  overflow-x: auto; white-space: nowrap;
}
.nav-container a {
  color: var(--text, #1a1916); text-decoration: none; font-size: 13px; font-weight: 600;
  padding: 6px 14px; border-radius: 20px; background: var(--surface2, #e8e6e0);
  transition: background 0.15s, color 0.15s;
}
.nav-container a:hover { background: var(--accent-light, #d4ede3); color: var(--accent, #2a5c45); }
</style>
"@

$info_kyoumi = @"
  <div class="info-section" style="margin-top:40px;border-top:1px solid var(--border);padding-top:32px;">
    <div style="margin-bottom:28px;">
      <h2 style="font-size:15px;font-weight:700;color:var(--accent);margin-bottom:10px;">このツールについて</h2>
      <p style="font-size:14px;color:var(--text2);line-height:1.8;">厚生労働省「別紙様式3-1（興味・関心チェックシート）」に準拠した入力・印刷ツールです。44項目をタップ操作で「している／してみたい／興味がある」の3択で評価し、そのまま印刷・PDF保存できます。</p>
      <p style="font-size:14px;color:var(--text2);line-height:1.8;margin-top:8px;">興味・関心チェックシートは、通所介護・地域密着型通所介護で個別機能訓練加算を算定する際に、利用者の日常生活や社会生活等について、現在行っていること・今後行いたいことを把握するために活用する様式です（別紙様式３－１）。個別機能訓練計画の目標設定にあたり、居宅訪問での聞き取りと合わせて使用します。</p>
      <h3 style="font-size:14px;font-weight:700;color:var(--text);margin-top:16px;margin-bottom:6px;">生活機能チェックシートとの関係</h3>
      <p style="font-size:14px;color:var(--text2);line-height:1.8;">興味・関心チェックシートは、生活機能チェックシート（別紙様式３－２）とセットで使うことが想定されています。生活機能チェックシートがADL・IADLなど「できること・できないこと」を把握するのに対し、興味・関心チェックシートは「本人がしたいこと・興味があること」を把握するもので、両方の情報を合わせることで個別機能訓練計画の目標がより具体的になります。</p>
    </div>
    <div style="margin-bottom:28px;">
      <h2 style="font-size:15px;font-weight:700;color:var(--accent);margin-bottom:10px;">記入方法</h2>
      <p style="font-size:14px;color:var(--text2);line-height:1.8;">現在している生活行為には「している」、していないがしてみたいものには「してみたい」、できる・できないに関わらず興味があるものには「興味がある」を選択してください。どれにも該当しない場合は「×」を押してください。</p>
    </div>
    <div style="margin-bottom:28px;">
      <h2 style="font-size:15px;font-weight:700;color:var(--accent);margin-bottom:10px;">現場での使い方（臨床の視点から）</h2>
      <p style="font-size:14px;color:var(--text2);line-height:1.8;">理学療法士として25年以上、通所・在宅を含む幅広い現場に携わってきた立場から見ていて、このシートの価値がもっとも発揮される瞬間は、○×だけで終わらせなかったときだと感じています。</p>
      <p style="font-size:14px;color:var(--text2);line-height:1.8;margin-top:8px;">「している」「してみたい」「興味がある」のチェックだけで終えてしまうと、本人の本当のニーズまで届かないことがあります。チェックの後に「いつ」「どこで」「誰と」「どんな場面で」まで聞けるかどうかで、その後の目標設定の解像度が大きく変わってきます。</p>
      <p style="font-size:14px;color:var(--text2);line-height:1.8;margin-top:8px;">たとえば「料理」に○がついていても、毎日の食事作りなのか、季節の行事料理だけなのか、一人でやりたいのか誰かと一緒がいいのかによって、個別機能訓練の組み立て方は変わってきます。表面的なチェックで終わらせず、その先の会話まで踏み込めるかが、このシートを本当に活かすポイントだと考えています。</p>
    </div>
  </div>
"@

$info_seikatsu = @"
  <div class="info-section" style="margin-top:40px;border-top:1px solid var(--border);padding-top:32px;">
    <div style="margin-bottom:28px;">
      <h2 style="font-size:15px;font-weight:700;color:var(--accent);margin-bottom:10px;">このツールについて</h2>
      <p style="font-size:14px;color:var(--text2);line-height:1.8;">厚生労働省「別紙様式3-2（生活機能チェックシート）」に準拠した入力・印刷ツールです。通所介護（デイサービス）の個別機能訓練加算の算定に必要な居宅訪問時の評価を、スマートフォンやタブレットで入力し、そのまま印刷・PDF保存できます。</p>
      <p style="font-size:14px;color:var(--text2);line-height:1.8;margin-top:8px;">生活機能チェックシートは、通所介護・地域密着型通所介護で個別機能訓練加算を算定する際に、利用者の居宅での生活状況を把握するために活用する様式です（別紙様式３－２）。ADL（食事・排泄・入浴・更衣など）、IADL（調理・洗濯・買い物など）、起居動作について、居宅を訪問した上で自立レベルと課題を確認します。</p>
      <h3 style="font-size:14px;font-weight:700;color:var(--text);margin-top:16px;margin-bottom:6px;">いつ使うか</h3>
      <p style="font-size:14px;color:var(--text2);line-height:1.8;">個別機能訓練計画の作成前、および計画の見直し時（3か月ごとに1回以上）の居宅訪問で使用します。生活機能チェックシートは、目標設定・個別機能訓練計画の作成の前に行うものとされています。</p>
      <h3 style="font-size:14px;font-weight:700;color:var(--text);margin-top:16px;margin-bottom:6px;">確認する内容</h3>
      <p style="font-size:14px;color:var(--text2);line-height:1.8;">ADL・IADL・起居動作の各項目を「自立」「見守り」「一部介助」「全介助」の4段階で評価し、それぞれに課題の有無を記載します。あわせて、実施場所や使用している福祉用具などの「環境」、生活環境の問題点や課題があれば「状況・生活課題」の欄に記載します。</p>
      <h3 style="font-size:14px;font-weight:700;color:var(--text);margin-top:16px;margin-bottom:6px;">興味・関心チェックシートとの関係</h3>
      <p style="font-size:14px;color:var(--text2);line-height:1.8;">生活機能チェックシートは、興味・関心チェックシート（別紙様式３－１）とセットで使うことが想定されています。生活機能チェックシートが「できること・できないこと」を把握するのに対し、興味・関心チェックシートは「本人がしたいこと・興味があること」を把握するもので、両方の情報を合わせることで個別機能訓練計画の目標がより具体的になります。</p>
    </div>
    <div style="margin-bottom:28px;">
      <h2 style="font-size:15px;font-weight:700;color:var(--accent);margin-bottom:10px;">個別機能訓練加算(Ⅱ)とLIFE提出</h2>
      <p style="font-size:14px;color:var(--text2);line-height:1.8;">個別機能訓練加算(Ⅱ)を算定する場合、LIFEへのデータ提出として「生活機能チェックシート」と「個別機能訓練計画書」の2点が必須です。居宅訪問は3か月ごとに1回以上行い、生活機能チェックシートも同様の頻度で作成します。</p>
    </div>
    <div style="margin-bottom:28px;">
      <h2 style="font-size:15px;font-weight:700;color:var(--accent);margin-bottom:10px;">現場での使い方（臨床の視点から）</h2>
      <p style="font-size:14px;color:var(--text2);line-height:1.8;">理学療法士として25年以上、通所・在宅を含む幅広い現場に携わってきた立場から繰り返し実感してきたのは、通所や入院中の様子だけで判断すると、自宅での実際の姿とズレが生じやすいということです。</p>
      <p style="font-size:14px;color:var(--text2);line-height:1.8;margin-top:8px;">施設の中では車椅子で過ごしている方でも、自宅では手すりを使ってつたい歩きで移動できていたり、なんとか自分でトイレまで行けていたりすることがあります。施設内の場面だけで「入浴」「排泄」「更衣」を課題と決めつけてしまうと、本人が自宅で発揮できている力を見落としたまま計画を立てることになりかねません。</p>
      <p style="font-size:14px;color:var(--text2);line-height:1.8;margin-top:8px;">生活機能チェックシートを使った居宅訪問は、この「施設で見えている姿」と「自宅での実際の姿」のギャップを埋めるための重要な機会だと捉えています。環境・課題の欄には、単なるチェックだけでなく、その場で気づいた具体的な工夫や課題も書き添えるようにしています。</p>
    </div>
    <div style="margin-bottom:28px;">
      <h2 style="font-size:15px;font-weight:700;color:var(--accent);margin-bottom:10px;">よくある質問</h2>
      <div style="margin-bottom:16px;">
        <p style="font-size:14px;font-weight:700;color:var(--text);margin-bottom:4px;">Q. 入力したデータはどこかに送信されますか？</p>
        <p style="font-size:14px;color:var(--text2);line-height:1.8;">A. すべての入力はブラウザ内で完結しており、外部に送信されることはありません。</p>
      </div>
    </div>
  </div>
"@

$utf8NoBom = New-Object System.Text.UTF8Encoding $False

foreach ($f in @("kihon-checklist.html", "kyoumi-tool.html", "seikatsu-tool.html")) {
    $c = [System.IO.File]::ReadAllText("$PWD\$f")
    
    # 1. Replace the first </style>
    $idx = $c.IndexOf("</style>")
    if ($idx -ge 0) {
        $c = $c.Substring(0, $idx) + $css + $c.Substring($idx + 8)
    }

    if ($f -eq "kyoumi-tool.html") {
        $c = $c -replace '(?s)<div class="info-section"[^>]*>.*?</div>\s*</div>\s*<div class="ref-section"', ($info_kyoumi + "`r`n`r`n  <div class=`"ref-section`"")
    }
    
    if ($f -eq "seikatsu-tool.html") {
        $c = $c -replace '(?s)<div class="info-section"[^>]*>.*?</div>\s*</div>\s*<div class="ref-section"', ($info_seikatsu + "`r`n`r`n  <div class=`"ref-section`"")
    }

    [System.IO.File]::WriteAllText("$PWD\$f", $c, $utf8NoBom)
}

# Fix about.html
$about = [System.IO.File]::ReadAllText("$PWD\about.html")
$about = $about.Replace("同グループの介護施設への助言・指導にも関わる", "同グループの介護施設やデイケア、デイサービスへの助言・指導にも関わる")
[System.IO.File]::WriteAllText("$PWD\about.html", $about, $utf8NoBom)
