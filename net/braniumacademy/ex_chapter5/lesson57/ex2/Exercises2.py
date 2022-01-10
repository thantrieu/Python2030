from abc import ABC, abstractmethod


class Employee(ABC):
    def __init__(self, eid, name, email, phone, salary):
        self.__emp_id = eid
        self.__full_name = name
        self.__email = email
        self.__phone_number = phone
        self.__salary = salary
        
    @property
    def email(self):
        return self.__email
    
    @property
    def full_name(self):
        return self.__full_name
    
    @property
    def emp_id(self):
        return self.__emp_id

    @property
    def phone_number(self):
        return self.__phone_number

    @property
    def salary(self):
        return self.__salary

    def checkin(self, time):
        print(f'{self.full_name} is checkin at {time}')

    def checkout(self, time):
        print(f'{self.full_name} is checkout at {time}')

    def work(self, task):
        print(f'{self.full_name} is doing {task}')

    @abstractmethod
    def calculate_salary(self, work_day):
        pass


class Director(Employee):
    def __init__(self, role, term, quater_salary,
                 eid='', name='', email='', phone='', salary=0):
        super().__init__(eid, name, email, phone, salary)
        self.__role = role
        self.__term = term
        self.__quater_salary = quater_salary

    def sign(self, doc):
        print(f'Director {self.full_name} signed at {doc}')

    def meeting(self, time):
        print(f'Director {self.full_name} is attending a meeting at {time}.')

    def calculate_salary(self, work_day):
        return self.salary * work_day / 22 + 0.8 * self.__quater_salary


class Developer(Employee):
    def __init__(self, major, language, project, kpi,
                 eid='', name='', email='', phone='', salary=0):
        super().__init__(eid, name, email, phone, salary)
        self.__major = major
        self.__language = language
        self.__project = project
        self.__kpi = kpi

    def code(self, task):
        print(f'Dev {self.full_name} is coding task {task}.')

    def fix_error(self, err):
        print(f'Dev {self.full_name} is fixing error {err}.')

    def receive_task(self, task):
        print(f'Dev {self.full_name} is receiving task {task}.')

    def report(self, to, typeof):
        print(f'Dev {self.full_name} is sending a report of {typeof} to {to}.')

    def calculate_salary(self, work_day):
        real_salary = self.salary * work_day / 22
        return real_salary + 0.3 * (real_salary * self.__kpi / 100)


class ProjectManager(Developer):
    def __init__(self, manage_proj, manage_emp, manage_buget,
                 major, language='', project=0, kpi=0, eid='', name='',
                 email='', phone='', salary=0):
        super().__init__(major, language, project, kpi, eid,
                         name, email, phone, salary)
        self.__manage_proj = manage_proj
        self.__manage_emp = manage_emp
        self.__manage_budget = manage_buget

    @property
    def manage_proj(self):
        return self.__manage_proj

    @property
    def manage_emp(self):
        return self.__manage_emp

    @property
    def manage_budget(self):
        return self.__manage_budget

    def join_meeting(self, time):
        print(f'Project manager has a meeting at {time}.')

    def release_product(self, product, time):
        print(f'Project manager relase project {product} at {time}.')

    def disbursing(self, amount):
        print(f'Project manager is rewarding {amount}$ for team member.')

    def calculate_salary(self, work_day):
        return self.salary * work_day / 22 + 0.2 * self.salary


class Tester(Employee):
    def __init__(self, major, tool, bug, completed,
                 eid='', name='', email='', phone='', salary=0):
        super().__init__(eid, name, email, phone, salary)
        self.__bug = bug
        self.__major = major
        self.__tool = tool
        self.__completed_testcase = completed

    def receive_project(self, project):
        print(f'Tester {self.full_name} receive project {project}.')

    def test(self, task):
        print(f'Tester {self.full_name} is testing task {task}.')

    def write_testcase(self):
        print(f'Tester {self.full_name} is writing tescases.')

    def report(self, to):
        print(f'Tester {self.full_name} sent report to {to}.')

    def calculate_salary(self, work_day):
        real_salary = self.salary * work_day / 22
        return real_salary + 0.2 * real_salary * self.__completed_testcase / 100 \
               + 50 * self.__bug


if __name__ == '__main__':
    # tạo giám đốc
    print('=================================================================')
    director = Director('Marketing director', '2025-2030',
                        160000, name='Trương Văn Hồng')
    director.meeting('14:00')
    director.sign('Contract')
    print(f'Salary: {director.calculate_salary(22)}')

    # tạo lập trình viên
    print('=================================================================')
    dev = Developer('Backend', 20, 16, 20, salary=19800)
    dev.code('Login authentication')
    dev.receive_task('Create login page')
    dev.fix_error('Login button does not work as expected')
    dev.report('Technical Director', 'Completed tasks')
    print(f'Salary: {dev.calculate_salary(22)}')

    # tạo tester
    print('=================================================================')
    tester = Tester('Automation test', 'Selenium', 70, 35,
                    name='Lee Thị Hồng Nhung', salary=14690)
    tester.receive_project('ATM of VCB')
    tester.test('Transfer at ATM')
    tester.write_testcase()
    tester.report('Tester manager')
    print(f'Salary: {tester.calculate_salary(22)}')

    # tạo quản lý dự án
    print('=================================================================')
    projmanager = ProjectManager(manage_proj=20, manage_emp=30,
                                 manage_buget=154000, kpi=25,
                                 major='Core technical manager',
                                 name='Mai Thanh Hà', salary=36500)
    projmanager.join_meeting('15:00')
    projmanager.release_product('ATM of VCB', '15:00')
    projmanager.disbursing('14000')
    print(f'Salary: {projmanager.calculate_salary(22)}')
    print('=================================================================')
