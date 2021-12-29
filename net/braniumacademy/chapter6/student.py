class Student:
    def __init__(self, name, age, address, gpa):
        self.full_name = name
        self.age = age
        self.address = address
        self.gpa = gpa

    def __str__(self):
        return f'Student[full_name={self.full_name}, ' \
               f'age={self.age}, address={self.address}, gpa={self.gpa}]'
