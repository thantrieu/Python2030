import json


class StudentEncoder(json.JSONEncoder):
    """Lớp mã hóa thông tin sinh viên."""

    def default(self, obj):
        return {
            "person_id": obj.person_id,
            "full_name": {
                "first": obj.full_name.first_name,
                "mid": obj.full_name.mid_name,
                "last": obj.full_name.last_name
            },
            "birth_date": obj.birth_date.strftime('%d/%m/%Y'),
            "student_id": obj.student_id,
            "gpa": obj.gpa,
            "major": obj.major
        }


class SubjectEncoder(json.JSONEncoder):
    """Lớp mã hóa thông tin môn học."""

    def default(self, obj):
        return {
            "subject_id": obj.subject_id,
            "subject_name": obj.name,
            "credit": obj.credit
        }


class TeacherEncoder(json.JSONEncoder):
    """Lớp mã hóa thông tin giảng viên."""

    def default(self, obj):
        return {
            "person_id": obj.person_id,
            "full_name": {
                "first": obj.full_name.first_name,
                "mid": obj.full_name.mid_name,
                "last": obj.full_name.last_name
            },
            "birth_date": obj.birth_date.strftime('%d/%m/%Y'),
            "teacher_id": obj.teacher_id,
            "salary": obj.salary,
            "expertise": obj.expertise
        }


class CourseEncoder(json.JSONEncoder):
    """Lớp mã hóa thông tin lớp học."""

    def default(self, obj):
        return {
            "course_id": obj.course_id,
            "course_name": obj.name,
            "subject_id": obj.subject.subject_id,
            "teacher_id": obj.teacher.teacher_id,
            "room": obj.room
        }


class TranscriptEncoder(json.JSONEncoder):
    """Lớp mô tả thông tin bảng điểm của sinh viên."""

    def default(self, obj):
        return {
            "transcript_id": obj.transcript_id,
            "course_id": obj.course_id,
            "student_id": obj.student.student_id,
            "gpa": obj.gpa,
            "capacity": obj.capacity
        }
