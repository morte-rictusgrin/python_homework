# Task 2: Read a CSV File

import csv
import traceback
import os
import custom_module
from datetime import datetime


def read_employees():
    employees_data = {}
    rows = []
    try:
        with open("../csv/employees.csv", "r") as file:
            reader = csv.reader(file)
            for i, row in enumerate(reader):
                if i == 0:
                    employees_data["fields"] = row
                else:
                    rows.append(row)
            employees_data["rows"] = rows
            return employees_data
    except Exception as e:
        trace_back = traceback.extract_tb(e.__traceback__)
        stack_trace = list()
        for trace in trace_back:
            stack_trace.append(
                f"File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}"
            )
        print(f"Exception type: {type(e).__name__}")
        message = str(e)
        if message:
            print(f"Exception message: {message}")
        print(f"Stack trace: {stack_trace}")


employees = read_employees()
print(employees)

# Task 3: Find the Column Index


def column_index(column):
    return employees["fields"].index(column)


employee_id_column = column_index("employee_id")


# Task 4: Find the Employee First Name


def first_name(row_number):
    index = column_index("first_name")
    return employees["rows"][row_number][index]


# print(first_name(4))

# Task 5: Find the Employee: a Function in a Function


def employee_find(employee_id):
    def employee_match(row):
        return int(row[employee_id_column]) == employee_id

    matches = list(filter(employee_match, employees["rows"]))
    return matches


# print(employee_find(18))

# Task 6: Find the Employee with a Lambda


def employee_find_2(employee_id):
    matches = list(
        filter(
            lambda row: int(row[employee_id_column]) == employee_id, employees["rows"]
        )
    )
    return matches


# Task 7: Sort the Rows by last_name Using a Lambda


def sort_by_last_name():

    last_name_index = column_index("last_name")
    employees["rows"].sort(key=lambda row: row[last_name_index])
    return employees["rows"]
    print(employees)
# print(sort_by_last_name())

# Task 8: Create a dict for an Employee

def employee_dict(row):
    empl_dict = {}
    for i, field in enumerate(employees["fields"]):
        if field != "employee_id":
            empl_dict[field] = row[i]
    return empl_dict

# Task 9: A dict of dicts, for All Employees

def all_employees_dict():
    result = {}
    for row in employees["rows"]:
        employee_id = row[column_index("employee_id")]
        result[employee_id] = employee_dict(row)

    return result
# print(all_employees_dict())    

# Task 10: Use the os Module

def get_this_value():
    return os.getenv("THISVALUE")

# Task 11: Creating Your Own Module

def set_that_secret(new_secret):
    custom_module.set_secret(new_secret)
# set_that_secret("kotik")
# print(custom_module.secret)

# Task 12: Read minutes1.csv and minutes2.csv

def read_minutes_file(path):
    minutes_data = {"fields": [], "rows": []}
    try:
        with open(path, "r") as file:
            reader = csv.reader(file)
            for i, row in enumerate(reader):
                if i == 0:
                    minutes_data["fields"] = row
                else: 
                    minutes_data["rows"].append(tuple(row))
    except Exception as e:
        trace_back = traceback.extract_tb(e.__traceback__)
        stack_trace = list()
        for trace in trace_back:
            stack_trace.append(
                f"File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}"
            )
        print(f"Exception type: {type(e).__name__}")
        message = str(e)
        if message:
            print(f"Exception message: {message}")
        print(f"Stack trace: {stack_trace}")

    return minutes_data

def read_minutes():

    minutes1 = read_minutes_file("../csv/minutes1.csv")
    minutes2 = read_minutes_file("../csv/minutes2.csv")
    return minutes1, minutes2
minutes1, minutes2 = read_minutes()
# print(minutes1)

# Task 13: Create minutes_set

def create_minutes_set():
    set1 = set(minutes1["rows"])
    set2 = set(minutes2["rows"])
    combined_set = set1.union(set2)

    return combined_set
minutes_set = create_minutes_set()

# Task 14: Convert to datetime

def create_minutes_list():
    minutes_list = list(minutes_set)
    converted_data = list(map(
        lambda x: (x[0], datetime.strptime(x[1], "%B %d, %Y")), minutes_list))
    return converted_data
minutes_list = create_minutes_list()

# Task 15: Write Out Sorted List

def write_sorted_list():
    sorted_minutes = sorted(minutes_list, key = lambda x: (x[1]))
    converted_list = list(map(lambda x: (x[0], datetime.strftime(x[1], "%B %d, %Y")), sorted_minutes))
    try:
        with open("./minutes.csv", "w") as file:
            writer = csv.writer(file)
            writer.writerow(minutes1["fields"])
            for row in converted_list:
                writer.writerow(row)
    except Exception as e:
        trace_back = traceback.extract_tb(e.__traceback__)
        stack_trace = list()
        for trace in trace_back:
            stack_trace.append(
                f"File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}"
            )
        print(f"Exception type: {type(e).__name__}")
        message = str(e)
        if message:
            print(f"Exception message: {message}")
        print(f"Stack trace: {stack_trace}")

    return converted_list
sorted_minutes_final = write_sorted_list()








    



    

