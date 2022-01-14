from datetime import datetime
import json


class StudentEncoder(json.JSONEncoder):
    """Lớp mã hóa thông tin sinh viên."""

    def default(self, obj):
        return {
            "id": obj.person_id,
            "full_name": {
                "first": obj.full_name.first_name,
                "mid": obj.full_name.mid_name,
                "last": obj.full_name.last_name
            },
            "birth_date": {
                "day": obj.birth_date.day,
                "month": obj.birth_date.month,
                "year": obj.birth_date.year
            },
            "student_id": obj.student_id,
            "gpa": obj.gpa,
            "major": obj.major
        }


class SubjectEncoder(json.JSONEncoder):
    """Lớp mã hóa thông tin môn học."""

    def default(self, obj):
        return {"subject_id": obj.subject_id,
                "subject_name": obj.name, "credit": obj.credit}


class RegisterEncoder(json.JSONEncoder):
    """Lớp mã hóa thông tin đăng ký."""

    def default(self, obj):
        dt = datetime.strftime(obj.register_time, '%d/%m/%Y %H:%M:%S')
        return {"id": obj.register_id, "subject_id": obj.subject.subject_id,
                "student_id": obj.student.student_id,
                "register_time": dt
                }
