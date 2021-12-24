from net.braniumacademy.ex_chapter5.lesson52.exercises3.bank_account import BankAccount


def create_bank_account():
    acc_num = input("Nhập số TK: ")
    owner = input("Nhập tên chủ thẻ: ")
    acc_type = input("Loại tài khoản: ")
    bank = input("Ngân hàng phát hành: ")
    balance = int(input("Số dư: "))
    start_date = input("Ngày phát hành: ")
    end_date = input("Ngày hết hạn: ")
    return BankAccount(acc_num, owner,
                       acc_type, balance,
                       bank, start_date, end_date)


def show_list_accounts(accounts):
    print(f'{"Số TK":15}{"Chủ TK":22}{"Loại thẻ":10}'
          f'{"Số dư":12}{"Ngân hàng":10}{"Ngày PH":12}{"Ngày KT":12}')
    print('====================== DANH SÁCH TÀI KHOẢN ======================')
    for acc in accounts:
        show_acc(acc)


def show_acc(acc):
    print(f'{acc.acc_number:15}{acc.owner:22}{acc.card_type:10}'
          f'{acc.balance:12}{acc.bank:10}{acc.start:12}{acc.end:12}')
