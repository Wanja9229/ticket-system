from models import Cstm, Acnt

def main():
    customer = {}
    while True:
        print("\n---은행 시스템---")
        print('1. 고객 등록')
        print('2. 계좌 개설')
        print('3. 입금')
        print('4. 출금')
        print('5. 잔액 조회')
        print('0. 종료')
        menu_num = int(input('메뉴 입력:').strip())
        if menu_num == 1:

            print('고객 등록')
            name = input('이름 입력 :').strip()
            birth = input('생일 입력(YYYYMMDD) :').strip()
            if len(birth) == 8 and birth.isdigit():
                customer[name] = Cstm(name, birth)
                print(customer[name])
            else:
                print('생년월일을 확인해주세요')

        elif menu_num == 2:

            print('계좌 개설')
            name = input('이름 입력 :').strip()
            if name in customer:
                balance = int(input('초기 입금액 :').strip())
                new_account = customer[name].add_account(balance)
                print(new_account)
            else:
                print('고객 등록을 먼저 진행해주세요')
            
        elif menu_num == 3:

            print('입금')
            name = input('이름 입력 :').strip()
            if name in customer:
                acc_no = input('계좌번호 입력 :').strip()
                account = customer[name].get_account(acc_no)
                if account:
                    balance = int(input('입금 금액 :').strip())
                    if account.deposit(balance):
                        print(account)
                else:
                    print('등록된 계좌번호가 아닙니다')
            else:
                print('등록된 고객이 아닙니다')
            
        elif menu_num == 4:

            print('출금')
            name = input('이름 입력 :').strip()
            if name in customer:
                acc_no = input('계좌번호 입력 :').strip()
                account = customer[name].get_account(acc_no)
                if account:
                    balance = int(input('출금 금액 :').strip())
                    if account.withdraw(account, balance):
                        print(account)
                else:
                    print('등록된 계좌번호가 아닙니다')
            else:
                print('등록된 고객이 아닙니다')

        elif menu_num == 5:
            print('잔액 조회')
            name = input('이름 입력 :').strip()
            if name in customer:
                for acut in customer[name].accounts:
                    print(acut)
                    
                print(f"계좌 총액 : {customer[name].view_balance()} 원")
            else:
                print('등록된 고객이 아닙니다')


        elif menu_num == 0:
            print('종료')
            return False
        
main()
