class BankCard:
    def __init__(self, acc_number, balance, owner):
        self.__owner = owner
        self.__acc_number = acc_number
        self.__balance = balance

    def withdraw(self, amount):
        if amount > self.__balance:
            return -1
        else:
            self.__balance -= amount
            return amount

    @property
    def balance(self):
        return self.__balance


class ATM:
    session_id = 100

    def __init__(self, atm_id, bank, address):
        self.__atm_id = atm_id
        self.__bank_owner = bank
        self.__address = address
        self.__sessions = dict()

    def withdraw_transaction(self, card):
        amount = int(input('Enter amount you want to withdraw: '))
        result = card.withdraw(amount)
        self.__sessions[ATM.session_id] = 'Successfully' if result > 0 else 'Failed'
        header = f'Transaction ref id\'{ATM.session_id}\'' \
                 f' was {self.__sessions[ATM.session_id]}.'
        detail = f'-{result}$. Your current balance: {card.balance}$' if result > 0 \
            else f'-0$. Your current balance: {card.balance}$'
        self.push_notification(header, detail)

    def push_notification(self, header, detail):
        print(header)
        print(detail)


card = BankCard(acc_number='0021000842687', balance=15000, owner='TRAN THANH TUNG')
atm = ATM(1025374, 'VCB', '125, Center Point, Wakanda')
atm.withdraw_transaction(card)
