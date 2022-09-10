import re


def is_name_valid(name):
    """
        Phương thức kiểm tra họ tên có hợp lệ không.
        Giả định họ tên hợp lệ chỉ chứa kí tự chữ cái và khoảng trắng.
    """
    if len(name.strip()) == 0:  # nếu chuỗi rỗng -> tên k hợp lệ
        return False
    if 2 <= len(name) <= 30:
        for c in name.lower():
            if not c.isalpha() and c != ' ':
                return False
        return True
    else:
        return False


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
        return False
    pattern = '^\\d{2}/\\d{2}/\\d{4}$'  # chi tiết bạn vui lòng xem bài học 9.1
    if re.match(pattern, birth_date.strip()):
        return True
    return False


def is_gpa_valid(gpa_str):
    """Phương thức kiểm tra xem giá trị gpa có hợp lệ không."""
    if len(gpa_str.strip()) == 0:
        return False
    pattern = '^\\d.\\d{1,2}$'  # chi tiết bạn vui lòng xem bài học 9.1
    if re.match(pattern, gpa_str):
        return True
    else:
        return False


def is_credit_valid(credit_str):
    """Phương thức kiểm tra số tín chỉ có hợp lệ không."""
    if len(credit_str.strip()) == 0:
        return False
    if credit_str.isdigit() and 1 <= int(credit_str) <= 15:
        return True
    return False


def is_salary_valid(salary_str):
    """Phương thức kiểm tra mức lương có hợp lệ không."""
    if salary_str.strip().isdigit() and int(salary_str) > 0:  # nếu là các con số
        return True
    return False
