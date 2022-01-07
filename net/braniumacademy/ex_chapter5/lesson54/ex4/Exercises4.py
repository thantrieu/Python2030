class BankAcc:
    DEFAULT_BALANCE = 70000

    def __init__(self, acc_num, owner, start, end,
                 balance, bank='VCB', avg_balance=0, status=1, total=0):
        self.acc_number = acc_num
        self.owner = owner
        self.start = start
        self.end = end
        self.balance = balance
        self.bank = bank
        self.status = status
        self.avg_balance = avg_balance
        self.total = total

    def check_balance(self):
        """Kiểm tra số dư trong tài khoản."""
        if self.status == 1:
            print(f'Account number: {self.acc_number}')
            print(f'Owner: {self.owner}')
            print(f'Balance: {self.balance}$')
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

    def withdraw(self, amount, bank):
        """Rút tiền."""
        if self.status == 1:
            if 0 < amount < self.balance - BankAcc.DEFAULT_BALANCE \
                    and len(bank) > 0:
                self.balance -= amount
                return amount
            else:
                return -1
        else:
            print('Your account locked. Please unlock and try again.')
            return -1

    def pay_bill(self, bill, amount, inter=False):
        """Thanh toán hóa đơn."""
        if self.status == 1:
            if 0 < amount < self.balance - BankAcc.DEFAULT_BALANCE:
                print(f'Pay for {bill} {amount}$')
                self.balance -= amount
            else:
                print('Your balance is not enough.')
        else:
            print('Your account locked. Please unlock and try again.')
            return -1

    def saving(self, amount):
        """Gửi tiết kiệm."""
        if self.status == 1:
            if 0 < amount < self.balance - BankAcc.DEFAULT_BALANCE:
                print(f'Saving {amount}$')
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


class DomesticCard(BankAcc):
    INTRA_FEE = 1100
    INTER_FEE = 3300
    BALANCE_NO_FEE = 2000000

    def __init__(self, acc_num, owner, bank, start, end, balance, limit):
        super().__init__(acc_num, owner, start, end, balance, bank)
        self.limit = limit  # hạn mức giao dịch / lần

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


class VisaCard(BankAcc):
    INTRA_FEE = 0
    INTER_FEE = 9900
    FOREIN_FEE = 23900
    BALANCE_NO_FEE = 5000000
    EXCHANGE_RATE = 23500

    def __init__(self, acc_num, owner, bank, start, end, balance,
                 anual_fee, transaction_fee, limit, uuid=8484):
        super().__init__(acc_num, owner, start, end, balance, bank)
        self.anual_fee = anual_fee
        self.limit = limit
        self.transaction_fee = transaction_fee
        self.uuid = uuid

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
            self.balance -= self.transaction_fee * VisaCard.EXCHANGE_RATE

    def transfer(self, other, amount):
        if self.total < self.limit:
            return super(VisaCard, self).transfer(other, amount)
        else:
            print('Your account has exceeded its daily transaction limit.')
            return -1


def create_dom_acc():
    """Tạo và trả về thông tin thẻ thanh toán nội địa."""
    acc_num = input('Nhập số tài khoản: ')
    owner = input('Nhập tên chủ TK: ')
    bank = input('Ngân hàng phát hành thẻ(tên viết tắt tiếng Anh): ')
    start = input('Bắt đầu có hiệu lực từ: ')
    end = input('Ngày hết hiệu lực: ')
    balance = int(input('Số dư: '))
    limit = int(input('Hạn mức mỗi giao dịch: '))
    return DomesticCard(acc_num, owner, bank, start, end, balance, limit)


def create_visa_acc():
    """Tạo và trả về thông tin thẻ thanh toán quốc tế."""
    acc_num = input('Nhập số tài khoản: ')
    owner = input('Nhập tên chủ TK: ')
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
            case _:
                print('==> Chức năng không hợp lệ. Vui lòng chọn lại! <==')
