## utils.py
```python

# 메인 메뉴를 화면에 출력하는 함수
def show_menu() -> None:

# 사용자로부터 메뉴 선택을 입력받아 반환하는 함수
def get_menu_choice() -> str:

# 회원 정보를 보기 좋은 형태로 포맷팅하여 문자열로 반환하는 함수
def format_member_info(member: Dict[str, str], show_password: bool = False) -> str:

# 현재 날짜와 시간을 "YYYY-MM-DD HH:MM:SS" 형식의 문자열로 반환하는 함수
def get_current_datetime() -> str:

# Enter 키를 누를 때까지 대기하는 함수 (화면 멈춤용)
def press_enter_to_continue() -> None:

# Y/N 선택을 입력받아 True/False로 반환하는 함수
def get_yes_no_input(prompt: str) -> bool:
```
## validators.py
```python
# validators.py 에 함수 내역

# 날짜 문자열이 YYYY-MM-DD 형식인지 검증하는 함수
def validate_date(date_str: str) -> bool:

# 회원 이름의 유효성을 검증하는 함수 (빈값, 2자 이상, 중복 체크)
def validate_name(name: str, members: List[Dict[str, str]]) -> bool:

# 패스워드의 유효성을 검증하는 함수 (빈값, 4자 이상 체크)
def validate_password(password: str) -> bool:

# 주어진 이름이 이미 등록된 회원인지 확인하는 함수
def is_duplicate_member(name: str, members: List[Dict[str, str]]) -> bool:

# 생년월일의 유효성을 검증하는 함수 (형식, 미래날짜, 150세 이상 체크)
def validate_birth_date(birth_date_str: str) -> bool:

# 파일명의 유효성을 검증하는 함수 (빈값, 특수문자 체크)
def validate_filename(filename: str) -> bool:
```

## file_handler.py
```python

# JSON 파일에서 회원 데이터를 읽어와 리스트로 반환하는 함수
def load_from_file(filename: str) -> List[Dict[str, str]]:

# 회원 데이터를 JSON 파일로 저장하는 함수
def save_to_file(members: List[Dict[str, str]], filename: str) -> bool:

# 지정한 파일을 삭제하는 함수
def delete_file(filename: str) -> bool:

# 파일의 존재 여부를 확인하는 함수
def check_file_exists(filename: str) -> bool:

# 파일의 상세 정보(크기, 수정시간, 경로)를 딕셔너리로 반환하는 함수
def get_file_info(filename: str) -> Dict[str, str]:
```

## member_management.py
```python
# JSON 파일에서 회원 데이터를 읽어와 리스트로 반환하는 함수
def load_from_file(filename: str) -> List[Dict[str, str]]:

# 회원 데이터를 JSON 파일로 저장하는 함수
def save_to_file(members: List[Dict[str, str]], filename: str) -> bool:

# 지정한 파일을 삭제하는 함수
def delete_file(filename: str) -> bool:

# 파일의 존재 여부를 확인하는 함수
def check_file_exists(filename: str) -> bool:

```

## main.py

```python
# 프로그램의 메인 함수 (메뉴 시스템과 전체 흐름 제어)
def main() -> None:

# 회원가입 기능을 처리하는 핸들러 함수
def handle_register(members: List[Dict[str, str]]) -> None:

# 파일 저장 기능을 처리하는 핸들러 함수
def handle_save_to_file(members: List[Dict[str, str]]) -> None:

# 회원 정보 조회 기능을 처리하는 핸들러 함수
def handle_search_member() -> None:

# 전체 회원 목록 보기 기능을 처리하는 핸들러 함수
def handle_list_all_members() -> None:

# 회원 정보 수정 기능을 처리하는 핸들러 함수
def handle_update_member() -> None:

# 파일 삭제 기능을 처리하는 핸들러 함수
def handle_delete_file() -> None:

# 프로그램 종료를 처리하는 함수 (저장 안 된 데이터 경고)
def handle_exit(members: List[Dict[str, str]]) -> bool:
```