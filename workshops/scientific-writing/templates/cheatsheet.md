# LaTeX Quick Reference Cheatsheet

> Workshop: Scientific Writing with LaTeX, Overleaf & Prism

---

## Document Structure

```latex
\documentclass[12pt, a4paper]{article}   % or book, report, beamer
\usepackage[utf8]{inputenc}
\usepackage{amsmath, amssymb, amsthm}
\usepackage{graphicx}
\usepackage{booktabs}
\usepackage{hyperref}

\title{Your Title}
\author{Your Name}
\date{\today}

\begin{document}
\maketitle
\tableofcontents

\section{...}
\subsection{...}
\subsubsection{...}

\end{document}
```

---

## Text Formatting

| Command | Result |
|---------|--------|
| `\textbf{bold}` | **bold** |
| `\textit{italic}` | *italic* |
| `\texttt{monospace}` | `monospace` |
| `\underline{underline}` | underlined text |
| `\emph{emphasis}` | context-dependent emphasis |
| `\textsc{Small Caps}` | small capitals |

---

## Lists

```latex
% Bullet list
\begin{itemize}
    \item First item
    \item Second item
\end{itemize}

% Numbered list
\begin{enumerate}
    \item First item
    \item Second item
\end{enumerate}

% Description list
\begin{description}
    \item[Term] Definition here.
\end{description}
```

---

## Math Mode

### Inline vs Display

```latex
Inline: $E = mc^{2}$

Display (numbered):
\begin{equation}
    x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}
    \label{eq:quadratic}
\end{equation}

Display (unnumbered):
\[ a^2 + b^2 = c^2 \]
```

### Common Math Symbols

| Symbol | Command | Symbol | Command |
|--------|---------|--------|---------|
| Alpha | `\alpha` | Sigma | `\sigma` |
| Beta | `\beta` | Omega | `\omega` |
| Gamma | `\gamma` | Pi | `\pi` |
| Delta | `\delta` | Theta | `\theta` |
| Epsilon | `\varepsilon` | Lambda | `\lambda` |
| Infinity | `\infty` | Partial | `\partial` |
| Not equal | `\neq` | Approx | `\approx` |
| Less/equal | `\leq` | Greater/equal | `\geq` |
| In (element) | `\in` | Subset | `\subseteq` |
| Arrow right | `\rightarrow` | Double arrow | `\Rightarrow` |
| Times | `\times` | Dot product | `\cdot` |

### Fractions, Roots, and Sums

```latex
\frac{a}{b}              % fraction
\sqrt{x}                 % square root
\sqrt[3]{x}              % cube root
\sum_{i=1}^{n} x_i       % summation
\prod_{i=1}^{n} x_i      % product
\int_{a}^{b} f(x)\,dx    % integral
\lim_{x \to 0} f(x)      % limit
```

### Multi-line Equations

```latex
\begin{align}
    a &= b + c    \\
    d &= e + f
\end{align}

% No numbering:
\begin{align*}
    a &= b + c    \\
    d &= e + f
\end{align*}
```

### Matrices

```latex
\begin{pmatrix} a & b \\ c & d \end{pmatrix}   % round brackets
\begin{bmatrix} a & b \\ c & d \end{bmatrix}   % square brackets
\begin{vmatrix} a & b \\ c & d \end{vmatrix}   % determinant bars
```

---

## Figures

```latex
\usepackage{graphicx}   % in preamble

\begin{figure}[htbp]
    \centering
    \includegraphics[width=0.8\textwidth]{filename}
    \caption{Caption text.}
    \label{fig:label}
\end{figure}
```

**Placement options:** `h` = here, `t` = top, `b` = bottom, `p` = own page.

---

## Tables

```latex
\usepackage{booktabs}   % in preamble

\begin{table}[htbp]
    \centering
    \caption{Caption text.}
    \label{tab:label}
    \begin{tabular}{lcc}
        \toprule
        \textbf{Col 1} & \textbf{Col 2} & \textbf{Col 3} \\
        \midrule
        Row 1 & data & data \\
        Row 2 & data & data \\
        \bottomrule
    \end{tabular}
\end{table}
```

**Column types:** `l` = left, `c` = centre, `r` = right, `p{3cm}` = paragraph.

---

## Cross-References

```latex
\label{sec:intro}          % Place after \section, \figure, \equation, etc.
\ref{sec:intro}             % Prints the number (e.g., "1")
\eqref{eq:quadratic}        % Prints the number in parentheses: "(1)"
\pageref{sec:intro}         % Prints the page number
```

**Tip:** Compile twice for references to resolve.

---

## Citations and Bibliography

### Using BibTeX (external .bib file)

```latex
% In the .tex file:
\cite{einstein1905}                   % (Einstein, 1905)
\bibliographystyle{plain}            % plain, abbrv, alpha, unsrt, ...
\bibliography{sample}                % loads sample.bib
```

Compile sequence: `pdflatex` -> `bibtex` -> `pdflatex` -> `pdflatex`

### Inline bibliography (no .bib file needed)

```latex
\begin{thebibliography}{9}
    \bibitem{key} Author, \emph{Title}, Journal, Year.
\end{thebibliography}
```

---

## Theorem Environments (amsthm)

```latex
\usepackage{amsthm}   % in preamble

\newtheorem{theorem}{Theorem}[section]
\newtheorem{lemma}[theorem]{Lemma}

\begin{theorem}
    Statement of the theorem.
\end{theorem}

\begin{proof}
    Your proof here.  Ends with a QED square automatically.
\end{proof}
```

---

## Beamer (Presentations)

```latex
\documentclass{beamer}
\usetheme{Madrid}

\begin{document}

\begin{frame}{Slide Title}
    Content goes here.
\end{frame}

\end{document}
```

---

## Useful Packages

| Package | Purpose |
|---------|---------|
| `amsmath, amssymb, amsthm` | Math and theorems |
| `graphicx` | Images |
| `booktabs` | Professional tables |
| `hyperref` | Clickable links and refs |
| `geometry` | Page margins |
| `natbib` or `biblatex` | Advanced citations |
| `tikz` | Diagrams and plots |
| `listings` or `minted` | Code listings |
| `xcolor` | Custom colours |
| `algorithm2e` | Pseudocode |
| `cleveref` | Smart cross-references |

---

## Common Compilation Commands

```bash
pdflatex document.tex          # Compile to PDF
bibtex document                # Process bibliography
pdflatex document.tex          # Resolve references (run twice)

# Or use latexmk for automatic multi-pass compilation:
latexmk -pdf document.tex
```

---

## Special Characters

| Character | LaTeX command |
|-----------|---------------|
| % | `\%` |
| $ | `\$` |
| & | `\&` |
| # | `\#` |
| _ | `\_` |
| { } | `\{ \}` |
| ~ | `\textasciitilde` |
| ^ | `\textasciicircum` |
| \ | `\textbackslash` |

---

## Spacing Helpers

```latex
\,        % thin space (use in math: $f(x)\,dx$)
\;        % medium space
\quad     % wide space (1em)
\qquad    % extra wide space (2em)
~         % non-breaking space (e.g., Figure~1)
\hfill    % horizontal fill
\vspace{1cm}  % vertical space
\newpage      % page break
```
