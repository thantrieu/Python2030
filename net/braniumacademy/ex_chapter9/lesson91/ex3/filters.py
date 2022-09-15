import re
from exceptions import *


def is_name_valid(name):
    """
        Phương thức kiểm tra họ tên có hợp lệ không.
        Giả định họ tên hợp lệ chỉ chứa kí tự chữ cái và khoảng trắng.
        Độ dài tên hợp lệ từ 2-30 kí tự.
    """
    if 2 <= len(name) <= 30:
        for c in name.lower():
            if not c.isalpha() and c != ' ':
                raise FullNameError(name, 'Họ và tên chứa kí tự không hợp lệ')
        return True
    else:
        raise FullNameError(name, 'Họ và tên quá ngắn hoặc quá dài')


def is_birth_date_valid(birth_date):
    """Phương thức kiểm tra xem ngày sinh có hợp lệ không."""
    if len(birth_date.strip()) < 10:
        return False
    pattern = '^\\d{2}/\\d{2}/\\d{4}$'  # chi tiết bạn vui lòng xem bài học 9.1
    if re.match(pattern, birth_date.strip()):
        return True
    raise BirthDateError(birth_date, 'Ngày sinh không đúng định dạng')


def is_gpa_valid(gpa_str):
    """Phương thức kiểm tra xem giá trị gpa có hợp lệ không."""
    if len(gpa_str.strip()) == 0:
        raise GpaError(gpa_str, 'Điểm gpa không được để trống')
    pattern = '^\\d{1}.\\d{1,2}$'  # chi tiết bạn vui lòng xem bài học 9.1
    if re.match(pattern, gpa_str) and 0.0 <= float(gpa_str) <= 4.0:
        return True
    else:
        raise GpaError(gpa_str, 'Điểm gpa không hợp lệ')


def is_credit_valid(credit_str):
    """Phương thức kiểm tra số tín chỉ có hợp lệ không."""
    if len(credit_str.strip()) == 0:
        raise CreditError(credit_str, 'Số tín chỉ không thể bỏ trống')
    if credit_str.isdigit() and 1 <= int(credit_str) <= 15:
        return True
    raise CreditError(credit_str, 'Số tín chỉ không hợp lệ')


def is_salary_valid(salary_str):
    """Phương thức kiểm tra mức lương có hợp lệ không."""
    if salary_str.strip().isdigit() and int(salary_str) > 0:  # nếu là các con số
        return True
    raise SalaryError(salary_str, 'Mức lương không hợp lệ')


def is_subject_id_valid(subject_id):
    """Phương thức kiểm tra mã môn học có hợp lệ không."""
    if subject_id.isdigit() and int(subject_id) >= 1000:
        return True
    raise SubjectIdError(subject_id, 'Mã môn học không hợp lệ')


def is_transcript_id_valid(transcript_id):
    """Phương thức kiểm tra mã bảng điểm có hợp lệ không."""
    if transcript_id.isdigit() and int(transcript_id) >= 100:
        return True
    raise TranscriptIdError(transcript_id, 'Mã bảng đăng ký không hơp lệ')


def is_student_id_valid(student_id):
    """Phương thức kiểm tra mã sinh viên có hợp lệ không."""
    pattern = '^SV\\d{4}$'
    if len(student_id) == 6 and re.match(pattern, student_id, re.IGNORECASE):
        if int(student_id[2:]) >= 1000:
            return True
    raise StudentIdError(student_id, 'Mã sinh viên không hợp lệ')


def is_teacher_id_valid(teacher_id):
    """Phương thức kiểm tra mã giảng viên có hợp lệ không."""
    pattern = '^GV\\d{4}$'
    if len(teacher_id) == 6 and re.match(pattern, teacher_id, re.IGNORECASE):
        if int(teacher_id[2:]) >= 1001:
            return True
    raise TeacherIdError(teacher_id, 'Mã giảng viên không hợp lệ')


def is_course_id_valid(course_id):
    """Phương thức kiểm tra mã lớp học có hợp lệ không."""
    pattern = '^C\\d{3}$'
    if len(course_id) == 4 and re.match(pattern, course_id, re.IGNORECASE):
        if int(course_id[1:]) >= 100:
            return True
    raise CourseIdError(course_id, 'Mã khóa học không hợp lệ')
