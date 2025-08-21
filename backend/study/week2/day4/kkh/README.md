```python

import json, os
from datetime import datetime
from typing import List, Dict

print("\n===== 메뉴 =====")
print("1. 회원가입")
print("2. 파일 저장")
print("3. 회원 정보 조회")
print("4. 전체 회원 목록 보기")
print("5. 회원 정보 수정")
print("6. 회원 삭제")
print("7. 프로그램 종료")

# mem: members
# name: name
# birth_date: birth_date
# register_date: register_date
# password: password

DF_FN = "members.json"  # default filename

# 현재 날짜와 시간을 문자열 형태로 반환하는 함수
# 회원 등록일시를 기록하는데 사용되며, "YYYY-MM-DD HH:MM:SS" 형식으로 반환
def now() -> str:
# "%Y-%m-%d %H:%M:%S"

# 사용자에게 y/n 질문을 던지고 불린값으로 결과를 반환하는 함수
# 삭제 확인, 종료 확인 등 중요한 작업 전 사용자 의사를 확인할 때 사용
def yn(msg: str) -> bool:

# 메뉴를 화면에 출력하고 사용자의 선택을 입력받아 반환하는 함수
# 1-7번까지의 메뉴 옵션을 제공하고 사용자가 입력한 번호를 문자열로 반환
def menu() -> str:

# 회원 리스트를 JSON 파일로 저장하는 함수
# 메모리상의 회원 데이터를 DF_FN 파일에 UTF-8 인코딩과 들여쓰기를 적용하여 저장
# 저장 성공/실패 메시지를 출력하고 성공 여부를 불린값으로 반환
def save(mem: List[Dict[str, str]]) -> bool:

# JSON 파일에서 회원 리스트를 로드하는 함수
# DF_FN 파일이 존재하지 않거나 읽기 실패 시 빈 리스트를 반환
def load() -> List[Dict[str, str]]:

# 파일 존재 여부를 확인하는 함수
# DF_FN 파일의 존재 여부를 불린값으로 반환하는 os.path.exists() 래퍼 함수
def fchk() -> bool:

# 새로운 회원을 등록하는 함수
# 이름, 생년월일, 패스워드를 입력받아 현재시간과 함께 메모리 리스트에 추가
# 빈 입력 시 회원가입을 취소하며 완료 후 저장 안내 메시지 출력
def reg(mem: List[Dict[str, str]]) -> None:

# 메모리상의 회원 데이터를 파일로 저장하는 함수
# save() 함수를 호출하여 실제 저장 작업을 수행하며 빈 리스트 체크 포함
def sv(mem: List[Dict[str, str]]) -> None:

# 파일에서 전체 회원 목록을 조회하여 출력하는 함수
# 번호, 이름, 생년월일, 등록일시를 포함한 목록과 총 회원수를 출력
def lst() -> None:

# 특정 회원의 정보를 수정하는 함수
# 파일에서 이름으로 회원을 찾아 생년월일 또는 패스워드를 수정하고 다시 파일에 저장
def upd(name: str) -> None:

# 특정 회원의 정보를 조회하여 출력하는 함수
# 파일에서 이름으로 회원을 검색하여 상세 정보를 딕셔너리 형태로 출력
def dsp(name: str) -> None:

# 회원을 삭제하는 함수
# 전체 회원 목록을 보여주고 삭제할 회원을 선택받아 확인 후 삭제
def del_mem() -> None:

# 프로그램의 메인 실행 함수
# 메뉴를 반복 출력하고 사용자 선택에 따라 각 기능을 실행하며 저장되지 않은 데이터 관리
def main() -> None:
```