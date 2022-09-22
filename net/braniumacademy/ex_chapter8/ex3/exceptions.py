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


class SubjectNameError(Exception):
    """
        Lớp mô tả ngoại lệ tên môn học không hợp lệ.
        Các thuộc tính:
            subject_name: giá trị tên gây ra ngoại lệ
            message: thông điệp mô tả về ngoại lệ đã xảy ra""
    """

    def __init__(self, name='', message=''):
        super(SubjectNameError, self).__init__(message)
        self.__name = name
        self.__message = message

    def __str__(self):
        return f'SubjectNameError: {self.__message}: {self.__name}'


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


class RegisterIdError(Exception):
    """
        Lớp mô tả ngoại lệ mã đăng ký không hợp lệ.
        Các thuộc tính:
            register_id: giá trị mã đăng ký gây ra ngoại lệ
            message: thông điệp mô tả về ngoại lệ đã xảy ra
    """

    def __init__(self, register_id, message=''):
        super().__init__(message)
        self.__register_id = register_id
        self.__message = message

    def __str__(self):
        return f'RegisterIdError: {self.__message} : {self.__register_id}'


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


class AddressError(Exception):
    """
        Lớp mô tả ngoại lệ địa chỉ không hợp lệ.
        Các thuộc tính:
            address: giá trị địa chỉ nơi ở gây ra ngoại lệ
            message: thông điệp mô tả về ngoại lệ đã xảy ra""
    """

    def __init__(self, address='', message=''):
        super().__init__(message)
        self.__address = address
        self.__message = message

    def __str__(self):
        return f'AddressError: {self.__message}: {self.__address}'
