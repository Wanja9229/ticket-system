import os
from datetime import datetime
from typing import Dict

def show_menu() -> None:
  print("\n===회원 관리 시스템==")
  print("1. 회원가입")
  print("2. 파일저장")
  print("3. 회원정보조회")
  print("4. 전체 회원 목록보기")
  print("5. 회원 정보 수정")
  print("6. 파일 삭제")
  print("7. 프로그램 종료")
  print("=====================")
  
def get_menu_choice() -> str:
  choice = input("\n메뉴를 선택하세요 (1-7): ").strip()
  return choice

# Dict[str, str] 의 의미 : Dict[키의_타입, 값의_타입]
def format_member_info(member: Dict[str, str], show_password: bool = False) -> str:
  info_lines = []
  info_lines.append("==회원 정보 ===")
  info_lines.append(f"이름: {member['name']}")
  info_lines.append(f"생년월일: {member['birth_date']}")
  info_lines.append(f"등록일시: {member['register_date']}")
  
  if show_password:
    info_lines.append(f"패스워드: {member['password']}")
  else:
    info_lines.append("패스워드: ***** ")
    
  info_lines.append("=============")
  
  return "\n".join(info_lines)

def get_current_datetime() -> str:
  return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
  
def press_enter_to_continue() -> None:
  input("\nEnter 키를 눌러 계속하세요...")
  
def get_yes_no_input(prompt: str) -> bool:
  while True:
    answer = input(f"{prompt} (Y/N):").strip.lower()
    
    if answer in ['y','yes','예','네','sp']:
      return True
    elif answer in ['n','no','아니오','아니요']:
      return False
    else:
      print("Y 또는 N을 입력하세요")