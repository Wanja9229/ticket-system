import json, os
from datetime import datetime
from typing import List, Dict

# mem: members
# name: name
# birth_date: birth_date
# register_date: register_date
# password: password

DF_FN = "members.json"  # default filename

# 현재 날짜와 시간을 문자열 형태로 반환하는 함수
# 회원 등록일시를 기록하는데 사용되며, "YYYY-MM-DD HH:MM:SS" 형식으로 반환
def now() -> str:
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# 사용자에게 y/n 질문을 던지고 불린값으로 결과를 반환하는 함수
# 삭제 확인, 종료 확인 등 중요한 작업 전 사용자 의사를 확인할 때 사용
def yn(msg: str) -> bool:
    return input(f"{msg} (y/n): ").strip().lower() == 'y'

# 메뉴를 화면에 출력하고 사용자의 선택을 입력받아 반환하는 함수
# 1-7번까지의 메뉴 옵션을 제공하고 사용자가 입력한 번호를 문자열로 반환
def menu() -> str:
    print("\n===== 메뉴 =====")
    print("1. 회원가입")
    print("2. 파일 저장")
    print("3. 회원 정보 조회")
    print("4. 전체 회원 목록 보기")
    print("5. 회원 정보 수정")
    print("6. 회원 삭제")
    print("7. 프로그램 종료")
    return input("선택 (1-7): ").strip()

# 회원 리스트를 JSON 파일로 저장하는 함수
# 메모리상의 회원 데이터를 DF_FN 파일에 UTF-8 인코딩과 들여쓰기를 적용하여 저장
# 저장 성공/실패 메시지를 출력하고 성공 여부를 불린값으로 반환
def save(mem: List[Dict[str, str]]) -> bool:
    try:
        with open(DF_FN, 'w', encoding='utf-8') as f:
            json.dump(mem, f, ensure_ascii=False, indent=2)
        print(f"{DF_FN} 파일에 저장되었습니다.")
        return True
    except:
        print("파일 저장에 실패했습니다.")
        return False

# JSON 파일에서 회원 리스트를 로드하는 함수
# DF_FN 파일이 존재하지 않거나 읽기 실패 시 빈 리스트를 반환
def load() -> List[Dict[str, str]]:
    if not os.path.exists(DF_FN):
        return []
    try:
        with open(DF_FN, 'r', encoding='utf-8') as f:
            return json.load(f)
    except:
        return []

# 파일 존재 여부를 확인하는 함수
# DF_FN 파일의 존재 여부를 불린값으로 반환하는 os.path.exists() 래퍼 함수
def fchk() -> bool:
    return os.path.exists(DF_FN)

# 새로운 회원을 등록하는 함수
# 이름, 생년월일, 패스워드를 입력받아 현재시간과 함께 메모리 리스트에 추가
# 빈 입력 시 회원가입을 취소하며 완료 후 저장 안내 메시지 출력
def reg(mem: List[Dict[str, str]]) -> None:
    print("\n===== 회원가입 =====")
    name = input("이름을 입력하세요: ").strip()
    if not name:
        print("회원가입을 취소했습니다.")
        return
    
    birth_date = input("생년월일을 입력하세요 (YYYY-MM-DD): ").strip()
    if not birth_date:
        print("회원가입을 취소했습니다.")
        return
    
    password = input("패스워드를 입력하세요: ").strip()
    if not password:
        print("회원가입을 취소했습니다.")
        return
    
    mem.append({"name": name, "birth_date": birth_date, "register_date": now(), "password": password})
    print(f"\n{name}님의 회원가입이 완료되었습니다!")
    print("파일로 저장하려면 '2. 파일 저장' 메뉴를 선택하세요.")

# 메모리상의 회원 데이터를 파일로 저장하는 함수
# save() 함수를 호출하여 실제 저장 작업을 수행하며 빈 리스트 체크 포함
def sv(mem: List[Dict[str, str]]) -> None:
    if not mem:
        print("저장할 회원 정보가 없습니다.")
        return
    save(mem)

# 파일에서 전체 회원 목록을 조회하여 출력하는 함수
# 번호, 이름, 생년월일, 등록일시를 포함한 목록과 총 회원수를 출력
def lst() -> None:
    mem = load()
    if not mem:
        print("등록된 회원이 없습니다.")
        return
    print("\n===== 전체 회원 목록 =====")
    for i,m in enumerate(mem,1):
        print(f"{i}. {m['name']} | {m['birth_date']} | {m['register_date']}")
    print(f"\n총 {len(mem)}명의 회원이 등록되어 있습니다.")

# 특정 회원의 정보를 수정하는 함수
# 파일에서 이름으로 회원을 찾아 생년월일 또는 패스워드를 수정하고 다시 파일에 저장
def upd(name: str) -> None:
    mem = load()
    if not mem:
        print("등록된 회원이 없습니다.")
        return
    idx = -1
    for i,m in enumerate(mem):
        if m['name']==name:
            idx=i
            break
    if idx==-1:
        print(f"'{name}' 회원을 찾을 수 없습니다.")
        return
    print("\n현재 회원 정보:")
    print(mem[idx])
    print("\n수정할 항목을 선택하세요:")
    print("1. 생년월일")
    print("2. 패스워드")
    print("3. 취소")
    c=input("선택 (1-3): ").strip()
    if c=='1':
        new_birth_date=input("새로운 생년월일 (YYYY-MM-DD): ").strip()
        if not new_birth_date:
            print("수정을 취소했습니다.")
            return
        mem[idx]['birth_date']=new_birth_date
        print("생년월일이 수정되었습니다.")
    elif c=='2':
        new_password=input("새로운 패스워드: ").strip()
        if not new_password:
            print("수정을 취소했습니다.")
            return
        mem[idx]['password']=new_password
        print("패스워드가 수정되었습니다.")
    elif c=='3':
        print("수정을 취소했습니다.")
        return
    else:
        print("잘못된 선택입니다.")
        return
    save(mem)

# 특정 회원의 정보를 조회하여 출력하는 함수
# 파일에서 이름으로 회원을 검색하여 상세 정보를 딕셔너리 형태로 출력
def dsp(name: str) -> None:
    mem = load()
    for m in mem:
        if m['name'] == name:
            print("\n회원 정보:")
            print({"이름":m['name'],"생년월일":m['birth_date'],"등록일시":m['register_date']})
            return
    print(f"'{name}' 회원을 찾을 수 없습니다.")

# 회원을 삭제하는 함수
# 전체 회원 목록을 먼저 보여주고 삭제할 회원을 선택받아 확인 후 삭제하고 파일에 저장
def del_mem() -> None:
    mem = load()
    if not mem:
        print("등록된 회원이 없습니다.")
        return
    
    # 먼저 회원 목록 보여주기
    print("\n===== 등록된 회원 목록 =====")
    for i,m in enumerate(mem,1):
        print(f"{i}. {m['name']} | {m['birth_date']} | {m['register_date']}")
    print(f"\n총 {len(mem)}명의 회원이 등록되어 있습니다.")
    
    name = input("\n삭제할 회원 이름: ").strip()
    if not name:
        print("삭제를 취소했습니다.")
        return
    
    # 회원 찾기
    for i, m in enumerate(mem):
        if m['name'] == name:
            print(f"\n삭제할 회원 정보:")
            print(f"이름: {m['name']}")
            print(f"생년월일: {m['birth_date']}")
            print(f"등록일시: {m['register_date']}")
            
            if yn(f"정말로 '{name}' 회원을 삭제하시겠습니까?"):
                mem.pop(i)
                save(mem)
                print(f"'{name}' 회원이 삭제되었습니다.")
            else:
                print("회원 삭제를 취소했습니다.")
            return
    
    print(f"'{name}' 회원을 찾을 수 없습니다.")

# 프로그램의 메인 실행 함수
# 메뉴를 반복 출력하고 사용자 선택에 따라 각 기능을 실행하며 저장되지 않은 데이터 관리
def main() -> None:
    print("회원 관리 시스템에 오신 것을 환영합니다!")
    # 기존 파일이 있으면 미리 로드
    mem = load() if fchk() else []
    org_cnt = len(mem)  # 기존 회원 수 기록
    
    while True:
        c = menu()
        if c=='1':
            reg(mem)
        elif c=='2':
            sv(mem)
            org_cnt = len(mem)  # 저장 후 기존 회원 수 업데이트
        elif c=='3':
            if not fchk():
                print(f"{DF_FN} 파일을 찾을 수 없습니다.")
                continue
            nm=input("조회할 회원 이름: ").strip()
            if nm:
                dsp(nm)
            else:
                print("조회를 취소했습니다.")
        elif c=='4':
            if fchk():
                lst()
            else:
                print(f"{DF_FN} 파일을 찾을 수 없습니다.")
        elif c=='5':
            if not fchk():
                print(f"{DF_FN} 파일을 찾을 수 없습니다.")
                continue
            nm=input("수정할 회원 이름: ").strip()
            if nm:
                upd(nm)
            else:
                print("수정을 취소했습니다.")
        elif c=='6':
            if not fchk():
                print(f"{DF_FN} 파일을 찾을 수 없습니다.")
                continue
            del_mem()
        elif c=='7':
            unsaved_cnt = len(mem) - org_cnt
            if unsaved_cnt > 0:
                print(f"\n주의: 메모리에 {unsaved_cnt}명의 저장되지 않은 회원 정보가 있습니다!")
                if not yn("정말로 종료하시겠습니까?"):
                    continue
            print("\n프로그램을 종료합니다.")
            break
        else:
            print("잘못된 메뉴 번호입니다. 1-7 사이의 숫자를 입력하세요.")
        input("\n계속하려면 Enter 키를 누르세요...")

# 프로그램 실행
main()