class Cstm:
    def __init__(self, name, birth):
        self.name = name
        self.birth = birth
        self.accounts = []

    def __str__(self):
        return f"{self.name}({self.birth}) 님의 보유 계좌 : {len(self.accounts)} 개"
    
    def add_account(self, balance=0):
        acc_no = f"{self.birth}-{len(self.birth)+1:02d}"
        new_acc = Acut(acc_no, balance)
        self.accounts.append(new_acc)
        return new_acc
    

class Acut:
    def __init__(self, acc_no, balance=0):
        self.acc_no = acc_no
        self.balance = balance
    
    def __str__(self):
        return f"{self.acc_no} 계좌의 잔액 : {self.balance} 원"
    
    def deposit(self, balance)->bool:
        if balance > 0:
            self.balance += balance
            return True
        else:
            return False
