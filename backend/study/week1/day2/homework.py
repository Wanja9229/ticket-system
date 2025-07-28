"""
Week 1 - Day 2 과제

클래스, 모듈, 예외 처리 연습
"""

# 과제 1: 은행 계좌 클래스 만들기
class BankAccount:
    """
    요구사항:
    1. 계좌번호(account_number)와 잔액(balance) 속성
    2. 입금(deposit) 메서드 - 음수 입금 시 ValueError
    3. 출금(withdraw) 메서드 - 잔액 부족 시 InsufficientFundsError (직접 만들기)
    4. 이체(transfer) 메서드 - 다른 계좌로 송금
    5. __str__ 메서드로 계좌 정보 출력
    """
    
    def __init__(self, account_number, initial_balance=0):
        # TODO: 구현하세요
        pass
    
    def deposit(self, amount):
        # TODO: 구현하세요
        pass
    
    def withdraw(self, amount):
        # TODO: 구현하세요
        pass
    
    def transfer(self, other_account, amount):
        # TODO: 구현하세요
        pass
    
    def __str__(self):
        # TODO: 구현하세요
        pass


# 과제 2: 사용자 정의 예외 만들기
class InsufficientFundsError(Exception):
    """잔액 부족 예외"""
    # TODO: 구현하세요
    pass


# 과제 3: 상속을 활용한 특별 계좌
class SavingsAccount(BankAccount):
    """
    저축 계좌 - BankAccount 상속
    요구사항:
    1. 이자율(interest_rate) 속성 추가
    2. 이자 계산(calculate_interest) 메서드
    3. 최소 잔액(minimum_balance) 체크 - 출금 시 최소 잔액 유지
    """
    
    def __init__(self, account_number, initial_balance=0, interest_rate=0.02, minimum_balance=10000):
        # TODO: 구현하세요
        pass
    
    def calculate_interest(self):
        # TODO: 구현하세요
        pass
    
    def withdraw(self, amount):
        # TODO: 부모 클래스 메서드 오버라이딩
        pass


# 과제 4: 계산기 모듈 만들기
# calculator_module.py 라는 별도 파일을 만들고 아래 기능 구현
"""
calculator_module.py 파일에 구현할 내용:

1. 기본 연산 함수들 (add, subtract, multiply, divide)
2. Calculator 클래스
   - 연산 기록 저장 (history)
   - 마지막 결과 저장 (last_result)
   - 연산 수행 시 기록에 추가
3. 0으로 나누기 시 적절한 예외 처리
"""


# 과제 5: 파일 처리 클래스
class FileManager:
    """
    파일 관리 클래스
    요구사항:
    1. 파일 읽기 - 파일이 없으면 FileNotFoundError 처리
    2. 파일 쓰기 - 쓰기 실패 시 예외 처리
    3. JSON 파일 읽기/쓰기
    4. with 문과 함께 사용 가능하도록 __enter__, __exit__ 구현
    """
    
    def __init__(self, filename):
        self.filename = filename
        self.file = None
    
    def read_text(self):
        # TODO: 구현하세요
        pass
    
    def write_text(self, content):
        # TODO: 구현하세요
        pass
    
    def read_json(self):
        # TODO: 구현하세요
        pass
    
    def write_json(self, data):
        # TODO: 구현하세요
        pass
    
    def __enter__(self):
        # TODO: 구현하세요
        pass
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        # TODO: 구현하세요
        pass


# 테스트 코드 (수정하지 마세요)
if __name__ == "__main__":
    print("=== 과제 1, 2 테스트: 은행 계좌 ===")
    try:
        # 계좌 생성
        account1 = BankAccount("123-456", 50000)
        account2 = BankAccount("789-012", 30000)
        
        print(account1)
        print(account2)
        
        # 입금
        account1.deposit(10000)
        print(f"입금 후: {account1}")
        
        # 출금
        account1.withdraw(20000)
        print(f"출금 후: {account1}")
        
        # 이체
        account1.transfer(account2, 15000)
        print(f"이체 후 계좌1: {account1}")
        print(f"이체 후 계좌2: {account2}")
        
        # 잔액 부족 테스트
        account1.withdraw(50000)
        
    except InsufficientFundsError as e:
        print(f"잔액 부족: {e}")
    except ValueError as e:
        print(f"값 오류: {e}")
    
    print("\n=== 과제 3 테스트: 저축 계좌 ===")
    savings = SavingsAccount("555-666", 100000, 0.03, 20000)
    print(savings)
    
    # 이자 계산
    interest = savings.calculate_interest()
    print(f"이자: {interest:,.0f}원")
    
    # 최소 잔액 테스트
    try:
        savings.withdraw(85000)  # 100000 - 85000 = 15000 (최소 잔액 미달)
    except Exception as e:
        print(f"출금 실패: {e}")
    
    print("\n=== 과제 5 테스트: 파일 관리 ===")
    # 텍스트 파일 테스트
    with FileManager("test.txt") as fm:
        fm.write_text("Hello, Python!")
    
    fm = FileManager("test.txt")
    content = fm.read_text()
    print(f"파일 내용: {content}")
    
    # JSON 파일 테스트
    data = {"name": "김철수", "age": 25, "scores": [90, 85, 88]}
    fm_json = FileManager("test.json")
    fm_json.write_json(data)
    
    loaded_data = fm_json.read_json()
    print(f"JSON 데이터: {loaded_data}")


# 보너스 과제: 데코레이터 만들기
def timer(func):
    """
    함수 실행 시간을 측정하는 데코레이터
    
    사용 예시:
    @timer
    def slow_function():
        time.sleep(1)
    """
    # TODO: 구현하세요
    pass


def retry(max_attempts=3):
    """
    실패 시 재시도하는 데코레이터
    
    사용 예시:
    @retry(max_attempts=3)
    def unstable_function():
        # 가끔 실패하는 함수
        pass
    """
    # TODO: 구현하세요
    pass
