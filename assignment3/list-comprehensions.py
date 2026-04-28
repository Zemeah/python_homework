import csv

# Task 3
employees = []
with open("../csv/employees.csv", newline="") as file:
    reader = csv.reader(file)
    employees = list(reader)

names = [row[0] + " " + row[1] for row in employees[1:]]

print("All names:")
print(names)

names_with_e = [name for name in names if "e" in name.lower()]

print("\nNames containing 'e':")
print(names_with_e)