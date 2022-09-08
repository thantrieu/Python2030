from utils import *

if __name__ == '__main__':
    students = read_students_from_file()
    subjects = read_subject_from_file()
    registers = read_register_from_file(students, subjects)
    update_student_auto_id(students)
    update_subject_auto_id(subjects)
    update_register_auto_id(registers)

    option = '============================ CÁC LỰA CHỌN ============================\n' \
             '1. Thêm mới sinh viên vào danh sách sinh viên.\n' \
             '2. Thêm mới môn học vào danh sách môn học.\n' \
             '3. Thêm mới bảng đăng ký môn học vào danh sách đăng ký.\n' \
             '4. Sắp xếp danh sách sinh viên theo tên a-z.\n' \
             '5. Sắp xếp danh sách môn học theo tên a-z.\n' \
             '6. Sắp xếp danh sách bảng đăng ký theo thời gian đăng ký.\n' \
             '7. Hiển thị danh sách sinh viên.\n' \
             '8. Hiển thị danh sách môn học.\n' \
             '9. Hiển thị danh sách bảng đăng ký.\n' \
             '10. Liệt kê danh sách môn học mà sinh viên đăng ký.\n' \
             '11. Liệt kê danh sách sinh viên đăng ký theo mã môn.\n' \
             '12. Thống kê số lượng sinh viên đăng ký theo từng môn học.\n' \
             '13. Cho biết thông tin bản ghi đăng ký sớm nhất.\n' \
             '14. Cho biết thông tin bản ghi đăng ký muộn nhất.\n' \
             '15. Kết thúc chương trình.\n' \
             'Xin mời chọn chức năng(1-15): '
    while True:
        choice = int(input(option))
        match choice:
            case 1:
                try:
                    new_student = create_student()
                    students.append(new_student)
                    print('==> Tạo mới sinh viên thành công! <==')
                except ValueError as e:
                    print(e)
            case 2:
                try:
                    new_subject = create_subject()
                    subjects.append(new_subject)
                    print('==> Tạo mới môn học thành công! <==')
                except ValueError as e:
                    print(e)
            case 3:
                new_register = create_register(registers, students, subjects)
                if new_register is not None:
                    registers.append(new_register)
                    print('==> Đăng ký môn học thành công! <==')
                else:
                    print('==> Tạo bản đăng ký thất bại.')
            case 4:
                if len(students) > 0:
                    students.sort(key=lambda x: (x.full_name.first_name, x.full_name.last_name))
                    print('==> Danh sách sinh viên sau khi sắp xếp: ')
                    show_students(students)
                else:
                    print('==> Danh sách sinh viên rỗng <==')
            case 5:
                if len(subjects) > 0:
                    subjects.sort(key=lambda x: x.subject_name)
                    print('==> Danh sách môn học sau khi sắp xếp: ')
                    show_subjects(subjects)
                else:
                    print('==> Danh sách môn học rỗng <==')
            case 6:
                if len(registers) > 0:
                    sort_registers(registers)
                    print('==> Danh sách đăng ký sau khi sắp xếp: ')
                    show_registers(registers)
                else:
                    print('==> Danh sách đăng ký rỗng <==')
            case 7:
                if len(students) > 0:
                    show_students(students)
                else:
                    print('==> Danh sách sinh viên rỗng <==')
            case 8:
                if len(subjects) > 0:
                    show_subjects(subjects)
                else:
                    print('==> Danh sách môn học rỗng <==')
            case 9:
                if len(registers) > 0:
                    show_registers(registers)
                else:
                    print('==> Danh sách đăng ký rỗng <==')
            case 10:
                if len(registers) > 0:
                    find_registed_subject(registers)
                else:
                    print('==> Danh sách đăng ký rỗng <==')
            case 11:
                if len(registers) > 0:
                    find_student_by_subject(registers)
                else:
                    print('==> Danh sách đăng ký rỗng <==')
            case 12:
                if len(registers) > 0:
                    statistics_by_subject(registers, subjects)
                else:
                    print('==> Danh sách đăng ký rỗng <==')
            case 13:
                if len(registers) > 0:
                    sort_registers(registers)
                    earliest_register(registers)
                else:
                    print('==> Danh sách đăng ký rỗng <==')
            case 14:
                if len(registers) > 0:
                    sort_registers(registers)
                    latest_register(registers)
                else:
                    print('==> Danh sách đăng ký rỗng <==')
            case 15:
                print('==> WOOHO... Cảm ơn bạn đã sử dụng dịch vụ của Branium Academy! <==')
                break
            case _:
                print('==> Lựa chọn không hợp lệ. Vui lòng nhập số 1-15. <==')
