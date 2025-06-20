import math

import constraint as pyc
from collections import Counter, defaultdict



class ConstraintsSolver:
    def __init__(self, students, group_ids, max_group_size, courses):
        self._list = students
        self.student_index = {x.id: x for x in students}
        self.group_ids = group_ids
        self.max_group_size = max_group_size
        self.max_size_per_course = self.create_course_max_value(courses, group_ids)

    def create_course_max_value(self, courses, group_count):
        course_max_value = dict()
        for course in courses:
            if (courses[course] % group_count) != 0:
                _max = math.ceil(courses[course] / group_count)
            else:
                _max = courses[course] // group_count

            course_max_value[course] = _max

            print(course.name,_max)

        return course_max_value


    def solve(self):
        problem = pyc.Problem()

        for row in self._list:
            problem.addVariable(row.id, list(range(self.group_ids)))

        problem.addConstraint(self.limit_group_size)
        problem.addConstraint(self.apply_avoid)
        problem.addConstraint(self.limit_group_makeup)

        return problem.getSolution()

    def limit_group_size(self, *row):
        c = Counter(row)
        for value in c.values():
            if value > self.max_group_size:
                return False
        return True

    def build_student_groups(self, row):
        student_groups = defaultdict(set)
        for idx, group_id in enumerate(row):
            student = self._list[idx]
            student_groups[group_id].add(student.id)

        return student_groups

    def apply_avoid(self, *row):
        student_groups = self.build_student_groups(row)

        for group_id, members in student_groups.items():
            for student in members:
                curr_student = self.student_index[student]
                if curr_student.avoid_list.intersection(members):
                    return False
        return True

    def limit_group_makeup(self, *row):
        student_groups = self.build_student_groups(row)

        for group_id, members in student_groups.items():
            group_makeup = defaultdict(int)

            for student in members:
                curr_student = self.student_index[student]
                group_makeup[curr_student.specialism] += 1

            for course, max_size in self.max_size_per_course.items():
                if max_size < group_makeup[course]:
                    print("sadness mode", max_size, group_makeup[course])
                    return False

        return True

