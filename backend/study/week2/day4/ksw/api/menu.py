import json, os, re
from datetime import datetime
from typing import List, Dict, Optional

# fn: filename
# mem: members
# nm: name
# bd: birth_date
# rd: register_date
# pw: password
# mn: menu

DF_FN = "members.json"  # default filename
MIN_PW_LEN = 4

# utils

# get current time now
def now() -> str:
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# yes or no input
def yn(msg: str) -> bool:
    return input(f"{msg} (y/n): ").strip().lower() == 'y'

# press enter to continue
def enter() -> None:
    input("\n계속하려면 Enter 키를 누르세요...")

# display menu
def menu() -> None:
    print("\n===== 메뉴 =====")
    print("1. 회원가입")
    print("2. 파일 저장")
    print("3. 회원 정보 조회")
    print("4. 전체 회원 목록 보기")
    print("5. 회원 정보 수정")
    print("6. 회원 삭제")
    print("7. 프로그램 종료")

# menu choice
def mch() -> str:
    return input("선택 (1-7): ").strip()

# validators

# validate name
def vnm(nm: str, mem: List[Dict[str, str]]) -> bool:
    if not nm:
        print("이름은 비워둘 수 없습니다.")
        return False
    for m in mem:
        if m['nm'] == nm:
            print("이미 존재하는 이름입니다.")
            return False
    return True

# validate birth date
def vbd(bd: str) -> bool:
    if not re.match(r"^\d{4}-\d{2}-\d{2}$", bd):
        print("생년월일 형식이 올바르지 않습니다. (YYYY-MM-DD)")
        return False
    return True

# validate password
def vpw(pw: str) -> bool:
    if len(pw) < MIN_PW_LEN:
        print(f"패스워드는 최소 {MIN_PW_LEN}자 이상이어야 합니다.")
        return False
    return True

# file handler

# save members to file
def save(mem: List[Dict[str, str]], fn: str) -> bool:
    try:
        with open(fn, 'w', encoding='utf-8') as f:
            json.dump(mem, f, ensure_ascii=False, indent=2)
        print(f"{fn} 파일에 저장되었습니다.")
        return True
    except:
        print("파일 저장에 실패했습니다.")
        return False

# load members from file
def load(fn: str) -> List[Dict[str, str]]:
    if not os.path.exists(fn):
        return []
    try:
        with open(fn, 'r', encoding='utf-8') as f:
            return json.load(f)
    except:
        return []

# file check if exists
def fchk(fn: str) -> bool:
    return os.path.exists(fn)

# file delete
def fdel(fn: str) -> None:
    try:
        os.remove(fn)
        print(f"{fn} 파일이 삭제되었습니다.")
    except:
        print("파일 삭제에 실패했습니다.")

# member management

# register new member
def reg(mem: List[Dict[str, str]]) -> None:
    print("\n===== 회원가입 =====")
    while True:
        nm = input("이름을 입력하세요 (취소: 빈 입력): ").strip()
        if not nm:
            print("회원가입을 취소했습니다.")
            return
        if vnm(nm, mem):
            break
    while True:
        bd = input("생년월일을 입력하세요 (YYYY-MM-DD): ").strip()
        if not bd:
            print("회원가입을 취소했습니다.")
            return
        if vbd(bd):
            break
    while True:
        pw = input(f"패스워드를 입력하세요 (최소 {MIN_PW_LEN}자): ").strip()
        if not pw:
            print("회원가입을 취소했습니다.")
            return
        if vpw(pw):
            break
    mem.append({"nm": nm, "bd": bd, "rd": now(), "pw": pw})
    print(f"\n{nm}님의 회원가입이 완료되었습니다!")
    print("파일로 저장하려면 '2. 파일 저장' 메뉴를 선택하세요.")

# save members to file
def sv(mem: List[Dict[str, str]], fn: str) -> None:
    if not mem:
        print("저장할 회원 정보가 없습니다.")
        return
    save(mem, fn)

# search member by name
def sch(fn: str, nm: str) -> Optional[Dict[str, str]]:
    mem = load(fn)
    for m in mem:
        if m['nm'] == nm:
            return m
    return None

# list all members
def lst(fn: str) -> None:
    mem = load(fn)
    if not mem:
        print("등록된 회원이 없습니다.")
        return
    print("\n===== 전체 회원 목록 =====")
    print(f"{'번호':<4} | {'이름':<10} | {'생년월일':<12} | {'등록일시'}")
    print("-"*50)
    for i,m in enumerate(mem,1):
        print(f"{i:<4} | {m['nm']:<10} | {m['bd']:<12} | {m['rd']}")
    print("-"*50)
    print(f"총 {len(mem)}명의 회원이 등록되어 있습니다.")

# update member information
def upd(fn: str, nm: str) -> None:
    mem = load(fn)
    if not mem:
        print("등록된 회원이 없습니다.")
        return
    idx = -1
    for i,m in enumerate(mem):
        if m['nm']==nm:
            idx=i;break
    if idx==-1:
        print(f"'{nm}' 회원을 찾을 수 없습니다.")
        return
    print("\n현재 회원 정보:")
    print(mem[idx])
    print("\n수정할 항목을 선택하세요:")
    print("1. 생년월일")
    print("2. 패스워드")
    print("3. 취소")
    c=input("선택 (1-3): ").strip()
    if c=='1':
        while True:
            nbd=input("새로운 생년월일 (YYYY-MM-DD): ").strip()
            if not nbd:
                print("수정을 취소했습니다.")
                return
            if vbd(nbd):
                mem[idx]['bd']=nbd;print("생년월일이 수정되었습니다.");break
    elif c=='2':
        while True:
            npw=input(f"새로운 패스워드 (최소 {MIN_PW_LEN}자): ").strip()
            if not npw:
                print("수정을 취소했습니다.")
                return
            if vpw(npw):
                mem[idx]['pw']=npw;print("패스워드가 수정되었습니다.");break
    elif c=='3':
        print("수정을 취소했습니다.");return
    else:
        print("잘못된 선택입니다.");return
    save(mem,fn)

# display member information
def dsp(fn: str, nm: str) -> None:
    m=sch(fn,nm)
    if m:
        print("\n회원 정보:")
        print({"이름":m['nm'],"생년월일":m['bd'],"등록일시":m['rd']})
    else:
        print(f"'{nm}' 회원을 찾을 수 없습니다.")

# delete member
def delete_member(fn: str, nm: str) -> None:
    mem = load(fn)
    if not mem:
        print("등록된 회원이 없습니다.")
        return
    
    # 회원 찾기
    member_found = False
    for i, m in enumerate(mem):
        if m['nm'] == nm:
            member_found = True
            print(f"\n삭제할 회원 정보:")
            print(f"이름: {m['nm']}")
            print(f"생년월일: {m['bd']}")
            print(f"등록일시: {m['rd']}")
            
            if yn(f"정말로 '{nm}' 회원을 삭제하시겠습니까?"):
                mem.pop(i)
                save(mem, fn)
                print(f"'{nm}' 회원이 삭제되었습니다.")
            else:
                print("회원 삭제를 취소했습니다.")
            break
    
    if not member_found:
        print(f"'{nm}' 회원을 찾을 수 없습니다.")

# main

# main function
def main() -> None:
    print("회원 관리 시스템에 오신 것을 환영합니다!")
    mem=[]
    while True:
        menu()
        c=mch()
        if c=='1':reg(mem)
        elif c=='2':sv(mem,DF_FN)
        elif c=='3':
            fn=input(f"파일명 (기본값: {DF_FN}): ").strip() or DF_FN
            if not fchk(fn):print(f"{fn} 파일을 찾을 수 없습니다.");continue
            nm=input("조회할 회원 이름: ").strip()
            if nm:dsp(fn,nm)
            else:print("조회를 취소했습니다.")
        elif c=='4':
            fn=input(f"파일명 (기본값: {DF_FN}): ").strip() or DF_FN
            if fchk(fn):lst(fn)
            else:print(f"{fn} 파일을 찾을 수 없습니다.")
        elif c=='5':
            fn=input(f"파일명 (기본값: {DF_FN}): ").strip() or DF_FN
            if not fchk(fn):print(f"{fn} 파일을 찾을 수 없습니다.");continue
            nm=input("수정할 회원 이름: ").strip()
            if nm:upd(fn,nm)
            else:print("수정을 취소했습니다.")
        elif c=='6':
            fn=input(f"파일명 (기본값: {DF_FN}): ").strip() or DF_FN
            if not fchk(fn):print(f"{fn} 파일을 찾을 수 없습니다.");continue
            nm=input("삭제할 회원 이름: ").strip()
            if nm:delete_member(fn,nm)
            else:print("삭제를 취소했습니다.")
        elif c=='7':
            if mem:
                print(f"\n주의: 메모리에 {len(mem)}명의 저장되지 않은 회원 정보가 있습니다!")
                if not yn("정말로 종료하시겠습니까?"):continue
            print("\n프로그램을 종료합니다. 이용해 주셔서 감사합니다!");break
        else:print("잘못된 메뉴 번호입니다. 1-7 사이의 숫자를 입력하세요.")
        enter()

if __name__=="__main__":
    main()