def create_course_id():
    couse_id = f'C{Course.AUTO_ID}'
    Course.AUTO_ID += 1
    return couse_id


class Course:
    """Lớp mô tả thông tin lớp học phần."""
    AUTO_ID = 100

    def __init__(self, cid='', name='', subject=None, teacher=None, room=''):
        self.course_id = cid
        self.name = name
        self.subject = subject
        self.teacher = teacher
        self.room = room
        self.transcripts = []

    @property
    def course_id(self):
        return self.__couse_id

    @course_id.setter
    def course_id(self, value):
        if value == '' or value is None:
            self.__couse_id = create_course_id()
        else:
            self.__couse_id = value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def subject(self):
        return self.__subject

    @subject.setter
    def subject(self, value):
        self.__subject = value

    @property
    def teacher(self):
        return self.__teacher

    @teacher.setter
    def teacher(self, value):
        self.__teacher = value

    @property
    def room(self):
        return self.__room

    @room.setter
    def room(self, value):
        self.__room = value

    @property
    def transcripts(self):
        return self.__transcripts

    @transcripts.setter
    def transcripts(self, value):
        self.__transcripts = value

    def __str__(self):
        return f'{self.course_id:10}{self.name:20}{self.subject.subject_id:<10}' \
               f'{self.subject.name:30}{self.teacher.teacher_id:10}' \
               f'{self.teacher.full_name.full_name:30}{self.room:10}'

    def __eq__(self, other):
        return other.course_id == self.course_id
