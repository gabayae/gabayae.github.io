"""
Chapter 5: DataFrames and Data Wrangling
=========================================
All code examples from Chapter 5 of the Julia programming course.
Covers: DataFrames.jl, CSV reading/writing, selecting, filtering,
transforming, sorting, grouping, joins, reshaping.
"""

using DataFrames
using Statistics

# ============================================================
# Section: The DataFrames.jl package
# ============================================================

println("=== Creating DataFrames ===")

df = DataFrame(
    name   = ["Alice", "Bob", "Charlie", "Diana", "Eve"],
    age    = [28, 35, 42, 31, 27],
    salary = [55000, 72000, 88000, 63000, 51000],
    dept   = ["Engineering", "Marketing", "Engineering", "HR", "Marketing"]
)

println("size(df) = $(size(df))")
println("nrow(df), ncol(df) = $(nrow(df)), $(ncol(df))")
println("names(df) = $(names(df))")
println("\nfirst(df, 3):")
display(first(df, 3))
println()

println("describe(df):")
display(describe(df))
println()

println("Column types: $(eltype.(eachcol(df)))")

# ============================================================
# Section: Reading and writing data (CSV)
# ============================================================

println("\n=== CSV Reading/Writing ===")

using CSV

# Write a sample CSV
CSV.write("sample_data.csv", df)
println("Wrote sample_data.csv")

# Read it back
df_read = CSV.read("sample_data.csv", DataFrame)
println("Read back $(nrow(df_read)) rows from CSV")
display(df_read)
println()

# Clean up
rm("sample_data.csv")

# ============================================================
# Section: Selecting and filtering
# ============================================================

println("\n=== Selecting and Filtering ===")

# Select columns
println("Select name and dept:")
display(select(df, :name, :dept))
println()

println("Select all except salary:")
display(select(df, Not(:salary)))
println()

# Create new columns with select
println("Computed column (name length):")
display(select(df, :name, :name => ByRow(length) => :name_length))
println()

# Filter rows
println("Filter age > 30:")
display(filter(row -> row.age > 30, df))
println()

println("Filter Engineering dept:")
display(filter(:dept => ==("Engineering"), df))
println()

# subset
println("Subset salary > 60000:")
display(subset(df, :salary => x -> x .> 60000))
println()

# ============================================================
# Section: Transforming data
# ============================================================

println("\n=== Transforming Data ===")

df_cities = DataFrame(
    city = ["Paris", "London", "Berlin", "Madrid", "Rome"],
    pop_million = [2.16, 8.98, 3.64, 3.22, 2.87],
    area_km2 = [105, 1572, 892, 604, 1285]
)

# Add a new column
println("With density column:")
display(transform(df_cities, [:pop_million, :area_km2] =>
    ByRow((p, a) -> p * 1e6 / a) => :density))
println()

# In-place transformation
transform!(df_cities, :city => ByRow(uppercase) => :city_upper)
println("After in-place transform:")
display(df_cities)
println()

# Multiple transformations
println("Multiple transforms:")
display(transform(df_cities,
    :pop_million => (x -> x .* 1e6) => :population,
    :area_km2 => (x -> x ./ 2.59) => :area_sq_miles
))
println()

# Handle missing data
df_missing = DataFrame(
    x = [1, 2, missing, 4, missing],
    y = [missing, 2, 3, missing, 5]
)
println("Original with missing:")
display(df_missing)
println()

println("dropmissing:")
display(dropmissing(df_missing))
println()

println("coalesce with 0:")
println("x filled: $(coalesce.(df_missing.x, 0))")

# ============================================================
# Section: Sorting
# ============================================================

println("\n=== Sorting ===")

println("Sort by age:")
display(sort(df, :age))
println()

println("Sort by salary descending:")
display(sort(df, :salary, rev=true))
println()

println("Sort by dept then age:")
display(sort(df, [:dept, :age]))
println()

# ============================================================
# Section: Grouping and split-apply-combine
# ============================================================

println("\n=== Grouping and Split-Apply-Combine ===")

# Group by department
gdf = groupby(df, :dept)
println("Number of groups: $(length(gdf))")

# Apply aggregation
result = combine(gdf,
    :salary => mean => :mean_salary,
    :salary => std => :std_salary,
    :age => mean => :mean_age,
    nrow => :count
)
println("Aggregated by dept:")
display(result)
println()

# Transform within groups (z-score)
println("Z-score of salary within dept:")
display(transform(groupby(df, :dept),
    :salary => (x -> length(x) > 1 ? (x .- mean(x)) ./ std(x) : zeros(length(x))) => :salary_zscore
))
println()

# ============================================================
# Section: Joins
# ============================================================

println("\n=== Joins ===")

employees = DataFrame(
    id = [1, 2, 3, 4, 5],
    name = ["Alice", "Bob", "Charlie", "Diana", "Eve"],
    dept_id = [10, 20, 10, 30, 20]
)

departments = DataFrame(
    dept_id = [10, 20, 30, 40],
    dept_name = ["Engineering", "Marketing", "HR", "Finance"]
)

println("Inner join:")
display(innerjoin(employees, departments, on=:dept_id))
println()

println("Left join:")
display(leftjoin(employees, departments, on=:dept_id))
println()

println("Right join:")
display(rightjoin(employees, departments, on=:dept_id))
println()

println("Outer join:")
display(outerjoin(employees, departments, on=:dept_id))
println()

# Join on different column names
sales = DataFrame(emp_id=[1, 2, 3], revenue=[1000, 2000, 1500])
println("Join on different column names (id => emp_id):")
display(innerjoin(employees, sales, on=:id => :emp_id))
println()

# Anti-join
println("Anti-join (employees NOT in sales):")
display(antijoin(employees, sales, on=:id => :emp_id))
println()

# Semi-join
println("Semi-join (employees who ARE in sales):")
display(semijoin(employees, sales, on=:id => :emp_id))
println()

# ============================================================
# Section: Reshaping -- stack and unstack
# ============================================================

println("\n=== Reshaping ===")

# Wide format
wide = DataFrame(
    country = ["France", "Germany", "Italy"],
    pop_2020 = [67.39, 83.24, 59.55],
    pop_2021 = [67.75, 83.16, 59.24],
    pop_2022 = [67.97, 84.08, 58.86]
)

println("Wide format:")
display(wide)
println()

# Wide -> Long (stack)
long = stack(wide, r"pop_", :country;
    variable_name=:year, value_name=:population)
println("Long format (stacked):")
display(long)
println()

# Clean the year column
transform!(long, :year => ByRow(y -> parse(Int, last(string(y), 4))) => :year)
println("With cleaned year column:")
display(long)
println()

# Long -> Wide (unstack)
wide_again = unstack(long, :country, :year, :population)
println("Wide format (unstacked):")
display(wide_again)
println()

# ============================================================
# Exercises
# ============================================================

println("\n=== Exercises ===")

# Exercise: Create student/grades DataFrames and join
students = DataFrame(
    id = [1, 2, 3, 4],
    name = ["Alice", "Bob", "Charlie", "Diana"],
    major = ["Math", "CS", "Math", "CS"]
)

grades = DataFrame(
    student_id = [1, 1, 2, 2, 3, 3, 4, 4],
    course = ["Calc", "Stats", "Calc", "ML", "Calc", "Stats", "ML", "Stats"],
    grade = [95, 88, 78, 92, 85, 90, 88, 82]
)

joined = innerjoin(students, grades, on=:id => :student_id)
println("Average grade per major:")
display(combine(groupby(joined, :major),
    :grade => mean => :avg_grade,
    nrow => :count
))
println()

# Exercise: Monthly sales reshape
products = ["Widget", "Gadget", "Doohickey", "Thingamajig"]
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
sales_wide = DataFrame(:Product => products)
for m in months
    sales_wide[!, Symbol(m)] = rand(100:500, 4)
end
println("Wide sales data:")
display(sales_wide)
println()

sales_long = stack(sales_wide, Not(:Product);
    variable_name=:Month, value_name=:Sales)
annual = combine(groupby(sales_long, :Product), :Sales => sum => :AnnualTotal)
println("Annual sales per product:")
display(annual)
println()
