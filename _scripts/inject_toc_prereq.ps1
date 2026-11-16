# Inject TOC + Prérequis sections into 5 thin course landings.
# Insertion anchor: the empty section placeholders (whitespace-only) before </div><footer>.

$base = 'C:\Users\User\Desktop\CLAUDE-LE-TOUT\Academic-Prof\al-folio\courses'

$plans = @(
    @{
        slug = 'probabilites'
        chapters = @(
            'Espaces Probabilis&eacute;s',
            'Probabilit&eacute; Conditionnelle et Ind&eacute;pendance',
            'Variables Al&eacute;atoires Discr&egrave;tes',
            'Variables Al&eacute;atoires Continues',
            'Esp&eacute;rance, Variance, Moments',
            'Lois Usuelles et leurs Propri&eacute;t&eacute;s',
            'Fonctions de Variables Al&eacute;atoires',
            'Couples de Variables Al&eacute;atoires',
            'Lois des Grands Nombres',
            'Th&eacute;or&egrave;me Central Limite',
            'Fonctions Caract&eacute;ristiques',
            'Introduction aux Cha&icirc;nes de Markov'
        )
        prereq = 'Analyse r&eacute;elle (s&eacute;ries, int&eacute;grales), notions d&rsquo;ensembles et d&eacute;nombrement. La th&eacute;orie de la mesure n&rsquo;est pas suppos&eacute;e connue.'
    },
    @{
        slug = 'processus-stochastiques'
        chapters = @(
            'Rappels de Probabilit&eacute;s',
            'Processus Stochastiques &mdash; D&eacute;finitions',
            'Cha&icirc;nes de Markov &agrave; Temps Discret',
            'Cha&icirc;nes de Markov &agrave; Temps Continu',
            'Processus de Poisson',
            'Martingales &mdash; Temps Discret',
            'Martingales &mdash; Temps Continu',
            'Mouvement Brownien',
            'Int&eacute;grale Stochastique d&rsquo;It&ocirc;',
            'Calcul d&rsquo;It&ocirc; et &Eacute;quations Diff&eacute;rentielles Stochastiques',
            'Applications'
        )
        prereq = 'Probabilit&eacute;s (L2-L3), analyse r&eacute;elle. Notions de th&eacute;orie de la mesure utiles mais rappel&eacute;es au fil du cours.'
    },
    @{
        slug = 'statistique'
        chapters = @(
            'Statistique Descriptive &mdash; R&eacute;sum&eacute; et Visualisation',
            'Mod&egrave;le Statistique et &Eacute;chantillonnage',
            'Estimation Ponctuelle &mdash; EMV et M&eacute;thode des Moments',
            'Propri&eacute;t&eacute;s des Estimateurs &mdash; Biais, Convergence, Efficacit&eacute;',
            'Intervalles de Confiance',
            'Tests d&rsquo;Hypoth&egrave;ses &mdash; Cadre G&eacute;n&eacute;ral',
            'Tests Classiques : <em>z</em>, <em>t</em>, &chi;<sup>2</sup>, <em>F</em>',
            'R&eacute;gression Lin&eacute;aire Simple',
            'R&eacute;gression Lin&eacute;aire Multiple et ANOVA',
            'Introduction &agrave; la Statistique Bay&eacute;sienne',
            'M&eacute;thodes Non-Param&eacute;triques'
        )
        prereq = 'Probabilit&eacute;s (L2-L3), alg&egrave;bre lin&eacute;aire. Programmation de base en Python ou R pour les travaux pratiques.'
    },
    @{
        slug = 'statistique-bayesienne'
        chapters = @(
            'Paradigme Bay&eacute;sien',
            'Lois A Priori et A Posteriori &mdash; Conjugaison',
            'Estimation Bay&eacute;sienne et Fonctions de Perte',
            'Tests d&rsquo;Hypoth&egrave;ses Bay&eacute;siens',
            'Pr&eacute;diction Bay&eacute;sienne',
            'Mod&egrave;les Hi&eacute;rarchiques',
            'M&eacute;thodes MCMC &mdash; Metropolis-Hastings',
            'Algorithme de Gibbs',
            'Inf&eacute;rence Variationnelle',
            'Mod&egrave;les Bay&eacute;siens Non-Param&eacute;triques',
            'Applications'
        )
        prereq = 'Probabilit&eacute;s et statistique inf&eacute;rentielle. Bases d&rsquo;analyse et d&rsquo;alg&egrave;bre lin&eacute;aire. Programmation Python (NumPy, PyMC) pour les TP MCMC.'
    },
    @{
        slug = 'systemes-dynamiques'
        chapters = @(
            'Syst&egrave;mes Dynamiques &mdash; D&eacute;finitions et Exemples',
            'Stabilit&eacute; de Lyapunov',
            'Syst&egrave;mes Lin&eacute;aires et Classification des Portraits de Phase',
            'Syst&egrave;mes Non Lin&eacute;aires &mdash; Lin&eacute;arisation et Vari&eacute;t&eacute; Centrale',
            'Cycles Limites et Th&eacute;or&egrave;me de Poincar&eacute;-Bendixson',
            'Bifurcations',
            'Chaos &mdash; D&eacute;finitions et Propri&eacute;t&eacute;s',
            'Exposants de Lyapunov',
            'Attracteurs &Eacute;tranges',
            'Syst&egrave;mes Dynamiques Discrets',
            'Introduction &agrave; la Th&eacute;orie Ergodique'
        )
        prereq = 'Analyse r&eacute;elle, &eacute;quations diff&eacute;rentielles ordinaires (EDO), alg&egrave;bre lin&eacute;aire. Topologie g&eacute;n&eacute;rale souhait&eacute;e.'
    }
)

foreach ($plan in $plans) {
    $slug = $plan.slug
    $path = Join-Path $base "$slug\index.html"
    if (-not (Test-Path $path)) { Write-Host "MISSING: $path"; continue }

    $c = Get-Content -Raw -Path $path -Encoding UTF8

    # Build TOC HTML
    $tocLines = @('  <section><h2>Table des mati&egrave;res</h2><ol class="toc">')
    for ($i = 0; $i -lt $plan.chapters.Count; $i++) {
        $n = $i + 1
        $title = $plan.chapters[$i]
        $tocLines += "      <li><span class=`"ch-num`">Chapitre $n</span> $title</li>"
    }
    $tocLines[-1] = $tocLines[-1] -replace '</li>$','</li></ol></section>'
    $tocBlock = ($tocLines -join "`n")
    $prereqBlock = "  <section><h2>Pr&eacute;requis</h2><p class=`"prereq`">$($plan.prereq)</p></section>"

    $injection = "$tocBlock`n$prereqBlock`n"

    # Replace the empty-placeholder region: 2 spaces + newline + 2 spaces + newline + </div>
    $pattern = '(?s)[ \t]*\r?\n[ \t]*\r?\n(</div>\s*\r?\n<footer>)'
    $replacement = $injection + '$1'
    $new = [regex]::Replace($c, $pattern, $replacement, 'None', [TimeSpan]::FromSeconds(5))

    if ($new -eq $c) {
        Write-Host "SKIP (no anchor matched): $slug"
        continue
    }
    $utf8NoBom = New-Object System.Text.UTF8Encoding $false
    [System.IO.File]::WriteAllText($path, $new, $utf8NoBom)
    Write-Host "injected: $slug ($($plan.chapters.Count) chapters)"
}
