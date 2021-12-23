from abc import ABC, abstractmethod


class Person(ABC):
    def __init__(self, pid, name):
        self.id = pid
        self.name = name

    @abstractmethod
    def work(self):
        pass

    # def __init__(self, id, name, major):
    #     self.student_id = id
    #     self.name = name
    #     self.major = major


class Student:
    """Lớp mô tả thông tin và hành động sinh viên"""
    student_count = 0  # Class variable

    def __init__(self, id='SV001', name='No Name', major='CNTT'):
        self.student_id = id  # Instance variable
        self.name = name  # Instance variable
        self.major = major  # Instance variable
        Student.student_count += 1  # Access class variable inside method

    def do_exam(self, subject):
        print(f'Student {self.name} is doing {subject} exam.')

    def work(self):
        print(f'Student {self.name} is working')

    def do_homework(self, subject):
        print(f'Student {self.name} is doing {subject} homework.')


oanh = Student(name="Oanh")  # Call constructor with one params
huong = Student(id="SV002", name="Huong")  # Call constructor with two params
lan = Student(id="SV003", name="Lan", major="QTKD")  # # Call constructor with full params

# huong = Student("SV001", "Huong", "CNTT")
# huong.do_exam('Python')
# huong.work()
# huong.do_homework('Math')

oanh = Student(name="Oanh")  # Call constructor with one params
huong = Student(id="SV002", name="Huong")  # Call constructor with two params
lan = Student(id="SV003", name="Lan", major="QTKD")  # # Call constructor with full params
oanh.gpa = 3.75  # Create instance variable outside method
print(oanh.gpa)  # Ok
print(huong.gpa)  # AttributeError
print(Person.gpa)  # AttributeError

print(f'{hasattr(lan, "name")}')  # True
print(f'{getattr(lan, "name")}')  # Lan
setattr(lan, 'name', 'Mai')  # Change value of attribute name to 'Mai'
print(f'{getattr(lan, "name")}')  # Mai
delattr(lan, 'name')  # Delete attribute name of lan
print(lan.name)  # AttributeError

print(f'Student.__doc__: {Student.__doc__}')
print(f'Student.__name__: {Student.__name__}')
print(f'Student.__module__: {Student.__module__}')
print(f'Student.__dict__: {Student.__dict__}')
print(f'Student.__bases__: {Student.__bases__}')
# Student.__doc__: Lớp mô tả thông tin và hành động sinh viên
# Student.__name__: Student
# Student.__module__: __main__
# Student.__dict__: {'__module__': '__main__',
# '__doc__': 'Lớp mô tả thông tin và hành động sinh viên',
# 'student_count': 3, '__init__': <function Student.__init__ at 0x00000266E68DCB80>,
# 'do_exam': <function Student.do_exam at 0x00000266E68DCC10>,
# 'work': <function Student.work at 0x00000266E68DCCA0>,
# 'do_homework': <function Student.do_homework at 0x00000266E68DCD30>,
# '__dict__': <attribute '__dict__' of 'Student' objects>,
# '__weakref__': <attribute '__weakref__' of 'Student' objects>}
# Student.__bases__: (<class 'object'>,)

# huong.do_exam('Python')
# huong.work()
# huong.do_homework('Math')
# huong.hello = "OK";
# print(huong.hello)

# class ClassName:
#     [docstring]
#     methods
#     variables
