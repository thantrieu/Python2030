from datetime import datetime

from Exercises1 import Subject, Student, FullName, BirthDate, Register


def decode_birth_date(birth_date):
    if 'day' in birth_date:
        day = int(birth_date['day'])
        month = int(birth_date['month'])
        year = int(birth_date['year'])
        return BirthDate(day, month, year)
    else:
        return birth_date


def decode_full_name(fname):
    if 'first' in fname:
        return FullName(fname['first'], fname['mid'], fname['last'])
    else:
        return fname


def decode_student(dct):
    if 'id' in dct:
        pid = dct['id']
        name = decode_full_name(dct['full_name'])
        birth_date = decode_birth_date(dct['birth_date'])
        student_id = dct['student_id']
        gpa = float(dct['gpa'])
        major = dct['major']
        return Student(pid, name, birth_date, gpa, major, student_id)
    else:
        return dct


def decode_subject(dct):
    if 'subject_id' in dct:
        sid = int(dct['subject_id'])
        name = dct['subject_name']
        credit = int(dct['credit'])
        return Subject(name, credit, sid)
    else:
        return None


def decode_register(dct):
    if 'register_time' in dct:
        rid = int(dct['id'])
        subject_id = int(dct['subject_id'])
        student_id = dct['student_id']
        mformat = '%d/%m/%Y %H:%M:%S'
        date_time_str = dct['register_time']
        reg_time = datetime.strptime(date_time_str, mformat)
        return Register(rid, student_id, subject_id, reg_time)
    else:
        return dct
