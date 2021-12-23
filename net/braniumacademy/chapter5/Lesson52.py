class Student:
    """This class describe student infomation and behaviors"""

    def __init__(self, student_id, full_name, major, gpa):
        self.student_id = student_id
        self.major = major
        self.gpa = gpa
        self.set_full_name(full_name)
        self.full_name = self.last_name + ' ' + self.mid_name + self.first_name

    def set_full_name(self, full_name):
        words = full_name.split()
        self.last_name = words[0]
        self.first_name = words[len(words) - 1]
        self.mid_name = ''
        for i in range(1, len(words) - 1):
            self.mid_name += words[i] + ' '

    def show_info(self):
        print(f'[{self.student_id}, {self.full_name}, {self.major}, {self.gpa}]')


def create_student():
    print('========================================')
    id = input('Enter student id: ')
    full_name = input('Enter full name: ')
    major = input('Enter student major: ')
    gpa = float(input('Enter gpa: '))
    return Student(student_id=id, major=major, gpa=gpa, full_name=full_name)


students = []
n = int(input('Enter number of student: '))
for index in range(n):
    student = create_student()
    students.append(student)
students.sort(key=lambda x: x.gpa, reverse=True)
# Show students info
print('================== LIST OF STUDENTS ==================')
for s in students:
    s.show_info()
