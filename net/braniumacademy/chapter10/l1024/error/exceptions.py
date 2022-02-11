class GpaError(Exception):
    def __init__(self, value, message='GPA out of range [0.0, 4.0]'):
        super(GpaError, self).__init__(value, message)
        self.__invalid_gpa = value
        self.__message = message

    def __str__(self):
        return f'GpaError: {self.__message}: {self.__invalid_gpa}'


class NameInvalidError(Exception):
    def __init__(self, value, message='Name contain invalid character'):
        super(NameInvalidError, self).__init__(value, message)
        self.__invalid_name = value
        self.__message = message

    def __str__(self):
        return f'NameInvalidError: {self.__message}: {self.__invalid_name}'


class BirthdateError(Exception):
    def __init__(self, value, message='Invalid birthdate'):
        super(BirthdateError, self).__init__(value, message)
        self.__invalid_birthdate = value
        self.__message = message

    def __str__(self):
        return f'BirthdateError: {self.__message}: {self.__invalid_birthdate}'


class EmailError(Exception):
    def __init__(self, value, message='Invalid email'):
        super(EmailError, self).__init__(value, message)
        self.__invalid_email = value
        self.__message = message

    def __str__(self):
        return f'EmailError: {self.__message}: {self.__invalid_email}'
