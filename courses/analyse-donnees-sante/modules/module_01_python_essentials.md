# Module 1: Python essentials for health professionals

**Duration:** 3 hours (1h theory + 1h live coding + 1h exercises)
**Prerequisites:** Basic computer literacy. No programming experience required.

---

## Learning objectives

By the end of this module, students will be able to:
1. Explain why Python is preferred over Excel/SPSS for reproducible health research
2. Create and run code in a Jupyter notebook (locally or on Google Colab)
3. Use variables, lists, and dictionaries to represent patient data
4. Write conditional logic to classify clinical measurements (BP, BMI, HbA1c)
5. Define reusable functions for common health calculations
6. Import and use core data science libraries (pandas, numpy, matplotlib)

---

## Session structure

### Hour 1 — Theory (slides)
- Why Python for health data? (reproducibility, scale, ecosystem)
- The Jupyter notebook environment
- Variables and types (int, float, str, bool) with clinical examples
- Collections: lists (lab values) and dictionaries (patient records)
- Control flow: if/elif/else for clinical classification
- Functions: BMI, eGFR, BP classification

### Hour 2 — Live coding demo
- Set up Google Colab (or local Jupyter)
- Build a patient record dictionary
- Write a diabetes screening loop (HbA1c thresholds)
- Create a BMI calculator function
- Import pandas and load a small CSV

### Hour 3 — Exercises
- Exercise 1: Write `classify_bp(systolic, diastolic)` using AHA/ACC guidelines
- Exercise 2: Create 5 patient dicts, compute BMI, print categories
- Exercise 3: Write `egfr(creatinine, age, sex)` using CKD-EPI equation
- Mini-project: Build a "patient intake tool" that takes inputs and prints a summary report

---

## Reading list

- [Python Data Science Handbook, Ch. 1](https://jakevdp.github.io/PythonDataScienceHandbook/) — Jake VanderPlas (free online)
- [Google Colab getting started](https://colab.research.google.com/notebooks/intro.ipynb)
- [WHO ICD-11 coding reference](https://icd.who.int/en)

---

## Datasets used

None (this module uses manually created data). Libraries introduced: pandas, numpy, matplotlib.

---

## Mini-project: Patient intake tool

Build a Jupyter notebook that:
1. Defines a function `intake(name, age, sex, weight_kg, height_m, systolic, diastolic, hba1c)`
2. Computes BMI and classifies it
3. Classifies blood pressure
4. Screens for diabetes (HbA1c thresholds)
5. Prints a formatted summary:
```
Patient: Alice, 58F
BMI: 27.3 (Overweight)
BP: 148/92 — Stage 2 Hypertension
HbA1c: 6.8 — Diabetic
```

**Deliverable:** A single .ipynb notebook with the function and 3 test patients.
