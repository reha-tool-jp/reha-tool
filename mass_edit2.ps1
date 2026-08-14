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
        Write-Host "Skipping $file, not found"
        continue
    }

    $content = [System.IO.File]::ReadAllText($file, [System.Text.Encoding]::UTF8)
    $modified = $false

    if ($file -match "articles") {
        $rel_path = "../about.html"
    } else {
        $rel_path = "about.html"
    }

    $top_block = @"
<div style="font-size:13px;color:var(--text2);margin-bottom:16px;padding-bottom:12px;border-bottom:1px solid var(--border);">
執筆・監修：理学療法士（臨床25年目）・認知症ケア専門士　|　<a href="$rel_path" style="color:var(--accent);font-weight:700;text-decoration:none;">運営者について →</a>
</div>
"@

    $bottom_block = @"
<div style="background:var(--surface);border:1px solid var(--border);border-radius:var(--radius);padding:16px 20px;margin:24px 0;font-size:14px;color:var(--text2);line-height:1.8;">
この記事は、理学療法士（臨床25年目・認知症ケア専門士、病院リハビリテーション科長として勤務）が、臨床経験と厚生労働省等の一次資料をもとに執筆・監修しています。<br>
経歴の詳細はこちら → <a href="$rel_path" style="color:var(--accent);font-weight:700;text-decoration:none;">運営者について</a>
</div>
"@

    # 1. Update Global Nav
    $nav_search = '<a href="/#tools">評価ツール</a>'
    $nav_replace = '<a href="/#tools">評価ツール</a>' + "`r`n" + '    <a href="/about.html">このサイトについて</a>'
    if ($content.Contains($nav_search) -and -not $content.Contains('<a href="/about.html">このサイトについて</a>')) {
        $content = $content.Replace($nav_search, $nav_replace)
        $modified = $true
    }

    # 2. Insert Top Block
    if (-not $content.Contains("執筆・監修：理学療法士（臨床25年目）")) {
        $pattern = '(?s)(<div class="breadcrumb.*?">.*?</div>)'
        if ($content -match $pattern) {
            $breadcrumb = $matches[1]
            $replacement = "$breadcrumb`r`n$top_block"
            $content = $content -replace [regex]::Escape($breadcrumb), $replacement
            $modified = $true
        } else {
            Write-Host "Breadcrumb not found in $file"
        }
    }

    # 3. Insert Bottom Block
    if (-not $content.Contains("病院リハビリテーション科長として勤務")) {
        $pattern_footer = '(?i)<div class="(?:references|related-section|footer)[^"]*">'
        $match = [regex]::Match($content, $pattern_footer)
        if ($match.Success) {
            $insert_idx = $match.Index
            $content = $content.Substring(0, $insert_idx) + "$bottom_block`r`n`r`n  " + $content.Substring($insert_idx)
            $modified = $true
        } else {
            Write-Host "Footer insertion point not found in $file"
        }
    }

    if ($modified) {
        [System.IO.File]::WriteAllText($file, $content, [System.Text.Encoding]::UTF8)
        Write-Host "Updated $file"
    }
}
Write-Host "Done"
