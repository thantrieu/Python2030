from utils import *

if __name__ == '__main__':
    students = read_students_from_file()
    teachers = read_teachers_from_file()
    subjects = read_subject_from_file()
    courses = read_course_from_file(teachers, subjects)
    fill_transcript_for_courses(courses, students)

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
                students.append(new_student)
            case 2:
                new_teacher = create_teacher()
                teachers.append(new_teacher)
            case 3:
                subject = create_subject()
                subjects.append(subject)
            case 4:
                break
            case 5:
                break
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
                break
            case 12:
                break
            case 13:
                break
            case 14:
                break
            case 15:
                break
            case 16:
                break
            case 17:
                break
            case 18:
                break
            case 19:
                break
            case 20:
                break
            case 21:
                print("==> Chương trình kết thúc. <==")
                break
            case _:
                print('==> Lựa chọn không hợp lệ. Vui lòng nhập số 1-20. <==')
