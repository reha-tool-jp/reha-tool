$tools = @(
    'balance-tool.html', 'bi-tool.html', 'fim-tool.html', 'hdsr-tool.html',
    'kihon-checklist.html', 'kyoumi-tool.html', 'santei-tool.html',
    'seikatsu-tool.html', 'walk-tool.html'
)

$articles = Get-ChildItem -Path "articles" -Filter "*.html" | Where-Object { $_.Name -ne "index.html" } | Select-Object -ExpandProperty FullName

$all_files = @()
foreach ($t in $tools) {
    $all_files += (Join-Path (Get-Location) $t)
}
$all_files += $articles

foreach ($file in $all_files) {
    if (-Not (Test-Path $file)) {
        continue
    }

    $content = [System.IO.File]::ReadAllText($file, [System.Text.Encoding]::UTF8)
    
    if ($file -match "articles") {
        $rel_path = "../about.html"
    } else {
        $rel_path = "about.html"
    }

    $bottom_block = @"
<div style="background:var(--surface);border:1px solid var(--border);border-radius:var(--radius);padding:16px 20px;margin:24px 0;font-size:14px;color:var(--text2);line-height:1.8;">
この記事は、理学療法士（臨床25年目・認知症ケア専門士、病院リハビリテーション科長として勤務）が、臨床経験と厚生労働省等の一次資料をもとに執筆・監修しています。<br>
経歴の詳細はこちら → <a href="$rel_path" style="color:var(--accent);font-weight:700;text-decoration:none;">運営者について</a>
</div>
"@

    if (-not $content.Contains("病院リハビリテーション科長として勤務")) {
        # Find index of '<div class="footer"'
        $idx = $content.IndexOf('<div class="footer"')
        if ($idx -ne -1) {
            $content = $content.Substring(0, $idx) + "$bottom_block`r`n`r`n  " + $content.Substring($idx)
            [System.IO.File]::WriteAllText($file, $content, [System.Text.Encoding]::UTF8)
            Write-Host "Fixed footer in $file"
        } else {
            Write-Host "Still couldn't find footer in $file"
        }
    }
}
Write-Host "Done"
