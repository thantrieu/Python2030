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
    print('============ Nhập thông tin sinh viên ============')
    last = input('Họ: ')
    mid = input('Đệm: ')
    first = input('Name: ')
    emp.email = input('Email: ')
    emp.phone_number = input('Số điện thoại: ')
    emp.salary = float(input('Mức lương: '))
    emp.full_name = FullName(first, mid, last)
    return emp


def create_manager():
    """Phương thức tạo thông tin người quản lý, giám đốc."""
    staff = create_staff_info()
    manager = Manager()

    return manager


def create_developer():
    """Phương thức tạo thông tin cho nhân viên lập trình viên."""
    pass


def create_tester():
    """Phương thức tạo thông tin cho nhân viên tester."""
    pass


def create_task():
    """Phương thức tạo thông tin đầu công việc."""
    pass


def create_assignment():
    """Phương thức tạo bảng phân công công việc cho các nhân viên."""
    pass


def create_payroll():
    """Phương thức lập bảng lương cho các nhân viên trong danh sách nhân viên."""
    pass


def show_leader(staffs):
    """Phương thức hiển thị danh sách nhân viên quản lý(leader, giám đốc)."""
    pass


def show_dev(staffs):
    """Phương thức hiển thị danh sách nhân viên lập trình viên."""
    pass


def show_tester(staffs):
    """Phương thức hiển thị danh sách nhân viên tester."""
    pass


def show_task(tasks):
    """Phương thức hiển thị danh sách các công việc."""
    pass


def show_assignment(assignments):
    """Phương thức hiển thị danh sách bảng phân công."""
    pass


def sort_assgn_by_staff_name(assments):
    """Phương thức sắp xếp bảng phân công theo tên nhân viên a-z."""
    pass


def sort_assgn_by_deadline(assments):
    """Phương thức sắp xếp bảng phân công theo deadline giảm dần(từ gần deadline nhất đến xa nhất)."""
    pass


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
                assgn = create_assignment()
                if assgn is not None:
                    assignments.append(assgn)
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
