class Subject:
    """Lớp Subject dùng để mô tả thông tin của môn học."""
    def __init__(self, sid='', name='', credit=0, lesson=0, test=0):
        self.subject_id = sid
        self.name = name
        self.credit = credit
        self.lesson = lesson
        self.test = test
