$files = "hdsr-tool.html","walk-tool.html","bi-tool.html","balance-tool.html","santei-tool.html","kihon-checklist.html","kyoumi-tool.html","seikatsu-tool.html"

foreach ($file in $files) {
    $content = Get-Content -Path $file -Raw -Encoding UTF8
    
    # Strip script, style, comments
    $content = $content -replace "(?s)<script.*?</script>", ""
    $content = $content -replace "(?s)<style.*?</style>", ""
    $content = $content -replace "(?s)<!--.*?-->", ""
    
    # Get body
    if ($content -match "(?s)<body[^>]*>(.*?)</body>") {
        $body = $matches[1]
    } else {
        $body = $content
    }
    
    # Total body length (strip tags)
    $textOnly = $body -replace "(?s)<[^>]*>", ""
    $textOnly = $textOnly -replace "\s+", ""
    $totalLen = $textOnly.Length
    
    Write-Host "--- $file ---"
    Write-Host "Total Body: $totalLen"
    
    # Split by <h2>
    $parts = $body -split "(?i)<h2[^>]*>"
    for ($i=1; $i -lt $parts.Length; $i++) {
        $p = $parts[$i]
        $idx = $p.IndexOf("</h2>")
        if ($idx -ge 0) {
            $h2Text = $p.Substring(0, $idx) -replace "(?s)<[^>]*>", ""
            $h2Text = $h2Text -replace "\s+", ""
            
            $after = $p.Substring($idx+5)
            $afterText = $after -replace "(?s)<[^>]*>", ""
            $afterText = $afterText -replace "\s+", ""
            
            $faqCount = ([regex]::Matches($after, "(?i)<details[^>]*>")).Count
            
            Write-Host "H2: $h2Text | TextLen: $($afterText.Length) | FAQ: $faqCount"
        }
    }
}
