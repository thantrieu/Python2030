from net.braniumacademy.ex_chapter5.lesson58.ex3.Exercises3 import FullName
from net.braniumacademy.ex_chapter5.lesson58.ex3.Exercises3 import Employee
from net.braniumacademy.ex_chapter5.lesson58.ex3.Exercises3 import Manager
from net.braniumacademy.ex_chapter5.lesson58.ex3.Exercises3 import Developer
from net.braniumacademy.ex_chapter5.lesson58.ex3.Exercises3 import Tester
from net.braniumacademy.ex_chapter5.lesson58.ex3.Exercises3 import Task
from net.braniumacademy.ex_chapter5.lesson58.ex3.Exercises3 import Payroll
from net.braniumacademy.ex_chapter5.lesson58.ex3.Exercises3 import Assignment


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
    dev.monthly_kpi = input('KPI trong tháng: ')
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


def create_assignment(staffs, tasks):
    """Phương thức tạo bảng phân công công việc cho các nhân viên."""
    assgn = Assignment()
    assgn.ass_id = None
    emp_id = input("Mã nhân viên: ")
    emp = Employee()
    emp.emp_id = emp_id
    staff = None
    staff_index = staffs.index(emp)
    if staff_index >= 0:
        staff = staffs[staff_index]
    else:
        print('==> Không tồn tại nhân viên cần tìm <==')
    task_id = input("Mã công việc: ")
    target_task = Task()
    target_task.task_id = task_id
    task_index = tasks.index(target_task)
    task = None
    if task_index >= 0:
        task = tasks[task_index]
    else:
        print('==> Không tồn tại task cần phân công <==')
    assgn.start_time = input('Thời gian bắt đầu: ')
    assgn.deadline = input('Thời gian kết thúc: ')
    assgn.result = input('Kết quả: ')
    assgn.task = task
    assgn.staff = staff
    return assgn


def create_payroll():
    """
        Phương thức lập bảng lương cho các nhân viên trong danh sách nhân viên.
    """
    payroll = Payroll()
    payroll.payroll_id = None
    payroll.total_task = int(input('Tổng số các công việc: '))
    payroll.total_finished = int(input('Số công việc đã hoàn tất: '))
    payroll.total_unfinished = int(input('Số công việc chưa hoàn tất: '))
    payroll.working_day = float(input('Số ngày làm việc thực tế: '))
    return payroll


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
    task_id = 'Mã CV'
    start_time = 'Bắt đầu'
    deadline = 'Kết thúc'
    result = 'Kết quả'
    title = f'{ass_id:12}{emp_id:20}{task_id:12}' \
            f'{start_time:12}{deadline:12}{result:12}'
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
    assments.sort(key=lambda x: x.deadline)


def sort_payroll_by_received_salary(payrolls):
    """Phương thức sắp xếp bảng lương theo mức lương thực lĩnh giảm dần."""
    pass


def sort_payroll_by_staff_name(payrolls):
    """Phương thức sắp xếp bảng lương theo họ tên nhân viên a-z."""
    pass


def sort_payroll_by_penalty_fee(payrolls):
    """Phương thức sắp xếp bảng lương theo phí phạt giảm dần."""
    pass


def listed_staff_with_highest_salary(payrolls):
    """Phương thức liệt kê các nhân viên có mức lương cao nhất."""
    pass


def listed_staff_with_given_salary(payrolls):
    """Phương thức liệt kê các nhân viên có mức lương trong khoảng cho trước."""
    pass


def main_function():
    staffs = []  # danh sách nhân viên chứa cả giám đốc, lập trình viên, tester
    tasks = []  # danh sách công việc
    assignments = []  # danh sách bảng phân công
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
             '13. Lập bảng lương cho nhân viên và hiển thị lên màn hình.\n' \
             '14. Sắp xếp bảng lương theo lương thực lĩnh giảm dần, tên, họ a-z.\n' \
             '15. Sắp xếp bảng lương theo tên nhân viên a-z.\n' \
             '16. Sắp xếp bảng lương theo tổng tiền phạt giảm dần.\n' \
             '17. Liệt kê các nhân viên có lương thực lĩnh cao nhất trong tháng.\n' \
             '18. Liệt kê các nhân viên có lương thực lĩnh từ khoảng x đến y.\n' \
             '19. Kết thúc chương trình.\n' \
             'Xin mời chọn chức năng(1-19): '
    while True:
        choice = int(input(option))
        match choice:
            case 1:
                manager = create_manager()
                if (manager is not None):
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
                    show_leader(staffs)
                else:
                    print("==> Danh sách nhân viên rỗng <==")
            case 7:
                if len(staffs) > 0:
                    show_dev(staffs)
                else:
                    print("==> Danh sách nhân viên rỗng <==")
            case 8:
                if len(staffs) > 0:
                    show_tester(staffs)
                else:
                    print("==> Danh sách nhân viên rỗng <==")
            case 9:
                if len(tasks) > 0:
                    show_task(tasks)
                else:
                    print("==> Danh sách công việc rỗng <==")
            case 10:
                if len(assignments) > 0:
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
                    payroll = create_payroll()
                    if payroll is not None:
                        payrolls.append(payroll)
                else:
                    print("==> Danh sách nhân viên rỗng <==")
            case 14:
                if len(payrolls) > 0:
                    sort_payroll_by_received_salary(payrolls)
                else:
                    print("==> Danh sách bảng lương rỗng <==")
            case 15:
                if len(payrolls) > 0:
                    sort_payroll_by_staff_name(payrolls)
                else:
                    print("==> Danh sách bảng lương rỗng <==")
            case 16:
                if len(payrolls) > 0:
                    sort_payroll_by_penalty_fee(payrolls)
                else:
                    print("==> Danh sách bảng lương rỗng <==")
            case 17:
                if len(payrolls) > 0:
                    listed_staff_with_highest_salary(payrolls)
                else:
                    print("==> Danh sách bảng lương rỗng <==")
            case 18:
                if len(payrolls) > 0:
                    listed_staff_with_given_salary(payrolls)
                else:
                    print("==> Danh sách bảng lương rỗng <==")
            case 19:
                print('==> Chương trình kết thúc <==')
                break
            case _:
                print('==> Lựa chọn không hợp lệ. Vui lòng nhập số 1-15. <==')


if __name__ == '__main__':
    main_function()
