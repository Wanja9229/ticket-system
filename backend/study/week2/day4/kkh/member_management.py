"""
member_management.py - 회원 관리 기능 모듈
회원 등록, 조회, 수정 등 핵심 비즈니스 로직을 담당하는 모듈입니다.
"""

# 필요한 모듈들을 가져옵니다
from typing import List, Dict, Optional  # 타입 힌트를 위한 모듈
import file_handler as fh  # 파일 처리 모듈
import validators as val  # 검증 모듈
import utils  # 유틸리티 모듈

# 상수를 가져옵니다
from __init__ import MIN_PASSWORD_LENGTH, TABLE_WIDTH, COLUMN_WIDTHS


def register_member(members: List[Dict[str, str]]) -> None:
    """
    새로운 회원을 등록하는 함수입니다.
    
    매개변수:
        members: 현재 메모리에 저장된 회원 리스트
    
    반환값: None
    
    처리 과정:
        1. 사용자로부터 이름, 생년월일, 패스워드 입력받기
        2. 입력값 검증
        3. 회원 정보 딕셔너리 생성
        4. 메모리의 회원 리스트에 추가
    """
    print("\n===== 회원가입 =====")
    
    # 1. 이름 입력받기 (중복 확인 포함)
    while True:
        name = input("이름을 입력하세요 (취소: 빈 입력): ").strip()
        
        # 빈 입력시 회원가입 취소
        if not name:
            print("회원가입을 취소했습니다.")
            return
        
        # 이름 유효성 검증
        if val.validate_name(name, members):
            break  # 유효한 이름이면 반복문 종료
    
    # 2. 생년월일 입력받기
    while True:
        birth_date = input("생년월일을 입력하세요 (YYYY-MM-DD): ").strip()
        
        # 빈 입력시 회원가입 취소
        if not birth_date:
            print("회원가입을 취소했습니다.")
            return
        
        # 생년월일 유효성 검증
        if val.validate_birth_date(birth_date):
            break
    
    # 3. 패스워드 입력받기
    while True:
        password = input(f"패스워드를 입력하세요 (최소 {MIN_PASSWORD_LENGTH}자): ").strip()
        
        # 빈 입력시 회원가입 취소
        if not password:
            print("회원가입을 취소했습니다.")
            return
        
        # 패스워드 유효성 검증
        if val.validate_password(password):
            break
    
    # 4. 회원 정보 딕셔너리 생성
    new_member = {
        "name": name,
        "birth_date": birth_date,
        "register_date": utils.get_current_datetime(),  # 현재 시간 자동 설정
        "password": password
    }
    
    # 5. 메모리의 회원 리스트에 추가
    members.append(new_member)
    
    print(f"\n✅ {name}님의 회원가입이 완료되었습니다!")
    print("💡 파일로 저장하려면 '2. 파일 저장' 메뉴를 선택하세요.")


def save_to_file(members: List[Dict[str, str]], filename: str) -> None:
    """
    메모리의 회원 정보를 파일로 저장하는 함수입니다.
    
    매개변수:
        members: 저장할 회원 리스트
        filename: 저장할 파일명
    
    반환값: None
    """
    # 저장할 회원이 있는지 확인
    if not members:
        print("❌ 저장할 회원 정보가 없습니다.")
        return
    
    # 파일이 이미 존재하는 경우 덮어쓰기 확인
    if fh.check_file_exists(filename):
        if not utils.get_yes_no_input(f"{filename} 파일이 이미 존재합니다. 덮어쓰시겠습니까?"):
            print("파일 저장을 취소했습니다.")
            return
    
    # file_handler 모듈의 save_to_file 함수 호출
    fh.save_to_file(members, filename)


def search_member(filename: str, name: str) -> Optional[Dict[str, str]]:
    """
    파일에서 특정 회원을 검색하는 함수입니다.
    
    매개변수:
        filename: 검색할 파일명
        name: 검색할 회원 이름
    
    반환값: Optional[Dict[str, str]] - 찾은 회원 정보 또는 None
    """
    # 파일에서 전체 회원 정보 로드
    members = fh.load_from_file(filename)
    
    # 회원 정보가 없으면 None 반환
    if not members:
        return None
    
    # 이름으로 회원 검색
    for member in members:
        if member['name'] == name:
            return member
    
    # 찾지 못한 경우 None 반환
    return None


def list_all_members(filename: str) -> None:
    """
    파일에 저장된 모든 회원을 목록으로 출력하는 함수입니다.
    
    매개변수:
        filename: 읽을 파일명
    
    반환값: None
    """
    # 파일에서 전체 회원 정보 로드
    members = fh.load_from_file(filename)
    
    # 회원이 없는 경우
    if not members:
        print("등록된 회원이 없습니다.")
        return
    
    # 회원 목록 헤더 출력
    print("\n===== 전체 회원 목록 =====")
    print(f"{'번호':<{COLUMN_WIDTHS['number']}} | "
          f"{'이름':<{COLUMN_WIDTHS['name']}} | "
          f"{'생년월일':<{COLUMN_WIDTHS['birth_date']}} | "
          f"{'등록일시':<{COLUMN_WIDTHS['register_date']}}")
    print("-" * TABLE_WIDTH)
    
    # enumerate()를 사용하여 번호와 함께 출력
    # start=1로 번호를 1부터 시작
    for idx, member in enumerate(members, start=1):
        print(f"{idx:<{COLUMN_WIDTHS['number']}} | "
              f"{member['name']:<{COLUMN_WIDTHS['name']}} | "
              f"{member['birth_date']:<{COLUMN_WIDTHS['birth_date']}} | "
              f"{member['register_date']:<{COLUMN_WIDTHS['register_date']}}")
    
    print("-" * TABLE_WIDTH)
    print(f"총 {len(members)}명의 회원이 등록되어 있습니다.")
    print("========================")


def update_member(filename: str, name: str) -> None:
    """
    회원 정보를 수정하는 함수입니다.
    
    매개변수:
        filename: 회원 정보가 저장된 파일명
        name: 수정할 회원의 이름
    
    반환값: None
    
    처리 과정:
        1. 파일에서 전체 회원 정보 로드
        2. 수정할 회원 찾기
        3. 수정할 항목 선택
        4. 새로운 값 입력 및 검증
        5. 정보 수정
        6. 파일에 저장
    """
    # 파일에서 전체 회원 정보 로드
    members = fh.load_from_file(filename)
    
    if not members:
        print("등록된 회원이 없습니다.")
        return
    
    # 수정할 회원 찾기
    member_index = -1  # 찾은 회원의 인덱스 저장
    for idx, member in enumerate(members):
        if member['name'] == name:
            member_index = idx
            break
    
    # 회원을 찾지 못한 경우
    if member_index == -1:
        print(f"❌ '{name}' 회원을 찾을 수 없습니다.")
        return
    
    # 현재 회원 정보 출력
    print("\n현재 회원 정보:")
    print(utils.format_member_info(members[member_index], show_password=True))
    
    # 수정할 항목 선택
    print("\n수정할 항목을 선택하세요:")
    print("1. 생년월일")
    print("2. 패스워드")
    print("3. 취소")
    
    choice = input("선택 (1-3): ").strip()
    
    if choice == '1':
        # 생년월일 수정
        while True:
            new_birth_date = input("새로운 생년월일 (YYYY-MM-DD): ").strip()
            
            if not new_birth_date:
                print("수정을 취소했습니다.")
                return
            
            if val.validate_birth_date(new_birth_date):
                members[member_index]['birth_date'] = new_birth_date
                print("✅ 생년월일이 수정되었습니다.")
                break
    
    elif choice == '2':
        # 패스워드 수정
        while True:
            new_password = input(f"새로운 패스워드 (최소 {MIN_PASSWORD_LENGTH}자): ").strip()
            
            if not new_password:
                print("수정을 취소했습니다.")
                return
            
            if val.validate_password(new_password):
                members[member_index]['password'] = new_password
                print("✅ 패스워드가 수정되었습니다.")
                break
    
    elif choice == '3':
        print("수정을 취소했습니다.")
        return
    
    else:
        print("❌ 잘못된 선택입니다.")
        return
    
    # 수정된 정보를 파일에 저장
    if fh.save_to_file(members, filename):
        print("✅ 수정된 정보가 파일에 저장되었습니다.")
    else:
        print("❌ 파일 저장에 실패했습니다.")


def display_member_info(filename: str, name: str) -> None:
    """
    특정 회원의 정보를 조회하여 출력하는 함수입니다.
    
    매개변수:
        filename: 회원 정보가 저장된 파일명
        name: 조회할 회원의 이름
    
    반환값: None
    """
    # 회원 검색
    member = search_member(filename, name)
    
    if member:
        # 회원 정보 출력 (패스워드는 마스킹 처리)
        print("\n" + utils.format_member_info(member, show_password=False))
    else:
        print(f"❌ '{name}' 회원을 찾을 수 없습니다.")