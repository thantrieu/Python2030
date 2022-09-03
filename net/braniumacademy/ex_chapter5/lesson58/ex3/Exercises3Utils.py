from datetime import datetime

from net.braniumacademy.ex_chapter5.lesson58.ex3.Exercises3 import FullName
from net.braniumacademy.ex_chapter5.lesson58.ex3.Exercises3 import Employee
from net.braniumacademy.ex_chapter5.lesson58.ex3.Exercises3 import Manager
from net.braniumacademy.ex_chapter5.lesson58.ex3.Exercises3 import Developer
from net.braniumacademy.ex_chapter5.lesson58.ex3.Exercises3 import Tester
from net.braniumacademy.ex_chapter5.lesson58.ex3.Exercises3 import Task
from net.braniumacademy.ex_chapter5.lesson58.ex3.Exercises3 import Payroll
from net.braniumacademy.ex_chapter5.lesson58.ex3.Exercises3 import Assignment


def create_staff(key, first, last, mid, email, phone, salary,
                 role, language=0, project=0, kpi=0, term='',
                 quater_salary=0, tool='', error=0, testcase=0):
    """This method create and return a fake staff infomation."""
    if key == 'M':
        manager = Manager()
        manager.emp_id = None
        manager.full_name = FullName(first=first, last=last, mid=mid)
        manager.email = email
        manager.phone_number = phone
        manager.salary = salary
        manager.role = role
        manager.term = term
        manager.quater_salary = quater_salary
        return manager
    elif key == 'D':
        dev = Developer()
        dev.emp_id = None
        dev.email = email
        dev.full_name = FullName(first=first, last=last, mid=mid)
        dev.phone_number = phone
        dev.salary = salary
        dev.role = role
        dev.num_of_project = project
        dev.num_of_language = language
        dev.monthly_kpi = kpi
        return dev
    elif key == 'T':
        tester = Tester()
        tester.emp_id = None
        tester.full_name = FullName(first=first, last=last, mid=mid)
        tester.email = email
        tester.salary = salary
        tester.phone_number = phone
        tester.role = role
        tester.tools.append(tool)
        tester.number_of_testcase = testcase
        tester.error_found = error
        return tester
    return None


def create_fake_employees():
    """This method create fake data for testing other functions."""
    staffs = []
    m = create_staff('M', 'Trung', 'Trần', 'Quốc', 'quoctrung@xmail.com',
                     '0972123123', 50000, role='Marketing leader',
                     term='2020-2025', quater_salary=150)
    s1 = create_staff('D', 'Nam', 'Nguyễn', 'Văn', 'namnguyen@xmail.com',
                      '0972123126', 25000, role='Backend dev',
                      project=11, language=6, kpi=54)
    s2 = create_staff('D', 'Hưng', 'Trần', 'Đức', 'duchung@xmail.com',
                      '0972123127', 30000, role='Backend dev',
                      project=19, language=9, kpi=64)
    s3 = create_staff('D', 'Minh', 'Hoàng', 'Quốc', 'minhhoang@xmail.com',
                      '0972123128', 20000, role='Backend dev',
                      project=15, language=8, kpi=50)
    s4 = create_staff('T', 'Nhung', 'Mai', 'Trần', 'nhungtran@xmail.com',
                      '0972123129', 15000, role='Automation tester',
                      error=23, tool='Selenium', testcase=300)
    staffs.append(m)
    staffs.append(s1)
    staffs.append(s2)
    staffs.append(s3)
    staffs.append(s4)
    return staffs


def fake_task(name, amount):
    """This method create and return a fake task"""
    task = Task()
    task.task_id = None
    task.task_name = name
    task.estimated_time = amount
    return task


def create_fake_tasks():
    """This method create and return fake tasks."""
    tasks = [fake_task('Add login form', 2),
             fake_task('Add register form', 2),
             fake_task('Add item to cart', 2),
             fake_task('Fix bug in login logic', 1),
             fake_task('Fix bug in register logic', 1),
             fake_task('Fix bug in payment function', 3),
             fake_task('Test login function', 1),
             fake_task('Test register function', 1.5),
             fake_task('Test change password function', 1),
             fake_task('Test change email function', 1),
             ]
    return tasks


def fake_assignment(staff, task, start, deadline, result):
    """Method create and return a fake assignment."""
    assgn = Assignment()
    assgn.ass_id = None
    assgn.task = task
    assgn.staff = staff
    assgn.start_time = start
    assgn.deadline = deadline
    assgn.result = result
    return assgn


def create_fake_assignments(staffs, tasks):
    assignments = []
    task1 = fake_assignment(staffs[1], tasks[0], '02/09/2022 14:00', '02/09/2022 18:00', 'Completed')
    task2 = fake_assignment(staffs[2], tasks[1], '02/09/2022 15:00', '03/09/2022 10:00', 'Completed')
    task3 = fake_assignment(staffs[3], tasks[2], '02/09/2022 14:30', '03/09/2022 15:00', 'Completed')
    task4 = fake_assignment(staffs[1], tasks[3], '02/09/2022 14:20', '04/09/2022 16:00', 'Completed')
    task5 = fake_assignment(staffs[2], tasks[4], '03/09/2022 14:10', '04/09/2022 14:00', 'Completed')
    task6 = fake_assignment(staffs[3], tasks[5], '03/09/2022 15:00', '05/09/2022 15:00', 'Completed')
    task7 = fake_assignment(staffs[4], tasks[6], '03/09/2022 16:00', '05/09/2022 18:00', 'Completed')
    task8 = fake_assignment(staffs[4], tasks[7], '03/09/2022 16:00', '05/09/2022 18:00', 'Completed')
    task9 = fake_assignment(staffs[4], tasks[8], '03/09/2022 16:00', '05/09/2022 18:00', 'Completed')
    task10 = fake_assignment(staffs[4], tasks[9], '03/09/2022 16:00', '05/09/2022 18:00', 'Completed')
    assignments.append(task1)
    assignments.append(task2)
    assignments.append(task3)
    assignments.append(task4)
    assignments.append(task5)
    assignments.append(task6)
    assignments.append(task7)
    assignments.append(task8)
    assignments.append(task9)
    assignments.append(task10)
    return assignments


def create_staff_info():
    emp = Employee()
    print('============ Nhập thông tin nhân viên ============')
    last = input('Họ: ')
    mid = input('Đệm: ')
    first = input('Name: ')
    emp.email = input('Email: ')
    emp.phone_number = input('Số điện thoại: ')
    emp.salary = float(input('Mức lương: '))
    emp.full_name = FullName(first, mid, last)
    emp.emp_id = None
    return emp


def create_manager():
    """Phương thức tạo thông tin người quản lý, giám đốc."""
    staff = create_staff_info()
    manager = Manager()
    manager.emp_id = staff.emp_id
    manager.full_name = staff.full_name
    manager.phone_number = staff.phone_number
    manager.salary = staff.salary
    manager.email = staff.email
    manager.role = input('Chức vụ: ')
    manager.term = input('Nhiệm kỳ: ')
    manager.quater_salary = input('Lương thực lĩnh theo quý: ')
    return manager


def create_developer():
    """Phương thức tạo thông tin cho nhân viên lập trình viên."""
    staff = create_staff_info()
    dev = Developer()
    dev.emp_id = staff.emp_id
    dev.full_name = staff.full_name
    dev.phone_number = staff.phone_number
    dev.salary = staff.salary
    dev.email = staff.email
    dev.role = input('Chức vụ: ')
    dev.num_of_language = input('Số ngôn ngữ lập trình thành thạo: ')
    dev.num_of_project = input('Số project đã tham gia: ')
    # không nhập vào kpi và để đến cuối tháng xét lượng công việc hoàn thành để tính kpi
    return dev


def create_tester():
    """Phương thức tạo thông tin cho nhân viên tester."""
    staff = create_staff_info()
    tester = Tester()
    tester.emp_id = staff.emp_id
    tester.full_name = staff.full_name
    tester.phone_number = staff.phone_number
    tester.salary = staff.salary
    tester.email = staff.email
    tester.role = input('Chức vụ: ')
    tester.error_found = int(input('Số lỗi phát hiện được trong tháng: '))
    tester.number_of_testcase = \
        int(input('Số testcase hoàn thành trong tháng: '))
    tester.tools.append(input('Công cụ làm việc chính: '))
    return tester


def create_task():
    """Phương thức tạo thông tin đầu công việc."""
    task = Task()
    task.task_id = None
    task.task_name = input('Tên công việc: ')
    task.estimated_time = input('Thời gian cần thiết để hoàn thành(giờ): ')
    return task


def find_task_by_id(tasks):
    """
        This method find and return task if it exists.
        If not found, return None.
    """
    task = Task()
    task.task_id = input("Mã công việc: ")
    task_index = tasks.index(task)
    if task_index >= 0:
        return tasks[task_index]
    return None


def create_assignment(staffs, tasks):
    """Phương thức tạo bảng phân công công việc cho các nhân viên."""
    assgn = Assignment()
    assgn.ass_id = None
    staff = find_staff_by_id(staffs)
    if staff is None:
        print('==> Không tồn tại nhân viên cần tìm <==')
    task = find_task_by_id(tasks)
    if task is not None:
        print('==> Không tồn tại task cần phân công <==')
    assgn.start_time = input('Thời gian bắt đầu: ')
    assgn.deadline = input('Thời gian kết thúc: ')
    assgn.result = input('Kết quả: ')
    assgn.task = task
    assgn.staff = staff
    return assgn


def find_staff_by_id(staffs):
    """
        This method find staff by id then return None if not found
        and return staff if exists.
    """
    staff = Employee()
    staff.emp_id = input('Mã nhân viên: ')
    staff_index = staffs.index(staff)
    if staff_index >= 0:
        return staffs[staff_index]
    return None


def count_task(assignments, status):
    """This method count and return tasks have same status."""
    counter = 0
    for ass in assignments:
        if ass.result.lower() == status.lower():
            counter += 1
    return counter


def get_working_day(emp_id):
    """This method get and confirm working day of each staff then return result."""
    working_day = float(input(f'Số ngày làm việc của nhân viên mã {emp_id}: '))
    if working_day < 0 or working_day > 33:
        print('==> Số ngày làm việc không hợp lệ! Giá trị hợp lệ từ 0-33. <==')
        # giả định 1 tháng đi làm 22 ngày, mỗi ngày 8h. Nếu tăng 1 ca 4h liên tục ta có 33 ngày.
        return 0
    return working_day


def get_error(emp_id):
    """This method get the number of error that a tester found. Then check the value and return."""
    num_of_error = int(input(f'Số lỗi mà nhân viên {emp_id} tìm ra: '))
    if num_of_error < 0 or num_of_error > 200:
        return 0
    return num_of_error


def create_payrolls(staffs, assignments, payrolls):
    """
        Phương thức lập bảng lương cho các nhân viên trong danh sách nhân viên.
    """
    for staff in staffs:
        payroll = Payroll()
        payroll.payroll_id = None
        payroll.staff = staff
        payroll.working_day = get_working_day(staff.emp_id)
        for ass in assignments:
            if ass is not None and ass.staff == staff:
                payroll.assignments.append(ass)
        payroll.total_task = len(payroll.assignments)
        payroll.total_finished = count_task(payroll.assignments, "Completed")
        payroll.total_unfinished = count_task(payroll.assignments, 'Incompleted')
        payroll.total_penalty_fee = payroll.total_unfinished * 100

        if isinstance(staff, Developer):  # nếu nhân viên là developer
            staff.monthly_kpi = 2 * payroll.total_finished  # xét KPI cho dev

        if isinstance(staff, Tester):  # nếu là tester thì cập nhật số testcase
            staff.number_of_testcase = payroll.total_finished
            staff.error_found = get_error(staff.emp_id)  # và số lỗi phát hiện đc

        payroll.received_salary = \
            payroll.staff.calculate_salary(payroll.working_day) - \
            payroll.total_penalty_fee
        payrolls.append(payroll)


def show_leader(staffs):
    """Phương thức hiển thị danh sách nhân viên quản lý(leader, giám đốc)."""
    emp_id = 'Mã NV'
    full_name = 'Họ và tên'
    email = 'Email'
    phone_number = 'Số ĐT'
    salary = 'Mức lương'
    term = "Nhiệm kì"
    role = 'Chức vụ'
    quater_salary = 'Lương quý'
    title = f'{emp_id:12}{full_name:30}' \
            f'{email:30}{phone_number:15}{salary:12}' \
            f'{term:12}{role:20}{quater_salary:12}'
    print(title)
    for s in staffs:
        # nếu đối tượng s là một đối tượng kiểu Manager
        # thì ta hiển thị thông tin của đối tượng này ra màn hình
        if isinstance(s, Manager):
            print(s)


def show_dev(staffs):
    """Phương thức hiển thị danh sách nhân viên lập trình viên."""
    emp_id = 'Mã NV'
    full_name = 'Họ và tên'
    email = 'Email'
    phone_number = 'Số ĐT'
    salary = 'Mức lương'
    languages = "Số NNLT"
    role = 'Chức vụ'
    projects = 'Số project'
    kpi = 'KPI tháng'
    title = f'{emp_id:12}{full_name:30}' \
            f'{email:30}{phone_number:15}{salary:12}' \
            f'{role:20}{languages:12}{projects:12}{kpi:12}'
    print(title)
    for s in staffs:
        if isinstance(s, Developer):
            print(s)


def show_tester(staffs):
    """Phương thức hiển thị danh sách nhân viên tester."""
    emp_id = 'Mã NV'
    full_name = 'Họ và tên'
    email = 'Email'
    phone_number = 'Số ĐT'
    salary = 'Mức lương'
    tool = "Công cụ SD"
    role = 'Chức vụ'
    error = 'Số lỗi'
    testcase = 'Số tescase'
    title = f'{emp_id:12}{full_name:30}' \
            f'{email:30}{phone_number:15}{salary:12}' \
            f'{role:20}{tool:20}{error:12}{testcase:12}'
    print(title)
    for s in staffs:
        if isinstance(s, Tester):
            print(s)


def show_task(tasks):
    """Phương thức hiển thị danh sách các công việc."""
    task_id = 'Mã CV'
    task_name = 'Tên CV'
    estimated_time = 'TG dự kiến'
    title = f'{task_id:12}{task_name:50}{estimated_time:20}'
    print(title)
    for t in tasks:
        print(t)


def show_assignment(assignments):
    """Phương thức hiển thị danh sách bảng phân công."""
    ass_id = 'Mã BPC'  # mã bảng phân công
    emp_id = 'Mã NV'
    emp_name = 'Tên nhân viên'
    task_id = 'Mã CV'
    start_time = 'Bắt đầu'
    deadline = 'Kết thúc'
    result = 'Kết quả'
    title = f'{ass_id:12}{emp_id:12}{emp_name:30}{task_id:12}' \
            f'{start_time:25}{deadline:25}{result:25}'
    print(title)
    for a in assignments:
        print(a)


def sort_assgn_by_staff_name(assments):
    """Phương thức sắp xếp bảng phân công theo tên nhân viên a-z."""
    assments.sort(key=lambda x: (
        x.staff.full_name.first_name,
        x.staff.full_name.last_name
    )
                  )


def sort_assgn_by_deadline(assments):
    """
        Phương thức sắp xếp bảng phân công theo deadline
        giảm dần(từ gần deadline nhất đến xa nhất).
    """
    now = datetime.now()
    datetime_format = '%H:%M %d/%m/%Y'
    date_time_str = now.strftime(datetime_format)
    assments.sort(key=lambda x: (date_time_str > x.deadline, x.deadline))


def sort_payroll_by_received_salary(payrolls):
    """Phương thức sắp xếp bảng lương theo mức lương thực lĩnh giảm dần."""
    payrolls.sort(key=lambda x: (
        -x.received_salary, x.staff.full_name.first_name, x.staff.full_name.last_name))


def sort_payroll_by_staff_name(payrolls):
    """Phương thức sắp xếp bảng lương theo họ tên nhân viên a-z."""
    payrolls.sort(key=lambda x: (x.staff.full_name.first_name, x.staff.full_name.last_name))


def sort_payroll_by_penalty_fee(payrolls):
    """Phương thức sắp xếp bảng lương theo phí phạt giảm dần."""
    payrolls.sort(key=lambda x: (
        -x.total_penalty_fee, x.staff.full_name.first_name, x.staff.full_name.last_name))


def find_highest_received_salary(payrolls):
    """This method find and return max received salary of staffs in a company."""
    max_salary = 0
    for p in payrolls:
        if p.received_salary > max_salary:
            max_salary = p.received_salary
    return max_salary


def listed_staff_with_highest_salary(payrolls):
    """Phương thức liệt kê các nhân viên có mức lương cao nhất."""
    max_salary = find_highest_received_salary(payrolls)
    results = []
    for p in payrolls:
        if p.received_salary == max_salary:
            results.append(p)
    print('==> Các nhân viên lương cao nhất: <==')
    show_payrolls(results)


def listed_staff_with_given_salary(payrolls):
    """Phương thức liệt kê các nhân viên có mức lương trong khoảng cho trước."""
    start_salary = int(input('Mức lương khởi điểm: '))
    end_salary = int(input('Mức lương tối đa: '))
    results = []
    for p in payrolls:
        if start_salary <= p.received_salary <= end_salary:
            results.append(p)
    if len(results) == 0:
        print('==> Không có nhân viên nào có mức lương cần tìm. <==')
    else:
        show_payrolls(results)


def show_payrolls(payrolls):
    """This method display payroll on the screen."""
    payroll_id = 'Mã B.Lương'
    emp_id = 'Mã nhân viên'
    full_name = 'Họ và tên'
    total_task = 'Tổng C.Việc'
    working_day = 'Số NL.Việc'
    total_finished = 'Hoàn tất'
    total_unfinished = 'Chưa H.Tất'
    total_penalty_fee = 'Tiền phạt'
    received_salary = 'Thực nhận'
    title = f'{payroll_id:<12}{emp_id:20}{full_name:30}' \
            f'{total_task:<12}{working_day:<12}' \
            f'{total_finished:<12}{total_unfinished:<12}' \
            f'{total_penalty_fee:<12}{received_salary:<12}'
    print(title)
    for p in payrolls:
        print(p)


def main_function():
    # danh sách nhân viên chứa cả giám đốc, lập trình viên, tester
    staffs = create_fake_employees()
    tasks = create_fake_tasks()  # danh sách công việc
    assignments = create_fake_assignments(staffs, tasks)  # danh sách bảng phân công
    payrolls = []  # danh sách bảng lương
    option = '============================ OPTION ============================\n' \
             '1. Thêm mới một giám đốc vào danh sách nhân viên.\n' \
             '2. Thêm mới một lập trình viên vào danh sách nhân viên.\n' \
             '3. Thêm mới một tester vào danh sách nhân viên.\n' \
             '4. Thêm mới một công việc vào danh sách công việc.\n' \
             '5. Thêm mới một bảng phân công vào danh sách bảng phân công.\n' \
             '6. Hiển thị danh sách giám đốc ra màn hình.\n' \
             '7. Hiển thị danh sách lập trình viên ra màn hình.\n' \
             '8. Hiển thị danh sách tester ra màn hình.\n' \
             '9. Hiển thị danh sách công việc ra màn hình.\n' \
             '10. Hiển thị danh sách bảng phân công công việc ra màn hình.\n' \
             '11. Sắp xếp danh sách bảng phân công theo tên nhân viên a-z.\n' \
             '12. Sắp xếp danh sách bảng phân công theo deadline giảm dần.\n' \
             '13. Lập bảng lương cho nhân viên.\n' \
             '14. Hiển thị bảng lương lên màn hình.\n' \
             '15. Sắp xếp bảng lương theo lương thực lĩnh giảm dần, tên, họ a-z.\n' \
             '16. Sắp xếp bảng lương theo tên nhân viên a-z.\n' \
             '17. Sắp xếp bảng lương theo tổng tiền phạt giảm dần.\n' \
             '18. Liệt kê các nhân viên có lương thực lĩnh cao nhất trong tháng.\n' \
             '19. Liệt kê các nhân viên có lương thực lĩnh từ khoảng x đến y.\n' \
             '20. Kết thúc chương trình.\n' \
             'Xin mời chọn chức năng(1-20): '
    while True:
        choice = int(input(option))
        match choice:
            case 1:
                manager = create_manager()
                if manager is not None:
                    staffs.append(manager)
            case 2:
                dev = create_developer()
                if dev is not None:
                    staffs.append(dev)
            case 3:
                tester = create_tester()
                if tester is not None:
                    staffs.append(tester)
            case 4:
                task = create_task()
                if task is not None:
                    tasks.append(task)
            case 5:
                if len(staffs) > 0 and len(tasks) > 0:
                    assgn = create_assignment(staffs, tasks)
                    if assgn is not None:
                        assignments.append(assgn)
                else:
                    print('==> Danh sách nhân viên hoặc công việc rỗng <==')
            case 6:
                if len(staffs) > 0:
                    print('==> Danh sách nhân viên quản lý <==')
                    show_leader(staffs)
                else:
                    print("==> Danh sách nhân viên rỗng <==")
            case 7:
                if len(staffs) > 0:
                    print('==> Danh sách các lập trình viên <==')
                    show_dev(staffs)
                else:
                    print("==> Danh sách nhân viên rỗng <==")
            case 8:
                if len(staffs) > 0:
                    print('==> Danh sách các tester <==')
                    show_tester(staffs)
                else:
                    print("==> Danh sách nhân viên rỗng <==")
            case 9:
                if len(tasks) > 0:
                    print('==> Danh sách các công việc <==')
                    show_task(tasks)
                else:
                    print("==> Danh sách công việc rỗng <==")
            case 10:
                if len(assignments) > 0:
                    print('==> Danh sách bảng phân công công việc <==')
                    show_assignment(assignments)
                else:
                    print("==> Danh sách bảng phân công rỗng <==")
            case 11:
                if len(assignments) > 0:
                    sort_assgn_by_staff_name(assignments)
                else:
                    print("==> Danh sách bảng phân công rỗng <==")
            case 12:
                if len(assignments) > 0:
                    sort_assgn_by_deadline(assignments)
                else:
                    print("==> Danh sách bảng phân công rỗng <==")
            case 13:
                if len(staffs) > 0:
                    create_payrolls(staffs, assignments, payrolls)
                    print('==> Lập bảng lương hoàn tất <==')
                else:
                    print("==> Danh sách nhân viên rỗng <==")
            case 14:
                if len(payrolls) > 0:
                    show_payrolls(payrolls)
                else:
                    print("==> Danh sách bảng lương rỗng <==")
            case 15:
                if len(payrolls) > 0:
                    sort_payroll_by_received_salary(payrolls)
                else:
                    print("==> Danh sách bảng lương rỗng <==")
            case 16:
                if len(payrolls) > 0:
                    sort_payroll_by_staff_name(payrolls)
                else:
                    print("==> Danh sách bảng lương rỗng <==")
            case 17:
                if len(payrolls) > 0:
                    sort_payroll_by_penalty_fee(payrolls)
                else:
                    print("==> Danh sách bảng lương rỗng <==")
            case 18:
                if len(payrolls) > 0:
                    listed_staff_with_highest_salary(payrolls)
                else:
                    print("==> Danh sách bảng lương rỗng <==")
            case 19:
                if len(payrolls) > 0:
                    listed_staff_with_given_salary(payrolls)
                else:
                    print("==> Danh sách bảng lương rỗng <==")
            case 20:
                print('==> Chương trình kết thúc <==')
                break
            case _:
                print('==> Lựa chọn không hợp lệ. Vui lòng nhập số 1-20. <==')


if __name__ == '__main__':
    main_function()
