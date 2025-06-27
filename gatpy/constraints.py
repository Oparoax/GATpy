import math

from ortools.sat.python import cp_model
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
        problem = cp_model.CpModel()

        vars = {}
        for row in self._list:
            for group in range(self.group_ids):
                vars[(row.id, group)] = problem.new_bool_var("{}_{}".format(row.id, group))


        # A student can only be attached to a single group
        for row in self._list:
            problem.add_at_most_one(vars[(row.id, group)] for group in range(self.group_ids))

        # A team can only be as big as the max group size
        for group in range(self.group_ids):
            group_vars = []
            for row in self._list:
                group_vars.append(vars[(row.id, group)])
            problem.add(sum(group_vars) <= self.max_group_size)

        # A team cannot consist of team members who have avoided each other
        for group in range(self.group_ids):
            for row in self._list:
                student_1_var = vars[(row.id, group)]

                for avoidee in row.avoid_list:
                    student_2_var = vars[(avoidee.id, group)]

                    problem.add(not (student_1_var and student_2_var))

        student_specialism = defaultdict(list)
        for row in self._list:
            student_specialism[row.specialism].append(row.id)

        for group in range(self.group_ids):

            for (specialism,students) in student_specialism.items():
                spec_student_vars = []
                for student in students:
                    spec_student_vars.append(vars[(student, group)])

                problem.add(sum(spec_student_vars) <= self.max_size_per_course[specialism])

        solver = cp_model.CpSolver()

        # Solve.
        status = solver.solve(problem)
        print(status)

        return status

    def build_student_groups(self, row):
        student_groups = defaultdict(set)
        for idx, group_id in enumerate(row):
            student = self._list[idx]
            student_groups[group_id].add(student.id)

        return student_groups