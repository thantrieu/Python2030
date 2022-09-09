from utils import *

if __name__ == '__main__':
    students = read_students_from_file()
    teachers = read_teachers_from_file()
    subjects = read_subject_from_file()
    courses = read_course_from_file(teachers, subjects)
    fill_transcript_for_courses(courses, students)

    # update auto increment id for classes:
    update_course_auto_id(courses)
    update_student_auto_id(students)
    update_subject_auto_id(subjects)
    update_teacher_auto_id(teachers)
    update_transcript_auto_id(courses)

    option = '============================== OPTION ==============================\n' \
             '1. Thêm mới sinh viên vào danh sách sinh viên.\n' \
             '2. Thêm mới giảng viên vào danh sách giảng viên.\n' \
             '3. Thêm mới môn học vào danh sách môn học.\n' \
             '4. Thêm mới lớp học vào danh sách lớp học.\n' \
             '5. Nhập danh sách sinh viên cho lớp học.\n' \
             '6. Hiển thị danh sách sinh viên ra màn hình.\n' \
             '7. Hiển thị danh sách môn học ra màn hình.\n' \
             '8. Hiển thị danh sách giảng viên ra màn hình.\n' \
             '9. Hiển thị danh sách các lớp học.\n' \
             '10. Hiển thị danh sách bảng điểm của từng lớp.\n' \
             '11. Sắp xếp danh sách sinh viên theo tên tăng dần.\n' \
             '12. Sắp xếp danh sách sinh viên theo ngày sinh tăng dần.\n' \
             '13. Sắp xếp danh sách môn học theo tên môn học.\n' \
             '14. Sắp xếp danh sách lớp học theo tên phòng học.\n' \
             '15. Sắp xếp danh sách sinh viên trong lớp theo điểm giảm dần.\n' \
             '16. Liệt kê các sinh viên có điểm cao nhất trong lớp theo mã lớp.\n' \
             '17. Liệt kê các sinh viên có điểm cao nhất theo từng môn học.\n' \
             '18. Tìm sinh viên trong lớp theo điểm và mã lớp.\n' \
             '19. Thống kê số lượng sinh viên trong một lớp theo học lực giảm dần.\n' \
             '20. Thống kê số lượng sinh viên có học lực giỏi, xuất sắc theo từng môn.\n' \
             '21. Kết thúc chương trình.\n' \
             'Xin mời chọn chức năng(1-21): '
    while True:
        choice = int(input(option))
        match choice:
            case 1:
                new_student = create_student()
                if new_student is None:
                    print('==> Tạo sinh viên thất bại. <==')
                else:
                    students.append(new_student)
                    print('==> Tạo sinh viên thành công. <==')
            case 2:
                new_teacher = create_teacher()
                if new_teacher is None:
                    print('==> Tạo mới giảng viên thất bại. <==')
                else:
                    teachers.append(new_teacher)
                    print('==> Tạo mới giảng viên thành công. <==')
            case 3:
                subject = create_subject()
                if subject is None:
                    print('==> Tạo mới môn học thất bại. <==')
                else:
                    subjects.append(subject)
                    print('==> Tạo mới môn học thành công. <==')
            case 4:
                course = create_new_course(subjects, teachers)
                if course is None:
                    print('==> Tạo khóa học thất bại. <==')
                else:
                    courses.append(course)
                    print('==> Tạo khóa học thành công. <==')
            case 5:
                if len(courses) > 0:
                    create_new_transcript(courses, students)
                else:
                    print('==> Danh sách các lớp học trống. <==')
            case 6:
                if len(students) > 0:
                    show_students(students)
                else:
                    print("==> Danh sách sinh viên rỗng. <==")
            case 7:
                if len(subjects) > 0:
                    show_subjects(subjects)
                else:
                    print("==> Danh sách môn học rỗng. <==")
            case 8:
                if len(teachers) > 0:
                    show_teacher(teachers)
                else:
                    print("==> Danh sách giảng viên rỗng. <==")
            case 9:
                show_course(courses)
            case 10:
                show_transcripts(courses)
            case 11:
                if len(students) > 0:
                    students.sort(key=lambda x: (x.full_name.first_name, x.full_name.last_name))
                    show_students(students)
                else:
                    print('==> Danh sách sinh viên rỗng. <==')
            case 12:
                if len(students) > 0:
                    students.sort(key=lambda x: x.birth_date)
                    show_students(students)
                else:
                    print('==> Danh sách sinh viên rỗng. <==')
            case 13:
                if len(subjects) > 0:
                    subjects.sort(key=lambda x: x.name)
                    show_subjects(subjects)
                else:
                    print('==> Danh sách môn học viên rỗng. <==')
            case 14:
                if len(courses) > 0:
                    courses.sort(key=lambda x: x.room)
                    show_course(courses)
                else:
                    print('==> Danh sách các lớp học rỗng. <==')
            case 15:
                if len(courses) > 0:
                    course_id = input('Mã lớp cần sắp xếp: ')
                    for i in range(len(courses)):
                        if courses[i].course_id == course_id:
                            courses[i].transcripts.sort(key=lambda x: -x.gpa)
                            show_transcripts([courses[i]])
                            break
                else:
                    print('==> Danh sách các lớp học rỗng. <==')
            case 16:
                if len(courses) > 0:
                    listed_student_with_max_gpa(courses)
                else:
                    print('==> Danh sách các lớp học rỗng. <==')
            case 17:
                if len(courses) > 0:
                    find_highest_gpa_by_subject(subjects, courses)
                else:
                    print('==> Danh sách các lớp học rỗng. <==')
            case 18:
                if len(courses) > 0:
                    find_student_in_course(courses)
                else:
                    print('==> Danh sách các lớp học rỗng. <==')
            case 19:
                if len(courses) > 0:
                    stat_student_in_course(courses)
                else:
                    print('==> Danh sách các lớp học rỗng. <==')
            case 20:
                if len(courses) > 0:
                    stat_student_by_subjects(subjects, courses)
                else:
                    print('==> Danh sách các lớp học rỗng. <==')
            case 21:
                print("==> Chương trình kết thúc. <==")
                break
            case _:
                print('==> Lựa chọn không hợp lệ. Vui lòng nhập số 1-20. <==')
