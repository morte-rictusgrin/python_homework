# Task 1: Introduction to Pandas - Creating and Manipulating DataFrames
# Subtask 1.1: Create a DataFrame from a dictionary:

import pandas as pd  # Importing Pandas
import numpy as np  # Importing NumPy

# These lines were added to perform the test successfully ignoring future behaviour warnings.
# import warnings
# warnings.simplefilter(action='ignore', category=FutureWarning)

data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["New York", "Los Angeles", "Chicago"],
}

df = pd.DataFrame(data)
print("1.1: Initial data:\n", df, "\n")

task1_data_frame = df

# Subtask 1.2: adding new column as a list

task1_with_salary = task1_data_frame.copy(deep=True)
task1_with_salary.loc[:, "Salary"] = [
    70000,
    80000,
    90000,
]  ## Changed erroneously added 7000, 8000, 9000.
print("1.2: Added salary to the table:\n", task1_with_salary, "\n")


# Subtask 1.3: Modifying the existing column

task1_older = task1_with_salary.copy(deep=True)

# going through extracting the column and modifying it, then replacing original Age in the dataframe:

# og_series = task1_older['Age'].copy()
# older_series = og_series + 1
# task1_older['Age'] = older_series

# Another approach: direct assignment with in-place:

task1_older.loc[:, "Age"] += 1

print("1.3: A year later...:\n", task1_older, "\n")


# Subtask 1.4: Save the DataFrame as a CSV file

task1_older.to_csv("employees.csv", sep=",", index=False, header=True, encoding=None)

print("1.4: task1_older is saved to employees.csv", "\n")


# Task 2: Loading Data from CSV and JSON

# Subtask 2.1: Read data from a CSV file

df = pd.read_csv("employees.csv")  # Reading DataFrame from the csv
task2_employees = df  # Saving read data to variable
print("2.1: Reading data from csv:\n", task2_employees, "\n")  # printing result

# Subtask 2.2: Read data from a JSON file

json_employees = pd.read_json("additional_employees.json")
print("2.2: New employees to add from json:\n", json_employees, "\n")

# Subtask 2.3: Combine DataFrames

more_employees = pd.concat([task2_employees, json_employees], ignore_index=True)
print("2.3: New table with all employees:\n", more_employees, "\n")

# Task 3: Data Inspection - Using Head, Tail, and Info Methods

# Subtask 3.1: Use the head() method
first_three = more_employees.head(3)
print("3.1: First three employees from the table:\n", first_three, "\n")

# Subtask 3.2: Use the tail() method
last_two = more_employees.tail(2)
print("3.2: Last two employees from the table:\n", last_two, "\n")

# Subtask 3.3: Get the shape of a DataFrame
employee_shape = more_employees.shape
print("3.3: Table shape is: ", employee_shape, "\n")

# Subtask 3.4: Use the info() method

print("3.4: DataFrame information is following:\n", more_employees.info(), "\n")

# Task 4: Data Cleaning
# Subtask 4.1: Create a DataFrame from dirty_data.csv file and assign it to the variable dirty_data.
dirty_data = pd.read_csv("dirty_data.csv")
print("4.1: New initial data to clean up:\n", dirty_data, "\n")
clean_data = dirty_data.copy(deep=True)

# Subtask 4.2: Remove any duplicate rows from the DataFrame

clean_data = clean_data.drop_duplicates()
print("4.2: After cleaning-up the duplicates:\n", clean_data, "\n")

# Subtask 4.3: Convert Age to numeric and handle missing values

clean_data.loc[:, "Age"] = pd.to_numeric(
    clean_data["Age"], errors="coerce"
)  # converting all values in Age to numeric.
clean_data["Age"] = clean_data["Age"].astype("float64")
print("4.3: Converted Age to numeric format:\n", clean_data, "\n")
clean_data.info()

# Subtask 4.4: Convert Salary to numeric and replace known placeholders (unknown, n/a) with NaN

clean_data.loc[:, "Salary"] = pd.to_numeric(clean_data["Salary"], errors="coerce")
clean_data["Salary"] = clean_data["Salary"].astype("float64")
print("4.4: Converted Salary to numeric, cleaned-up placeholders:\n", clean_data, "\n")
clean_data.info()

# Subtask 4.5: Fill missing numeric values (use fillna).  Fill Age which the mean and Salary with the median
mean_age = clean_data["Age"].mean()
median_salary = clean_data["Salary"].median()
print(
    "Calculating mean age to use as placeholder for unknown age. Mean age is",
    mean_age,
    "\n",
)
print(
    "Calculating median salary to use as placeholder if salary is unknown. Median salary is",
    median_salary,
    "\n",
)
clean_data.loc[:, "Age"] = clean_data["Age"].fillna(mean_age)
clean_data.loc[:, "Salary"] = clean_data["Salary"].fillna(median_salary)
print("Normalized data now is:\n", clean_data, "\n")

# Subtask 4.6: Convert Hire Date to datetime
clean_data.loc[:, "Hire Date"] = pd.to_datetime(
    clean_data["Hire Date"], format="mixed", errors="coerce"
)
print("Table with recognizeable Hire date:\n", clean_data, "\n")

# Subtask 4.7: Strip extra whitespace and standardize Name and Department as uppercase
clean_data.loc[:, "Name"] = clean_data["Name"].str.strip().str.upper()
clean_data.loc[:, "Department"] = clean_data["Department"].str.strip().str.upper()

print("Cleaned-up DataFrame:\n", clean_data)
