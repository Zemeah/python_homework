import csv
import traceback
import os
import custom_module
from datetime import datetime

# Task 2
def read_employees():
    data = {}
    rows = []

    try:
        with open("../csv/employees.csv", "r") as file:
            reader = csv.reader(file)

            for i, row in enumerate(reader):
                if i == 0:
                    data["fields"] = row
                else:
                    rows.append(row)

        data["rows"] = rows

        return data
    
    except Exception as e:
        trace_back = traceback.extract_tb(e.__traceback__)
        stack_trace = []
        
        for trace in trace_back:
            stack_trace.append(
                f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}')

        print(f"Exception type: {type(e).__name__}")
        message = str(e)
        if message:
            print(f"Exception message: {message}")
        print(f"Stack trace: {stack_trace}")
        exit()

employees = read_employees()

# Task 3
def column_index(column_name):
    return employees["fields"].index(column_name)

employee_id_column = column_index("employee_id")

# print(column_index("last_name"))

# Task 4
def first_name(row_number):
    index = column_index("first_name")
    return employees["rows"][row_number][index]

# Task 5
def employee_find(employee_id):
    def employee_match(row):
        return int(row[employee_id_column]) == employee_id
    
    matches = list(filter(employee_match, employees["rows"]))

    return matches

# Task 6
def employee_find_2(employee_id):
    matches = list(filter(lambda row: int(row[employee_id_column]) == employee_id, employees["rows"]))
    return matches

# Task 7
def sort_by_last_name():
    index = column_index("last_name")
    employees["rows"].sort(key=lambda row: row[index])
    return employees["rows"]

# Task 8
def employee_dict(row):
    result = {}

    for i, field in enumerate(employees["fields"]):
        if field != "employee_id":
            result[field] = row[i]

    return result

# Task 9
def all_employees_dict():
    result = {}

    for row in employees["rows"]:
        emp_id = row[employee_id_column]
        result[emp_id] = employee_dict(row)

    return result

# Task 10
def get_this_value():
    return os.getenv("THISVALUE")

# print(get_this_value())

# Task 11
def set_that_secret(new_secret):
    custom_module.set_secret(new_secret)

set_that_secret("apples")
# print(custom_module.secret)

# Task 12
def read_csv_to_dict(file_path):
    data = {}
    rows = []

    with open(file_path, "r") as file:
        reader = csv.reader(file)

        for i, row in enumerate(reader):
            if i == 0:
                data["fields"] = row
            else:
                rows.append(tuple(row)) 
    data["rows"] = rows
    return data

def read_minutes():
    try:
        minutes1 = read_csv_to_dict("../csv/minutes1.csv")
        minutes2 = read_csv_to_dict("../csv/minutes2.csv")

        return minutes1, minutes2

    except Exception as e:
        trace_back = traceback.extract_tb(e.__traceback__)
        stack_trace = []

        for trace in trace_back:
            stack_trace.append(
                f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}'
            )

        print(f"Exception type: {type(e).__name__}")
        message = str(e)
        if message:
            print(f"Exception message: {message}")
        print(f"Stack trace: {stack_trace}")
        exit()

minutes1, minutes2 = read_minutes()

# print(minutes1)
# print(minutes2)

def create_minutes_set():
    set1 = set(minutes1["rows"])
    set2 = set(minutes2["rows"])

    combined = set1.union(set2)

    return combined

minutes_set = create_minutes_set()

# Task 13
def create_minutes_list():
    minutes = list(minutes_set)

    converted = list(
        map(lambda x: (x[0], datetime.strptime(x[1], "%B %d, %Y")), minutes)
    )

    return converted

minutes_list = create_minutes_list()

# Task 14
def write_sorted_list():
    minutes_list.sort(key=lambda x: x[1])

    converted = list(
        map(lambda x: (x[0], x[1].strftime("%B %d, %Y")), minutes_list)
    )

    with open("minutes.csv", "w", newline="") as file:
        writer = csv.writer(file)

        writer.writerow(minutes1["fields"])  # header
        writer.writerows(converted)          # data rows

    return converted

write_sorted_list()