## ui_helper.py
### import 내용
from typing import Dict, List, Optional
from validators import Validator

### UIHelper 클래스
# 생성자, Validator 초기화
class UIHelper():
    def __init__(self):
        self.validator = Validator()

    # 메뉴 출력
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

    # 회원 정보 입력 받기
    def get_member_input(self) -> Optional[Dict[str, str]]:
        
        name = input("이름을 입력해주세요: ").strip()
        if not name:
            print("이름은 필수 입력 항목입니다.")
            return None
        
        birth_date = input("생년월일을 입력해주세요. (YYYY-MM-DD): ").strip()
        if not self.validator.validate_date(birth_date):
            print("생년월일 형식이 올바르지 않습니다. (YYYY-MM-DD)")
            return None
        
        password = input("비밀번호를 입력해주세요: ").strip()
        if not password:
            print("비밀번호는 필수 입력 항목입니다.")
            return None

        return {
            "name" : name,
            "birth_date" : birth_date,
            "password" : password
        }
        
    # 파일명 입력 받기
    def get_filename_input(self, prompt: str) -> str:
        filename = input(f"{prompt} (ex. memebrs.json)").strip()
        return self.validator.sanitize_filename(filename)

    # 단일 회원 정보 출력
    def display_member_info(self, member: Dict[str, str]) -> None:
        print("------찾으신 회원 정보 입니다-----")
        print(f"이름: {member['name']}")
        print(f"생년월일: {member['birth_date']}")
        print(f"패스워드: {'*' * len(member['password'])}")
        print(f"등록일: {member['register_date']}")


    # 전체 회원 목록 출력
    def display_members_list(self, members: List[Dict[str, str]]) -> None:
        print(f"\n총 {len(members)}명의 회원이 등록되어 있습니다.")
        print("-" * 80)
        print(f"{"번호":>4} {"이름":^10} {"생년월일":^12} {"패스워드":^10} {"등록일":^12}")
        print("-"*80)

        for i, member in enumerate(members, 1):
            masked_password = '*' * len(member['password'])

            print(f"{i:>4} {member['name']:^10} {member['birth_date']:^12} {masked_password:^12} {member['register_date']:^10}")
            
        print("-"*80)

    # 파일 삭제 확인
    def get_delete_confirmation(self, filename: str) -> bool:
        confirm = input(f"정말로 '{filename}' 파일을 삭제하시겠습니까? (y or n): ").strip().lower()
        return confirm in ['y', 'yes']

    # 수정할 항목 선택
    def get_update_choice(self) -> str:
        print("----- 수정 가능 정보 -----")
        print("1. 생년월일")
        print("2. 패스워드")
        
        choice_num = input("수정하실 내용을 선택해주세요 (1 or 2): ").strip()
        return choice_num

    # 새로운 생년월일 입력
    def get_new_birth_date(self) -> str:
        print("-----생년월일 변경-----")
        new_birth = input("새로운 생년월일을 입력하세요 (YYYY-MM-DD): ").strip()
        return new_birth
             

    # 새로운 패스워드 입력
    def get_new_password(self) -> str:
        print("-----패스워드 변경-----")
        new_password = input("새로운 패스워드를 입력하세요: ").strip()
        return new_password