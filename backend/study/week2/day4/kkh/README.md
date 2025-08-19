# 회원 관리 시스템 프로그램

## 📋 프로젝트 개요

Python의 모듈, 파일 입출력, 예외 처리 기능을 종합적으로 활용한 회원 관리 시스템입니다. 이 프로그램은 회원 정보를 관리하고, JSON 파일로 저장하며, CRUD(Create, Read, Update, Delete) 기능을 제공합니다.

## 🎯 주요 기능

### 1. 회원가입 (Create)
- 회원 정보(이름, 생년월일, 패스워드) 입력
- 등록일시 자동 생성
- 중복 회원 검증
- 메모리에 임시 저장

### 2. 파일 저장
- 메모리의 모든 회원 정보를 JSON 파일로 저장
- 사용자 지정 파일명 가능
- 덮어쓰기 확인 기능

### 3. 회원 정보 조회 (Read)
- 파일명과 회원 이름으로 검색
- 개별 회원 상세 정보 출력
- 패스워드 마스킹 처리

### 4. 전체 회원 목록 조회 (List)
- 저장된 모든 회원 정보를 표 형태로 출력
- 회원 번호, 이름, 생년월일, 등록일시 표시
- 총 회원 수 표시

### 5. 회원 정보 수정 (Update)
- 생년월일, 패스워드 수정 가능
- 이름은 수정 불가 (Primary Key)
- 수정 후 자동 저장

### 6. 파일 삭제 (Delete)
- 지정한 회원 데이터 파일 완전 삭제
- 삭제 전 확인 절차

## 📊 데이터 구조

### 회원 정보 구조
```python
{
    "name": str,           # 회원 이름 (중복 불가, Primary Key)
    "birth_date": str,     # 생년월일 (YYYY-MM-DD 형식)
    "register_date": str,  # 등록일시 (YYYY-MM-DD HH:MM:SS 형식)
    "password": str        # 패스워드 (최소 4자 이상)
}
```

### JSON 파일 구조 예시
```json
[
   {
       "name": "김철수",
       "birth_date": "1985-03-15",
       "register_date": "2024-08-19 09:15:42",
       "password": "mypass123"
   },
   {
       "name": "이영희", 
       "birth_date": "1992-07-22",
       "register_date": "2024-08-19 09:16:18",
       "password": "secure456"
   },
   {
       "name": "박민수",
       "birth_date": "1988-11-08", 
       "register_date": "2024-08-19 09:17:05",
       "password": "password789"
   },
   {
       "name": "최지은",
       "birth_date": "1995-01-30",
       "register_date": "2024-08-19 09:17:52",
       "password": "mypassword"
   },
   {
       "name": "정현우",
       "birth_date": "1990-09-12", 
       "register_date": "2024-08-19 09:18:30",
       "password": "qwerty123"
   }
]
```

## 🔧 기술 스택

### 사용 모듈
- `json`: JSON 파일 처리
- `datetime`: 날짜/시간 처리
- `os`: 파일 시스템 작업
- `typing`: 타입 힌트

### 모듈 구조 및 함수 분리

#### 1. **main.py** - 메인 실행 파일
```python
import member_management as mm
import file_handler as fh
import validators as val
import utils

def main() -> None:
    # 메인 실행 로직
    # 함수 호출 예시:
    # mm.register_member(members)
    # fh.load_from_file("members.json")
    # val.validate_date(date_input)
    # utils.show_menu()
```

#### 2. **member_management.py** - 회원 관리 기능
```python
def register_member(members: List[Dict[str, str]]) -> None      # 회원가입
def save_to_file(members: List[Dict[str, str]], filename: str) -> None  # 파일 저장
def search_member(filename: str, name: str) -> Optional[Dict[str, str]]  # 회원 조회
def list_all_members(filename: str) -> None                     # 전체 목록
def update_member(filename: str, name: str) -> None              # 회원 수정
```

#### 3. **file_handler.py** - 파일 입출력 처리
```python
def load_from_file(filename: str) -> List[Dict[str, str]]       # 파일 로드
def delete_file(filename: str) -> None                          # 파일 삭제
def check_file_exists(filename: str) -> bool                    # 파일 존재 확인
def create_backup(filename: str) -> bool                        # 백업 생성
```

#### 4. **validators.py** - 입력 검증 함수
```python
def validate_date(date_str: str) -> bool                        # 날짜 형식 검증
def validate_name(name: str, members: List[Dict[str, str]]) -> bool  # 이름 검증
def validate_password(password: str) -> bool                    # 패스워드 검증
def is_duplicate_member(name: str, members: List[Dict[str, str]]) -> bool  # 중복 확인
```

#### 5. **utils.py** - 유틸리티 함수
```python
def show_menu() -> None                                         # 메뉴 출력
def get_menu_choice() -> str                                    # 메뉴 선택 입력
def format_member_info(member: Dict[str, str], show_password: bool = False) -> str  # 회원 정보 포맷팅
def get_current_datetime() -> str                               # 현재 날짜시간 문자열
def clear_screen() -> None                                      # 화면 지우기
```

## 📝 입력 검증 규칙

### 회원가입 시 검증
- **이름**: 공백 불가, 2자 이상, 중복 불가
- **생년월일**: YYYY-MM-DD 형식, 유효한 날짜
- **패스워드**: 최소 4자 이상
- **등록일시**: 자동 생성 (수정 불가)

## 🚨 예외 처리

### 파일 관련 예외
- `FileNotFoundError`: 파일이 존재하지 않을 때
- `PermissionError`: 파일 접근 권한이 없을 때
- `json.JSONDecodeError`: JSON 파싱 오류 시
- `IOError`: 기타 입출력 오류

### 데이터 검증 예외
- `ValueError`: 날짜 형식 오류, 타입 변환 오류
- `KeyError`: 딕셔너리 키 오류
- 중복 회원, 잘못된 입력 등 사용자 정의 예외

## 💻 실행 방법

### 프로그램 실행
```bash
python main.py
```

### 모듈 import 예시 (main.py)
```python
# 각 모듈을 별칭으로 import
import member_management as mm
import file_handler as fh
import validators as val
import utils

# 타입 힌트를 위한 import
from typing import List, Dict, Optional

# 사용 예시
members = []
mm.register_member(members)  # 회원가입 함수 호출
fh.load_from_file("members.json")  # 파일 로드 함수 호출
val.validate_date("2024-08-19")  # 날짜 검증 함수 호출
utils.show_menu()  # 메뉴 표시 함수 호출
```

### 메뉴 구성
```
===== 회원 관리 시스템 =====
1. 회원가입
2. 파일 저장
3. 회원 정보 조회
4. 전체 회원 목록 보기
5. 회원 정보 수정
6. 파일 삭제
7. 프로그램 종료
========================
```

### 사용 예시

#### 1. 회원가입
```
이름을 입력하세요: 김철수
생년월일을 입력하세요 (YYYY-MM-DD): 1985-03-15
패스워드를 입력하세요: mypass123
✅ 회원가입이 완료되었습니다!
```

#### 2. 회원 정보 조회
```
파일명을 입력하세요: members.json
조회할 회원 이름을 입력하세요: 김철수

===== 회원 정보 =====
이름: 김철수
생년월일: 1985-03-15
등록일시: 2024-08-19 09:15:42
패스워드: ********
==================
```

#### 3. 전체 회원 목록
```
===== 전체 회원 목록 =====
번호 | 이름    | 생년월일    | 등록일시
-----------------------------------------
1    | 김철수  | 1985-03-15 | 2024-08-19 09:15:42
2    | 이영희  | 1992-07-22 | 2024-08-19 09:16:18
-----------------------------------------
총 2명의 회원이 등록되어 있습니다.
========================
```

## ⚠️ 주의사항

1. **데이터 저장**: 회원가입 후 반드시 '파일 저장' 기능을 실행해야 데이터가 영구 저장됩니다.
2. **파일명**: 기본 파일명은 `members.json`이며, 다른 이름으로도 저장 가능합니다.
3. **중복 회원**: 동일한 이름의 회원은 등록할 수 없습니다.
4. **파일 삭제**: 파일 삭제는 복구할 수 없으므로 신중히 진행하세요.

## 📁 프로젝트 구조

```
member-management-system/
│
├── main.py                 # 메인 프로그램 파일
├── member_management.py    # 회원 관리 기능 모듈
├── file_handler.py        # 파일 입출력 처리 모듈
├── validators.py          # 입력 검증 모듈
├── utils.py               # 유틸리티 함수 모듈
├── members.json           # 회원 데이터 파일 (자동 생성)
└── README.md              # 프로젝트 문서
```

### 모듈별 역할

- **main.py**: 프로그램의 진입점, 메인 루프 및 메뉴 처리
- **member_management.py**: 회원 CRUD 핵심 기능 구현
- **file_handler.py**: JSON 파일 읽기/쓰기/삭제 등 파일 작업
- **validators.py**: 사용자 입력 데이터 검증 로직
- **utils.py**: 메뉴 출력, 포맷팅 등 공통 유틸리티 함수

## 🤝 기여 방법

이 프로젝트는 Python 학습을 위한 과제 프로젝트입니다. 코드 개선이나 버그 수정에 대한 제안은 언제든 환영합니다.

## 📄 라이선스

이 프로젝트는 학습 목적으로 작성되었습니다.