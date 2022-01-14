import json


class StudentEncoder(json.JSONEncoder):
    """Lớp mã hóa thông tin sinh viên."""

    def default(self, obj):
        return obj.__dict__


class SubjectEncoder(json.JSONEncoder):
    """Lớp mã hóa thông tin môn học."""

    def default(self, obj):
        return obj.__dict__


class RegisterEncoder(json.JSONEncoder):
    """Lớp mã hóa thông tin đăng ký."""

    def default(self, obj):
        return obj.__dict__
