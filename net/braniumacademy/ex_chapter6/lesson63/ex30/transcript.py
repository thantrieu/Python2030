class Transcript:
    """Lớp mô tả thông tin về bảng điểm."""
    AUTO_ID = 100

    def __int__(self, tid=0, student=None, gpa=0.0, capacity=''):
        self.transcript_id = tid
        self.student = student
        self.gpa = gpa
        self.capacity = capacity

    @property
    def transcript_id(self):
        return self.__transcript_id

    @transcript_id.setter
    def transcript_id(self, value):
        if value == 0:
            self.__transcript_id = Transcript.AUTO_ID
            Transcript.AUTO_ID += 1
        else:
            self.__transcript_id = value

    @property
    def student(self):
        return self.__student

    @student.setter
    def student(self, value):
        self.__student = value

    @property
    def gpa(self):
        return self.__gpa

    @gpa.setter
    def gpa(self, value):
        self.__gpa = value

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, value):
        self.__capacity = value

    def __str__(self):
        return f'{self.transcript_id:10}{self.student.student_id:10}' \
               f'{self.gpa:<10}{self.capacity:15}'

    def __eq__(self, other):
        return self.__transcript_id == other.transcript_id
