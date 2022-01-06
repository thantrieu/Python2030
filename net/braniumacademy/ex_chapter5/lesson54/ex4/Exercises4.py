class BankAcc:
    def __init__(self, acc_num, owner, start, end,
                 balance, bank='VCB', avg_balance=0, status=1):
        self.acc_number = acc_num
        self.owner = owner
        self.start = start
        self.end = end
        self.balance = balance
        self.bank = bank
        self.status = status
        self.avg_balance = avg_balance

    def check_balance(self):
        print(f'Account number: {self.acc_number}')
        print(f'Owner: {self.owner}')
        print(f'Balance: {self.balance}$')

    def transfer(self, other, amount):
        if amount < self.balance:
            other.balance += amount
            self.balance -= amount
            return amount  # trả về số tiền đã chuyển
        else:
            print('Your balance is not enough to transfer.')
            return -1  # giả định trả về số âm nếu giao dịch thất bại

    def deposit(self, amount):
        pass

    def withdraw(self, amount):
        pass

    def pay_bill(self, bill, amount):
        pass

    def saving(self, amount):
        pass

    def lock(self):
        self.status = 0

    def active(self):
        self.status = 1


class DomCard(BankAcc):
    pass


class InterCard(BankAcc):
    pass
