from net.braniumacademy.ex_chapter5.lesson52.exercises3.bank_account import BankAccount


def create_bank_account():
    acc_num = input("Nhập số TK: ")
    owner = input("Nhập tên chủ thẻ: ").upper()  # viết hoa tên chủ thẻ
    acc_type = input("Loại tài khoản: ")
    bank = input("Ngân hàng phát hành: ")
    balance = int(input("Số dư: "))
    start_date = input("Ngày phát hành: ")
    end_date = input("Ngày hết hạn: ")
    return BankAccount(acc_num, owner,
                       acc_type, balance,
                       bank, start_date, end_date)


def show_list_accounts(accounts):
    print('====================== DANH SÁCH TÀI KHOẢN ======================')
    print(f'{"Số TK":15}{"Chủ TK":22}{"Loại thẻ":10}'
          f'{"Số dư":12}{"Ngân hàng":10}{"Ngày PH":12}{"Ngày KT":12}')
    for acc in accounts:
        show_acc(acc)


def show_acc(acc):
    print(f'{acc.acc_number:15}{acc.owner:22}{acc.card_type:10}'
          f'{acc.balance:<12}{acc.bank:10}{acc.start:12}{acc.end:12}')


def deposit(accounts):
    acc_num = input('Nhập số tài khoản: ')
    if accounts.get(acc_num) is not None:
        amount = int(input('Nhập số tiền muốn nạp: '))
        accounts.get(acc_num).deposit(amount)
    else:
        print('=== Tài khoản đích không tồn tại ===')


def withdraw(accounts):
    acc_num = input('Nhập số tài khoản: ')
    if accounts.get(acc_num) is not None:
        amount = int(input('Nhập số tiền muốn rút: '))
        accounts.get(acc_num).withdraw(amount)
    else:
        print('=== Tài khoản đích không tồn tại ===')


def transfer(accounts):
    source_acc = input('Nhập số tài khoản nguồn: ')
    if accounts.get(source_acc) is not None:
        target_acc = input('Nhập số tài khoản đích: ')
        if accounts.get(target_acc) is not None:
            amount = int(input('Nhập số tiền muốn chuyển: '))
            accounts.get(source_acc).transfer(accounts.get(target_acc), amount)
    else:
        print('=== Tài khoản đích không tồn tại ===')


def find_by_name(accounts):
    result = []
    key = input('Enter name to search: ')
    for e in accounts.keys():
        if accounts.get(e).owner.count(key) > 0:
            result.append(accounts.get(e))
    return result


def find_by_balance(accounts, x):
    print(f'=== Danh sách tài khoản có số dư >= {x} ===')
    for a in accounts:
        if a.balance >= x:
            show_acc(a)
