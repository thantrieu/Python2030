import datetime

from person import FullName
from student import Student
from subject import Subject
from teacher import Teacher
from course import Course
from transcript import Transcript


def decode_full_name(fname):
    if 'first' in fname:
        return FullName(fname['first'], fname['mid'], fname['last'])
    else:
        return fname


def decode_student(dct):
    if 'person_id' in dct:
        pid = dct['person_id']
        name = decode_full_name(dct['full_name'])
        birth_date = datetime.datetime.strptime(dct['birth_date'], '%d/%m/%Y')
        student_id = dct['student_id']
        gpa = float(dct['gpa'])
        major = dct['major']
        return Student(pid, name, birth_date, student_id, major, gpa)
    else:
        return dct


def decode_subject(dct):
    if 'subject_id' in dct:
        subject_id = int(dct['subject_id'])
        name = dct['subject_name']
        credit = int(dct['credit'])
        return Subject(subject_id, name, credit)
    else:
        return None


def decode_teacher(dct):
    if 'person_id' in dct:
        pid = dct['person_id']
        name = decode_full_name(dct['full_name'])
        birth_date = datetime.datetime.strptime(dct['birth_date'], '%d/%m/%Y')
        teacher_id = dct['teacher_id']
        salary = int(dct['salary'])
        expertise = dct['expertise']
        return Teacher(pid, name, birth_date, teacher_id, salary, expertise)
    else:
        return dct


def decode_course(dct):
    if 'course_id' in dct:
        course_id = dct['course_id']
        course_name = dct['course_name']
        subject_id = int(dct['subject_id'])
        teacher_id = dct['teacher_id']
        room = dct['room']
        return Course(course_id, course_name, subject_id, teacher_id, room)
    else:
        return dct


def decode_transcript(dct):
    if 'transcript_id' in dct:
        tran = Transcript()
        tran.transcript_id = dct['transcript_id']
        tran.course_id = dct['course_id']
        tran.student = dct['student_id']
        tran.gpa = float(dct['gpa'])
        tran.capacity = dct['capacity']
        return tran
    else:
        return dct
