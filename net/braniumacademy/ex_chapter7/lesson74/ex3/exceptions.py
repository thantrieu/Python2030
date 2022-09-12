class FullNameError(Exception):
    """
        Lớp mô tả ngoại lệ họ và tên không hợp lệ.
        Các thuộc tính:
            full_name: giá trị họ và tên gây ra ngoại lệ
            message: thông điệp mô tả về ngoại lệ đã xảy ra
    """

    def __init__(self, name, message):
        super().__init__(message)
        self.__full_name = name
        self.__message = message

    def __str__(self):
        return f'FullNameError: {self.__message} : {self.__full_name}'


class StudentIdError(Exception):
    """
        Lớp mô tả ngoại lệ mã sinh viên không hợp lệ.
        Các thuộc tính:
            student_id: giá trị mã sinh viên gây ra ngoại lệ
            message: thông điệp mô tả về ngoại lệ đã xảy ra
    """

    def __init__(self, student_id, message=''):
        super().__init__(message)
        self.__student_id = student_id
        self.__message = message

    def __str__(self):
        return f'StudentIdError: {self.__message} : {self.__student_id}'


class SubjectIdError(Exception):
    """
        Lớp mô tả ngoại lệ mã môn học không hợp lệ.
        Các thuộc tính:
            subject_id: giá trị mã đăng ký gây ra ngoại lệ
            message: thông điệp mô tả về ngoại lệ đã xảy ra
    """

    def __init__(self, subject_id, message=''):
        super().__init__(message)
        self.__subject_id = subject_id
        self.__message = message

    def __str__(self):
        return f'SubjectIdError: {self.__message} : {self.__subject_id}'


class TeacherIdError(Exception):
    """
        Lớp mô tả ngoại lệ mã giảng viên không hợp lệ.
        Các thuộc tính:
            teacher_id: giá trị mã giảng viên gây ra ngoại lệ
            message: thông điệp mô tả về ngoại lệ đã xảy ra
    """

    def __init__(self, teacher_id, message=''):
        super().__init__(message)
        self.__teacher_id = teacher_id
        self.__message = message

    def __str__(self):
        return f'TeacherIdError: {self.__message} : {self.__teacher_id}'


class CourseIdError(Exception):
    """
        Lớp mô tả ngoại lệ mã lớp học không hợp lệ.
        Các thuộc tính:
            course_id: giá trị mã lớp học gây ra ngoại lệ
            message: thông điệp mô tả về ngoại lệ đã xảy ra
    """

    def __init__(self, course_id, message=''):
        super().__init__(message)
        self.__course_id = course_id
        self.__message = message

    def __str__(self):
        return f'CourseIdError: {self.__message} : {self.__course_id}'


class TranscriptIdError(Exception):
    """
        Lớp mô tả ngoại lệ mã bảng điểm không hợp lệ.
        Các thuộc tính:
            transcript_id: giá trị mã bảng điểm gây ra ngoại lệ
            message: thông điệp mô tả về ngoại lệ đã xảy ra
    """

    def __init__(self, transcript_id, message=''):
        super().__init__(message)
        self.__transcript_id = transcript_id
        self.__message = message

    def __str__(self):
        return f'TranscriptIdError: {self.__message} : {self.__transcript_id}'


class GpaError(Exception):
    """
        Lớp mô tả ngoại lệ điểm gpa của sinh viên không hợp lệ.
        Các thuộc tính:
            gpa: giá trị gpa gây ra ngoại lệ
            message: thông điệp mô tả về ngoại lệ đã xảy ra
    """

    def __init__(self, gpa, message=''):
        super().__init__(message)
        self.__gpa = gpa
        self.__message = message

    def __str__(self):
        return f'GpaError: {self.__message} : {self.__gpa}'


class CreditError(Exception):
    """
        Lớp mô tả ngoại lệ số tín chỉ của môn học không hợp lệ.
        Các thuộc tính:
            credit: giá trị số tín chỉ gây ra ngoại lệ
            message: thông điệp mô tả về ngoại lệ đã xảy ra
    """

    def __init__(self, credit, message=''):
        super().__init__(message)
        self.__credit = credit
        self.__message = message

    def __str__(self):
        return f'GpaError: {self.__message} : {self.__credit}'


class BirthDateError(Exception):
    """
        Lớp mô tả ngoại lệ ngày sinh không hợp lệ.
        Các thuộc tính:
            birth_date: giá trị ngày sinh gây ra ngoại lệ
            message: thông điệp mô tả về ngoại lệ đã xảy ra
    """

    def __init__(self, birth_date, message=''):
        super().__init__(message)
        self.__birth_date = birth_date
        self.__message = message

    def __str__(self):
        return f'BirthDateError: {self.__message} : {self.__birth_date}'


class SalaryError(Exception):
    """
        Lớp mô tả ngoại lệ mức lương không hợp lệ.
        Các thuộc tính:
            salary: giá trị mức lương gây ra ngoại lệ
            message: thông điệp mô tả về ngoại lệ đã xảy ra
    """

    def __init__(self, salary, message=''):
        super().__init__(message)
        self.__salary = salary
        self.__message = message

    def __str__(self):
        return f'SalaryError: {self.__message} : {self.__salary}'
