$tools = @(
    'balance-tool.html', 'bi-tool.html', 'fim-tool.html', 'hdsr-tool.html',
    'kihon-checklist.html', 'kyoumi-tool.html', 'santei-tool.html',
    'seikatsu-tool.html', 'walk-tool.html'
)

$all_files = @()
foreach ($t in $tools) {
    $all_files += (Join-Path (Get-Location) $t)
}

foreach ($file in $all_files) {
    if (-Not (Test-Path $file)) {
        continue
    }

    $content = [System.IO.File]::ReadAllText($file, [System.Text.Encoding]::UTF8)
    $modified = $false

    # 1. Add class to top block
    $top_search = '<div style="font-size:13px;color:var(--text2);margin-bottom:16px;padding-bottom:12px;border-bottom:1px solid var(--border);">'
    $top_replace = '<div class="author-block-top" style="font-size:13px;color:var(--text2);margin-bottom:16px;padding-bottom:12px;border-bottom:1px solid var(--border);">'
    if ($content.Contains($top_search) -and -not $content.Contains('class="author-block-top"')) {
        $content = $content.Replace($top_search, $top_replace)
        $modified = $true
    }

    # 2. Add class to bottom block
    $bottom_search = '<div style="background:var(--surface);border:1px solid var(--border);border-radius:var(--radius);padding:16px 20px;margin:24px 0;font-size:14px;color:var(--text2);line-height:1.8;">'
    $bottom_replace = '<div class="author-block-bottom" style="background:var(--surface);border:1px solid var(--border);border-radius:var(--radius);padding:16px 20px;margin:24px 0;font-size:14px;color:var(--text2);line-height:1.8;">'
    if ($content.Contains($bottom_search) -and -not $content.Contains('class="author-block-bottom"')) {
        $content = $content.Replace($bottom_search, $bottom_replace)
        $modified = $true
    }

    # 3. Add to @media print
    if (-not $content.Contains(".author-block-top, .author-block-bottom { display: none !important; }")) {
        # Find first @media print {
        $idx = $content.IndexOf("@media print {")
        if ($idx -ne -1) {
            $insert = " .author-block-top, .author-block-bottom { display: none !important; }"
            $content = $content.Substring(0, $idx + 14) + $insert + $content.Substring($idx + 14)
            $modified = $true
        } else {
            Write-Host "@media print not found in $file"
        }
    }

    if ($modified) {
        [System.IO.File]::WriteAllText($file, $content, [System.Text.Encoding]::UTF8)
        Write-Host "Fixed print CSS in $file"
    }
}
Write-Host "Done"
