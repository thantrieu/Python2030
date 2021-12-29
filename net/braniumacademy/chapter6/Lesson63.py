from net.braniumacademy.chapter6.student import Student


def read_file(file_name):
    mstudents = []
    with open(file_name, encoding='UTF-8') as reader:
        full_name = reader.readline().strip()
        while True:
            age = int(reader.readline())
            address = reader.readline().strip()
            gpa = float(reader.readline())
            mstudents.append(Student(full_name, age, address, gpa))
            full_name = reader.readline().strip()
            if full_name == '':
                break
    return mstudents


def show_students(mstudents):
    for student in mstudents:
        print(student)


path = 'input.txt'
students = read_file(path)
show_students(students)
