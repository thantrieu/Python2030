import re
from exceptions import *


def is_grade_valid(grade):
    """Phương thức kiểm tra xem điểm có hợp lệ không. Điểm hợp lệ là số thực hệ 10."""
    # điểm nhập vào hợp lệ có dạng 3 hoặc 3.25 hoặc 3.25
    if not re.match('(\\d.\\d{1,2})|(\\d)', grade):
        raise GradeError(grade, 'Điểm không hợp lệ.')
    else:
        if float(grade) > 4.0:
            raise GradeError(grade, 'Điểm phải nằm trong khoảng [0.0, 4.0]')
    return True


def is_birth_date_valid(birth_date):
    """
        Phương thức kiểm tra xem birth_date có phải là ngày sinh hợp lệ không.
    """
    if not re.match(r'\d{2}/\d{2}/\d{4}', birth_date.strip()):
        raise StudentAgeError(birth_date, f'Ngày sinh không hợp lệ')
    return True


def is_name_valid(name):
    """
        Phương thức kiểm tra họ tên có hợp lệ không.
        Giả định họ tên hợp lệ chỉ chứa kí tự chữ cái và khoảng trắng.
    """
    if len(name.strip()) < 2 or len(name.strip()) > 30:  # nếu chuỗi rỗng -> tên k hợp lệ
        raise FullNameError(name, f'Họ và tên phải có từ 2-30 kí tự')
    elif re.match(r'\W+|.*[0-9_]+.*', name, re.UNICODE):
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
