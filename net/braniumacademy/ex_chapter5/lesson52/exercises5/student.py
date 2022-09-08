class Student:
    """Lớp mô tả thông tin sinh viên."""

    def __init__(self, student_id='', first='', last='', mid='',
                 address='', email='', gender='', faculty=''):
        self.student_id = student_id
        self.first_name = first
        self.last_name = last
        self.mid_name = mid
        self.address = address
        self.email = email
        self.gender = gender
        self.faculty = faculty
