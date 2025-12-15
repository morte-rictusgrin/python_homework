# Task 3: List Comprehensions Practice
import csv
import os
import traceback

def read_employees():
    names_list = []
    try:
        with open("../csv/employees.csv", "r") as file:
            reader = csv.reader(file)
            rows = list(reader)
            # for row in rows[1:]:
            #  names_list.append(row[1] + " " + row[2])
            names_list = [row[1] + " " + row[2] for row in rows[1:]]
        return names_list
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


result = read_employees()
print(result)


def employees_with_e(names_list):
    e_list = [item for item in names_list if "e" in item]
    return e_list


result = read_employees()
e_names = employees_with_e(result)
print(e_names)
