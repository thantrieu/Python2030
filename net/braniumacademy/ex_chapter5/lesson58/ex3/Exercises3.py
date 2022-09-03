class FullName:
    """Lớp mô tả thông tin họ và tên."""

    def __init__(self, first, mid, last):
        self.__first = first
        self.__last = last
        self.__mid = mid

    @property
    def first_name(self):
        return self.__first

    @first_name.setter
    def first_name(self, value):
        self.__first = value

    @property
    def mid_name(self):
        return self.__mid

    @mid_name.setter
    def mid_name(self, value):
        self.__mid = value

    @property
    def last_name(self):
        return self.__last

    @last_name.setter
    def last_name(self, value):
        self.__last = value

    @property
    def full_name(self):
        return self.__str__()

    def __str__(self):
        return f'{self.last_name} {self.mid_name} {self.first_name}'


class Employee:
    """Lớp mô tả thông tin nhân viên."""
    AUTO_ID = 1000

    def __int__(self):
        self.__emp_id = ''
        self.__full_name = None
        self.__email = ''
        self.__phone_number = ''
        self.__salary = 0

    @property
    def emp_id(self):
        return self.__emp_id

    @emp_id.setter
    def emp_id(self, value):
        if value is None or value == '':
            self.__emp_id = f'EMP{Employee.AUTO_ID + 1}'
            Employee.AUTO_ID += 1
        else:
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

    def __str__(self):
        return f'{self.emp_id:<12}{self.full_name.full_name:30}' \
               f'{self.email:30}{self.phone_number:15}{self.salary:<12}'

    def __eq__(self, other):
        return self.emp_id == other.emp_id


class Manager(Employee):
    """Lớp mô tả thông tin người quản lý."""

    def __int__(self):
        super().__int__()
        self.__term = ''
        self.__role = ''
        self.__quater_salary = 0

    @property
    def term(self):
        return self.__term

    @term.setter
    def term(self, value):
        self.__term = value

    @property
    def role(self):
        return self.__role

    @role.setter
    def role(self, value):
        self.__role = value

    @property
    def quater_salary(self):
        return self.__quater_salary

    @quater_salary.setter
    def quater_salary(self, value):
        self.__quater_salary = value

    def meeting(self, partner):
        print(f"Giám đốc {self.full_name} đang họp với đối tác {partner}.")

    def sign(self, document):
        print(f"Giám đốc đang duyệt văn bản {document}.")

    def calculate_salary(self, working_day):
        return super().calculate_salary(working_day) + \
               0.8 * self.quater_salary

    def __str__(self):
        return f'{super().__str__()}{self.term:12}{self.role:20}{self.quater_salary:12}'


class Developer(Employee):
    """Lớp mô tả thông tin của lập trình viên."""

    def __init__(self):
        self.__role = ''
        self.__number_of_planguage = 0
        self.__number_of_project = 0
        self.__monthly_kpi = 0

    @property
    def role(self):
        return self.__role

    @role.setter
    def role(self, value):
        self.__role = value

    @property
    def num_of_language(self):
        return self.__number_of_planguage

    @num_of_language.setter
    def num_of_language(self, value):
        self.__number_of_planguage = value

    @property
    def num_of_project(self):
        return self.__number_of_project

    @num_of_project.setter
    def num_of_project(self, value):
        self.__number_of_project = value

    @property
    def monthly_kpi(self):
        return self.__monthly_kpi

    @monthly_kpi.setter
    def monthly_kpi(self, value):
        self.__monthly_kpi = value

    def receive_task(self, task):
        print(f"Lập trình viên {self.full_name} đã nhận task {task}.")

    def solve(self, task):
        print(f"Lập trình viên {self.full_name} đang thực hiện task {task}.")

    def fix(self, task):
        print(f"Lập trình viên {self.full_name} đang fix bugs task {task}.")

    def report(self, task, manager):
        print(f"Lập trình viên {self.full_name} "
              f"đang làm báo cáo task {task} "
              f"cho quản lý {manager.full_name}.")

    def calculate_salary(self, working_day):
        base_salary = super().calculate_salary(working_day)
        bonus = base_salary * 0.3 / 100 * self.monthly_kpi
        return base_salary + bonus

    def __str__(self):
        return f'{super().__str__()}{self.role:20}{self.num_of_language:<12}' \
               f'{self.num_of_project:<12}{self.monthly_kpi:<12}'


class Tester(Employee):
    def __init__(self):
        self.__role = ''
        self.__tools = []
        self.__error_found = 0
        self.__number_of_testcase = 0

    @property
    def role(self):
        return self.__role

    @property
    def tools(self):
        return self.__tools

    @property
    def error_found(self):
        return self.__error_found

    @property
    def number_of_testcase(self):
        return self.__number_of_testcase

    @role.setter
    def role(self, value):
        self.__role = value

    @tools.setter
    def tools(self, value):
        self.__tools = value

    @error_found.setter
    def error_found(self, value):
        self.__error_found = value

    @number_of_testcase.setter
    def number_of_testcase(self, value):
        self.__number_of_testcase = value

    def receive_project(self, project_name):
        print(f"Tester {self.full_name} đã nhận dự án {project_name}.")

    def prepare_testcase(self, project_name):
        print(f"Tester {self.full_name} "
              f"đang chuẩn bị testcase cho dự án {project_name}.")

    def test(self, function):
        print(f"Tester {self.full_name} đang test chức năng {function}.")

    def report(self, error_name, dev_name):
        print(f"Tester {self.full_name} "
              f"đã report {error_name} đến dev {dev_name}.")

    def calculate_salary(self, working_day):
        base_salary = super().calculate_salary(working_day)
        bonus = base_salary * 0.2 / 100 * self.number_of_testcase + 50 * self.error_found
        return base_salary + bonus

    def __str__(self):
        return f'{super().__str__()}{self.role:20}{self.tools[0]:20}' \
               f'{self.error_found:<12}{self.number_of_testcase:<12}'


class Task:
    """Lớp mô tả công việc."""
    AUTO_ID = 1000

    def __init__(self):
        self.__task_id = ''
        self.__task_name = ''
        self.__estimated_time = 0

    @property
    def task_id(self):
        return self.__task_id

    @task_id.setter
    def task_id(self, value):
        if value is None or value == '':
            self.__task_id = f"T{Task.AUTO_ID + 1}"
            Task.AUTO_ID += 1  # mã công việc tự tăng lên 1
        else:
            self.__task_id = value

    @property
    def task_name(self):
        return self.__task_name

    @task_name.setter
    def task_name(self, value):
        self.__task_name = value

    @property
    def estimated_time(self):
        return self.__estimated_time

    @estimated_time.setter
    def estimated_time(self, value):
        self.__estimated_time = value

    def __str__(self):
        return f'{self.task_id:<12}{self.task_name:50}{self.estimated_time:<20}'

    def __eq__(self, other):
        return self.task_id == other.task_id


class Assignment:
    """Lớp mô tả bảng phân công công việc."""
    AUTO_ID = 1000

    def __init__(self):
        self.__ass_id = 0
        self.__staff = None
        self.__task = None
        self.__start_time = None
        self.__deadline = None
        self.__result = ''

    @property
    def ass_id(self):
        return self.__ass_id

    @ass_id.setter
    def ass_id(self, value):
        if value is None or value == 0:
            self.__ass_id = Assignment.AUTO_ID + 1
            Assignment.AUTO_ID += 1
        else:
            self.__ass_id = value

    @property
    def staff(self):
        return self.__staff

    @staff.setter
    def staff(self, value):
        self.__staff = value

    @property
    def task(self):
        return self.__task

    @task.setter
    def task(self, value):
        self.__task = value

    @property
    def start_time(self):
        return self.__start_time

    @start_time.setter
    def start_time(self, value):
        self.__start_time = value

    @property
    def deadline(self):
        return self.__deadline

    @deadline.setter
    def deadline(self, value):
        self.__deadline = value

    @property
    def result(self):
        return self.__result

    @result.setter
    def result(self, value):
        self.__result = value

    def __str__(self):
        staff_id = ''
        staff_name = ''
        if self.staff is not None:
            staff_id = self.staff.emp_id
            staff_name = self.staff.full_name.full_name
        task_id = ''
        if self.task is not None:
            task_id = self.task.task_id
        return f'{self.ass_id:<12}{staff_id:12}{staff_name:30}{task_id:12}' \
               f'{self.start_time:25}{self.deadline:25}{self.result:25}'


class Payroll:
    """Lớp mô tả thông tin về bảng lương nhân viên."""
    AUTO_ID = 1000

    def __init__(self):
        self.__payroll_id = 0
        self.__assignments = []
        self.__staff = None
        self.__total_task = 0
        self.__total_finished = 0
        self.__total_unfinished = 0
        self.__total_penalty_fee = 0
        self.__received_salary = 0
        self.__working_day = 0.0

    @property
    def payroll_id(self):
        return self.__payroll_id

    @payroll_id.setter
    def payroll_id(self, value):
        if value is None or value == 0:
            self.__payroll_id = Payroll.AUTO_ID + 1
            Payroll.AUTO_ID += 1
        else:
            self.__payroll_id = value

    @property
    def assignments(self):
        return self.__assignments

    @assignments.setter
    def assignments(self, value):
        self.__assignments = value

    @property
    def staff(self):
        return self.__staff

    @staff.setter
    def staff(self, value):
        self.__staff = value

    @property
    def total_task(self):
        return self.__total_task

    @total_task.setter
    def total_task(self, value):
        self.__total_task = value

    @property
    def total_finished(self):
        return self.__total_finished

    @total_finished.setter
    def total_finished(self, value):
        self.__total_finished = value

    @property
    def total_unfinished(self):
        return self.__total_unfinished

    @total_unfinished.setter
    def total_unfinished(self, value):
        self.__total_unfinished = value

    @property
    def total_penalty_fee(self):
        return self.__total_penalty_fee

    @total_penalty_fee.setter
    def total_penalty_fee(self, value):
        self.__total_penalty_fee = value

    @property
    def received_salary(self):
        return self.__received_salary

    @received_salary.setter
    def received_salary(self, value):
        self.__received_salary = value

    @property
    def working_day(self):
        return self.__working_day

    @working_day.setter
    def working_day(self, value):
        self.__working_day = value

    def __str__(self): # 12.1f: làm tròn đến 1 chữ số sau phần thập phân
        return f'{self.payroll_id:<12}{self.staff.emp_id:20}' \
               f'{self.staff.full_name.full_name:30}' \
               f'{self.total_task:<12}{self.working_day:<12.1f}' \  
               f'{self.total_finished:<12}{self.total_unfinished:<12}' \
               f'{self.total_penalty_fee:<12.0f}{self.received_salary:<12.0f}'
