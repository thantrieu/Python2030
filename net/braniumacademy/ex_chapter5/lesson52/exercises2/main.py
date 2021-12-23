import net.braniumacademy.ex_chapter5.lesson52.exercises2.employee_utils as utils

option = "========================= CÁC LỰA CHỌN =========================\n" \
         "01. Thêm mới một nhân viên vào danh sách.\n" \
         "02. Hiển thị danh sách nhân viên hiện có.\n" \
         "03. Tìm nhân viên theo mã nhân viên\n" \
         "04. Xóa nhân viên theo mã cho trước.\n" \
         "05. Sắp xếp danh sách nhân viên theo mức lương giảm dần.\n" \
         "06. Sắp xếp danh sách nhân viên theo tên tăng dần a-z.\n" \
         "07. Sắp xếp danh sách nhân viên theo lương giảm, tên tăng, họ tăng.\n" \
         "08. Liệt kê các nhân viên có lương cao nhất.\n" \
         "09. Liệt kê các nhân viên có tên x nhập vào từ bàn phím.\n" \
         "10. Liệt kê các nhân viên có tuổi x nhập vào từ bàn phím.\n" \
         "11. Liệt kê các nhân viên có n năm kinh nghiệm.\n" \
         "12. Tìm nhân viên theo 3 chữ số cuối số điện thoại.\n" \
         "0. Thoát chương trình.\nBạn chọn? "
employees = []
while True:
    choice = int(input(option))
    match choice:
        case 0:
            print("==> Chương trình kết thúc <==")
            break
        case 1:
            e = utils.create_employee()
            employees.append(e)
        case 2:
            if len(employees) > 0:
                print("== Các nhân viên có trong danh sách ==")
                utils.print_list_emp(employees)
            else:
                print('==> Danh sách nhân viên rỗng <==')
        case 3:
            if len(employees) > 0:
                emp_id = input('Nhập mã nhân viên cần tìm: ')
                result_index = utils.find_emp_by_id(employees, emp_id)
                if result_index == -1:
                    print(f'==> Không tìm thấy nhân viên mã "{emp_id}" <==')
                else:
                    print(f'==> Tìm thấy nhân viên mã "{emp_id}" <==')
                    utils.print_employee_info(employees[result_index])
            else:
                print('==> Danh sách nhân viên rỗng <==')
        case 4:
            if len(employees) > 0:
                emp_id = input('Nhập mã nhân viên cần xóa: ')
                utils.remove_employee_by_id(employees, emp_id)
            else:
                print('==> Danh sách nhân viên rỗng <==')
        case 5:
            if len(employees) > 0:
                employees.sort(key=lambda x: x.salary, reverse=True)
                print("==> Danh sách sau khi sắp xếp theo lương giảm dần <==")
                utils.print_list_emp(employees)
            else:
                print('==> Danh sách nhân viên rỗng <==')
        case 6:
            if len(employees) > 0:
                employees.sort(key=lambda x: x.first_name)
                print("==> Danh sách sau khi sắp xếp theo tên a-z <==")
                utils.print_list_emp(employees)
            else:
                print('==> Danh sách nhân viên rỗng <==')
        case 7:
            if len(employees) > 0:
                employees.sort(key=lambda x: (-x.salary, x.first_name, x.last_name))
                print("==> Danh sách sau khi sắp xếp theo lương giảm, tên tăng, họ tăng <==")
                utils.print_list_emp(employees)
            else:
                print('==> Danh sách nhân viên rỗng <==')
        case 8:
            if len(employees) > 0:
                print("==> Danh sách nhân viên có mức lương cao nhất <==")
                utils.find_employees_have_max_salary(employees)
            else:
                print('==> Danh sách nhân viên rỗng <==')
        case 9:
            if len(employees) > 0:
                name = input('Nhập tên nhân viên cần tìm: ')
                utils.find_employee_by_name(employees, name)
            else:
                print('==> Danh sách nhân viên rỗng <==')
        case 10:
            if len(employees) > 0:
                age = int(input('Nhập tuổi nhân viên cần tìm: '))
                utils.find_employee_by_age(employees, age)
            else:
                print('==> Danh sách nhân viên rỗng <==')
        case 11:
            if len(employees) > 0:
                age = float(input('Nhập số năm kinh nghiệm nhân viên cần tìm: '))
                utils.find_employee_by_experience(employees, age)
            else:
                print('==> Danh sách nhân viên rỗng <==')
        case 12:
            if len(employees) > 0:
                phone_number = input('Nhập 3 chữ số cuối số điện thoại nhân viên cần tìm: ')
                utils.find_employee_by_phone_number(employees, phone_number)
            else:
                print('==> Danh sách nhân viên rỗng <==')
        case _:
            print("Sai tùy chọn, vui lòng kiểm tra lại")
