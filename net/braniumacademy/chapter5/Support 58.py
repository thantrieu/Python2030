class FullName:
    def __init__(self, fname):
        self.__full_name = None
        self.__mid_name = ''
        self.__last_name = None
        self.__first_name = None
        self.full_name = fname

    @property
    def full_name(self):
        return self.__full_name

    @full_name.setter
    def full_name(self, value):
        self.__full_name = value
        words = value.split()
        self.__first_name = words[len(words) - 1]
        self.__last_name = words[0]
        for i in range(1, len(words) - 1):
            self.__mid_name += words[i] + ' '

    @property
    def first_name(self):
        return self.__first_name

    def __str__(self):
        return f'{self.__last_name} {self.__mid_name}{self.__first_name}'


class BirthDate:
    def __init__(self, dob):
        self.__day = 0
        self.__month = 0
        self.__year = 0
        self.set_dob(dob)

    def set_dob(self, dob):
        data = [int(x) for x in dob.split('/')]
        self.__day = data[0]
        self.__month = data[1]
        self.__year = data[2]

    def __str__(self):
        return f'{self.__day}/{self.__month}/{self.__year}'


class Person:
    def __init__(self, fname, gender, dob):
        self.__full_name = FullName(fname)
        self.__gender = gender
        self.__birth_date = BirthDate(dob)

    def eat(self, food):
        print(f'{self.full_name.first_name} is eating {food}')

    @property
    def full_name(self):
        return self.__full_name

    def __str__(self):
        return f'[{self.__full_name}, {self.__gender}, {self.__birth_date}]'


huong = Person('Tran Thi Thu Huong', 'Female', '28/08/2005')
print(huong.full_name)
huong.eat('Fish')
print(huong.full_name.first_name)


class BankCard:
    def __init__(self, acc_num, balance, owner):
        self.acc_number = acc_num
        self.balance = balance
        self.owner = owner

    def withdraw(self, amount):
        """Phương thức thực hiện việc rút tiền và trả về số tiền đã rút"""
        if amount > self.balance:
            return -1
        else:
            self.balance -= amount
            return amount


class ATM:
    transaction_id = 100

    def __init__(self, atm_id, bank, address):
        self.atm_id = atm_id
        self.bank_owner = bank
        self.address = address
        self.sessions = dict()

    def withdraw_transaction(self, card):
        """Phương thức liên kết thực hiện giao dịch rút tiền trong thẻ."""
        amount = int(input("Enter amount you want to withdraw: "))
        result = card.withdraw(amount)
        self.sessions[ATM.transaction_id] = 'Sucessfully' if result > 0 else 'Failed'
        header = f'Transaction ref id \'{ATM.transaction_id}\'' \
                 f' was {self.sessions.get(ATM.transaction_id)}.'
        detail = f'-{result}$. Your current balance: {card.balance}$' if result > 0 \
            else f'-{0}$. Your current balance: {card.balance}$'
        self.push_notification(header, detail)
        ATM.transaction_id += 1

    def push_notification(self, header, detail):
        print(header)
        print(detail)


card = BankCard(acc_num='0021000842687', balance=15000, owner='TRAN THANH TUNG')
atm = ATM(1025374, 'VCB', '125, Center Point, Wakanda')
atm.withdraw_transaction(card)

# Kết quả:
# Enter amount you want to withdraw: 1250
# Transaction ref id '100' was Sucessfully.
# -1250$. Your current balance: 13750$

# Enter amount you want to withdraw: 16000
# Transaction ref id '100' was Failed.
# -0$. Your current balance: 15000$
