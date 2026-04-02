"""
Chapter 1: Python essentials for health professionals
Data Analysis with Python for Health Specialists

Run in Jupyter notebook or Google Colab.
"""

# ============================================================
# 1. Variables and types
# ============================================================

patient_age = 45              # int
temperature = 37.2            # float
diagnosis = "Type 2 Diabetes" # str
is_hospitalized = True        # bool

print(f"Patient age: {patient_age} (type: {type(patient_age).__name__})")
print(f"Temperature: {temperature} (type: {type(temperature).__name__})")
print(f"Diagnosis: {diagnosis} (type: {type(diagnosis).__name__})")
print(f"Hospitalized: {is_hospitalized} (type: {type(is_hospitalized).__name__})")

# ============================================================
# 2. Collections
# ============================================================

# Lists
blood_pressures = [120, 135, 128, 142, 118]
print(f"\nNumber of readings: {len(blood_pressures)}")
print(f"First reading: {blood_pressures[0]}")
print(f"Last reading: {blood_pressures[-1]}")
print(f"Average: {sum(blood_pressures) / len(blood_pressures):.1f}")

# Dictionaries
patient = {
    "id": "PAT-0042",
    "age": 58,
    "sex": "F",
    "diagnosis": "Hypertension",
    "systolic_bp": 148,
    "medications": ["Amlodipine", "Hydrochlorothiazide"]
}
print(f"\nPatient {patient['id']}: {patient['diagnosis']}")
print(f"Medications: {', '.join(patient['medications'])}")

# ============================================================
# 3. Control flow
# ============================================================

# Blood pressure classification
systolic = 148

if systolic >= 140:
    category = "Stage 2 Hypertension"
elif systolic >= 130:
    category = "Stage 1 Hypertension"
elif systolic >= 120:
    category = "Elevated"
else:
    category = "Normal"

print(f"\nBP {systolic} mmHg -> {category}")

# Loop through patients
patients = [
    {"id": "P001", "age": 34, "hba1c": 5.4},
    {"id": "P002", "age": 67, "hba1c": 7.8},
    {"id": "P003", "age": 52, "hba1c": 6.1},
    {"id": "P004", "age": 29, "hba1c": 5.0},
    {"id": "P005", "age": 73, "hba1c": 9.1},
]

print("\nDiabetes screening:")
for p in patients:
    if p["hba1c"] >= 6.5:
        status = "Diabetic"
    elif p["hba1c"] >= 5.7:
        status = "Pre-diabetic"
    else:
        status = "Normal"
    print(f"  {p['id']} (age {p['age']}): HbA1c = {p['hba1c']} -> {status}")

# ============================================================
# 4. Functions
# ============================================================

def bmi(weight_kg, height_m):
    """Calculate Body Mass Index."""
    return weight_kg / (height_m ** 2)

def bmi_category(bmi_value):
    """Classify BMI according to WHO categories."""
    if bmi_value < 18.5:
        return "Underweight"
    elif bmi_value < 25.0:
        return "Normal weight"
    elif bmi_value < 30.0:
        return "Overweight"
    else:
        return "Obese"

# Test
test_patients = [
    {"name": "Alice", "weight": 55, "height": 1.62},
    {"name": "Bob", "weight": 95, "height": 1.78},
    {"name": "Clara", "weight": 72, "height": 1.70},
]

print("\nBMI calculations:")
for p in test_patients:
    value = bmi(p["weight"], p["height"])
    print(f"  {p['name']}: BMI = {value:.1f} ({bmi_category(value)})")

# ============================================================
# 5. Importing libraries
# ============================================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

print(f"\npandas version: {pd.__version__}")
print(f"numpy version: {np.__version__}")
print("All libraries imported successfully.")
