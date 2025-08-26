
class Acnt:
    def __init__(self, acc_no, balance=0):
        self.acc_no = acc_no
        self.balance = balance

    def __str__(self):
        return f'{self.acc_no} 계좌의 잔액 : {self.balance}'
    
    def deposit(self, balance=0):
        if balance > 0:
            self.balance += balance
            return True
        else:
            print('입금액은 0보다 커야합니다')
            return False

    def withdraw(self, balance=0):
        if balance > 0 and self.balance >= balance:
            self.balance -= balance
            return True
        else:
            print('잔액을 확인해주세요')
            return False

class Cstm:
    def __init__(self, name, birth):
        self.name = name
        self.birth = birth
        self.accounts = []

    def __str__(self):
        return f"{self.name}({self.birth})님의 계좌정보 : {len(self.accounts)} 개"

    def add_account(self, balance=0):
        acc_no = f"{self.birth}-{len(self.accounts)+1:02d}"
        new_account = Acnt(acc_no, balance)
        self.accounts.append(new_account)
        return new_account
    
    def get_account(self, acc_no):
        for x in self.accounts:
            if x.acc_no == acc_no:
                return x
        return None
    
    def view_balance(self):
        total = 0
        for acut in self.accounts:
            total += acut.balance
        return total