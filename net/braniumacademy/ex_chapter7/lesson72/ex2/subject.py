from exercises2_utils import is_credit_valid


class Subject:
    """Lớp mô tả thông tin môn học"""
    AUTO_ID = 1000

    def __init__(self, sid=None, name='', credit=''):
        self.subject_id = sid
        self.subject_name = name
        self.credit = credit

    @property
    def subject_id(self):
        return self.__subject_id

    @property
    def subject_name(self):
        return self.__subject_name

    @property
    def credit(self):
        return self.__credit

    @credit.setter
    def credit(self, value):
        if is_credit_valid(value):
            self.__credit = int(value)
        else:
            self.__credit = 0
            raise ValueError('Số tín chỉ không hợp lệ')

    @subject_id.setter
    def subject_id(self, value):
        if value is None:
            self.__subject_id = Subject.AUTO_ID
            Subject.AUTO_ID += 1
        else:
            self.__subject_id = value

    @subject_name.setter
    def subject_name(self, value):
        self.__subject_name = value

    def __str__(self):
        return f'{self.subject_id:15}{self.subject_name: 30}{self.credit:<15}'
