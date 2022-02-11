class Register:
    def __init__(self, reg_id=0, student=None, subject=None, reg_time=None):
        self.__register_id = reg_id
        self.__student = student
        self.__subject = subject
        self.__register_time = reg_time

    @property
    def register_id(self):
        return self.__register_id

    @register_id.setter
    def register_id(self, value):
        self.__register_id = value

    @property
    def student(self):
        return self.__student

    @student.setter
    def student(self, value):
        self.__student = value

    @property
    def subject(self):
        return self.__subject

    @subject.setter
    def subject(self, value):
        self.__subject = value

    @property
    def register_time(self):
        return self.__register_time

    @register_time.setter
    def register_time(self, value):
        self.__register_time = value
