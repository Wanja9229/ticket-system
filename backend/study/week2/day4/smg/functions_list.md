# Python 회원관리 시스템 함수 목록

## main.py
### 전역 함수
- `main()` - 메인 실행 함수
### import 내용
- from member_manager import MemberManager

---

## member_manager.py
### import 내용
from typing import List, Dict
from member_service import MemberService
from file_service import FileService
from ui_helper import UIHelper
from validators import Validator

### MemberManager 클래스
# 생성자, 서비스 클래스들 초기화
def __init__(self): 

# 회원가입 기능
def register_member(self) -> None:

# 파일 저장 기능
def save_to_file(self) -> None: 

# 회원 정보 조회 기능
def search_member(self) -> None:

# 전체 회원 목록 조회 기능
def list_all_members(self) -> None:

# 회원 정보 수정 기능
def update_member(self) -> None:

# 파일 삭제 기능
def delete_file(self) -> None:

# 메인 실행 함수
def run(self) -> None:
    while True:
        self.ui_helper.show_menu()
        choice = input("메뉴를 선택하세요 (1-7): ").strip()
        
        if choice == '1':
            self.register_member()
        elif choice == '2':
            self.save_to_file()
        elif choice == '3':
            self.search_member()
        elif choice == '4':
            self.list_all_members()
        elif choice == '5':
            self.update_member()
        elif choice == '6':
            self.delete_file()
        elif choice == '7':
            print("프로그램을 종료합니다. 감사합니다!")
            break
        else:
            print("잘못된 선택입니다. 1-7 사이의 숫자를 입력해주세요.")
        
        input("\n계속하려면 Enter 키를 누르세요...")

---

## member_service.py
### import 내용
from datetime import datetime
from typing import List, Dict, Optional
from validators import Validator

### MemberService 클래스

# 생성자, Validator 초기화
def __init__(self):

# 회원 정보 딕셔너리 생성
def create_member(self, member_data: Dict[str, str]) -> Dict[str, str]:

# 이름으로 회원 찾기
def find_member_by_name(self, members: List[Dict[str, str]], name: str) -> Optional[Dict[str, str]]:

# 이름으로 회원 인덱스 찾기
def find_member_index_by_name(self, members: List[Dict[str, str]], name: str) -> int:

# 수정할 회원 찾기, 인덱스와 에러 메시지 반환
def find_member_for_update(self, members: List[Dict[str, str]], member_name: str) -> tuple[int, Optional[str]]:
 
# 생년월일 수정
def update_birth_date(self, members: List[Dict[str, str]], member_index: int, new_birth_date: str) -> tuple[bool, str]:

# 패스워드 수정
def update_password(self, members: List[Dict[str, str]], member_index: int, new_password: str) -> tuple[bool, str]:

---

## file_service.py
### import 내용
import json
import os
from typing import List, Dict, Optional

### FileService 클래스

# 회원 정보를 JSON 파일로 저장
def save_members_to_file(self, members: List[Dict[str, str]], filename: str) -> bool:

# JSON 파일에서 회원 정보 불러오기
def load_members_from_file(self, filename: str) -> Optional[List[Dict[str, str]]]:

# 파일 삭제
def delete_file(self, filename: str) -> bool:

# 파일 존재 여부 확인
def file_exists(self, filename: str) -> bool:

---

## ui_helper.py
### import 내용
from typing import Dict, List, Optional
from validators import Validator

### UIHelper 클래스
# 생성자, Validator 초기화
def __init__(self):

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

# 파일명 입력 받기
def get_filename_input(self, prompt: str) -> str:

# 파일 삭제 확인
def get_delete_confirmation(self, filename: str) -> bool:

# 단일 회원 정보 출력
def display_member_info(self, member: Dict[str, str]) -> None:

# 전체 회원 목록 출력
def display_members_list(self, members: List[Dict[str, str]]) -> None:

# 수정할 회원의 현재 정보 출력
def display_current_member_info(self, member: Dict[str, str]) -> None:

# 수정할 항목 선택
def get_update_choice(self) -> str:

# 새로운 생년월일 입력
def get_new_birth_date(self) -> str:

# 새로운 패스워드 입력
def get_new_password(self) -> str:

---

## validators.py
### import 내용
from datetime import datetime

### Validator 클래스

# 날짜 형식 검증 (YYYY-MM-DD)
def validate_date(self, date_string: str) -> bool:

# 문자열이 비어있지 않은지 검증
def validate_string_not_empty(self, value: str) -> bool:

# 파일 확장자 검증
def validate_file_extension(self, filename: str, extension: str = '.json') -> bool:

# 파일명 정리 (확장자 자동 추가)
def sanitize_filename(self, filename: str) -> str:

---

## 프로젝트 구조 요약
- **총 6개 파일**
- **총 5개 클래스** (MemberManager, MemberService, FileService, UIHelper, Validator)
- **총 31개 함수** (전역 함수 1개 + 클래스 메서드 30개)
- **주요 기능**: 회원 관리, 파일 입출력, UI 처리, 데이터 검증