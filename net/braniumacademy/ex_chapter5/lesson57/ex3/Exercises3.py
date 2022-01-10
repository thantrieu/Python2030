from abc import abstractmethod, ABC


class BankAcc(ABC):
    DEFAULT_BALANCE = 70000

    def __init__(self, acc_num, owner, start, end,
                 balance, bank='VCB', avg_balance=0, status=1, total=0):
        self.__acc_number = acc_num
        self.__owner = owner
        self.__start = start
        self.__end = end
        self.__balance = balance
        self.__bank = bank
        self.__status = status
        self.__avg_balance = avg_balance
        self.__total = total

    @property
    def acc_number(self):
        return self.__acc_number

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, value):
        self.__balance = value

    @property
    def owner(self):
        return self.__owner

    @property
    def start(self):
        return self.__start

    @property
    def end(self):
        return self.end

    @property
    def bank(self):
        return self.__bank

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, value):
        self.__status = value

    @property
    def total(self):
        return self.__total

    @total.setter
    def total(self, value):
        self.__total = value

    @property
    def avg_balance(self):
        return self.__avg_balance

    @avg_balance.setter
    def avg_balance(self, value):
        self.__avg_balance = value

    def check_balance(self):
        """Kiểm tra số dư trong tài khoản."""
        if self.status == 1:
            print(f'Account number: {self.acc_number}')
            print(f'Owner: {self.__owner}')
            print(f'Balance: {self.balance}đ')
        else:
            print('Your account locked. Please unlock and try again.')

    def transfer(self, other, amount):
        """Thực hiện chuyển khoản."""
        if self.status == 1:
            if amount < self.balance - BankAcc.DEFAULT_BALANCE:
                other.balance += amount
                self.balance -= amount
                self.total += amount  # Giả định hạn mức giao dịch chỉ áp dụng với chuyển tiền.
                return amount  # trả về số tiền đã chuyển
            else:
                print('Your balance is not enough to transfer.')
                return -1  # giả định trả về số âm nếu giao dịch thất bại
        else:
            print('Your account locked. Please unlock and try again.')
            return -1

    def deposit(self, amount):
        """Nạp tiền vào tài khoản."""
        if self.status == 1:
            if amount > 0:
                self.balance += amount
                return amount
            else:
                return -1
        else:
            print('Your account locked. Please unlock and try again.')
            return -1

    @abstractmethod
    def withdraw(self, amount, bank):
        """ Rút tiền. Phương thức triển khai mặc định ở lớp cha.
            Lớp con phải override lại để sử dụng.
        """
        if self.status == 1:
            if 0 < amount < self.balance - BankAcc.DEFAULT_BALANCE \
                    and len(bank) > 0:
                self.balance -= amount
                return amount
            else:
                print('Your balance is not enough.')
                return -1
        else:
            print('Your account locked. Please unlock and try again.')
            return -1

    def pay_bill(self, bill, amount, inter=False):
        """Thanh toán hóa đơn."""
        if self.status == 1:
            if 0 < amount < self.balance - BankAcc.DEFAULT_BALANCE:
                print(f'Pay for {bill} {amount}đ')
                self.balance -= amount
                return amount
            else:
                print('Your balance is not enough.')
                return -1
        else:
            print('Your account locked. Please unlock and try again.')
            return -1

    def saving(self, amount):
        """Gửi tiết kiệm."""
        if self.status == 1:
            if 0 < amount < self.balance - BankAcc.DEFAULT_BALANCE:
                print(f'Saving {amount}đ')
                self.balance -= amount
            else:
                print('Your balance is not enough.')
        else:
            print('Your account locked. Please unlock and try again.')
            return -1

    def lock(self):
        """Khóa tài khoản."""
        self.status = 0

    def active(self):
        """Kích hoạt tài khoản."""
        self.status = 1

    @abstractmethod
    def __str__(self):
        pass


class DomesticCard(BankAcc):
    INTRA_FEE = 1100
    INTER_FEE = 3300
    BALANCE_NO_FEE = 2000000

    def __init__(self, acc_num, owner, bank, start, end, balance, limit):
        super().__init__(acc_num, owner, start, end, balance, bank)
        self.__limit = limit  # hạn mức giao dịch / lần

    @property
    def limit(self):
        return self.__limit

    def withdraw(self, amount, bank):
        """ Rút tiền thẻ nội địa sẽ tốn 1100đ nếu cùng ngân hàng
            và 3300đ nếu khác ngân hàng. Ta bổ sung giá trị này vào
            phương thức rút tiền của thẻ nội địa và trả về tổng
            chi phí rút tiền.
        """
        result = super().withdraw(amount, bank)
        # nếu số dư bình quân cuối tháng mà < 2tr thì mất phí rút tiền
        if result > 0 and self.avg_balance < DomesticCard.BALANCE_NO_FEE:
            if bank == self.bank:
                self.balance -= DomesticCard.INTRA_FEE
                result += DomesticCard.INTRA_FEE
            else:
                self.balance -= DomesticCard.INTER_FEE
                result += DomesticCard.INTER_FEE
        return result

    def transfer(self, other, amount):
        if amount < self.limit:
            return super(DomesticCard, self).transfer(other, amount)
        else:
            print('Your account has exceeded its transaction limit.')
            return -1

    def __str__(self):
        super_info = f'acc_num={self.acc_number}, owner={self.owner}, ' \
                     f'bank={self.bank}, balance={self.balance}, ' \
                     f'start={self.start}, end={self.end}, ' \
                     f'avg_balance={self.avg_balance}, total={self.total}, ' \
                     f'status={self.status}'
        return f'DomesticCard[{super_info}, limit={self.limit}]'


class VisaCard(BankAcc):
    INTRA_FEE = 0
    INTER_FEE = 9900
    FOREIN_FEE = 23900
    BALANCE_NO_FEE = 5000000
    EXCHANGE_RATE = 23500

    def __init__(self, acc_num, owner, bank, start, end, balance,
                 anual_fee, transaction_fee, limit, uuid=8484):
        super().__init__(acc_num, owner, start, end, balance, bank)
        self.__anual_fee = anual_fee
        self.__limit = limit
        self.__transaction_fee = transaction_fee
        self.__uuid = uuid

    @property
    def anual_fee(self):
        return self.__anual_fee

    @property
    def uuid(self):
        return self.__uuid

    @property
    def limit(self):
        return self.__limit

    @property
    def transaction_fee(self):
        return self.__transaction_fee

    def withdraw(self, amount, bank):
        """ Rút tiền thẻ nội địa sẽ tốn 1100đ nếu cùng ngân hàng
            và 3300đ nếu khác ngân hàng. Ta bổ sung giá trị này vào
            phương thức rút tiền của thẻ nội địa và trả về tổng
            chi phí rút tiền.
        """
        result = super().withdraw(amount, bank)
        # nếu số dư bình quân cuối tháng mà < 5tr thì mất phí rút tiền
        if result > 0 and self.avg_balance < VisaCard.BALANCE_NO_FEE:
            if bank == self.bank:
                fee = VisaCard.INTRA_FEE
                result += fee
            elif self.is_domestic_bank(bank):
                fee = VisaCard.INTER_FEE
                result += fee
            else:
                fee = VisaCard.FOREIN_FEE
                result += fee
            self.balance -= fee
        return result

    def is_domestic_bank(self, bank):
        """Kiểm tra ngân hàng là trong nước hay nước ngoài. Dưới đây là
            một số ngân hàng làm ví dụ. Bạn tự bổ sung các ngân hàng khác.
        """
        match bank:
            case 'VCB' | 'MSB' | 'MB' | 'ACB' | 'ABBANK' | 'VietinBank' | \
                 'BIDV' | 'Techcombank' | 'Agribank' | 'OCB' | 'VIB' | 'SHB' | \
                 'SCB' | 'VPBank':
                return True
            case _:
                return False

    def pay_bill(self, bill, amount, inter=False):
        """Khi thanh toán quốc tế thì trừ phí giao dịch quốc tế."""
        result = super().pay_bill(bill, amount)
        if inter is True and result > 0 and \
                self.balance > self.balance - BankAcc.DEFAULT_BALANCE:
            self.balance -= self.__transaction_fee * VisaCard.EXCHANGE_RATE
        return result

    def transfer(self, other, amount):
        if self.total < self.limit:
            return super(VisaCard, self).transfer(other, amount)
        else:
            print('Your account has exceeded its daily transaction limit.')
            return -1

    def __str__(self):
        super_info = f'acc_num={self.acc_number}, owner={self.owner}, ' \
                     f'bank={self.bank}, balance={self.balance}, ' \
                     f'start={self.start}, end={self.end}, ' \
                     f'avg_balance={self.avg_balance}, total={self.total}, ' \
                     f'status={self.status}'
        return f'VisaCard[{super_info}, anual_fee={self.anual_fee}, ' \
               f'transaction_fee={self.__transaction_fee}, limit={self.limit}, ' \
               f'uuid={self.__uuid}]'


def create_dom_acc():
    """Tạo và trả về thông tin thẻ thanh toán nội địa."""
    acc_num = input('Nhập số tài khoản: ')
    owner = input('Nhập tên chủ TK: ').upper()
    bank = input('Ngân hàng phát hành thẻ(tên viết tắt tiếng Anh): ')
    start = input('Bắt đầu có hiệu lực từ: ')
    end = input('Ngày hết hiệu lực: ')
    balance = int(input('Số dư: '))
    limit = int(input('Hạn mức mỗi giao dịch: '))
    return DomesticCard(acc_num, owner, bank, start, end, balance, limit)


def create_visa_acc():
    """Tạo và trả về thông tin thẻ thanh toán quốc tế."""
    acc_num = input('Nhập số tài khoản: ')
    owner = input('Nhập tên chủ TK: ').upper()
    bank = input('Ngân hàng phát hành thẻ(tên viết tắt tiếng Anh): ')
    start = input('Bắt đầu có hiệu lực từ: ')
    end = input('Ngày hết hiệu lực: ')
    balance = int(input('Số dư: '))
    limit = int(input('Hạn mức mỗi giao dịch trong ngày: '))
    anual_fee = int(input('Phí thường niên: '))
    transaction_fee = float(input('Phí thanh toán quốc tế(USD): '))
    uuid = int(input('Số định danh quốc tế: '))
    return VisaCard(acc_num, owner, bank, start, end,
                    balance, anual_fee, transaction_fee, limit, uuid)


def check_balance(accounts):
    acc_number = input('Nhập số tài khoản: ')
    for acc in accounts:
        if acc.acc_number == acc_number:
            acc.check_balance()


def deposit(accounts):
    acc_number = input('Nhập số tài khoản: ')
    is_success = False
    for acc in accounts:
        if acc.acc_number == acc_number:
            amount = int(input('Nhập số tiền muốn nộp: '))
            if acc.deposit(amount) > 0:
                print('==> Giao dịch thành công.')
                acc.check_balance()
                is_success = True
            else:
                print('==> Giao dịch thất bại.')
            break
    if is_success is False:
        print('==> Giao dịch thất bại. Không tìm thấy tài khoản đích.')


def withdraw(accounts):
    acc_number = input('Nhập số tài khoản: ')
    is_success = False
    for acc in accounts:
        if acc.acc_number == acc_number:
            is_success = True
            amount = int(input('Nhập số tiền muốn rút: '))
            if acc.withdraw(amount, acc.bank) > 0:
                print('==> Giao dịch thành công.')
                acc.check_balance()
            else:
                print('==> Giao dịch thất bại.')
            break
    if is_success is False:
        print('==> Giao dịch thất bại. Không tìm thấy tài khoản đích.')


def pay_the_bill(accounts):
    bill_name = input('Nhập tên hóa đơn: ')
    acc_number = input('Nhập số tài khoản: ')
    is_success = False
    for acc in accounts:
        if acc.acc_number == acc_number:
            amount = int(input('Nhập số tiền cần thanh toán: '))
            if acc.pay_bill(bill_name, amount) > 0:
                print('==> Giao dịch thành công.')
                acc.check_balance()
                is_success = True
            else:
                print('==> Giao dịch thất bại.')
            break
    if is_success is False:
        print('==> Giao dịch thất bại. Không tìm thấy tài khoản đích.')


def pay_the_international_bill(accounts):
    bill_name = input('Nhập tên hóa đơn: ')
    acc_number = input('Nhập số tài khoản: ')
    is_success = False
    for acc in accounts:
        if acc.acc_number == acc_number:
            if isinstance(acc, DomesticCard):
                print('Tài khoản thanh toán nội địa không thể chuyển tiền quốc tế.')
                break
            amount = int(input('Nhập số tiền cần thanh toán: '))
            if acc.pay_bill(bill_name, amount, True) > 0:
                print('==> Giao dịch thành công.')
                acc.check_balance()
                is_success = True
            else:
                print('==> Giao dịch thất bại.')
            break
    if is_success is False:
        print('==> Giao dịch thất bại. Không tìm thấy tài khoản đích.')


def transfer(accounts):
    src = input('Nhập số tài khoản nguồn: ')
    is_success = False
    for acc in accounts:
        if acc.acc_number == src:
            dst = input('Nhập số tài khoản đích: ')
            for acc_dst in accounts:
                if acc_dst.acc_number == dst:
                    if acc_dst.bank != acc.bank:
                        print('==> Tài khoản khác ngân hàng.')
                        break
                    amount = int(input('Nhập số tiền muốn chuyển: '))
                    if acc.transfer(acc_dst, amount) > 0:
                        print('==> Giao dịch thành công.')
                        acc.check_balance()
                        is_success = True
                    else:
                        print('==> Giao dịch thất bại.')
                    break
            break
    if is_success is False:
        print('==> Giao dịch thất bại. Không tồn tại tài khoản nguồn hoặc đích.')


def transfer_other_bank(accounts):
    src = input('Nhập số tài khoản nguồn: ')
    is_success = False
    for acc in accounts:
        if acc.acc_number == src:
            dst = input('Nhập số tài khoản đích: ')
            for acc_dst in accounts:
                if acc_dst.acc_number == dst:
                    is_success = True
                    if acc_dst.bank == acc.bank:
                        print('==> Tài khoản cùng ngân hàng.')
                        break
                    amount = int(input('Nhập số tiền muốn chuyển: '))
                    if acc.transfer(acc_dst, amount) > 0:
                        print('==> Giao dịch thành công.')
                        acc.check_balance()
                    else:
                        print('==> Giao dịch thất bại.')
                    break
            break
    if is_success is False:
        print('==> Giao dịch thất bại. Không tìm thấy tài khoản nguồn hoặc đích.')


def active_account(accounts):
    src = input('Nhập số tài khoản nguồn: ')
    is_success = False
    for acc in accounts:
        if acc.acc_number == src:
            acc.active()
            print('==> Kích hoạt tài khoản thành công.')
            break
    if is_success is False:
        print('==> Không tìm thấy tài khoản đích.')


def find_account_by_balance(accounts):
    balance = int(input('Nhập số dư: '))
    counter = 0
    for acc in accounts:
        if acc.balance == balance:
            print(acc)
            counter += 1
    if counter == 0:
        print('==> Không tìm thấy kết quả.')


def listed_accounts(accounts):
    print('==> Danh sách tài khoản hiện có: ')
    for acc in accounts:
        print(acc)


def transfer_international(accounts):
    src = input('Nhập số tài khoản nguồn: ')
    is_success = False
    for acc in accounts:
        if acc.acc_number == src:
            if isinstance(acc, DomesticCard):
                print('Tài khoản thanh toán nội địa không thể chuyển tiền quốc tế.')
                break
            dst = input('Nhập số tài khoản đích: ')
            for acc_dst in accounts:
                if acc_dst.acc_number == dst:
                    is_success = True
                    amount = int(input('Nhập số tiền muốn chuyển: '))
                    if acc.transfer(acc_dst, amount) > 0:
                        print('==> Giao dịch thành công.')
                        acc.check_balance()
                    else:
                        print('==> Giao dịch thất bại.')
                    break
            break
    if is_success is False:
        print('==> Giao dịch thất bại. Không tìm thấy tài khoản nguồn hoặc đích.')


if __name__ == '__main__':
    accounts = []
    option = '======================= MENU =======================\n' \
             '1. Thêm mới 1 tài khoản nội địa.\n' \
             '2. Thêm mới 1 tài khoản quốc tế.\n' \
             '3. Kiểm tra số dư theo số tài khoản.\n' \
             '4. Nạp tiền vào tài khoản theo số tài khoản.\n' \
             '5. Rút tiền nội ngân hàng.\n' \
             '6. Thanh toán hóa đơn nội địa.\n' \
             '7. Thanh toán hóa đơn quốc tế.\n' \
             '8. Chuyển tiền nội địa cùng ngân hàng.\n' \
             '9. Chuyển tiền nội địa khác ngân hàng.\n' \
             '10. Chuyển tiền quốc tế.\n' \
             '11. Kích hoạt tài khoản.\n' \
             '12. Liệt kê thông tin các tài khoản hiện có.\n' \
             '13. Sắp xếp danh sách tài khoản theo số dư giảm dần.\n' \
             '14. Tìm tài khoản theo số dư.\n' \
             '0. Thoát chương trình.\n' \
             'Xin mời chọn: '
    while True:
        choice = int(input(option))
        match choice:
            case 0:
                print('==> Chương trình kết thúc <==')
                break
            case 1:
                acc = create_dom_acc()
                accounts.append(acc)
            case 2:
                acc = create_visa_acc()
                accounts.append(acc)
            case 3:
                if len(accounts) > 0:
                    check_balance(accounts)
                else:
                    print('==> Danh sách tài khoản rỗng.')
            case 4:
                if len(accounts) > 0:
                    deposit(accounts)
                else:
                    print('==> Danh sách tài khoản rỗng.')
            case 5:
                if len(accounts) > 0:
                    withdraw(accounts)
                else:
                    print('==> Danh sách tài khoản rỗng.')
            case 6:
                if len(accounts) > 0:
                    pay_the_bill(accounts)
                else:
                    print('==> Danh sách tài khoản rỗng.')
            case 7:
                if len(accounts) > 0:
                    pay_the_international_bill(accounts)
                else:
                    print('==> Danh sách tài khoản rỗng.')
            case 8:
                if len(accounts) > 0:
                    transfer(accounts)
                else:
                    print('==> Danh sách tài khoản rỗng.')
            case 9:
                if len(accounts) > 0:
                    transfer_other_bank(accounts)
                else:
                    print('==> Danh sách tài khoản rỗng.')
            case 10:
                if len(accounts) > 0:
                    transfer_international(accounts)
                else:
                    print('==> Danh sách tài khoản rỗng.')
            case 11:
                if len(accounts) > 0:
                    active_account(accounts)
                else:
                    print('==> Danh sách tài khoản rỗng.')
            case 12:
                if len(accounts) > 0:
                    listed_accounts(accounts)
                else:
                    print('==> Danh sách tài khoản rỗng.')
            case 13:
                if len(accounts) > 0:
                    accounts.sort(key=lambda x: (-x.balance, x.owner[x.owner.rfind(' ') + 1:]))
                    listed_accounts(accounts)
                else:
                    print('==> Danh sách tài khoản rỗng.')
            case 14:
                if len(accounts) > 0:
                    find_account_by_balance(accounts)
                else:
                    print('==> Danh sách tài khoản rỗng.')
            case _:
                print('==> Chức năng không hợp lệ. Vui lòng chọn lại! <==')
