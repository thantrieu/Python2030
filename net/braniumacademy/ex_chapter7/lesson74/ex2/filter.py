import re
from exceptions import *


def is_name_valid(name):
    """
        Phương thức kiểm tra họ tên có hợp lệ không.
        Giả định họ tên hợp lệ chỉ chứa kí tự chữ cái và khoảng trắng.
    """
    if len(name.strip()) < 2:
        raise FullNameError(name, 'Họ và tên quá ngắn')
    if len(name.strip()) > 40:
        raise FullNameError(name, 'Họ và tên quá dài')
    for c in name.lower():
        if not c.isalpha() and c != ' ':
            raise FullNameError(name, 'Họ và tên chứa kí tự không hợp lệ')
    return True


def is_subject_name_valid(name):
    """
        Phương thức kiểm tra tên môn học có hợp lệ không.
        Giả định họ tên hợp lệ chỉ chứa kí tự chữ cái, số và khoảng trắng.
    """
    if len(name.strip()) < 2:
        raise SubjectNameError(name, 'Tên môn học quá ngắn')
    if len(name.strip()) > 50:
        raise SubjectNameError(name, 'Tên môn học quá dài')
    for c in name.lower():
        if not c.isalnum() and c != ' ' and c != '+' and c != '#' and c != '.':
            raise SubjectNameError(name, 'Tên môn học không hợp lệ')
    return True


def is_person_id_valid(person_id):
    """
        Phương thức kiểm tra xem mã số CMND/CCCD có hợp lệ không.
        Mã hợp lệ nếu chỉ chứa chữ cái và số.
    """
    if len(person_id.strip()) == 0:  # nếu chuỗi rỗng -> id ko hợp lệ
        return False
    if not person_id.isalnum():  # nếu số cmnd/cccd có kí tự khác số và chữ cái
        return False  # mã k hợp lệ
    return True


def is_birth_date_valid(birth_date):
    """Phương thức kiểm tra xem ngày sinh có hợp lệ không."""
    if len(birth_date.strip()) < 10:
        raise BirthDateError(birth_date, 'Ngày sinh không đúng định dạng')
    pattern = '^\\d{2}/\\d{2}/\\d{4}$'  # chi tiết bạn vui lòng xem bài học 9.1
    if re.match(pattern, birth_date.strip()):
        return True
    raise BirthDateError(birth_date, 'Ngày sinh không hợp lệ')


def is_gpa_valid(gpa_str):
    """Phương thức kiểm tra xem giá trị gpa có hợp lệ không."""
    if len(gpa_str.strip()) == 0:
        raise GpaError(gpa_str, 'Điểm gpa không được để trống')
    pattern = '^\\d.\\d{1,2}$'  # chi tiết bạn vui lòng xem bài học 9.1
    if re.match(pattern, gpa_str):
        return True
    else:
        raise GpaError(gpa_str, 'Điểm gpa không hợp lệ')


def is_student_id_valid(student_id):
    """Phương thức kiểm tra mã sinh viên cho trước có hợp lệ không."""
    if len(student_id) == 0:
        raise StudentIdError(student_id, 'Mã sinh viên rỗng')
    pattern = 'SV\\d{4}'
    if re.match(pattern, student_id, re.IGNORECASE) and int(student_id[2:]) >= 1000:
        return True
    raise StudentIdError(student_id, 'Mã sinh viên không hợp lệ')


def is_credit_valid(credit_str):
    """Phương thức kiểm tra số tín chỉ có hợp lệ không."""
    if len(credit_str.strip()) == 0:
        raise CreditError(credit_str, 'Số tín chỉ không thể để trống')
    if credit_str.isdigit():
        return True
    raise CreditError(credit_str, 'Số tín chỉ không hợp lệ')


def is_subject_id_valid(value):
    """Phương thức kiểm tra xem mã môn học có hợp lệ không."""
    if re.match('^\\d{4}$', value) and 1000 <= int(value) < 10000:
        return True
    raise SubjectIdError(value, 'Mã môn học không hợp lệ')


def is_register_id_valid(value):
    """Phương thức kiểm tra xem mã đăng ký có hợp lệ không."""
    if re.match('\\d{4}', value) and int(value) >= 1000:
        return True
    raise RegisterIdError(value, 'Mã đăng ký không hợp lệ')
