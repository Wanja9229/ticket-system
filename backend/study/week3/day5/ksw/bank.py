def bank_main():
    customer = {}

    while True:
        print('\n=== 메뉴 ===')
        print('1. 고객 등록')
        print('2. 계좌 개설')
        print('3. 입금')
        print('4. 출금')
        print('5. 잔액 조회')
        print('0. 종료')
        menu_num = int(input('실행할 메뉴를 입력해주세요 :'))
        if menu_num == 1:
            
            name = input('이름을 입력하세요 :').strip()
            birth = input('생년월일을 입력하세요(YYYYMMDD) :').strip()
            if len(birth) == 8 and birth.isdigit():
                customer[name] = Customer(name, birth)
                print(f'{name}님의 등록이 완료되었습니다')
                print(customer[name])
            else:
                print('생년월일 형식을 확인하세요')

        elif menu_num == 2:

            name = input('고객 이름 :')
            if name in customer:
                balance = int(input('초기 입금액 :').strip())
                account = customer[name].add_account(balance)
                print('새 계좌가 생성되었습니다')
                print(account)

        elif menu_num == 3:
            
            name = input('고객 이름 :')
            if name in customer:
                acc_no = input('계좌번호 :')
                account = customer[name].get_account(acc_no)
                if account:
                    amount = int(input('입금액 :').strip())
                    if account.deposit(amount):
                        print('입금 완료')
                        print(account)
                    else:
                        print('입금액은 0보다 커야 합니다')
                else:
                    print('계좌를 찾을 수 없습니다')
            else:
                print('등록되지 않은 고객입니다')

        elif menu_num == 4:
            
            name = input('고객 이름 :')
            if name in customer:
                acc_no = input('계좌번호 :')
                account = customer[name].get_account(acc_no)
                if account:
                    amount = int(input('출금액 :').strip())
                    if account.withdraw(amount):
                        print('출금 완료')
                        print(f'{account.acc_no} 계좌의 현재 잔액 : {account.balance}')
                    else:
                        print('잔액이 부족합니다')
                else:
                    print('등록되지 않은 계좌입니다')
            else:
                print('등록되지 않은 고객입니다')

        elif menu_num == 5:

            name = input('고객 이름 :').strip()
            if name in customer:
                print(customer[name])
                
                for account in customer[name].accounts:
                    print(account)
                
                total = customer[name].total_balance()
                print(f'총 잔액 : {total} 원')

        elif menu_num == 0:
            print('프로그램을 종료합니다')
            break
        else:
            print('올바른 숫자를 입력해주세요')
            continue

class Account:
    def __init__(self, acc_no, balance=0):
        self.acc_no = acc_no
        self.balance = balance

    def __str__(self):
        return f"{self.acc_no} 계좌의 잔액 : {self.balance}"
    
    def deposit(self, amount:int) -> bool:
        if amount > 0:
            self.balance += amount
            return True
        else:
            return False
        
    def withdraw(self, amount:int) -> bool:
        if amount > 0 and self.balance >= amount:
            self.balance -= amount
            return True
        else:
            return False

    
class Customer:
    def __init__(self, name, birth):
        self.name = name
        self.birth = birth
        self.accounts = []

    def __str__(self):
        return f"{self.name}({self.birth}) 님의 보유계좌 : {len(self.accounts)} 개"

    def add_account(self, balance=0):
        acc_no = f"{self.birth}-{len(self.accounts)+1:02d}"
        new_account = Account(acc_no, balance)

        self.accounts.append(new_account)
        return new_account
    
    def get_account(self, acc_no):
        for account in self.accounts:
            if account.acc_no == acc_no:
                return account
        return None
    
    def total_balance(self)->int:
        total = 0
        for account in self.accounts:
            total += account.balance
        return total

bank_main()