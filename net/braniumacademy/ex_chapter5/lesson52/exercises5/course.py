class Course:
    def __int__(self, cid=0, name='', room='', time='', subject=None):
        self.course_id = cid
        self.name = name
        self.room = room
        self.time = time
        self.subject = subject
        self.transcript = []  # danh sách bảng điểm
