import abc
import re
from abc import abstractmethod
from datetime import datetime

from net.braniumacademy.chapter10.l1024.model.student import Student, FullName
from net.braniumacademy.chapter10.l1024.error.exceptions import *


class IStudentController(abc.ABC):
    @abstractmethod
    def add(self) -> Student:
        pass

    @abstractmethod
    def edit(self, student: Student) -> Student:
        pass

    @abstractmethod
    def remove(self, students: list[Student], _id: str) -> bool:
        pass

    @abstractmethod
    def search_by_name(self, students: list[Student], key: str) -> list[Student]:
        pass

    @abstractmethod
    def search_by_gpa(self, students: list[Student], key: float) -> list[Student]:
        pass

    @abstractmethod
    def search_by_birth_date(self, students: list[Student], key: int) -> list[Student]:
        pass

    @abstractmethod
    def search_by_birth_month(self, students: list[Student], key: int) -> list[Student]:
        pass

    @abstractmethod
    def search_by_birth_year(self, students: list[Student], key: int) -> list[Student]:
        pass

    @abstractmethod
    def sort_by_name(self, students: list[Student]):
        pass

    @abstractmethod
    def sort_by_gpa(self, students: list[Student]):
        pass

    @abstractmethod
    def sort_by_birth_date(self, students: list[Student]):
        pass

    @abstractmethod
    def sort_by_name_gpa(self, students: list[Student]):
        pass

    @abstractmethod
    def check_name_valid(self, name: str) -> bool:
        pass

    @abstractmethod
    def check_birth_date_valid(self, birth_date: str) -> bool:
        pass

    @abstractmethod
    def check_gpa_valid(self, gpa: float) -> bool:
        pass

    @abstractmethod
    def check_email_valid(self, email: str) -> bool:
        pass

    @abstractmethod
    def read_file(self, file_name: str) -> list[Student]:
        pass

    @abstractmethod
    def write_file(self, file_name: str, students: list[Student]):
        pass


class StudentController(IStudentController):
    def add(self) -> Student:
        pass

    def edit(self, student: Student) -> Student:
        pass

    def remove(self, students: list[Student], _id: str) -> bool:
        pass

    def search_by_name(self, students: list[Student], key: str) -> list[Student]:
        pass

    def search_by_gpa(self, students: list[Student], key: float) -> list[Student]:
        pass

    def search_by_birth_date(self, students: list[Student], key: int) -> list[Student]:
        pass

    def search_by_birth_month(self, students: list[Student], key: int) -> list[Student]:
        pass

    def search_by_birth_year(self, students: list[Student], key: int) -> list[Student]:
        pass

    def sort_by_name(self, students: list[Student]):
        students.sort(key=lambda x: (x.full_name.first_name, x.full_name.last_name))

    def sort_by_gpa(self, students: list[Student]):
        students.sort(key=lambda x: x.gpa, reverse=True)

    def sort_by_birth_date(self, students: list[Student]):
        students.sort(key=lambda x: x.birth_date.totalseconds())

    def sort_by_name_gpa(self, students: list[Student]):
        students.sort(key=lambda x: (-x.gpa, x.full_name.first_name, x.full_name.last_name))

    def check_name_valid(self, name: str) -> bool:
        # Họ tên gồm chữ cái, dấu cách, dài 2-40 kí tự
        # cho phép tên tiếng Việt
        pattern = pattern = '^([a-zẮẰẲẴẶĂẤẦẨẪẬÂÁÀÃẢẠĐẾỀỂỄỆÊÉÈẺẼẸÍÌỈĨỊỐỒỔỖỘÔỚỜỞỠ' \
                            'ỢƠÓÒÕỎỌỨỪỬỮỰƯÚÙỦŨỤÝỲỶỸỴ]+\\s?){2,40}$'
        matcher = re.search(pattern, name, flags=re.IGNORECASE)
        if len(name) > 40:
            msg = 'Name too long. Permit only up to 40 characters long'
            raise NameInvalidError(name, message=msg)
        elif matcher:
            return True
        else:
            raise NameInvalidError(name)

    def check_birth_date_valid(self, birth_date: str) -> bool:
        # ngày sinh chỉ có thể từ 01-31, tháng sinh từ 01-12 và năm sinh có 4 chữ số
        pattern = r'^(0[1-9]|[12][0-9]|[3][0-1])/(0[1-9]|1[0-2])/\d{4}$'
        matcher = re.search(pattern, birth_date)
        if matcher:
            return True
        else:
            raise BirthdateError(birth_date)

    def check_gpa_valid(self, gpa: float) -> bool:
        if 0 <= gpa <= 4.0:
            return True
        else:
            raise GpaError(gpa)

    def check_email_valid(self, email: str) -> bool:
        # email không chứa chữ cái tiếng Việt, không chứa khoảng trắng và kí tụ
        # không được phép như dấu cách, tab, các dấu /?><,*+$%&~!
        pattern = '^[a-z_]+[a-z]+[0-9._-]*@[a-z0-9]+.[a-z]{2,4}$'
        matcher = re.search(pattern, email, flags=re.IGNORECASE)
        if matcher:
            return True
        else:
            raise EmailError(email)

    def read_file(self, file_name: str) -> list[Student]:
        students = []
        with open(file_name, encoding='UTF-8') as reader:
            person_id = reader.readline().strip()
            while True:
                fname = reader.readline().strip().split()
                birth_date_str = reader.readline().strip()
                student_id = reader.readline().strip()
                email = reader.readline().strip()
                gpa = float(reader.readline())
                major = reader.readline().strip()
                first_name = fname[len(fname) - 1]
                last_name = fname[0]
                mid_name = ''
                for i in range(1, len(fname) - 1):
                    mid_name += fname[i] + ' '
                full_name = FullName(first_name, last_name, mid_name.strip())
                birth_date = datetime.strptime(birth_date_str, '%d/%m/%Y')
                student = Student(person_id, full_name,
                                  birth_date, student_id, email, gpa, major)
                students.append(student)
                person_id = reader.readline().strip()
                if person_id == '':
                    break
        return students

    def write_file(self, file_name: str, students: list[Student]):
        with open(file_name, 'w', encoding='UTF-8') as writer:
            for student in students:
                writer.write(f'{student.person_id}\n')
                writer.write(f'{student.full_name}\n')
                writer.write(f'{student.birth_date.strftime("%d/%m/%Y")}\n')
                writer.write(f'{student.student_id}\n')
                writer.write(f'{student.email}\n')
                writer.write(f'{student.gpa}\n')
                writer.write(f'{student.major}\n')
