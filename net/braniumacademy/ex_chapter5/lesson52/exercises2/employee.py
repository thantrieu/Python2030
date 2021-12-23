class Employee:
    """Lớp mô tả thông tin và hành động của nhân viên"""

    def __init__(self, eid='', first='', mid='',
                 last='', address='', age='', phone='',
                 salary=0, experience=0.0):
        self.emp_id = eid
        self.first_name = first
        self.mid_name = mid
        self.last_name = last
        self.address = address
        self.age = age;
        self.phone_number = phone
        self.salary = salary
        self.experience = experience

    def work(self, task):
        """Phương thức mô tả hành động làm việc của nhân viên"""
        print(f'Nhân viên {self.first_name} đang thực hiện công việc {task}')

    def relax(self, by_something):
        """Phương thức mô tả hành động giải trí của nhân viên"""
        print(f'Nhân viên {self.first_name} đang giải trí với {by_something}')

    def travel(self, to):
        """Phương thức mô tả hành động đi du lịch của nhân viên"""
        print(f'Nhân viên {self.first_name} đang du hí tới {to}')

    def receive_salary(self, amount):
        """Phương thức mô tả hành động nhận lương của nhân viên"""
        print(f'Mức lương thực lĩnh của {self.first_name} là {amount}')
