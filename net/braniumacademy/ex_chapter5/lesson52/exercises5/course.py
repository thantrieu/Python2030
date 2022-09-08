class Course:
    def __init__(self, course_id='', name='', room='', time='', subject=None):
        self.course_id = course_id
        self.name = name
        self.room = room
        self.time = time
        self.subject = subject
        self.transcripts = []  # danh sách bảng điểm
