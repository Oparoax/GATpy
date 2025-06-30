from gatpy.csv_parser import CSVImport, CSVExport
from gatpy.constraints import ConstraintsSolver

import os

def main():
    team_size = 8
    group_size = 4

    filepath = os.getcwd() + "/student_list.csv"
    csv_import = CSVImport()
    student_list, course_count = csv_import.import_csv(filepath)

    cs = ConstraintsSolver(student_list.values(), group_size, team_size, course_count)

    result = cs.solve()

    if result:
        export_fpath = os.getcwd() + "/result.csv"
        csv_export = CSVExport()
        csv_export.export_csv(result, student_list, export_fpath)
    else:
        print("No solution found")

    print(result)
