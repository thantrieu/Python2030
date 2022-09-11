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


class StudentAgeError(Exception):
    """
        Lớp mô tả ngoại lệ tuổi học sinh không hợp lệ.
        Các thuộc tính:
            age: giá trị tuổi học sinh gây ra ngoại lệ
            message: thông điệp mô tả về ngoại lệ đã xảy ra
    """

    def __init__(self, age, message=''):
        super().__init__(message)
        self.__age = age
        self.__message = message

    def __str__(self):
        return f'StudentAgeError: {self.__message} : {self.__age}'


class GradeError(Exception):
    """
        Lớp mô tả ngoại lệ điểm của học sinh không hợp lệ.
        Các thuộc tính:
            grade: giá trị tuổi học sinh gây ra ngoại lệ
            message: thông điệp mô tả về ngoại lệ đã xảy ra
    """

    def __init__(self, grade, message=''):
        super().__init__(message)
        self.__grade = grade
        self.__message = message

    def __str__(self):
        return f'GradeError: {self.__message} : {self.__grade}'
