from exceptions import *


def is_grade_valid(grade):
    """Phương thức kiểm tra xem điểm có hợp lệ không. Điểm hợp lệ là số thực hệ 10."""
    for c in grade:
        if (c < '0' or c > '9') and c != '.':
            raise GradeError(grade, 'Điểm không hợp lệ.')
    else:
        if float(grade) > 10.0:
            raise GradeError(grade, 'Điểm phải nằm trong khoảng [0.0, 10.0]')
    return True


def is_age_valid(age_str):
    """
        Phương thức kiểm tra xem age_str có phải tuổi hợp lệ không.
        Tuổi hợp lệ chỉ chứa các kí tự số.
    """
    if not age_str.isdigit():
        raise StudentAgeError(age_str, f'Tuổi học sinh không hợp lệ')
    return True


def is_name_valid(name):
    """
        Phương thức kiểm tra họ tên có hợp lệ không.
        Giả định họ tên hợp lệ chỉ chứa kí tự chữ cái và khoảng trắng.
    """
    if len(name.strip()) < 2 or len(name.strip()) > 30:  # nếu chuỗi rỗng -> tên k hợp lệ
        raise FullNameError(name, f'Họ và tên không được quá 30 kí tự: {name}')
    for c in name.lower():
        if not c.isalpha() and c != ' ':
            raise FullNameError(name, f'Họ và tên chứa kí tự không hợp lệ: {name}')
    return True


def is_student_id_valid(student_id):
    """
        Phương thức kiểm tra xem mã sinh viên có hợp lệ không.
        Mã hợp lệ chỉ chứa chữ cái và số.
    """
    if not student_id.isalnum() or len(student_id) != 6:
        raise StudentIdError(student_id, 'Mã học sinh không hợp lệ')
    return True
