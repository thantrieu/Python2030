import re
from exceptions import *


def is_grade_valid(grade):
    """Phương thức kiểm tra xem điểm có hợp lệ không. Điểm hợp lệ là số thực hệ 10."""
    # điểm nhập vào hợp lệ có dạng 5 hoặc 5.25 hoặc 5.5
    if not re.match('(\\d{1,2}.\\d{1,2})|(\\d{1,2})', grade):
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
    if not re.match('\\d{1,3}', age_str):
        raise StudentAgeError(age_str, f'Tuổi học sinh không hợp lệ')
    elif int(age_str) < 4 or int(age_str) > 100:
        raise StudentAgeError(age_str, f'Tuổi học sinh phải nằm trong khoảng [4, 100]')
    return True


def is_name_valid(name):
    """
        Phương thức kiểm tra họ tên có hợp lệ không.
        Giả định họ tên hợp lệ chỉ chứa kí tự chữ cái và khoảng trắng.
    """
    if len(name.strip()) < 2 or len(name.strip()) > 30:  # nếu chuỗi rỗng -> tên k hợp lệ
        raise FullNameError(name, f'Họ và tên phải có từ 2-30 kí tự')
    elif not re.match(r'\w+', name, re.IGNORECASE):
        raise FullNameError(name, f'Họ và tên chứa kí tự không hợp lệ')
    return True


def is_student_id_valid(student_id):
    """
        Phương thức kiểm tra xem mã sinh viên có hợp lệ không.
        Mã hợp lệ chỉ chứa chữ cái và số dạng HSxxxx.
    """
    if not re.match('HS\\d{4}', student_id, re.IGNORECASE):
        raise StudentIdError(student_id, 'Mã học sinh không đúng định dạng, ví dụ HS0025')
    return True
