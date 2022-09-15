from student import Student


def create_student():
    student_id = input('Mã học sinh: ')
    full_name = input('Họ và tên: ')
    age_str = input("Tuổi: ")
    math_str = input('Điểm toán(hệ 10): ')
    physic_str = input('Điểm lý(hệ 10): ')
    english_str = input('Điểm tiếng Anh(hệ 10): ')
    return Student(student_id.upper(), full_name, age_str,
                   math_str, physic_str, english_str)


def show_student_info(student):
    """Phương thức hiển thị thông tin học sinh."""
    title = f'{"Mã HS":12}{"Họ và tên":30}' \
            f'{"Tuổi":12}{"Toán":12}' \
            f'{"Lý":12}{"Anh":12}'
    if student is not None:
        print(title)
        print(student)
    else:
        print('==> Thông tin học sinh không đúng. <==')
