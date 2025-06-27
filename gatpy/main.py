from gatpy.csv_parser import CSVImport
from gatpy.constraints import ConstraintsSolver
from ortools.sat.python import cp_model

import os

def main():
    team_count = 5

    filepath = os.getcwd() + "/student_list.csv"
    csv_import = CSVImport()
    student_list, course_count = csv_import.import_csv(filepath)

    cs = ConstraintsSolver(student_list, 4, 8, course_count)

    result = cs.solve()

    print(result)
