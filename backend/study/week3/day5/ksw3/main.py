from models import Cstm, Acut

def main():
    customers = {}

    while True:
        print('--은행 시스템--')
        print('1. 고객 등록')
        print('2. 계좌 개설')
        print('3. 입금')
        print('4. 출금')
        print('5. 잔액 조회')
        print('0. 종료')

        menu_num = int(input('메뉴 입력 :').strip())
        if menu_num == 1:
            
            print('고객 등록')
            name = input('이름 입력 :').strip()
            birth = input('생일 입력(YYYYMMDD) :').strip()
            if len(birth) == 8 and birth.isdigit():
                customers[name] = Cstm(name, birth)
                print(customers[name])
            else:
                print('날짜 형식을 확인해주세요')

        elif menu_num == 2:

            print('계좌 개설')
            name = input('이름 입력 :').strip()
            if name in customers:
                bal = int(input('입금액 : '))
                account = customers[name].add_account(bal)
                print(account)
            else:
                print('고객으로 등록해주세요')

        elif menu_num == 3:
            print('입금')
        elif menu_num == 4:
            print('출금')
        elif menu_num == 5:
            print('잔액 조회')
        elif menu_num == 0:
            print('종료')
            break

main()
