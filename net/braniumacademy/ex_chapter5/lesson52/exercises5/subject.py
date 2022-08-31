class Subject:
    """Lớp Subject dùng để mô tả thông tin của môn học."""
    def __init__(self, id, name, credit, lesson, test):
        self.id = id
        self.name = name
        self.credit = credit
        self.lesson = lesson
        self.test = test
