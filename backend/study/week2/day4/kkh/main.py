"""
main.py - 회원 관리 시스템 메인 프로그램
이 파일은 프로그램의 시작점입니다.
사용자와의 상호작용을 관리하고 다른 모듈들을 조정합니다.
"""

# 다른 모듈들을 가져옵니다 (별칭 사용)
import member_management as mm  # 회원 관리 기능
import file_handler as fh  # 파일 처리 기능
import validators as val  # 입력 검증 기능
import utils  # 유틸리티 기능

# 상수를 가져옵니다
from __init__ import DEFAULT_FILENAME, WELCOME_MESSAGE, EXIT_MESSAGE

# 타입 힌트를 위한 import
from typing import List, Dict


def main() -> None:
    """
    프로그램의 메인 함수입니다.
    메뉴를 표시하고 사용자의 선택에 따라 적절한 기능을 실행합니다.
    
    반환값: None
    """
    # 프로그램 시작 메시지
    print(WELCOME_MESSAGE)
    print("=" * 50)
    
    # 메모리에 저장할 회원 리스트 초기화
    # 이 리스트는 파일에 저장하기 전까지 임시로 데이터를 보관합니다
    members: List[Dict[str, str]] = []
    
    # 메인 루프 - 사용자가 종료를 선택할 때까지 계속 실행
    while True:
        # 메뉴 표시
        utils.show_menu()
        
        # 사용자 선택 받기
        choice = utils.get_menu_choice()
        
        # 선택에 따른 기능 실행
        if choice == '1':
            # 1. 회원가입
            handle_register(members)
            
        elif choice == '2':
            # 2. 파일 저장
            handle_save_to_file(members)
            
        elif choice == '3':
            # 3. 회원 정보 조회
            handle_search_member()
            
        elif choice == '4':
            # 4. 전체 회원 목록 보기
            handle_list_all_members()
            
        elif choice == '5':
            # 5. 회원 정보 수정
            handle_update_member()
            
        elif choice == '6':
            # 6. 파일 삭제
            handle_delete_file()
            
        elif choice == '7':
            # 7. 프로그램 종료
            if handle_exit(members):
                break
            
        else:
            # 잘못된 입력 처리
            print("❌ 잘못된 메뉴 번호입니다. 1-7 사이의 숫자를 입력하세요.")
        
        # 각 작업 후 Enter 키를 눌러 계속 진행
        utils.press_enter_to_continue()


def handle_register(members: List[Dict[str, str]]) -> None:
    """
    회원가입 기능을 처리하는 함수입니다.
    
    매개변수:
        members: 현재 메모리에 저장된 회원 리스트
    
    반환값: None
    """
    mm.register_member(members)


def handle_save_to_file(members: List[Dict[str, str]]) -> None:
    """
    파일 저장 기능을 처리하는 함수입니다.
    
    매개변수:
        members: 저장할 회원 리스트
    
    반환값: None
    """
    # 저장할 회원이 있는지 확인
    if not members:
        print("❌ 저장할 회원 정보가 없습니다. 먼저 회원가입을 진행하세요.")
        return
    
    print("\n===== 파일 저장 =====")
    
    # 상수로 정의된 파일명 사용
    filename = DEFAULT_FILENAME
    
    # 파일 저장 실행
    mm.save_to_file(members, filename)


def handle_search_member() -> None:
    """
    회원 정보 조회 기능을 처리하는 함수입니다.
    
    반환값: None
    """
    print("\n===== 회원 정보 조회 =====")
    
    # 파일명 입력받기
    filename = input(f"파일명을 입력하세요 (기본값: {DEFAULT_FILENAME}): ").strip()
    if not filename:
        filename = DEFAULT_FILENAME
    
    # 파일 존재 여부 확인
    if not fh.check_file_exists(filename):
        print(f"❌ {filename} 파일을 찾을 수 없습니다.")
        return
    
    # 조회할 회원 이름 입력받기
    name = input("조회할 회원 이름을 입력하세요: ").strip()
    if not name:
        print("조회를 취소했습니다.")
        return
    
    # 회원 정보 조회 및 출력
    mm.display_member_info(filename, name)


def handle_list_all_members() -> None:
    """
    전체 회원 목록 보기 기능을 처리하는 함수입니다.
    
    반환값: None
    """
    print("\n===== 전체 회원 목록 보기 =====")
    
    # 파일명 입력받기
    filename = input("파일명을 입력하세요 (기본값: members.json): ").strip()
    if not filename:
        filename = "members.json"
    
    # 파일 존재 여부 확인
    if not fh.check_file_exists(filename):
        print(f"❌ {filename} 파일을 찾을 수 없습니다.")
        return
    
    # 전체 회원 목록 출력
    mm.list_all_members(filename)


def handle_update_member() -> None:
    """
    회원 정보 수정 기능을 처리하는 함수입니다.
    
    반환값: None
    """
    print("\n===== 회원 정보 수정 =====")
    
    # 파일명 입력받기
    filename = input("파일명을 입력하세요 (기본값: members.json): ").strip()
    if not filename:
        filename = "members.json"
    
    # 파일 존재 여부 확인
    if not fh.check_file_exists(filename):
        print(f"❌ {filename} 파일을 찾을 수 없습니다.")
        return
    
    # 수정할 회원 이름 입력받기
    name = input("수정할 회원 이름을 입력하세요: ").strip()
    if not name:
        print("수정을 취소했습니다.")
        return
    
    # 회원 정보 수정
    mm.update_member(filename, name)


def handle_delete_file() -> None:
    """
    파일 삭제 기능을 처리하는 함수입니다.
    
    반환값: None
    """
    print("\n===== 파일 삭제 =====")
    
    # 삭제할 파일명 입력받기
    filename = input("삭제할 파일명을 입력하세요: ").strip()
    if not filename:
        print("삭제를 취소했습니다.")
        return
    
    # 파일 존재 여부 확인
    if not fh.check_file_exists(filename):
        print(f"❌ {filename} 파일을 찾을 수 없습니다.")
        return
    
    # 삭제 확인
    print(f"\n⚠️ 경고: {filename} 파일을 삭제하면 복구할 수 없습니다!")
    if utils.get_yes_no_input("정말로 삭제하시겠습니까?"):
        fh.delete_file(filename)
    else:
        print("파일 삭제를 취소했습니다.")


def handle_exit(members: List[Dict[str, str]]) -> bool:
    """
    프로그램 종료를 처리하는 함수입니다.
    저장하지 않은 데이터가 있으면 경고합니다.
    
    매개변수:
        members: 현재 메모리에 저장된 회원 리스트
    
    반환값: bool - 종료하면 True, 계속하면 False
    """
    # 메모리에 저장되지 않은 회원이 있는지 확인
    if members:
        print(f"\n⚠️ 주의: 메모리에 {len(members)}명의 저장되지 않은 회원 정보가 있습니다!")
        print("종료하면 이 정보들은 사라집니다.")
        
        if not utils.get_yes_no_input("정말로 종료하시겠습니까?"):
            return False
    
    print(f"\n{EXIT_MESSAGE}")
    return True


# 프로그램 시작점
# 이 파일을 직접 실행할 때만 main() 함수를 호출합니다
# 다른 파일에서 import할 때는 실행되지 않습니다
if __name__ == "__main__":
    main()