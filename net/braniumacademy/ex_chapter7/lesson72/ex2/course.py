from datetime import datetime

from student import Student
from subject import Subject


class Course:
    """Lớp mô tả lớp đăng ký"""
    AUTO_ID = 100

    def __init__(self, cid=0, rtime=None, student=None, subject=None):
        self.course_id = cid
        self.register_time = rtime
        self.student = student
        self.subject = subject

    @property
    def course_id(self):
        return self.__course_id

    @course_id.setter
    def course_id(self, value):
        self.__course_id = value

    @property
    def register_time(self):
        return self.__register_time

    @register_time.setter
    def register_time(self, value):
        if value is not None:
            self.__register_time = value
        else:
            self.__register_time = datetime.now

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

    def __str__(self):
        return f'{self.course_id:<10}{self.student.student_id:15}' \
               f'{self.subject.subject_id:15}{self.register_time:30}'
