from gatpy.csv_parser import CSVImport
from gatpy.constraints import ConstraintsSolver

import os

def main():
    team_count = 5

    filepath = os.getcwd() + "/student_list.csv"
    csv_import = CSVImport()
    student_list, course_count = csv_import.import_csv(filepath)

    print(course_count)

    cs = ConstraintsSolver(student_list, 4, 8, course_count)

    print(cs.solve())