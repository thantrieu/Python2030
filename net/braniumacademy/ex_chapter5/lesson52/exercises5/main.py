from utils import *

if __name__ == '__main__':
    students = []
    subjects = []
    course = []
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
                pass
            case 3:
                pass
            case 4:
                show_subjects(subjects)
            case 5:
                pass
            case 6:
                pass
            case 7:
                pass
            case 8:
                pass
            case 9:
                pass
            case 10:
                pass
            case 11:
                pass
            case 12:
                pass
            case 13:
                pass
            case 14:
                print('==> Tạm biệt! Cảm ơn bạn đã sử dụng dịch vụ! <==')
                break
            case _:
                print('==> Sai tùy chọn. Hãy chọn các chức năng từ 1-14. <==')
