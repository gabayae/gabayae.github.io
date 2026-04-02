# Module 2: Health data with Pandas

**Duration:** 3 hours (1h theory + 1h live coding + 1h exercises)
**Prerequisites:** Module 1 (Python essentials). Familiarity with variables, lists, dictionaries, and functions.

---

## Learning objectives

By the end of this module, students will be able to:
1. Create and manipulate DataFrames to represent clinical and epidemiological data
2. Load health datasets from CSV, Excel, and the WHO Global Health Observatory API
3. Explore datasets using `.head()`, `.describe()`, `.info()`, and `.dtypes`
4. Filter rows using boolean conditions (e.g., diabetic patients, African countries)
5. Group and aggregate data to answer "per-group" questions (mean life expectancy by continent)
6. Create new columns from existing ones (BMI, age groups, binary flags)

---

## Session structure

### Hour 1 — Theory (slides)
- What is a DataFrame? Rows = observations, columns = variables
- Loading data: `pd.read_csv()`, `pd.read_excel()`, WHO GHO API
- Exploring data: `.shape`, `.columns`, `.dtypes`, `.describe()`, `.info()`
- Selecting columns and filtering rows with boolean conditions
- Sorting and ranking
- Grouping with `.groupby()` and aggregation with `.agg()`
- Creating new columns: computed values, `pd.cut()`, binary flags

### Hour 2 — Live coding demo
- Load the Gapminder dataset from a URL
- Explore shape, columns, and summary statistics
- Filter to African countries and find the 5 with lowest life expectancy
- Compute mean life expectancy by continent using `.groupby()`
- Create a life expectancy category column with `pd.cut()`
- Save the cleaned subset to CSV

### Hour 3 — Exercises
- Exercise 1: Load WHO life expectancy data and display basic statistics
- Exercise 2: Filter to African countries, compute mean life expectancy by decade
- Exercise 3: Find the top 10 countries by life expectancy in 2007
- Mini-project: Build a complete WHO life expectancy analysis notebook

---

## Reading list

- [Python Data Science Handbook, Ch. 3 — Pandas](https://jakevdp.github.io/PythonDataScienceHandbook/) — Jake VanderPlas (free online)
- [Pandas official getting started tutorials](https://pandas.pydata.org/docs/getting_started/intro_tutorials/)
- [WHO Global Health Observatory data portal](https://www.who.int/data/gho/data/indicators)

---

## Datasets used

- **Gapminder** (life expectancy, GDP, population by country and year): `https://raw.githubusercontent.com/datasets/gapminder/main/data/gapminder.csv`
- **WHO GHO** maternal mortality ratio: `https://apps.who.int/gho/athena/api/GHO/MDG_0000000026?format=csv`

---

## Mini-project: WHO life expectancy analysis

Build a Jupyter notebook that:
1. Loads the Gapminder dataset from a URL
2. Displays basic statistics (shape, dtypes, summary)
3. Filters to African countries and counts unique countries
4. Computes mean life expectancy by decade (1950s, 1960s, ..., 2000s) for Africa vs. Europe
5. Finds the 5 African countries with the lowest life expectancy in 2007
6. Creates a `life_exp_category` column: "Low" (<55), "Medium" (55-70), "High" (>70)
7. Groups by continent and category, counts countries in each cell
8. Saves the Africa-only data to a CSV file

**Deliverable:** A single .ipynb notebook with all steps, printed outputs, and inline comments.
