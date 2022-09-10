import re

from student import Student


def create_student():
    student_id = input('Mã sinh viên: ')
    try:
        if is_student_id_valid(student_id):
            print('==> Mã học sinh hợp lệ!')
    except ValueError as e:
        print(e)
        student_id = None
    full_name = input('Họ và tên: ')
    try:
        if is_name_valid(full_name):
            print('==> Họ và tên hợp lệ')
    except ValueError as e:
        print(e)
        full_name = None
    age_str = input("Tuổi: ")
    try:
        if is_age_valid(age_str):
            print('==> Tuổi hợp lệ')
    except ValueError as e:
        print(e)
        age_str = '0'
    age = int(age_str)
    math_str = input('Điểm toán(hệ 10): ')
    physic_str = input('Điểm lý(hệ 10): ')
    english_str = input('Điểm tiếng Anh(hệ 10): ')
    if not is_grade_valid(math_str) or not \
            is_grade_valid(physic_str) or not \
            is_grade_valid(english_str):
        raise ValueError('Điểm không hợp lệ')
    math = float(math_str)
    physic = float(physic_str)
    english = float(english_str)
    if math > 10.0 or physic > 10.0 or english > 10.0:
        raise ValueError('Điểm không hợp lệ: điểm phải nằm trong khoảng [0.0, 10.0]')
    return Student(student_id, full_name, age, math, physic, english)


def is_grade_valid(grade):
    """Phương thức kiểm tra xem điểm có hợp lệ không. Điểm hợp lệ là số thực hệ 10."""
    pattern = "\\d*.\\d{1,3}"
    if not re.match(pattern, grade):
        return False
    return True


def is_age_valid(age_str):
    """
        Phương thức kiểm tra xem age_str có phải tuổi hợp lệ không.
        Tuổi hợp lệ chỉ chứa các kí tự số.
    """
    for c in age_str:
        if c < '0' or c > '9':
            raise ValueError(f'Tuổi không hợp lệ: {age_str}')
    return True


def is_name_valid(name):
    """
        Phương thức kiểm tra họ tên có hợp lệ không.
        Giả định họ tên hợp lệ chỉ chứa kí tự chữ cái và khoảng trắng.
    """
    if len(name.strip()) == 0:  # nếu chuỗi rỗng -> tên k hợp lệ
        raise ValueError(f'Họ và tên không hợp lệ: {name}')
    for c in name.lower():
        if not c.isalpha() and c != ' ':
            raise ValueError(f'Họ và tên không hợp lệ: {name}')
    return True


def is_student_id_valid(student_id):
    """
        Phương thức kiểm tra xem mã sinh viên có hợp lệ không.
        Mã hợp lệ chỉ chứa chữ cái và số.
    """
    if not student_id.isalnum():
        raise ValueError(f'Mã học sinh không hợp lệ: {student_id}. '
                         f'Ví dụ mã hợp lệ: HS1030')
    return True


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
