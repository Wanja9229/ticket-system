from typing import List, Optional, Dict

class Acc:
    def __init__(self, no: str, bal: int = 0) -> None:
        self.no = no
        self.bal = bal
    
    def dep(self, amt: int) -> bool:
        if amt > 0:
            self.bal += amt
            return True
        return False
    
    def wdr(self, amt: int) -> bool:
        if amt > 0 and amt <= self.bal:
            self.bal -= amt
            return True
        return False
    
    def __str__(self) -> str:
        return f"계좌: {self.no}, 잔액: {self.bal}원"


class Cust:
    def __init__(self, name: str, birth: str) -> None:
        self.name = name
        self.birth = birth
        self.accs: List[Acc] = []
    
    def add_acc(self, bal: int = 0) -> Acc:
        cnt = len(self.accs) + 1
        no = f"{self.birth}-{cnt:02d}"
        acc = Acc(no, bal)
        self.accs.append(acc)
        return acc
    
    def get_acc(self, no: str) -> Optional[Acc]:
        for acc in self.accs:
            if acc.no == no:
                return acc
        return None
    
    def total_bal(self) -> int:
        return sum(acc.bal for acc in self.accs)
    
    def __str__(self) -> str:
        return f"{self.name} ({self.birth}), 계좌: {len(self.accs)}개"


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


def main() -> None:
    custs: Dict[str, Cust] = {}
    
    while True:
        show_menu()
        ch = input("메뉴를 선택하세요: ")
        
        # 고객 등록
        if ch == "1":
            print("\n[고객 등록]")
            name = input("이름을 입력하세요: ")
            
            if name in custs:
                print(f"{name}님은 이미 등록된 고객입니다.")
                continue
            
            birth = input("생년월일 (YYYYMMDD): ")
            if len(birth) != 8 or not birth.isdigit():
                print("생년월일은 8자리 숫자로 입력해주세요.")
                continue
            
            custs[name] = Cust(name, birth)
            print(f"{name}님이 등록되었습니다.")
        
        # 계좌 개설
        elif ch == "2":
            print("\n[계좌 개설]")
            name = input("고객 이름: ")
            if name not in custs:
                print(f"{name}님은 등록되지 않은 고객입니다.")
                continue
            
            try:
                init_bal = int(input("초기 입금액 (0원 이상): "))
                if init_bal < 0:
                    print("입금액은 0원 이상이어야 합니다.")
                    continue
            except ValueError:
                print("올바른 금액을 입력해주세요.")
                continue
            
            cust = custs[name]
            acc = cust.add_acc(init_bal)
            print("계좌가 개설되었습니다.")
            print(f"   {acc}")
        
        # 입금
        elif ch == "3":
            print("\n[입금]")
            name = input("고객 이름: ")
            if name not in custs:
                print(f"{name}님은 등록되지 않은 고객입니다.")
                continue
            
            cust = custs[name]
            if not cust.accs:
                print(f"{name}님은 개설된 계좌가 없습니다.")
                continue
            
            no = input("계좌번호: ")
            acc = cust.get_acc(no)
            if acc is None:
                print(f"{no} 계좌를 찾을 수 없습니다.")
                continue
            
            try:
                amt = int(input("입금액: "))
            except ValueError:
                print("올바른 금액을 입력해주세요.")
                continue
            
            if acc.dep(amt):
                print(f"{amt}원이 입금되었습니다.")
                print(f"   현재 잔액: {acc.bal}원")
            else:
                print("0원보다 큰 금액을 입력해주세요.")
        
        # 출금
        elif ch == "4":
            print("\n[출금]")
            name = input("고객 이름: ")
            if name not in custs:
                print(f"{name}님은 등록되지 않은 고객입니다.")
                continue
            
            cust = custs[name]
            if not cust.accs:
                print(f"{name}님은 개설된 계좌가 없습니다.")
                continue
            
            no = input("계좌번호: ")
            acc = cust.get_acc(no)
            if acc is None:
                print(f"{no} 계좌를 찾을 수 없습니다.")
                continue
            
            print(f"   현재 잔액: {acc.bal}원")
            try:
                amt = int(input("출금액: "))
            except ValueError:
                print("올바른 금액을 입력해주세요.")
                continue
            
            if acc.wdr(amt):
                print(f"{amt}원이 출금되었습니다.")
                print(f"   현재 잔액: {acc.bal}원")
            else:
                print(f"출금 실패: 잔액 부족")
                print(f"   현재 잔액: {acc.bal}원")
        
        # 잔액 조회
        elif ch == "5":
            print("\n[잔액 조회]")
            name = input("고객 이름: ")
            if name not in custs:
                print(f"{name}님은 등록되지 않은 고객입니다.")
                continue
            
            cust = custs[name]
            print(f"\n고객 정보: {cust}")
            
            if not cust.accs:
                print("   - 개설된 계좌가 없습니다.")
            else:
                print("\n계좌 목록:")
                for i, acc in enumerate(cust.accs, 1):
                    print(f"   {i}. {acc}")
                total = cust.total_bal()
                print(f"\n전체 잔액 합계: {total:,}원")
        
        # 종료
        elif ch == "0":
            print("\n프로그램을 종료합니다. 감사합니다!")
            break
        
        else:
            print("잘못된 메뉴입니다.")
        
        input("\n계속하려면 Enter를 누르세요...")


if __name__ == "__main__":
    main()
