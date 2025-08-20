# ui_helper.py - 사용자 인터페이스 헬퍼
from typing import Dict, List, Optional
from validators import Validator

class UIHelper:
    def __init__(self):
        self.validator = Validator()
    
    def show_menu(self) -> None:
        """메뉴 출력"""
        print("\n" + "="*50)
        print("           회원 관리 시스템")
        print("="*50)
        print("1. 회원가입")
        print("2. 파일 저장")
        print("3. 회원 정보 조회")
        print("4. 전체 회원 목록 보기")
        print("5. 회원 정보 수정")
        print("6. 파일 삭제")
        print("7. 프로그램 종료")
        print("="*50)
    
    def get_member_input(self) -> Optional[Dict[str, str]]:
        """회원 정보 입력 받기"""
        name = input("이름을 입력하세요: ").strip()
        if not name:
            print("이름은 필수 입력 항목입니다.")
            return None
        
        birth_date = input("생년월일을 입력하세요 (YYYY-MM-DD): ").strip()
        if not self.validator.validate_date(birth_date):
            print("생년월일 형식이 올바르지 않습니다. (YYYY-MM-DD)")
            return None
        
        password = input("패스워드를 입력하세요: ").strip()
        if not password:
            print("패스워드는 필수 입력 항목입니다.")
            return None
        
        return {
            "name": name,
            "birth_date": birth_date,
            "password": password
        }
    
    def get_filename_input(self, prompt: str) -> str:
        """파일명 입력 받기"""
        filename = input(f"{prompt} (예: members.json): ").strip()
        return self.validator.sanitize_filename(filename)
    
    def get_delete_confirmation(self, filename: str) -> bool:
        """파일 삭제 확인"""
        confirm = input(f"정말로 '{filename}' 파일을 삭제하시겠습니까? (y/N): ").strip().lower()
        return confirm in ['y', 'yes']
    
    def display_member_info(self, member: Dict[str, str]) -> None:
        """단일 회원 정보 출력"""
        print(f"\n--- {member['name']} 회원 정보 ---")
        print(f"이름: {member['name']}")
        print(f"생년월일: {member['birth_date']}")
        print(f"등록일: {member['register_date']}")
        print(f"패스워드: {'*' * len(member['password'])}")  # 패스워드 마스킹
    
    def display_members_list(self, members: List[Dict[str, str]]) -> None:
        """전체 회원 목록 출력"""
        print(f"\n총 {len(members)}명의 회원이 등록되어 있습니다.")
        print("-" * 80)

        #{문자열:정렬방향너비}
        # > = 오른쪽 정렬 (< = 왼쪽 정렬 - 기본값)
        # 4 = 총 너비 4 칸
        # ^ = 가운데 정렬
        # 10 = 총 너비 10칸
        print(f"{'번호':>4} {'이름':^10} {'생년월일':^12} {'등록일':^12} {'패스워드':^10}")
        print("-" * 80)
        
        for i, member in enumerate(members, 1):
            masked_password = '*' * len(member['password'])  # 패스워드 마스킹
            print(f"{i:>4} {member['name']:^10} {member['birth_date']:^12} {member['register_date']:^12} {masked_password:^10}")
        
        print("-" * 80)

    def display_current_member_info(self, member: Dict[str, str]) -> None:
        """수정할 회원의 현재 정보 출력"""
        print(f"\n--- 현재 {member['name']} 회원 정보 ---")
        print(f"1. 이름: {member['name']}")
        print(f"2. 생년월일: {member['birth_date']}")
        print(f"3. 패스워드: {'*' * len(member['password'])}")
    
    def get_update_choice(self) -> str:
        """수정할 항목 선택"""
        print("\n수정할 항목을 선택하세요:")
        print("1. 생년월일")
        print("2. 패스워드")
        return input("선택 (1-2): ").strip()
    
    def get_new_birth_date(self) -> str:
        """새로운 생년월일 입력"""
        return input("새로운 생년월일을 입력하세요 (YYYY-MM-DD): ").strip()
    
    def get_new_password(self) -> str:
        """새로운 패스워드 입력"""
        return input("새로운 패스워드를 입력하세요: ").strip()
    



    '''
    print(f"{'번호':>4} {'이름':^10} {'생년월일':^12} {'등록일':^12} {'패스워드':^10}")
    print("-" * 80)
    for i, member in enumerate(members, 1):
        masked_password = '*' * len(member['password'])  # 패스워드 마스킹
        print(f"{i:>4} {member['name']:^10} {member['birth_date']:^12} {member['register_date']:^12} {masked_password:^10}")
    print("-" * 80)
    '''