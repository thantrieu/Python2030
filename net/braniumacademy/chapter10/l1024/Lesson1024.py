import re

from controller.studentcontroller import StudentController
from view.studentview import StudentView

if __name__ == '__main__':
    controller = StudentController()
    students = controller.read_file('STUDENT.DAT')
    for s in students:
        print(s.full_name)
