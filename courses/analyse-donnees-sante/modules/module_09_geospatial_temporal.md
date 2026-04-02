# Module 9: Geospatial and temporal health data

**Duration:** 3 hours (1h theory + 1h live coding + 1h exercises)
**Prerequisites:** Modules 2-8 (all previous modules). Familiarity with pandas, visualization, and basic modeling.

---

## Learning objectives

By the end of this module, students will be able to:
1. Parse dates, set datetime indices, and compute rolling averages for health time series
2. Decompose a time series into trend, seasonal, and residual components
3. Load and reshape wide-format epidemic data (JHU COVID-19) into long format
4. Create choropleth maps of disease burden using geopandas
5. Merge health indicator data with geospatial boundary files for mapping
6. Combine temporal and spatial analysis in a multi-panel dashboard

---

## Session structure

### Hour 1 — Theory (slides)
- Time series components: trend, seasonality, noise
- Rolling averages for smoothing daily case data
- Trend decomposition with `seasonal_decompose()`
- COVID-19 data: JHU CSSE format, wide-to-long reshaping, `.diff()` for daily cases
- Geospatial data formats: shapefiles vs. GeoJSON
- geopandas: GeoDataFrame, CRS, choropleth maps
- Merging health data with map data (country name matching)
- Small multiples vs. animated maps
- Colormaps for health: sequential, diverging, colorblind-safe

### Hour 2 — Live coding demo
- Create simulated daily malaria cases with seasonal pattern
- Plot daily cases with 7-day and 14-day rolling averages
- Decompose into trend, seasonal, and residual components
- Load JHU COVID-19 data for 5 African countries
- Reshape wide to long, compute daily cases and 7-day average
- Plot COVID-19 curves for 5 countries
- Load world map with geopandas, filter to Africa
- Create a choropleth map of population estimates
- Merge WHO malaria incidence data with the Africa map
- Create malaria incidence choropleth

### Hour 3 — Exercises
- Exercise 1: Plot COVID-19 death curves for 5 African countries with 7-day averages
- Exercise 2: Create a choropleth map of COVID-19 cases per million in Africa
- Exercise 3: Build small multiples showing cumulative cases at 3 time points
- Mini-project: COVID-19 dashboard for 5 African countries

---

## Reading list

- [geopandas documentation](https://geopandas.org/en/stable/)
- [statsmodels time series decomposition](https://www.statsmodels.org/stable/generated/statsmodels.tsa.seasonal.seasonal_decompose.html)
- [JHU CSSE COVID-19 data repository](https://github.com/CSSEGISandData/COVID-19)

---

## Datasets used

- **JHU CSSE COVID-19** confirmed cases: `https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv`
- **JHU CSSE COVID-19** deaths: `https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv`
- **Our World in Data** vaccination: `https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/vaccinations/vaccinations.csv`
- **Natural Earth** (built into geopandas): world country boundaries
- **WHO GHO** malaria incidence: `https://apps.who.int/gho/athena/api/GHO/MALARIA_INCIDENCE?format=csv`

---

## Mini-project: COVID-19 dashboard for 5 African countries

Build a Jupyter notebook with a 4-panel dashboard (`2x2` figure) for South Africa, Nigeria, Kenya, Egypt, and Morocco:

1. **Panel 1 — Confirmed cases over time:** Daily new cases (7-day rolling average) for all 5 countries
2. **Panel 2 — Deaths over time:** Daily deaths (7-day average) for all 5 countries
3. **Panel 3 — Vaccination progress:** `people_fully_vaccinated_per_hundred` over time
4. **Panel 4 — Choropleth map:** Total confirmed cases across all African countries, with the 5 focus countries highlighted

Bonus: Add a summary table with total cases, total deaths, CFR, and vaccination rate per country.

**Deliverable:** A single .ipynb notebook with the 4-panel figure saved as a high-resolution PNG and a 1-paragraph interpretation.
