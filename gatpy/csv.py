from collections import defaultdict

import pandas as pd
from gatpy.models import Student, SPECIALISM

class CSVImport:
    def import_csv(self, filepath):
        df = pd.read_csv(filepath)
        return df

    def parse_df(self, df):
        student_list = []
        course_count = defaultdict(int)

        for index, row in df.iterrows():
            specialism = self.what_course(row['course'])
            if specialism is None:
                break

            if row['avoid_list'] is None or row['avoid_list'] == '':
                avoid_list = []
            else:
                avoid_list = str(row['avoid_list']).split('|')

            student_list.append(Student(row['student_id'], row['name'], specialism, avoid_list))

            course_count[specialism] += 1

            print(row['name'] + " " + specialism.name + " " + avoid_list.__str__())

        return student_list, course_count

    def what_course(self, course):
        if "Art" in course:
            specialism = SPECIALISM.ART
        elif "Animation" in course:
            specialism = SPECIALISM.ANIMATION
        elif "Design" in course:
            specialism = SPECIALISM.DESIGN
        elif "Writing" in course:
            specialism = SPECIALISM.DESIGN
        elif "Programming" in course:
            specialism = SPECIALISM.GD_PROGRAMMING
        elif "Science" in course:
            specialism = SPECIALISM.CS_PROGRAMMING
        elif "Software" in course:
            specialism = SPECIALISM.SE_PROGRAMMING
        elif "Computing" in course:
            specialism = SPECIALISM.CFG_PROGRAMMING
        elif "Robotics" in course:
            specialism = SPECIALISM.ROBOTICS
        elif "Esports" in course:
            specialism = SPECIALISM.ESPORTS
        else:
            print("Course not recognised: " + course)
            return None

        return specialism