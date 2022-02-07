import Exercises1Utils as utils

if __name__ == '__main__':
    students = utils.load_students()
    subjects = utils.load_subjects()
    registers = utils.load_registers(students, subjects)
    option = '============================ OPTION ============================\n' \
             '1. Thêm mới sinh viên vào danh sách.\n' \
             '2. Thêm mới môn học vào danh sách.\n' \
             '3. Thêm mới bảng đăng ký môn học vào danh sách.\n' \
             '4. Sắp xếp danh sách sinh viên theo tên.\n' \
             '5. Sắp xếp danh sách môn học theo tên.\n' \
             '6. Sắp xếp danh sách bảng đăng ký.\n' \
             '7. Hiển thị danh sách sinh viên.\n' \
             '8. Hiển thị danh sách môn học.\n' \
             '9. Hiển thị danh sách bảng đăng ký.\n' \
             '10. Liệt kê danh sách môn học mà sinh viên đăng ký.\n' \
             '11. Liệt kê danh sách sinh viên đăng ký theo mã môn.\n' \
             '12. Thống kê số lượng sinh viên đăng ký theo từng môn học.\n' \
             '13. Cho biết thông tin bản ghi sớm nhất.\n' \
             '14. Cho biết thông tin bản ghi đăng ký muộn nhất.\n' \
             '15. Xóa bản đăng ký môn học của sinh viên gian lận.\n' \
             '16. Lưu các danh sách vào file.\n' \
             '17. Kết thúc chương trình.\n' \
             'Xin mời chọn chức năng(1-17): '
    while True:
        choice = int(input(option))
        match choice:
            case 1:
                new_student = utils.create_student()
                if new_student is not None:
                    students.append(new_student)
                else:
                    print('==> Tạo sinh viên thất bại <==')
            case 2:
                new_subject = utils.create_subject()
                subjects.append(new_subject)
            case 3:
                new_register = utils.create_register(students, subjects)
                if new_register is not None:
                    if not utils.is_register_exist(registers, new_register):
                        registers.append(new_register)
                    else:
                        print(f'==> Sinh viên mã '
                              f'{new_register.student.student_id} '
                              f'đã đăng ký môn học này.')
                else:
                    print('==> Tạo bản đăng ký thất bại.')
            case 4:
                if len(students) > 0:
                    students.sort(key=lambda x: (x.full_name.first_name, x.full_name.last_name))
                    print('==> Danh sách sinh viên sau khi sắp xếp: ')
                    utils.show_students(students)
                else:
                    print('==> Danh sách sinh viên rỗng <==')
            case 5:
                if len(subjects) > 0:
                    subjects.sort(key=lambda x: x.name)
                    print('==> Danh sách môn học sau khi sắp xếp: ')
                    utils.show_subjects(subjects)
                else:
                    print('==> Danh sách môn học rỗng <==')
            case 6:
                if len(registers) > 0:
                    utils.sort_registers(registers)
                    print('==> Danh sách đăng ký sau khi sắp xếp: ')
                    utils.show_registers(registers)
                else:
                    print('==> Danh sách đăng ký rỗng <==')
            case 7:
                if len(students) > 0:
                    utils.show_students(students)
                else:
                    print('==> Danh sách sinh viên rỗng <==')
            case 8:
                if len(subjects) > 0:
                    utils.show_subjects(subjects)
                else:
                    print('==> Danh sách môn học rỗng <==')
            case 9:
                if len(registers) > 0:
                    utils.show_registers(registers)
                else:
                    print('==> Danh sách đăng ký rỗng <==')
            case 10:
                if len(registers) > 0:
                    utils.find_registed_subject(registers)
                else:
                    print('==> Danh sách đăng ký rỗng <==')
            case 11:
                if len(registers) > 0:
                    utils.find_student_by_subject(registers)
                else:
                    print('==> Danh sách đăng ký rỗng <==')
            case 12:
                if len(registers) > 0:
                    utils.statistics_by_subject(registers, subjects)
                else:
                    print('==> Danh sách đăng ký rỗng <==')
            case 13:
                if len(registers) > 0:
                    utils.sort_registers(registers)
                    utils.earliest_register(registers)
                else:
                    print('==> Danh sách đăng ký rỗng <==')
            case 14:
                if len(registers) > 0:
                    utils.sort_registers(registers)
                    utils.latest_register(registers)
                else:
                    print('==> Danh sách đăng ký rỗng <==')
            case 15:
                if len(registers) > 0:
                    result = utils.remove_register(registers)
                    if result:
                        print('==> Xóa bản đăng ký thành công!')
                        if len(registers) > 0:
                            register_data = utils.create_register_xml_data(registers)
                            register_file_name = 'register.xml'
                            utils.update_xml_file(register_data, register_file_name)
                    else:
                        print('==> Sai mã sinh viên hoặc mã môn học. Xóa bản đăng ký thất bại!')
                else:
                    print('==> Danh sách đăng ký rỗng <==')
            case 16:
                if len(students) > 0:
                    students_data = utils.create_students_xml_data(students)
                    student_file_name = 'student.xml'
                    utils.update_xml_file(students_data, student_file_name)
                else:
                    print('==> Danh sách sinh viên rỗng <==')
                if len(subjects) > 0:
                    subjects_data = utils.create_subjects_xml_data(subjects)
                    subject_file_name = 'subject.xml'
                    utils.update_xml_file(subjects_data, subject_file_name)
                else:
                    print('==> Danh sách môn học rỗng <name==')
                if len(registers) > 0:
                    register_data = utils.create_register_xml_data(registers)
                    register_file_name = 'register.xml'
                    utils.update_xml_file(register_data, register_file_name)
                else:
                    print('==> Danh sách đăng ký rỗng <==')
            case 17:
                print('==> Chương trình kết thúc <==')
                break
            case _:
                print('==> Lựa chọn không hợp lệ. Vui lòng nhập số 1-17. <==')
