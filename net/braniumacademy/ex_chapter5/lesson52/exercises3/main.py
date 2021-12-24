from net.braniumacademy.ex_chapter5.lesson52.exercises3.bank_account import BankAccount
from net.braniumacademy.ex_chapter5.lesson52.exercises3 import utils

option = '=================== TÙY CHỌN ===================' \
         '1. Thêm mới một tài khoản vào danh sách tài khoản.\n' \
         '2. hiển thị danh sách tài khoản ra màn hình.\n' \
         '3. Nạp tiền vào tài khoản.\n' \
         '4. Rút tiền khỏi tài khoản.\n' \
         '5. Chuyển khoản.\n6. Tìm tài khoản theo tên tài khoản.\n' \
         '7. Tìm tài khoản theo số tài khoản.\n' \
         '8. Tìm tài khoản có số dư > x.\n' \
         '9. Xóa tài khoản.\n10. Sắp xếp danh sách TK theo số dư tăng dần.\n' \
         '11. Sắp xếp tài khoản theo số dư giảm dần.\n' \
         '0. Thoát chương trình.\n' \
         'Bạn chọn? '
accounts = []
while True:
    choice = int(input(option))
    match choice:
        case 0:
            print("=== Chương trình kết thúc ===")
            break
        case 1:
            acc = utils.create_bank_account()
            accounts.append(acc)
        case 2:
            if len(accounts) > 0:
                utils.show_list_accounts(accounts)
            else:
                print("=== Danh sách rỗng ===")
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
        case _:
            print("Sai chức năng. Vui lòng chọn lại!")


