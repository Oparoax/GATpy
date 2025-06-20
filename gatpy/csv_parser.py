from collections import defaultdict
import csv

from gatpy.models import Student, SPECIALISM

class CSVImport:
    def import_csv(self, filepath):
        student_list = []
        course_count = defaultdict(int)

        with open(filepath) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                data  = self.parse_row(row)

                if data is not None:
                    student_list.append(data)
                    course_count[data.specialism] += 1
                    print(data.id, data.name, data.specialism, str(data.avoid_list))

        return student_list, course_count

    def parse_row(self, row):
        specialism = self.what_course(row['course'])
        if specialism is None:
            return None

        if row['avoid_list'] is None or row['avoid_list'] == '':
            avoid_list = []
        else:
            avoid_list = str(row['avoid_list']).split('|')

        return Student(row['student_id'], row['name'], specialism, avoid_list)

    def what_course(self, course):
        if "Game Art" in course:
            specialism = SPECIALISM.ART
        elif "Game Development: Art" in course:
            specialism = SPECIALISM.ART
        elif "Animation" in course:
            specialism = SPECIALISM.ANIMATION
        elif "Design" in course:
            specialism = SPECIALISM.DESIGN
        elif "Writing" in course:
            specialism = SPECIALISM.WRITING
        elif "Programming" in course:
            specialism = SPECIALISM.PROGRAMMING
        elif "Computing" in course:
            specialism = SPECIALISM.PROGRAMMING
        elif "Esports" in course:
            specialism = SPECIALISM.ESPORTS
        else:
            print("Course not recognised: " + course)
            return None

        return specialism