$lines = Get-Content "bi-tool.html" -Encoding UTF8
$part1 = $lines[0..340]
$part2 = $lines[341..($lines.Length - 1)]

$colsStr = Get-Content "bi-cols.txt" -Raw -Encoding UTF8
$colsLines = $colsStr -split "`r`n"
if ($colsLines.Length -eq 1) {
    $colsLines = $colsStr -split "`n"
}

$newContent = [System.Collections.Generic.List[string]]::new()
$newContent.AddRange($part1)
$newContent.AddRange($colsLines)
$newContent.AddRange($part2)

$utf8NoBom = New-Object System.Text.UTF8Encoding $false
[IO.File]::WriteAllLines((Join-Path (Get-Location) "bi-tool.html"), $newContent, $utf8NoBom)
