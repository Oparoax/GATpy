from enum import Enum

class SPECIALISM(Enum):
    GD_ART= 0
    ANIMATION = 1
    DESIGN =2
    WRITING = 3
    GD_PROGRAMMING = 4
    CFG_PROGRAMMING = 5
    ESPORTS = 9
    G_ART = 10

class Student:
    def __init__(self, id, name, specialism, no_list):
        self.id = id
        self.name = name
        self.specialism = specialism
        self.no_list = no_list

class Team:
    def __init__(self, student_list):
        self.student_list = student_list
