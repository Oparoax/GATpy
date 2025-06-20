from gatpy.csv_parser import CSVImport
import os

def main():
    team_count = 5

    filepath = os.getcwd() + "/student_list.csv"
    csv_import = CSVImport()
    student_list, course_count = csv_import.import_csv(filepath)
