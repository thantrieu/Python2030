class AgeError(Exception):
    """Lớp cha chung giám sát ngoại lệ liên quan tới tuổi."""

    def __init__(self, age, message=''):
        self.age = age
        self.message = message

    def __str__(self):
        return f'{self.message}: {self.age}'


class AgeTooLowError(AgeError):
    def __init__(self, age, message='Tuổi quá thấp'):
        super(AgeTooLowError, self).__init__(age, message)


class AgeTwoHightError(AgeError):
    def __init__(self, age, message='Tuổi quá cao'):
        super(AgeTwoHightError, self).__init__(age, message)
