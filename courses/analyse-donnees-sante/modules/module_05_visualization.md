# Module 5: Visualization for health data

**Duration:** 3 hours (1h theory + 1h live coding + 1h exercises)
**Prerequisites:** Modules 2-4 (Pandas, cleaning, descriptive statistics). Ability to load, clean, and summarize DataFrames.

---

## Learning objectives

By the end of this module, students will be able to:
1. Apply visualization best practices for health data (labeled axes, units, colorblind palettes, sample sizes)
2. Create histograms and density plots to show distributions of clinical measurements
3. Build box plots and bar charts for group comparisons (disease prevalence, BP by sex)
4. Plot time trends and epidemic curves with rolling averages
5. Generate scatter plots with regression lines and correlation coefficients
6. Produce Kaplan-Meier survival curves using the `lifelines` library

---

## Session structure

### Hour 1 — Theory (slides)
- Principles: message, audience, comparison; labeling rules
- Colorblind-friendly palettes (Bang Wong, Nature Methods 2011)
- Histograms and KDE plots for distributions
- Box plots vs. violin plots for group comparisons
- Bar charts for counts and rates
- Line plots for time trends and epidemic curves
- Scatter plots for relationships (with regression lines)
- Kaplan-Meier survival curves (censoring, median survival)
- Heatmaps for correlation matrices and disease co-occurrence
- Multi-panel figures with `plt.subplots()`

### Hour 2 — Live coding demo
- Set up seaborn theme and colorblind palette
- Histogram of life expectancy with median line
- KDE plot of life expectancy by continent
- Box plot of BMI by sex and age group with threshold lines
- Horizontal bar chart of 15 countries with lowest life expectancy
- Epidemic curve: daily cases + 7-day rolling average + cumulative
- Gapminder bubble chart (GDP vs. life expectancy, bubble = population)
- Kaplan-Meier curves for two treatment groups
- Correlation heatmap of clinical indicators

### Hour 3 — Exercises
- Exercise 1: Modify the Gapminder dashboard for 2002 data
- Exercise 2: Build a clinical dashboard (BMI histogram, BP box plot, HbA1c scatter, diagnosis bar chart)
- Exercise 3: Create a Kaplan-Meier plot for 3 treatment groups
- Mini-project: 4-panel health dashboard

---

## Reading list

- [Python Data Science Handbook, Ch. 4 — Visualization with Matplotlib](https://jakevdp.github.io/PythonDataScienceHandbook/)
- [Seaborn tutorial and gallery](https://seaborn.pydata.org/tutorial.html)
- [Lifelines documentation — Kaplan-Meier](https://lifelines.readthedocs.io/en/latest/)

---

## Datasets used

- **Gapminder**: `https://raw.githubusercontent.com/datasets/gapminder/main/data/gapminder.csv`
- Simulated clinical data (glucose, BMI, blood pressure, survival times)

---

## Mini-project: 4-panel health dashboard

Build a Jupyter notebook that creates a single `2x2` multi-panel figure:
1. **Panel A:** Box plot of life expectancy by continent (2007)
2. **Panel B:** Bubble scatter plot of GDP per capita vs. life expectancy (log scale, bubble = population)
3. **Panel C:** Line plot of mean life expectancy trends by continent (1952-2007)
4. **Panel D:** Horizontal bar chart of the 10 countries with lowest life expectancy

Requirements:
- Colorblind-friendly palette
- All axes labeled with units
- Sample sizes in titles or annotations
- Save as high-resolution PNG (`dpi=150`)

**Deliverable:** A single .ipynb notebook with the dashboard figure and a 1-paragraph interpretation in a markdown cell.
