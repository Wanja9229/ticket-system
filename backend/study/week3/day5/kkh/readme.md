# 클래스 및 메서드 구조

이 문서는 `Acc`와 `Cust` 클래스의 메서드 구조를 정리한 문서입니다.

### 
```python

from typing import List, Optional, Dict


#은행 계좌를 나타내는 클래스
class Acc

  # Acc 객체 초기화
  # 계좌번호(no)와 초기 잔액(bal)을 설정
  def __init__(self, name: str, birth: str) -> None:

  # 입금 메서드
  # amt가 0보다 크면 잔액에 추가하고 True 반환, 아니면 False
  def dep(self, amt: int) -> bool

  # 출금 메서드
  # amt가 0보다 크고 잔액 이하이면 출금 후 True 반환, 아니면 False
  def wdr(self, amt: int) -> bool

  # 계좌 정보를 문자열로 반환
  # 예: "계좌: 계좌번호, 잔액: 금액원"
  def __str__(self) -> str:


  #고객 정보를 나타내는 클래스
  #여러 개의 Acc(계좌)를 가질 수 있음

class Cust:
  # Cust 객체 초기화
  # 고객 이름(name), 생년월일(birth), 계좌 목록(accs) 초기화
  def __init__(self, name: str, birth: str) -> None:

  # 새로운 계좌를 생성하여 accs 리스트에 추가
  # bal은 초기 잔액
  def add_acc(self, bal: int = 0) -> Acc:
  
  # 계좌번호(no)를 이용해 accs에서 계좌를 검색하여 반환
  # 없으면 None 반환
  def get_acc(self, no: str) -> Optional[Acc]:
  
  # 고객이 가진 모든 계좌의 총 잔액 합계 반환
  def total_bal(self) -> int:

  # 고객 정보를 문자열로 반환
  # 예: "이름 (생년월일), 계좌: n개"
  def __str__(self) -> str:
  
# 사용자 메뉴 화면 출력
def show_menu() -> None:
  print("\n" + "=" * 40)
  print("         간단한 은행 시스템")
  print("=" * 40)
  print("1. 고객 등록")
  print("2. 계좌 개설")
  print("3. 입금")
  print("4. 출금")
  print("5. 잔액 조회")
  print("0. 종료")
  print("=" * 40)
# 프로그램 실행 메인 함수
# 사용자 입력을 받아 기능 실행
def main() -> None:
  if c == "1":
  elif c == "2":
```