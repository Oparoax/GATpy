from enum import Enum

class SPECIALISM(Enum):
    ART= 0
    ANIMATION = 1
    DESIGN =2
    WRITING = 3
    PROGRAMMING = 4
    ESPORTS = 5

class Student:
    def __init__(self, id, name, specialism, no_list):
        self.id = id
        self.name = name
        self.specialism = specialism
        self.avoid_list = set(no_list)

class Team:
    def __init__(self, student_list):
        self.student_list = student_list
