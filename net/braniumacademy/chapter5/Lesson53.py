class Person:
    """This class describe person info and behaviors"""

    def __init__(self, first, mid, last, dob, gender):
        self.first = first
        self.last = last
        self.mid = mid
        self.birth_date = dob
        self.gender = gender

    def show_info(self):
        print(f'[Full name: {self.last} {self.mid} {self.first}, '
              f'Date of birth: {self.birth_date}, Gender: {self.gender}]')


class Employee(Person):
    def __init__(self, eid, first, mid, last, dob, gender, role, salary):
        super().__init__(first, mid, last, dob, gender)
        self.emp_id = eid
        self.role = role
        self.salary = salary

    def checkin(self, time):
        print(f'{self.first} checkin at {time}.')

    def calculate_salary(self, day):
        real_salary = 200 + self.salary / 22 * day
        print(f'Salary this month of {self.first} is {real_salary}$')


class Student(Person):
    def __init__(self, sid, first, mid, last, dob, gender, major, gpa):
        super().__init__(first, mid, last, dob, gender)
        # super(Student, self).__init__(first, mid, last, dob, gender)
        # Person.__init__(self, first, mid, last, dob, gender)
        self.student_id = sid
        self.gpa = gpa
        self.major = major

    def do_exam(self, subject):
        print(f'{self.first} is doing {subject} final exam.')


nam = Employee('NV001', 'Nam', 'Ba',
               'Tran', '22/10/2005', 'Nam', 'CEO', 50000)
nam.checkin('8:30')
nam.calculate_salary(13)
print("-----------------------------------------------------------")
linh = Student('SV001', 'Linh', 'Thuy',
               'Mai', '15/08/2005', 'Nu', 'CNTT', 3.75)
print(f'Student full name: {linh.last} {linh.mid} {linh.first}')
linh.show_info()
linh.do_exam('Python OOP')
