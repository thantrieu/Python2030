class BankAccount:
    """Lớp mô tả thông tin và hành động của tài khoản ngân hàng."""
    def __init__(self, acc_num, owner, type='Normal',
                 balance=0, bank='VCB', start=2025, end=2030):
        self.acc_number = acc_num
        self.owner = owner
        self.card_type = type
        self.balance = balance
        self.bank = bank
        self.start = start
        self.end = end

    def withdraw(self, amount):
        """Phương thức rút tiền. Số tiền cần rút phải < số dư"""
        if amount > self.balance:
            return -1
        else:
            self.balance -= amount
            self.check_balance()
            return amount

    def check_balance(self):
        """Phương thức kiểm tra số dư tài khoản."""
        print(f'Account {self.acc_number}\'s current balance is: {self.balance}$')

    def payment(self, service, amount):
        """Phương thức thanh toán dịch vụ nào đó có mức phí amount."""
        if self.balance < amount:
            return -1
        else:
            print(f'Make transaction pay for {service} amount: {amount}')
            self.balance -= amount
            print('Transaction success!')
            self.check_balance()

    def transfer(self, other, amount):
        """Phương thức này thực hiện việc chuyển tiền
        và trả về số tiền đã chuyển.
        """
        if len(other.acc_number) > 0 and amount < self.balance:
            self.balance -= amount
            other.balance += amount
            print(f'Transfer success!\nAccount {self.acc_number}: -{amount}$')
            self.check_balance()
            print(f'Account {other.acc_number}: +{amount}$')
            other.check_balance()
            return amount
        else:
            print('Transaction failed.')
            return -1

    def deposit(self, amount):
        """Phương thức nạp tiền vào tài khoản."""
        if amount > 0:
            self.balance += amount
            print(f'Transaction +{amount}$')
            self.check_balance()
            return amount
        else:
            print('Invalid amount!')
            return -1
