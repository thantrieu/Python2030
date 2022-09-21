from utils import *

if __name__ == '__main__':
    students = read_students_from_database()
    subjects = read_subject_from_database()
    registers = read_register_from_database(students, subjects)
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
             '13. Thống kê số lượng sinh viên theo từng thành phố.\n' \
             '14. Liệt kê các sinh viên có điểm TB >= 3.2.\n' \
             '15. Liệt kê các sinh viên cùng tên, cùng thành phố và cùng năm sinh.\n' \
             '16. Liệt kê top 5 sinh viên đăng ký sớm nhất.\n' \
             '17. Liệt kê top 5 sinh viên có điểm TB cao nhất..\n' \
             '18. Tìm các sinh viên có điểm TB cao thứ 2.\n' \
             '19. Liệt kê danh sách các sinh viên đăng ký nhiều môn học nhất.\n' \
             '20. Liệt kê danh sách các sinh viên không đăng ký môn học nào.\n' \
             '21. Cho biết thông tin bản ghi của bản đăng ký sớm nhất.\n' \
             '22. Cho biết thông tin bản ghi của bản đăng ký muộn nhất.\n' \
             '23. Cập nhật họ và tên cho sinh viên theo mã sinh viên. Có xử lý ngoại lệ.\n' \
             '24. Cập nhật điểm cho sinh viên theo mã sinh viên. Có xử lý ngoại lệ.\n' \
             '25. Kết thúc chương trình.\n' \
             'Xin mời chọn chức năng(1-25): '
    while True:
        choice = int(input(option))
        match choice:
            case 1:
                try:
                    new_student = create_student()
                    students.append(new_student)
                    save_students([new_student])  # insert this student into table student
                    print('==> Tạo mới sinh viên thành công! <==')
                except ValueError as e:
                    print(e)
            case 2:
                try:
                    new_subject = create_subject()
                    subjects.append(new_subject)
                    save_subjects([new_subject])  # insert into table subject
                    print('==> Tạo mới môn học thành công! <==')
                except ValueError as e:
                    print(e)
            case 3:
                new_register = create_register(registers, students, subjects)
                if new_register is not None:
                    registers.append(new_register)
                    save_registers([new_register])
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
                    find_registed_subject()
                else:
                    print('==> Danh sách đăng ký rỗng <==')
            case 11:
                if len(registers) > 0:
                    find_student_by_subject(students)
                else:
                    print('==> Danh sách đăng ký rỗng <==')
            case 12:
                if len(registers) > 0:
                    statistics_by_subject()
                else:
                    print('==> Danh sách đăng ký rỗng <==')
            case 13:
                if len(students) > 0:
                    stat_student_by_city()
                else:
                    print('==> Danh sách sinh viên rỗng <==')
            case 14:
                if len(registers) > 0:
                    sort_registers(registers)
                    earliest_register(registers)
                else:
                    print('==> Danh sách đăng ký rỗng <==')
            case 15:
                if len(registers) > 0:
                    sort_registers(registers)
                    latest_register(registers)
                else:
                    print('==> Danh sách đăng ký rỗng <==')
            case 16:
                if len(subjects) > 0:
                    update_subject_name(subjects)
            case 17:
                if len(subjects) > 0:
                    update_subject_credit(subjects)
            case 18:
                if len(students) > 0:
                    update_student_name(students)
            case 19:
                if len(students) > 0:
                    update_student_gpa(students)
            case 20:
                if len(registers) > 0:
                    remove_register(registers)
            case 21:
                if len(students) > 0:
                    save_students(students)
                    print('==> Ghi danh sách sinh viên ra CSDL thành công! <==')
                if len(subjects) > 0:
                    save_subjects(subjects)
                    print('==> Ghi danh sách môn học ra CSDL thành công! <==')
                if len(registers) > 0:
                    save_registers(registers)
                    print('==> Ghi danh sách đăng ký ra CSDL thành công! <==')
            case 25:
                print('==> WOOHO... Cảm ơn bạn đã sử dụng dịch vụ của Branium Academy! <==')
                break
            case _:
                print('==> Lựa chọn không hợp lệ. Vui lòng nhập số 1-18. <==')
