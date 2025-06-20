from gatpy.csv import CSVImport
import os

def main():
    filepath = os.getcwd() + "\student_list.csv"
    csv_import = CSVImport()
    df = csv_import.import_csv(filepath)
    student_list, course_count = csv_import.parse_df(df)
