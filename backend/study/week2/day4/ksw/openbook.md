# 회원 관리 시스템 - 개발 가이드

## 📋 프로젝트 개요
Python의 모듈, 파일 입출력, 예외 처리를 활용한 CRUD 기능을 갖춘 회원 관리 시스템

## 📝 모듈별 함수 구조

### **main.py**
```python
def main():
    # 메뉴 딕셔너리 매핑
    # 무한 루프
    # 메뉴 출력 및 선택
    # 조건별 처리 (0, 7, 나머지)
```

### **menu.py**
```python
def menu_pop():
    # 7개 메뉴 출력

def menu_choice() -> int:
    # try-except 입력 처리
    # 범위 검증
    # 에러시 0 반환
```

### **input.py**
```python
def date_input(text: str) -> str:
    # 날짜 형식 검증 루프
    # strptime() 활용
```

### **file.py**
```python
def file_open() -> list[dict[str, str]]:
    # 파일 존재 확인
    # JSON 로드 또는 빈 리스트

def file_save(data: list[dict[str, str]]) -> bool:
    # 폴더 생성
    # JSON 저장
    # 성공/실패 반환
```

### **crud.py**
```python
# 전역변수 초기화

def member_input():
    # 회원 정보 입력
    # 현재 시간 추가
    # 딕셔너리 생성 및 추가

def member_list_get():
    # enumerate로 목록 출력

def member_get():
    # 이름 입력
    # for-else로 검색
    # 정보 출력 또는 없음 메시지

def member_update():
    # 이름 입력
    # for-else로 검색
    # 수정 항목 선택
    # 항목별 수정 처리

def member_delete():
    # 이름 입력
    # for-else로 검색
    # 삭제 확인
    # 삭제 처리 또는 취소

def member_save():
    # 현재/기존 데이터 비교
    # 저장 확인
    # 파일 저장 호출
```

## 🎯 핵심 패턴

### **파일 I/O**
```python
# JSON 읽기
with open('data/members.json', 'r', encoding='utf-8') as f:
    return json.load(f)

# JSON 쓰기  
with open('data/members.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
```

### **JSON 데이터 구조**
```json
[
    {
        "name": "이름",
        "birth_date": "YYYY-MM-DD",
        "password": "비밀번호",
        "register_date": "YYYY-MM-DD HH:MM:SS"
    }
]
```