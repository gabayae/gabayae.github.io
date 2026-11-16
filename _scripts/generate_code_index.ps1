param(
    [string]$CoursesDir = 'C:\Users\User\Desktop\CLAUDE-LE-TOUT\Academic-Prof\al-folio\courses'
)

# Generate code/index.html for every course that has a `code/` subdirectory.
# Each listing: notebooks (+ Colab + nbviewer), Python/Julia/R scripts (source links).
# Matches the warm-dark palette used on sibling course landings.

$repo = 'gabayae/gabayae.github.io'
$branch = 'main'

function GetCourseTitle {
    param([string]$IndexPath, [string]$FallbackSlug)
    if (-not (Test-Path $IndexPath)) { return $FallbackSlug }
    $c = Get-Content -Raw -Path $IndexPath -Encoding UTF8
    if ($c -match '<h1[^>]*>(.*?)</h1>') {
        $t = $matches[1]
        $t = $t -replace '&eacute;','é' -replace '&egrave;','è' -replace '&ecirc;','ê'
        $t = $t -replace '&agrave;','à' -replace '&acirc;','â'
        $t = $t -replace '&icirc;','î' -replace '&iuml;','ï'
        $t = $t -replace '&ocirc;','ô' -replace '&ouml;','ö'
        $t = $t -replace '&ugrave;','ù' -replace '&ucirc;','û' -replace '&uuml;','ü'
        $t = $t -replace '&ccedil;','ç' -replace '&amp;','&'
        $t = $t -replace '<[^>]+>',''
        return $t.Trim()
    }
    return $FallbackSlug
}

function GetCourseLang {
    param([string]$IndexPath)
    if (-not (Test-Path $IndexPath)) { return 'fr' }
    $c = Get-Content -Raw -Path $IndexPath -Encoding UTF8
    if ($c -match '<html lang="([^"]+)"') { return $matches[1] }
    return 'fr'
}

function BuildFileItem {
    param([string]$RelPath, [string]$Slug, [bool]$IsNotebook, [string]$Lang)
    $name = Split-Path $RelPath -Leaf
    $ghPath = "courses/$Slug/code/$RelPath"
    $ghUrl = "https://github.com/$repo/blob/$branch/$ghPath"
    if ($IsNotebook) {
        $colab = "https://colab.research.google.com/github/$repo/blob/$branch/$ghPath"
        $nbv = "https://nbviewer.org/github/$repo/blob/$branch/$ghPath"
        $openLbl = if ($Lang -eq 'fr') { 'Ouvrir dans Colab' } else { 'Open in Colab' }
        return "        <li><span class=`"fname`">$name</span> <a href=`"$colab`" class=`"tag colab`" target=`"_blank`">$openLbl</a> <a href=`"$nbv`" class=`"tag`" target=`"_blank`">nbviewer</a> <a href=`"$ghUrl`" class=`"tag`" target=`"_blank`">GitHub</a></li>"
    }
    return "        <li><span class=`"fname`">$name</span> <a href=`"$ghUrl`" class=`"tag`" target=`"_blank`">source</a></li>"
}

function GenerateCodeIndex {
    param([string]$CourseDir)

    $slug = Split-Path $CourseDir -Leaf
    $codeDir = Join-Path $CourseDir 'code'
    if (-not (Test-Path $codeDir)) { return }

    $landingPath = Join-Path $CourseDir 'index.html'
    $title = GetCourseTitle -IndexPath $landingPath -FallbackSlug $slug
    $lang = GetCourseLang -IndexPath $landingPath

    $backLbl = if ($lang -eq 'fr') { 'Retour au cours' } else { 'Back to course' }
    $codeLbl = if ($lang -eq 'fr') { 'Code' } else { 'Code' }
    $nbLbl = if ($lang -eq 'fr') { 'Notebooks' } else { 'Notebooks' }
    $pyLbl = if ($lang -eq 'fr') { 'Scripts Python' } else { 'Python scripts' }
    $jlLbl = if ($lang -eq 'fr') { 'Scripts Julia' } else { 'Julia scripts' }
    $rLbl  = if ($lang -eq 'fr') { 'Scripts R' } else { 'R scripts' }
    $emptyLbl = if ($lang -eq 'fr') { 'Pas encore de contenu dans cette section.' } else { 'No files in this section yet.' }
    $metaFr = if ($lang -eq 'fr') { 'Les notebooks s''ouvrent directement dans Google Colab sans installation. Les sources Python, Julia et R sont consultables via GitHub.' } else { 'Notebooks open directly in Google Colab — no install required. Python, Julia and R sources are browsable via GitHub.' }

    $sb = New-Object System.Text.StringBuilder
    [void]$sb.AppendLine('<!DOCTYPE html>')
    [void]$sb.AppendLine("<html lang=`"$lang`">")
    [void]$sb.AppendLine('<head>')
    [void]$sb.AppendLine('<meta charset="UTF-8">')
    [void]$sb.AppendLine('<meta name="viewport" content="width=device-width, initial-scale=1.0">')
    [void]$sb.AppendLine("<title>$codeLbl &middot; $title &mdash; Y.U. Gaba</title>")
    [void]$sb.AppendLine('<link rel="preconnect" href="https://fonts.googleapis.com">')
    [void]$sb.AppendLine('<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>')
    [void]$sb.AppendLine('<link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500&family=IBM+Plex+Sans:wght@300;400;500;600;700&display=swap" rel="stylesheet">')
    [void]$sb.AppendLine('<style>')
    [void]$sb.AppendLine('*,*::before,*::after{margin:0;padding:0;box-sizing:border-box}')
    [void]$sb.AppendLine(":root{--bg:#162240;--bg-card:#1d2d4f;--bg-card-2:#243560;--text:#EDE9E2;--text-muted:#a8a196;--gold:#E8C230;--blue:#3B6FD4;--blue-light:#5a8be6;--border:rgba(237,233,226,.08);--font:'IBM Plex Sans',sans-serif;--mono:'IBM Plex Mono',monospace}")
    [void]$sb.AppendLine('html{scroll-behavior:smooth}body{font-family:var(--font);background:var(--bg);color:var(--text);line-height:1.6;min-height:100vh}')
    [void]$sb.AppendLine('a{color:var(--blue-light);text-decoration:none;transition:color .2s}a:hover{color:var(--gold)}')
    [void]$sb.AppendLine('.container{max-width:880px;margin:0 auto;padding:0 24px}')
    [void]$sb.AppendLine('.back{display:inline-block;margin:32px 0 18px;font-size:.95rem;font-family:var(--mono);color:var(--text-muted)}')
    [void]$sb.AppendLine('.back:hover{color:var(--gold)}')
    [void]$sb.AppendLine('header.pageh{margin:16px 0 28px;padding:22px 26px;background:linear-gradient(140deg,var(--bg-card) 0%,var(--bg-card-2) 100%);border:1px solid var(--border);border-radius:14px}')
    [void]$sb.AppendLine('h1{font-size:1.7rem;font-weight:700;margin-bottom:6px}')
    [void]$sb.AppendLine('.sub{color:var(--text-muted);font-size:.95rem}')
    [void]$sb.AppendLine('section{margin-bottom:28px}')
    [void]$sb.AppendLine('section h2{font-size:1.05rem;font-weight:600;color:var(--gold);margin-bottom:12px;border-bottom:1px solid var(--border);padding-bottom:6px;font-family:var(--mono);letter-spacing:.04em;text-transform:uppercase}')
    [void]$sb.AppendLine('ul.files{list-style:none}')
    [void]$sb.AppendLine('ul.files li{padding:10px 0;border-bottom:1px solid var(--border);display:flex;flex-wrap:wrap;gap:8px;align-items:center;font-size:.92rem}')
    [void]$sb.AppendLine('ul.files li:last-child{border-bottom:none}')
    [void]$sb.AppendLine('.fname{font-family:var(--mono);color:var(--text);flex:1;min-width:220px}')
    [void]$sb.AppendLine('.tag{display:inline-block;padding:3px 10px;border-radius:12px;font-size:.72rem;font-family:var(--mono);background:rgba(59,111,212,.15);border:1px solid rgba(59,111,212,.3);color:var(--blue-light);letter-spacing:.03em;white-space:nowrap}')
    [void]$sb.AppendLine('.tag:hover{background:rgba(59,111,212,.28);color:#fff}')
    [void]$sb.AppendLine('.tag.colab{background:rgba(255,164,38,.14);border-color:rgba(255,164,38,.38);color:#ffb95a}')
    [void]$sb.AppendLine('.tag.colab:hover{background:rgba(255,164,38,.28);color:#fff}')
    [void]$sb.AppendLine('.empty{color:var(--text-muted);font-style:italic;font-size:.9rem}')
    [void]$sb.AppendLine('footer{border-top:1px solid var(--border);padding:28px 0;margin-top:48px;text-align:center;font-size:.8rem;color:var(--text-muted);font-family:var(--mono)}')
    [void]$sb.AppendLine('</style>')
    [void]$sb.AppendLine('</head>')
    [void]$sb.AppendLine('<body>')
    [void]$sb.AppendLine('<div class="container">')
    [void]$sb.AppendLine("  <a href=`"../index.html`" class=`"back`">&larr; $backLbl</a>")
    [void]$sb.AppendLine('  <header class="pageh">')
    [void]$sb.AppendLine("    <h1>$codeLbl &middot; $title</h1>")
    [void]$sb.AppendLine("    <p class=`"sub`">$metaFr</p>")
    [void]$sb.AppendLine('  </header>')

    # Notebooks
    $nbDir = Join-Path $codeDir 'notebooks'
    if (Test-Path $nbDir) {
        $nbs = Get-ChildItem -Path $nbDir -Filter '*.ipynb' -File -ErrorAction SilentlyContinue | Sort-Object Name
        [void]$sb.AppendLine('  <section>')
        [void]$sb.AppendLine("    <h2>$nbLbl</h2>")
        if ($nbs.Count -eq 0) {
            [void]$sb.AppendLine("    <p class=`"empty`">$emptyLbl</p>")
        } else {
            [void]$sb.AppendLine('    <ul class="files">')
            foreach ($nb in $nbs) {
                $rel = "notebooks/$($nb.Name)"
                [void]$sb.AppendLine((BuildFileItem -RelPath $rel -Slug $slug -IsNotebook $true -Lang $lang))
            }
            [void]$sb.AppendLine('    </ul>')
        }
        [void]$sb.AppendLine('  </section>')
    }

    foreach ($pair in @(@{dir='python';lbl=$pyLbl;ext='*.py'}, @{dir='julia';lbl=$jlLbl;ext='*.jl'}, @{dir='r';lbl=$rLbl;ext='*.R'})) {
        $subDir = Join-Path $codeDir $pair.dir
        if (Test-Path $subDir) {
            $files = Get-ChildItem -Path $subDir -Filter $pair.ext -File -ErrorAction SilentlyContinue | Sort-Object Name
            [void]$sb.AppendLine('  <section>')
            [void]$sb.AppendLine("    <h2>$($pair.lbl)</h2>")
            if ($files.Count -eq 0) {
                [void]$sb.AppendLine("    <p class=`"empty`">$emptyLbl</p>")
            } else {
                [void]$sb.AppendLine('    <ul class="files">')
                foreach ($f in $files) {
                    $rel = "$($pair.dir)/$($f.Name)"
                    [void]$sb.AppendLine((BuildFileItem -RelPath $rel -Slug $slug -IsNotebook $false -Lang $lang))
                }
                [void]$sb.AppendLine('    </ul>')
            }
            [void]$sb.AppendLine('  </section>')
        }
    }

    [void]$sb.AppendLine('</div>')
    [void]$sb.AppendLine('<footer><div class="container">&copy; 2026 Y.U. Gaba</div></footer>')
    [void]$sb.AppendLine('</body>')
    [void]$sb.AppendLine('</html>')

    $outPath = Join-Path $codeDir 'index.html'
    $utf8NoBom = New-Object System.Text.UTF8Encoding $false
    [System.IO.File]::WriteAllText($outPath, $sb.ToString(), $utf8NoBom)
    return $outPath
}

$dirs = Get-ChildItem -Path $CoursesDir -Directory | Where-Object { Test-Path (Join-Path $_.FullName 'code') }
$count = 0
foreach ($d in $dirs) {
    $p = GenerateCodeIndex -CourseDir $d.FullName
    if ($p) { Write-Host "wrote: $p"; $count++ }
}
Write-Host ""
Write-Host "Done. $count code/index.html files generated."
