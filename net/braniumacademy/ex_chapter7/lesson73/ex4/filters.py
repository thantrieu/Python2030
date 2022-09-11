import re


def is_grade_valid(grade):
    """Phương thức kiểm tra xem điểm có hợp lệ không. Điểm hợp lệ là số thực hệ 10."""
    pattern = "\\d*.\\d{1,3}"
    if not re.match(pattern, grade):
        raise ValueError(f'Điểm không hợp lệ: {grade}')
    else:
        if float(grade) > 10.0:
            raise ValueError('Điểm không hợp lệ. Điểm phải nằm trong khoảng [0.0, 10.0]')
    return True


def is_age_valid(age_str):
    """
        Phương thức kiểm tra xem age_str có phải tuổi hợp lệ không.
        Tuổi hợp lệ chỉ chứa các kí tự số.
    """
    if not age_str.isdigit():
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
