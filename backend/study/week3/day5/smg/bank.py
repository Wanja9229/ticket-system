class Account:
    """계좌 클래스 - 개별 계좌의 정보와 기능을 관리"""
    
    def __init__(self, acc_no, balance=0):
        """계좌 객체를 초기화하는 생성자 메서드"""
        self.acc_no = acc_no        # 계좌번호를 인스턴스 변수에 저장
        self.balance = balance      # 초기 잔액을 인스턴스 변수에 저장 (기본값 0)
    
    def deposit(self, amount):
        """입금 기능을 수행하는 메서드"""
        if amount > 0:              # 입금액이 0보다 큰지 확인
            self.balance += amount  # 조건을 만족하면 잔액에 입금액 추가
            return True             # 성공을 의미하는 True 반환
        return False                # 실패를 의미하는 False 반환
    
    def withdraw(self, amount):
        """출금 기능을 수행하는 메서드"""
        # 출금액이 0보다 크고 AND 현재 잔액 이하인지 확인
        if amount > 0 and amount <= self.balance:
            self.balance -= amount  # 조건을 만족하면 잔액에서 출금액 차감
            return True             # 성공을 의미하는 True 반환
        return False                # 실패를 의미하는 False 반환
    
    def __str__(self):
        """계좌 정보를 문자열로 반환하는 특수 메서드 (print 시 호출됨)"""
        # f-string을 사용하여 계좌번호와 잔액을 보기 좋은 형태로 반환
        return f"계좌: {self.acc_no}, 잔액: {self.balance}원"


class Customer:
    """고객 클래스 - 고객 정보와 보유 계좌들을 관리"""
    
    def __init__(self, name, birth):
        """고객 객체를 초기화하는 생성자 메서드"""
        self.name = name            # 고객 이름을 인스턴스 변수에 저장
        self.birth = birth          # 생년월일을 인스턴스 변수에 저장
        self.accounts = []          # 보유 계좌들을 저장할 빈 리스트 초기화
    
    def add_account(self, balance=0):
        """새로운 계좌를 개설하는 메서드"""
        # 현재 보유 계좌 수 + 1로 순번 계산
        account_num = len(self.accounts) + 1
        
        # 계좌번호를 "생년월일-순번" 형식으로 생성 (:02d는 2자리 숫자로 포맷)
        acc_no = f"{self.birth}-{account_num:02d}"
        
        # 새로운 Account 객체를 생성하여 변수에 저장
        new_account = Account(acc_no, balance)
        
        # 생성된 계좌를 계좌 리스트에 추가
        self.accounts.append(new_account)
        
        # 생성된 계좌 객체를 반환
        return new_account
    
    def get_account(self, acc_no):
        """계좌번호로 특정 계좌를 찾는 메서드"""
        # 보유한 모든 계좌를 하나씩 반복하여 확인
        for account in self.accounts:
            # 현재 계좌의 계좌번호가 찾는 계좌번호와 같은지 확인
            if account.acc_no == acc_no:
                return account      # 찾으면 해당 계좌 객체 반환
        return None                 # 찾지 못하면 None 반환
    
    def total_balance(self):
        """모든 계좌의 잔액 합계를 계산하는 메서드"""
        # generator expression을 사용해 모든 계좌의 잔액을 합산
        return sum(account.balance for account in self.accounts)
    
    def __str__(self):
        """고객 정보를 문자열로 반환하는 특수 메서드"""
        # f-string을 사용하여 고객 정보와 보유 계좌 수를 반환
        return f"{self.name} ({self.birth}), 계좌: {len(self.accounts)}개"


def main():
    """메인 프로그램 - 은행 시스템의 메뉴와 기능을 제공"""
    # 고객들을 저장할 딕셔너리 (키: 고객이름, 값: Customer 객체)
    customers = {}
    
    # 무한 루프로 메뉴 시스템 구현
    while True:
        # 메뉴 화면 출력
        print("\n=== 은행 시스템 ===")
        print("1. 고객 등록")
        print("2. 계좌 개설")
        print("3. 입금")
        print("4. 출금")
        print("5. 잔액 조회")
        print("0. 종료")
        
        # 사용자로부터 메뉴 선택 입력받기
        choice = input("메뉴를 선택하세요: ")
        
        # 메뉴 1: 고객 등록
        if choice == "1":
            # 고객 정보 입력받기
            name = input("고객 이름을 입력하세요: ")
            birth = input("생년월일을 입력하세요 (YYYYMMDD): ")
            
            # 이미 등록된 고객인지 확인 (딕셔너리의 in 연산자 사용)
            if name in customers:
                print("이미 등록된 고객입니다.")
            else:
                # 새로운 Customer 객체 생성하여 딕셔너리에 저장
                customers[name] = Customer(name, birth)
                print(f"{name} 고객이 성공적으로 등록되었습니다.")
        
        # 메뉴 2: 계좌 개설
        elif choice == "2":
            # 고객 이름 입력받기
            name = input("고객 이름을 입력하세요: ")
            
            # 등록된 고객인지 확인
            if name not in customers:
                print("등록되지 않은 고객입니다.")
            else:
                try:
                    # 초기 입금액 입력받기 (문자열을 정수로 변환)
                    initial_balance = int(input("초기 입금액을 입력하세요: "))
                    
                    # 음수 체크
                    if initial_balance < 0:
                        print("초기 입금액은 0 이상이어야 합니다.")
                        continue  # 다시 메뉴로 돌아감
                    
                    # 고객 객체의 add_account 메서드 호출하여 계좌 생성
                    account = customers[name].add_account(initial_balance)
                    print(f"계좌가 개설되었습니다: {account}")
                    
                # 숫자가 아닌 입력에 대한 예외 처리
                except ValueError:
                    print("올바른 금액을 입력하세요.")
        
        # 메뉴 3: 입금
        elif choice == "3":
            # 고객 이름 입력받기
            name = input("고객 이름을 입력하세요: ")
            
            # 등록된 고객인지 확인
            if name not in customers:
                print("등록되지 않은 고객입니다.")
            else:
                # 계좌번호 입력받기
                acc_no = input("계좌번호를 입력하세요: ")
                
                # 해당 계좌 찾기
                account = customers[name].get_account(acc_no)
                
                # 계좌가 존재하는지 확인
                if account is None:
                    print("해당 계좌를 찾을 수 없습니다.")
                else:
                    try:
                        # 입금액 입력받기
                        amount = int(input("입금액을 입력하세요: "))
                        
                        # 계좌 객체의 deposit 메서드 호출
                        if account.deposit(amount):
                            print(f"입금 완료! 현재 잔액: {account.balance}원")
                        else:
                            print("입금 실패! 0보다 큰 금액을 입력하세요.")
                    
                    # 숫자가 아닌 입력에 대한 예외 처리
                    except ValueError:
                        print("올바른 금액을 입력하세요.")
        
        # 메뉴 4: 출금
        elif choice == "4":
            # 고객 이름 입력받기
            name = input("고객 이름을 입력하세요: ")
            
            # 등록된 고객인지 확인
            if name not in customers:
                print("등록되지 않은 고객입니다.")
            else:
                # 계좌번호 입력받기
                acc_no = input("계좌번호를 입력하세요: ")
                
                # 해당 계좌 찾기
                account = customers[name].get_account(acc_no)
                
                # 계좌가 존재하는지 확인
                if account is None:
                    print("해당 계좌를 찾을 수 없습니다.")
                else:
                    try:
                        # 출금액 입력받기
                        amount = int(input("출금액을 입력하세요: "))
                        
                        # 계좌 객체의 withdraw 메서드 호출
                        if account.withdraw(amount):
                            print(f"출금 완료! 현재 잔액: {account.balance}원")
                        else:
                            print("출금 실패! 잔액이 부족하거나 올바르지 않은 금액입니다.")
                    
                    # 숫자가 아닌 입력에 대한 예외 처리
                    except ValueError:
                        print("올바른 금액을 입력하세요.")
        
        # 메뉴 5: 잔액 조회
        elif choice == "5":
            # 고객 이름 입력받기
            name = input("고객 이름을 입력하세요: ")
            
            # 등록된 고객인지 확인
            if name not in customers:
                print("등록되지 않은 고객입니다.")
            else:
                # 해당 고객 객체 가져오기
                customer = customers[name]
                
                # 고객 기본 정보 출력 (__str__ 메서드 자동 호출)
                print(f"\n고객 정보: {customer}")
                
                # 보유 계좌가 있는지 확인
                if len(customer.accounts) == 0:
                    print("보유 계좌가 없습니다.")
                else:
                    print("보유 계좌 목록:")
                    
                    # 모든 계좌 정보를 반복하여 출력
                    for account in customer.accounts:
                        print(f"  {account}")  # 각 계좌의 __str__ 메서드 호출
                    
                    # 전체 잔액 합계 출력
                    print(f"전체 잔액 합계: {customer.total_balance()}원")
        
        # 메뉴 0: 종료
        elif choice == "0":
            print("은행 시스템을 종료합니다.")
            break  # while 루프 종료
        
        # 잘못된 메뉴 선택 시
        else:
            print("올바른 메뉴 번호를 입력하세요.")


# 파이썬에서 스크립트가 직접 실행될 때만 main() 함수 호출
# 다른 파일에서 import 할 때는 실행되지 않음
if __name__ == "__main__":
    main()  # 메인 함수 호출하여 프로그램 시작