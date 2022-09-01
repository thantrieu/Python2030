class FullName:
    """Lớp mô tả thông tin họ và tên."""
    def __init__(self, first, mid, last):
        self.__first = first
        self.__last = last
        self.__mid = mid

    @property
    def first_name(self):
        return self.__first

    @property
    def mid_name(self):
        return self.__mid

    @property
    def last_name(self):
        return self.__last

    @property
    def full_name(self):
        return self.__str__()

    def __str__(self):
        return f'{self.last_name} {self.mid_name} {self.first_name}'


class Employee:
    """Lớp mô tả thông tin nhân viên."""

    def __init__(self):
        self.__phone_number = None
        self.__email = None
        self.__full_name = None
        self.__emp_id = None
        self.__salary = None

    def __int__(self, emp_id, full_name, email, phone_number, salary):
        self.__emp_id = emp_id
        self.__full_name = full_name
        self.__email = email
        self.__phone_number = phone_number
        self.__salary = salary

    @property
    def emp_id(self):
        return self.__emp_id

    @emp_id.setter
    def emp_id(self, value):
        self.__emp_id = value

    @property
    def full_name(self):
        return self.__full_name

    @full_name.setter
    def full_name(self, value):
        self.__full_name = value

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, value):
        self.__email = value

    @property
    def phone_number(self):
        return self.__phone_number

    @phone_number.setter
    def phone_number(self, value):
        self.__phone_number = value

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, value):
        self.__salary = value

    def checkin(self, checkin_time):
        print(f"Employee {self.__full_name} check in at {checkin_time}.")

    def checkout(self, checkout_time):
        print(f"Employee {self.__full_name} check out at {checkout_time}.")

    def calculate_salary(self, working_day):
        real_salary = working_day / 22 * self.__salary
        return real_salary

    def work(self, some_work):
        print(f"Employee {self.__full_name} is doing {some_work}.")


class Manager(Employee):
    """Lớp mô tả thông tin người quản lý."""
    def __init__(self):
        super().__init__()
        self.__term = None
        self.__role = None
        self.__quater_salary = None

    def __int__(self, emp_id, full_name, email, phone_number, salary, role, term, quater_salary):
        super().__int__(emp_id, full_name, email, phone_number, salary)
        self.term = term
        self.role = role
        self.quater_salary = quater_salary
