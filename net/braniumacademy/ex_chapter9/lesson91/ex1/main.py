from utils import *

# nhập thử cả giá trị hợp lệ và không hợp lệ xem điều gì xảy ra
if __name__ == '__main__':
    try:
        student = create_student()
        print('==> Thông tin học sinh: <==')
        show_student_info(student)
    except ValueError as e:
        print(e)
