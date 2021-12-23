from net.braniumacademy.ex_chapter5.lesson52.exercises2.employee import Employee


def create_employee():
    """Phương thức nhập thông tin và tạo đối tượng nhân viên"""
    emp_id = input('Nhập mã nhân viên: ')
    full_name = input('Nhập họ và tên nhân viên: ')
    address = input('Nhập địa chỉ: ')
    age = int(input('Nhập tuổi: '))
    phone_number = input('Nhập số điện thoại: ')
    salary = int(input('Nhập mức lương: '))
    experience = float(input('Số năm kinh nghiệm: '))
    mid_name = ''
    words = full_name.split()
    for i in range(1, len(words) - 1):
        mid_name += words[i] + ' '
    return Employee(eid=emp_id, first=words[len(words) - 1], last=words[0],
                    mid=mid_name, age=age, phone=phone_number, salary=salary,
                    address=address, experience=experience)


def print_employee_info(e):
    """Phương thức hiển thị thông tin từng nhân viên"""
    print(f'{e.emp_id:10}{e.last_name:10} {e.mid_name:15} {e.first_name:10}'
          f'{e.address:12}{e.age:<6}{e.phone_number:15}{e.experience:<10}{e.salary:<12}')


def print_list_emp(employees):
    """Phương thức hiển thị danh sách nhân viên"""
    print(f'{"Mã NV":10}{"Họ":10} {"Đệm":15} {"Tên":10}'
          f'{"Địa chỉ":12}{"Tuổi":<6}{"Số ĐT":15}{"K.N":<10}{"Lương":<12}')
    for e in employees:
        print_employee_info(e)


def find_emp_by_id(employees, eid):
    """Phương thức tìm nhân viên theo mã cho trước. Nếu tìm thấy trả về chỉ số
    phần tử tương ứng trong list. Nếu không tìm thấy, trả về -1.
    """
    for i in range(len(employees)):
        if eid.lower() == employees[i].emp_id.lower():
            return i
    return -1


def remove_employee_by_id(employees, eid):
    """Phương thức xóa nhân viên khỏi danh sách nhân viên theo mã cho trước."""
    index = find_emp_by_id(employees, eid)
    if index != -1:
        employees.pop(index)
        print("==> Xóa nhân viên thành công! <==")
    else:
        print("==> Không tìm thấy nhân viên có mã cần xóa <==")


def find_max_salary(employees):
    """Phương thức tìm giá trị lớn nhất của mức lương các nhân viên trong danh sách."""
    max_salary = 0
    for x in employees:
        if x.salary > max_salary:
            max_salary = x.salary
    return max_salary


def find_employees_have_max_salary(employees):
    """Phương thức liệt kê các nhân viên có mức lương cao nhất trong danh sách."""
    print(f'========== Danh sách nhân viên có lương cao nhất ============')
    max_salary = find_max_salary(employees)
    for x in employees:
        if x.salary == max_salary:
            print_employee_info(x)


def find_employee_by_name(employees, name):
    """Phương thức liệt kê các nhân viên có tên x trong danh sách."""
    print(f'========== Danh sách nhân viên có tên \'{name}\' ============')
    for x in employees:
        if name.lower() == x.first_name.lower():
            print_employee_info(x)


def find_employee_by_age(employees, age):
    """Phương thức liệt kê các nhân viên có tên x trong danh sách."""
    print(f'========== Danh sách nhân viên có tuổi {age} ============')
    for x in employees:
        if age == x.age:
            print_employee_info(x)


def find_employee_by_experience(employees, exp):
    """Phương thức liệt kê các nhân viên có tên x trong danh sách."""
    print(f'========== Danh sách nhân viên có {exp} năm kinh nghiệm ============')
    for x in employees:
        if exp == x.experience:
            print_employee_info(x)


def find_employee_by_phone_number(employees, phone_num):
    """Phương thức liệt kê các nhân viên có tên x trong danh sách."""
    print(f'========== Danh sách nhân viên có 3 số cuối SĐT là {phone_num} ============')
    for x in employees:
        if x.phone_number.find(phone_num, len(x.phone_number) - 3) != -1:
            print_employee_info(x)
