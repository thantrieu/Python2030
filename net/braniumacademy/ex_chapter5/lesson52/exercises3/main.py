from net.braniumacademy.ex_chapter5.lesson52.exercises3.bank_account import BankAccount
from net.braniumacademy.ex_chapter5.lesson52.exercises3 import utils

option = '===================== TÙY CHỌN =====================\n' \
         '1. Thêm mới một tài khoản vào danh sách tài khoản.\n' \
         '2. Hiển thị danh sách tài khoản ra màn hình.\n' \
         '3. Nạp tiền vào tài khoản.\n' \
         '4. Rút tiền khỏi tài khoản.\n' \
         '5. Chuyển khoản.\n6. Tìm tài khoản theo tên tài khoản.\n' \
         '7. Tìm tài khoản theo số tài khoản.\n' \
         '8. Tìm tài khoản có số dư > x.\n' \
         '9. Xóa tài khoản.\n10. Sắp xếp danh sách TK theo số dư tăng dần.\n' \
         '11. Sắp xếp tài khoản theo số dư giảm dần.\n' \
         '0. Thoát chương trình.\n' \
         'Bạn chọn? '
accounts = dict()
while True:
    choice = int(input(option))
    match choice:
        case 0:
            print("=== Chương trình kết thúc ===")
            break
        case 1:
            acc = utils.create_bank_account()
            accounts[acc.acc_number] = acc
        case 2:
            if len(accounts) > 0:
                utils.show_list_accounts(accounts.values())
            else:
                print("=== Danh sách tài khoản rỗng ===")
        case 3:
            if len(accounts) > 0:
                utils.deposit(accounts)
            else:
                print("=== Danh sách tài khoản rỗng ===")
        case 4:
            if len(accounts) > 0:
                utils.withdraw(accounts)
            else:
                print("=== Danh sách tài khoản rỗng ===")
        case 5:
            if len(accounts) > 0:
                utils.transfer(accounts)
            else:
                print("=== Danh sách tài khoản rỗng ===")
        case 6:
            if len(accounts) > 0:
                result = utils.find_by_name(accounts)
                if len(result) > 0:
                    print('=== Danh sách tài khoản thỏa mãn ===')
                    utils.show_list_accounts(accounts.values())
                else:
                    print('=== Không tìm thấy kết quả nào ===')
            else:
                print("=== Danh sách tài khoản rỗng ===")
            
        case 7:
            if len(accounts) > 0:
                acc_num = input('Nhập số tài khoản cần tìm: ')
                if accounts.get(acc_num) is not None:
                    utils.show_acc(accounts.get(acc_num))
                else:
                    print('=== Không tìm thấy kết quả nào ===')
            else:
                print('=== Danh sách tài khoản rỗng ===')
        case 8:
            if len(accounts) > 0:
                x = int(input('Nhập số dư x: '))
                utils.find_by_balance(accounts.values(), x)
            else:
                print('=== Danh sách tài khoản rỗng ===')
        case 9:
            if len(accounts) > 0:
                acc_num = input('Nhập số tài khoản cần xóa: ')
                result = accounts.pop(acc_num, None)
                if result is not None:
                    print('=== Xóa thành công ===')
                else:
                    print('=== Xóa thất bại ===')
            else:
                print('=== Danh sách tài khoản rỗng ===')
        case 10:
            if len(accounts) > 0:
                list_accounts = list(accounts.values())
                list_accounts.sort(key=lambda x: x.balance)
                utils.show_list_accounts(list_accounts)
            else:
                print('=== Danh sách tài khoản rỗng ===')
        case 11:
            if len(accounts) > 0:
                list_accounts = list(accounts.values())
                list_accounts.\
                    sort(key=lambda x: (-x.balance, x.owner[x.owner.rfind(' ')]))
                utils.show_list_accounts(list_accounts)
            else:
                print('=== Danh sách tài khoản rỗng ===')
        case _:
            print("Sai chức năng. Vui lòng chọn lại!")
