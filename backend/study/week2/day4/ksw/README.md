# 회원 관리 시스템 개발 - 학습 정리

## 📅 학습 날짜: 2025년 1월

---

## 🎯 프로젝트 개요

Python의 모듈, 파일 입출력, 예외 처리를 활용한 회원 관리 시스템 개발
- **목표**: CRUD 기능을 갖춘 간단한 회원 관리 프로그램
- **핵심**: JSON 파일을 데이터베이스로 활용

---

## 📁 프로젝트 구조

```
ksw/
├── api/
│   ├── __init__.py      # 패키지 초기화 파일 (필수)
│   ├── menu.py          # 메뉴 시스템 함수
│   └── curd.py          # CRUD 기능 함수
├── data/
│   └── members.json     # 회원 데이터 저장
└── main.py              # 메인 실행 파일
```

### 📌 구조 설계 포인트
- `api/` : Python 패키지 → `__init__.py` 필요
- `data/` : 단순 파일 저장 폴더 → `__init__.py` 불필요
- 작업 디렉토리는 `main.py` 실행 위치 기준

---

## 💻 구현 코드

### 1️⃣ **메뉴 시스템 (api/menu.py)**

```python
def menu_pop():
    """메뉴 출력 함수"""
    print('------회원 관리 시스템------')
    print('1. 회원 가입')
    print('2. 전체 목록')
    print('3. 회원 조회')
    print('4. 회원 수정')
    print('5. 회원 삭제')
    print('6. 변경 저장')
    print('7. 프로그램 종료')
    print('---------------------------')
    print('실행할 메뉴의 숫자를 입력해 주세요.')

def menu_choice() -> int:
    """사용자 입력 받기 (타입힌트 포함)"""
    try:
        choice = int(input("메뉴 선택 : "))
        if 1 <= choice <= 7:
            return choice
        else:
            print('메뉴 번호를 확인해주세요.')
            return 0
    except ValueError:
        print('실행할 메뉴의 숫자를 입력해 주세요.')
        return 0
```

### 2️⃣ **메인 실행 파일 (main.py)**

```python
from api.menu import menu_pop, menu_choice
from api.curd import member_input, member_list_get, member_get, 
                     member_update, member_delete, file_save

def main():
    # 딕셔너리로 메뉴-함수 매핑 (깔끔한 구조)
    menu_dict = {
        1: member_input,
        2: member_list_get,
        3: member_get,
        4: member_update,
        5: member_delete,
        6: file_save
    }
    
    while True:
        menu_pop()
        menu_num = menu_choice()
        
        if menu_num == 0:  # 잘못된 입력
            continue
        elif menu_num == 7:  # 프로그램 종료
            print('------프로그램을 종료합니다------')
            break
        elif menu_num in menu_dict:
            menu_dict[menu_num]()  # 해당 함수 실행

main()
```

### 3️⃣ **CRUD 함수 - 전체 목록 조회 (api/curd.py)**

```python
import json
import os

def member_list_get():
    """전체 회원 목록 조회"""
    print('------전체 회원 목록------')
    
    # 1. 파일 존재 확인
    if not os.path.exists('data/members.json'):
        print('저장된 회원 정보가 없습니다.')
        return
    
    # 2. JSON 파일 읽기 (with문 사용)
    with open('data/members.json', 'r', encoding='utf-8') as f:
        members = json.load(f)  # JSON → Python 리스트
        
        # 3. 데이터 출력
        for i, member in enumerate(members, 1):  # 리스트는 enumerate
            print(f"\n{i}번째 회원")
            for key, val in member.items():  # 딕셔너리는 .items()
                print(f"  {key}: {val}")
            print("-" * 30)
```

---

## 📚 핵심 개념 정리

### 🔹 **Python import 방식**

```python
# 방법 1: 전체 경로 사용
import api.menu
api.menu.menu_pop()  # 사용시 전체 경로

# 방법 2: from import (추천)
from api.menu import menu_pop, menu_choice
menu_pop()  # 바로 사용

# 방법 3: 모든 함수 가져오기
from api.menu import *
menu_pop()  # 바로 사용
```

### 🔹 **파일 입출력 패턴**

```python
# JSON 읽기 보일러플레이트
with open('파일경로', 'r', encoding='utf-8') as f:
    data = json.load(f)

# JSON 쓰기 보일러플레이트
with open('파일경로', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
```

### 🔹 **with문의 역할**
- `open()` : 파일 열기 함수
- `with` : 자동 리소스 관리 (자동으로 close)
- 에러 발생해도 안전하게 파일 닫힘

### 🔹 **enumerate vs items**

```python
# enumerate: 리스트 순회 (인덱스 + 값)
리스트 = ["a", "b", "c"]
for i, val in enumerate(리스트, 1):  # 1부터 시작
    print(f"{i}: {val}")

# items: 딕셔너리 순회 (키 + 값)
딕셔너리 = {"name": "김철수", "age": 30}
for key, val in 딕셔너리.items():
    print(f"{key}: {val}")
```

### 🔹 **타입힌트**

```python
def function_name() -> int:  # int 반환
def function_name() -> None:  # 반환값 없음
def function_name(param: str) -> bool:  # str 받아서 bool 반환
```

---

## 📦 사용 모듈 (모두 내장)

| 모듈 | 용도 | pip 설치 |
|------|------|----------|
| `json` | JSON 파일 처리 | ❌ 불필요 |
| `os` | 파일/경로 작업 | ❌ 불필요 |
| `datetime` | 날짜/시간 처리 | ❌ 불필요 |

---

## 📋 JSON 데이터 구조

```json
[
    {
        "name": "김철수",
        "birth_date": "1990-05-15",
        "register_date": "2024-01-10",
        "password": "1234"
    },
    {
        "name": "이영희",
        "birth_date": "1995-08-20",
        "register_date": "2024-01-11",
        "password": "5678"
    }
]
```

---

## ✅ 완료된 작업

- [x] 프로젝트 구조 설계
- [x] 메뉴 시스템 구현 (`menu_pop`, `menu_choice`)
- [x] 메인 루프 구현 (딕셔너리 매핑 방식)
- [x] 전체 목록 조회 기능 (`member_list_get`)

## 📝 남은 작업

- [ ] 회원 가입 (`member_input`) - 메모리에 임시 저장
- [ ] 회원 조회 (`member_get`) - 특정 회원 검색
- [ ] 회원 수정 (`member_update`) - 정보 변경
- [ ] 회원 삭제 (`member_delete`) - 회원 제거
- [ ] 파일 저장 (`file_save`) - 메모리 → JSON 파일

---

## 💡 주요 학습 포인트

1. **모듈 구조**: 기능별 파일 분리로 코드 관리 용이
2. **예외 처리**: `try-except`로 안전한 입력 처리
3. **파일 I/O**: `with`문으로 안전한 파일 처리
4. **JSON 활용**: 구조화된 데이터 저장/불러오기
5. **딕셔너리 매핑**: 조건문 대신 깔끔한 함수 호출

---

## 🚀 다음 학습 계획

1. CRUD 나머지 기능 완성
2. 데이터 유효성 검증 추가
3. 에러 처리 강화
4. FastAPI로 REST API 변환 (향후 목표)