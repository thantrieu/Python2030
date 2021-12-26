class Transcript:
    """Lớp mô tả thông tin và hành vi của bảng điểm."""

    def __init__(self, tid, student, grade1, grade2, grade3):
        self.gpa = 0.0
        self.capacity = ''
        self.transcript_id = tid
        self.student = student
        self.grade1 = grade1
        self.grade2 = grade2
        self.grade3 = grade3
        self.calculate_gpa()
        self.calculate_capacity()

    def calculate_gpa(self):
        self.gpa = 0.1 * self.grade1 + 0.2 * self.grade2 + 0.7 * self.grade3

    def calculate_capacity(self):
        if 9.0 <= self.gpa <= 10.0:
            self.capacity = "Xuất sắc"
        elif 8.0 <= self.gpa < 9.0:
            self.capacity = "Giỏi"
        elif 6.5 <= self.gpa < 8:
            self.capacity = "Khá"
        elif 5.0 <= self.gpa < 6.5:
            self.capacity = 'Trung bình'
        elif 4.0 <= self.gpa < 5.0:
            self.capacity = 'Trung bình yếu'
        else:
            self.capacity = 'Trượt môn'
