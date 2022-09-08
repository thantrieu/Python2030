from utils import *

if __name__ == '__main__':
    students = create_fake_students()
    subjects = create_fake_subjects()
    courses = create_fake_couses(subjects)
    create_fake_transcripts(courses, students)

    option = "=============== OPTIONS ===============\n" \
             "1. Thêm mới môn học vào danh sách môn học.\n" \
             "2. Thêm mới sinh viên vào danh sách sinh viên.\n" \
             "3. Thêm mới một lớp học vào danh sách lớp học.\n" \
             "4. Hiển thị danh sách môn học.\n" \
             "5. Hiển thị danh sách sinh viên.\n" \
             "6. Hiển thị danh sách lớp học.\n" \
             "7. Nhập và tính điểm TB cho từng sinh viên.\n" \
             "8. Xét học lực cho từng sinh viên.\n" \
             "9. Hiển thị danh sách bảng điểm.\n" \
             "10. Sắp xếp danh sách bảng điểm theo điểm TB giảm dần.\n" \
             "11. Tìm sinh viên trong lớp học theo mã sinh viên.\n" \
             "12. Cho biết các sinh viên có điểm cao nhất.\n" \
             "13. Tìm thông tin bảng điểm của sinh viên theo điểm TB.\n" \
             "14. Thoát chương trình.\n" \
             "Bạn chọn? "
    while True:
        choice = int(input(option))
        match choice:
            case 1:
                subject = create_subject()
                if subject is not None:
                    subjects.append(subject)
                    print('==> Tạo mới môn học thành công! <==')
                else:
                    print('==> Tạo mới môn học thất bại. <==')
            case 2:
                student = create_student()
                if student is not None:
                    students.append(student)
                    print('==> Tạo mới sinh viên thành công. <==')
                else:
                    print('==> Tạo mới sinh viên thất bại. <==')
            case 3:
                course = create_course(subjects)
                if course is not None:
                    courses.append(course)
                    print('==> Tạo mới khóa học thành công. <==')
                else:
                    print('==> Tạo mới khóa học thất bại. <==')
            case 4:
                show_subjects(subjects)
            case 5:
                show_students(students)
            case 6:
                show_courses(courses)
            case 7:
                if len(courses) > 0:
                    add_transcript_to_course(courses, students)
                else:
                    print('==> Danh sách lớp học rỗng. <==')
            case 8:
                find_capacity(courses)
            case 9:
                show_transcripts(courses)
            case 10:
                sort_transcripts(courses)
                print('==> Danh bảng điểm sau khi sắp xếp: ')
                show_transcripts(courses)
            case 11:
                find_student_in_course(courses)
            case 12:
                find_student_with_max_gpa(courses)
            case 13:
                find_student_with_given_gpa(courses)
            case 14:
                print('==> Tạm biệt! Cảm ơn bạn đã sử dụng dịch vụ! <==')
                break
            case _:
                print('==> Sai tùy chọn. Hãy chọn các chức năng từ 1-14. <==')
