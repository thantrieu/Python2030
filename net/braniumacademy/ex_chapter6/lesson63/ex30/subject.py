def create_subject_id():
    sid = Subject.AUTO_ID
    Subject.AUTO_ID += 1
    return sid


class Subject:
    AUTO_ID = 1000

    def __init__(self, subject_id=0, name='', credit=0):
        if subject_id == 0:
            self.__subject_id = create_subject_id()
        else:
            self.__subject_id = subject_id
        self.__name = name
        self.__credit = credit

    @property
    def name(self):
        return self.__name

    @property
    def credit(self):
        return self.__credit

    @property
    def subject_id(self):
        return self.__subject_id

    def __str__(self):
        return f'{self.subject_id:<15}{self.name:35}{self.credit:<15}'

    def __eq__(self, other):
        """Hai môn học gọi là trùng khớp nếu chúng cùng mã môn."""
        return self.subject_id == other.subject_id
