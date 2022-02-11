class Subject:
    def __init__(self, subject_id, name, credit, category):
        self.__subject_id = subject_id
        self.__name = name
        self.__credit = credit
        self.__category = category

    @property
    def subject_id(self):
        return self.__subject_id

    @subject_id.setter
    def subject_id(self, value):
        self.__subject_id = value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def credit(self):
        return self.__credit

    @credit.setter
    def credit(self, value):
        self.__credit = value

    @property
    def category(self):
        return self.__category

    @category.setter
    def category(self, value):
        self.__category = value
