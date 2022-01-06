class Employee:
    def __init__(self, eid, name, email, phone, salary):
        self.emp_id = eid
        self.full_name = name
        self.email = email
        self.phone_number = phone
        self.salary = salary

    def checkin(self, time):
        print(f'{self.full_name} is checkin at {time}')

    def checkout(self, time):
        print(f'{self.full_name} is checkout at {time}')

    def work(self, task):
        print(f'{self.full_name} is doing {task}')

    def calculate_salary(self, work_day):
        return self.salary * work_day / 22


class Director(Employee):
    def __init__(self, role, term, quater_salary,
                 eid='', name='', email='', phone='', salary=0):
        super().__init__(eid, name, email, phone, salary)
        self.role = role
        self.term = term
        self.quater_salary = quater_salary

    def sign(self, doc):
        print(f'Director {self.full_name} signed at {doc}')

    def meeting(self, time):
        print(f'Director {self.full_name} is attending a meeting at {time}.')

    def calculate_salary(self, work_day):
        return super().calculate_salary(work_day) + 0.8 * self.quater_salary


class Developer(Employee):
    def __init__(self, major, language, project, kpi,
                 eid='', name='', email='', phone='', salary=0):
        super().__init__(eid, name, email, phone, salary)
        self.major = major
        self.language = language
        self.project = project
        self.kpi = kpi

    def code(self, task):
        print(f'Dev {self.full_name} is coding task {task}.')

    def fix_error(self, err):
        print(f'Dev {self.full_name} is fixing error {err}.')

    def receive_task(self, task):
        print(f'Dev {self.full_name} is receiving task {task}.')

    def report(self, to, typeof):
        print(f'Dev {self.full_name} is sending a report of {typeof} to {to}.')

    def calculate_salary(self, work_day):
        real_salary = super().calculate_salary(work_day)
        return real_salary + 0.3 * (real_salary * self.kpi / 100)


class ProjectManager(Developer):
    def __init__(self, manage_proj, manage_emp, manage_buget,
                 major, language='', project=0, kpi=0, eid='', name='',
                 email='', phone='', salary=0):
        super().__init__(major, language, project, kpi, eid,
                         name, email, phone, salary)
        self.manage_proj = manage_proj
        self.manage_emp = manage_emp
        self.manage_budget = manage_buget

    def join_meeting(self, time):
        print(f'Project manager has a meeting at {time}.')

    def release_product(self, product, time):
        print(f'Project manager relase project {product} at {time}.')

    def disbursing(self, amount):
        print(f'Project manager is rewarding {amount}$ for team member.')

    def calculate_salary(self, work_day):
        return super().calculate_salary(work_day) + 0.2 * self.salary


class Tester(Employee):
    def __init__(self, major, tool, bug, completed,
                 eid='', name='', email='', phone='', salary=0):
        super().__init__(eid, name, email, phone, salary)
        self.bug = bug
        self.major = major
        self.tool = tool
        self.completed_testcase = completed

    def receive_project(self, project):
        print(f'Tester {self.full_name} receive project {project}.')

    def test(self, task):
        print(f'Tester {self.full_name} is testing task {task}.')

    def write_testcase(self):
        print(f'Tester {self.full_name} is writing tescases.')

    def report(self, to):
        print(f'Tester {self.full_name} sent report to {to}.')

    def calculate_salary(self, work_day):
        real_salary = super().calculate_salary(work_day)
        return real_salary + 0.2 * real_salary * self.completed_testcase / 100 \
               + 50 * self.bug


if __name__ == '__main__':
    # tạo nhân viên
    print('=================================================================')
    emp = Employee('EMP001', 'Hoàng Văn Công',
                   'cong@xmail.com', '0356698754', 15200)
    emp.work('Cooking')
    emp.checkin('08:00')
    emp.checkout('17:00')
    print(f'Salary: {emp.calculate_salary(20)}')

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
