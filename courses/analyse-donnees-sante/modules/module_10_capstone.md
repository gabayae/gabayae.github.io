# Module 10: Capstone project

**Duration:** 3 hours (1h project planning + 1h initial coding + 1h peer review and Q&A)
**Prerequisites:** Modules 1-9 (all previous modules).

---

## Learning objectives

By the end of this module, students will be able to:
1. Formulate a clear, specific health research question from a real public dataset
2. Design a reproducible analysis pipeline from data loading through visualization and modeling
3. Structure a scientific report following the standard template (Introduction, Data, Methods, Results, Discussion, Limitations)
4. Create publication-quality visualizations (at least 3) with proper labels, captions, and sample sizes
5. Present analytical findings in a concise 5-minute oral presentation
6. Critically evaluate peer work and provide constructive feedback

---

## Session structure

### Hour 1 — Project planning (guided)
- Overview of the 5 suggested projects:
  - Project 1: Diabetes risk factor analysis (Pima dataset + CDC BRFSS)
  - Project 2: COVID-19 impact across African countries (JHU + OWID + World Bank)
  - Project 3: Maternal mortality determinants (WHO GHO + World Bank + DHS)
  - Project 4: Heart disease prediction model comparison (UCI Heart Disease)
  - Project 5: Malaria burden and intervention effectiveness (WHO GHO + Malaria Atlas)
- Timeline: Week 1 (exploration), Week 2 (analysis + report), Week 3 (presentation)
- Report template walkthrough: Introduction, Data, Methods, Results, Discussion, Limitations
- Grading rubric review (100 points: question 10, data 15, EDA 15, stats 20, report 20, code 10, presentation 10)
- Custom project proposals: requirements and approval

### Hour 2 — Initial coding (hands-on)
- Each student chooses a project and downloads the primary dataset
- Load data into a Jupyter notebook: `.head()`, `.shape`, `.info()`, `.describe()`
- Write the research question in one sentence
- List 3 planned visualizations and 1 planned statistical test/model
- Identify potential problems: missing data, messy columns, merging multiple files
- Create the project folder structure (data/raw, data/cleaned, notebooks, figures)

### Hour 3 — Peer review and Q&A
- Students pair up and present their research question + initial data exploration
- Peer feedback: is the question clear? Is the dataset appropriate? What problems do you foresee?
- Instructor Q&A: address common issues and discuss approaches
- Presentation guidelines: 5 minutes, 6 slides max, no code on slides, practice with timer

---

## Reading list

- [Peng (2011) "Reproducible Research in Computational Science"](https://doi.org/10.1126/science.1213847) (Science)
- [WHO Global Health Observatory — Data catalog](https://www.who.int/data/gho)
- [Our World in Data — Health](https://ourworldindata.org/health-meta)

---

## Datasets used

Depends on the chosen project:
- **Project 1:** Pima Indians Diabetes (`jbrownlee/Datasets`), CDC BRFSS
- **Project 2:** JHU CSSE COVID-19, Our World in Data COVID, World Bank
- **Project 3:** WHO GHO (MMR, skilled birth attendance, antenatal care), World Bank, DHS
- **Project 4:** UCI Heart Disease Dataset (Cleveland)
- **Project 5:** WHO GHO (malaria incidence and mortality), Malaria Atlas Project, DHS

---

## Mini-project: Capstone kick-off deliverable

By the end of this session, submit the following to the instructor:

1. **Project choice** (1-5 or custom proposal with justification)
2. **Research question** in one sentence (e.g., "Is diabetes prevalence associated with BMI after adjusting for age and sex?")
3. **Dataset confirmation:** a notebook cell showing the data loaded with `.head()` and `.shape`
4. **Analysis plan:** list of 3 visualizations and 1 statistical test/model
5. **Risk assessment:** identified data quality issues and proposed solutions
6. **Project folder** with the standard structure:
```
capstone_project/
    data/
        raw/          # original downloaded files
        cleaned/      # processed data
    notebooks/
        01_exploration.ipynb
        02_analysis.ipynb
    figures/
    report.pdf
```

**Deliverable:** A single .ipynb notebook with items 1-5 and the folder structure created.
