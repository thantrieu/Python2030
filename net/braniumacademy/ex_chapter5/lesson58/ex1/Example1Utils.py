import datetime

from .Exercises1 import Subject, Student, Register

if __name__ == '__main__':
    students = []
    subjects = []
    registers = []
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
             '15. Kết thúc chương trình.\n' \
             'Xin mời chọn chức năng(1-15): '
    while True:
        choice = int(input(option))
        match choice:
            case 1:
                pass
            case 2:
                pass
            case 3:
                pass
            case 4:
                pass
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
                pass
            case 15:
                print('==> Chương trình kết thúc <==')
            case _:
                print('==> Lựa chọn không hợp lệ. Vui lòng nhập số 1-15. <==')
