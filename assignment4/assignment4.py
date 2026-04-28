import pandas as pd
import numpy as np

# Task 1
data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["New York", "Los Angeles", "Chicago"]
}

task1_data_frame = pd.DataFrame(data)
print("Original DataFrame:")
print(task1_data_frame)


task1_with_salary = task1_data_frame.copy()
task1_with_salary["Salary"] = [70000, 80000, 90000]

print("\nDataFrame with Salary:")
print(task1_with_salary)


task1_older = task1_with_salary.copy()
task1_older["Age"] = task1_older["Age"] + 1

print("\nDataFrame with Age incremented:")
print(task1_older)


task1_older.to_csv("employees.csv", index=False)

# Task 2
task2_employees = pd.read_csv("employees.csv")
print("CSV Data:")
print(task2_employees)


json_employees = pd.read_json("additional_employees.json")
print("\nJSON Data:")
print(json_employees)


more_employees = pd.concat([task2_employees, json_employees], ignore_index=True)
print("\nCombined Data:")
print(more_employees)

# Task 3
first_three = more_employees.head(3)
print("First three rows:")
print(first_three)


last_two = more_employees.tail(2)
print("\nLast two rows:")
print(last_two)


employee_shape = more_employees.shape
print("\nShape of DataFrame:")
print(employee_shape)


print("\nDataFrame Info:")
more_employees.info()

# Task 4
dirty_data = pd.read_csv("dirty_data.csv")
print("Original Dirty Data:")
print(dirty_data)


clean_data = dirty_data.copy()


clean_data = clean_data.drop_duplicates()
print("\nAfter removing duplicates:")
print(clean_data)


clean_data["Age"] = pd.to_numeric(clean_data["Age"], errors="coerce")
print("\nAfter converting Age to numeric:")
print(clean_data)


clean_data["Salary"] = clean_data["Salary"].replace(["unknown", "n/a"], pd.NA)
clean_data["Salary"] = pd.to_numeric(clean_data["Salary"], errors="coerce")
print("\nAfter cleaning Salary:")
print(clean_data)


clean_data["Age"] = clean_data["Age"].fillna(clean_data["Age"].mean())
clean_data["Salary"] = clean_data["Salary"].fillna(clean_data["Salary"].median())
print("\nAfter filling missing values:")
print(clean_data)


clean_data["Hire Date"] = pd.to_datetime(clean_data["Hire Date"], errors="coerce")
clean_data["Hire Date"] = clean_data["Hire Date"].fillna(pd.Timestamp("2000-01-01"))
print("\nAfter converting Hire Date:")
print(clean_data)


clean_data["Name"] = clean_data["Name"].str.strip()
clean_data["Department"] = clean_data["Department"].str.strip().str.upper()
print("\nFinal Cleaned Data:")
print(clean_data)