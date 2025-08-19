"""
utils.py - 유틸리티 함수 모듈
이 파일은 프로그램 전체에서 사용되는 공통 기능들을 모아둔 곳입니다.
메뉴 출력, 사용자 입력 받기, 날짜/시간 처리 등의 기능을 제공합니다.
"""

# 필요한 모듈들을 가져옵니다
import os  # 운영체제 관련 기능 (화면 지우기 등)
from datetime import datetime  # 날짜와 시간을 다루기 위한 모듈
from typing import Dict  # 타입 힌트를 위한 모듈 (딕셔너리 타입 명시)

# 상수를 가져옵니다
from __init__ import DATETIME_FORMAT


def show_menu() -> None:
    """
    메인 메뉴를 화면에 출력하는 함수입니다.
    
    반환값: None (아무것도 반환하지 않음)
    """
    # 메뉴를 보기 좋게 출력합니다
    print("\n===== 회원 관리 시스템 =====")
    print("1. 회원가입")
    print("2. 파일 저장")
    print("3. 회원 정보 조회")
    print("4. 전체 회원 목록 보기")
    print("5. 회원 정보 수정")
    print("6. 파일 삭제")
    print("7. 프로그램 종료")
    print("========================")


def get_menu_choice() -> str:
    """
    사용자로부터 메뉴 선택을 입력받는 함수입니다.
    
    반환값: str - 사용자가 입력한 메뉴 번호 (문자열)
    """
    # input() 함수로 사용자 입력을 받습니다
    # strip()은 입력값 앞뒤의 공백을 제거합니다
    choice = input("\n메뉴를 선택하세요 (1-7): ").strip()
    return choice


def format_member_info(member: Dict[str, str], show_password: bool = False) -> str:
    """
    회원 정보를 보기 좋은 형태로 포맷팅하는 함수입니다.
    
    매개변수:
        member: 회원 정보가 담긴 딕셔너리
        show_password: 패스워드를 보여줄지 여부 (기본값: False)
    
    반환값: str - 포맷팅된 회원 정보 문자열
    """
    # 여러 줄의 문자열을 만들기 위해 리스트를 사용합니다
    info_lines = []
    info_lines.append("===== 회원 정보 =====")
    info_lines.append(f"이름: {member['name']}")
    info_lines.append(f"생년월일: {member['birth_date']}")
    info_lines.append(f"등록일시: {member['register_date']}")
    
    # show_password가 True면 실제 패스워드를, False면 마스킹 처리
    if show_password:
        info_lines.append(f"패스워드: {member['password']}")
    else:
        # '*' 문자를 8개 반복해서 마스킹 처리
        info_lines.append("패스워드: ********")
    
    info_lines.append("==================")
    
    # 리스트의 모든 요소를 줄바꿈(\n)으로 연결해서 하나의 문자열로 만듭니다
    return "\n".join(info_lines)


def get_current_datetime() -> str:
    """
    현재 날짜와 시간을 문자열로 반환하는 함수입니다.
    
    반환값: str - "YYYY-MM-DD HH:MM:SS" 형식의 날짜시간 문자열
    """
    # datetime.now()로 현재 시간을 가져오고
    # strftime()으로 원하는 형식의 문자열로 변환합니다
    return datetime.now().strftime(DATETIME_FORMAT)


def clear_screen() -> None:
    """
    콘솔 화면을 지우는 함수입니다.
    운영체제에 따라 다른 명령어를 사용합니다.
    
    반환값: None
    """
    # os.name이 'nt'면 Windows, 아니면 Unix/Linux/Mac
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # Unix/Linux/Mac
        os.system('clear')


def press_enter_to_continue() -> None:
    """
    사용자가 Enter 키를 누를 때까지 대기하는 함수입니다.
    메뉴로 돌아가기 전에 결과를 확인할 시간을 줍니다.
    
    반환값: None
    """
    input("\nEnter 키를 눌러 계속하세요...")


def get_yes_no_input(prompt: str) -> bool:
    """
    사용자로부터 Y/N 입력을 받아 True/False로 반환하는 함수입니다.
    
    매개변수:
        prompt: 사용자에게 보여줄 질문 문자열
    
    반환값: bool - Y/y 입력시 True, N/n 입력시 False
    """
    while True:  # 올바른 입력을 받을 때까지 반복
        # lower()로 소문자로 변환해서 대소문자 구분 없이 처리
        answer = input(f"{prompt} (Y/N): ").strip().lower()
        
        if answer in ['y', 'yes', '예', '네']:
            return True
        elif answer in ['n', 'no', '아니오', '아니요']:
            return False
        else:
            print("Y 또는 N을 입력해주세요.")