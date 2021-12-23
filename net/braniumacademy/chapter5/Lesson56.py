class Person:
    def __int__(self, fname, gender, dob):
        self.__full_name = fname
        self.__gender = gender
        self.__birth_date = dob

    def eat(self, food):
        print(f'{self.__full_name} is eating {food}')

    def __str__(self):
        return f'[{self.__full_name}, {self.__gender}, {self.__birth_date}]'


class Student(Person):
    def __init__(self, sid, fname, gender, dob, gpa):
        super(Student, self).__init__(fname, gender, dob)
        self.__student_id = sid
        self.__gpa = gpa

    def do_exam(self, subject):  # Truy cập __full_name từ trong lớp con của Person
        print(f'Student {self._Person__full_name} is doing {subject} final exam.')

    def update_gpa(self, gpa):
        self.__gpa = gpa

    def __str__(self):
        return f'Student[Person{super(Student, self).__str__()}, ' \
               f'__student_id={self.__student_id}, __gpa={self.__gpa}]'


loan = Person("Nguyen Thi Loan", "Female", "12/05/2005")
# print(f'Birth date: {loan._dob}')
print(loan)
hung = Student("SV001", "Long Quoc Hung", "Male", "15/08/2005", 3.35)
hung.do_exam('Python OOP')
hung.update_gpa(3.55)
print(f'GPA: {hung._Student__gpa}')
print(hung)
