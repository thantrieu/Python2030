if __name__ == '__main__':
    students = []
    teachers = []
    subjects = []
    courses = []
    option = '============================== OPTION ==============================\n' \
             '1. Thêm mới sinh viên vào danh sách sinh viên.\n' \
             '2. Thêm mới giảng viên vào danh sách giảng viên.\n' \
             '3. Thêm mới môn học vào danh sách môn học.\n' \
             '4. Thêm mới lớp học vào danh sách lớp học.\n' \
             '5. Lập danh sách lớp học.\n' \
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
                break
            case _:
                print('==> Lựa chọn không hợp lệ. Vui lòng nhập số 1-20. <==')