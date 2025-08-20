회원 관리 시스템 개발 - 학습 정리
📅 학습 기간: 2025년 1월

🎯 프로젝트 개요
Python의 모듈, 파일 입출력, 예외 처리를 활용한 회원 관리 시스템 개발

목표: CRUD 기능을 갖춘 간단한 회원 관리 프로그램
핵심: JSON 파일을 데이터베이스로 활용, 메모리 기반 작업 후 명시적 저장


📋 과제 요구사항
주요 기능 (6가지)

회원가입 - 회원 정보를 메모리에 임시 저장
파일 저장 - 메모리의 모든 회원정보를 JSON 파일로 저장
회원 조회 - 특정 회원 정보 검색 및 출력
전체 목록 - 모든 회원 목록 표시
회원 수정 - 기존 회원 정보 변경
회원 삭제 - 회원 데이터 삭제

기술 요구사항

표준 라이브러리 활용 (datetime, os, json)
타입힌트 작성
예외 처리 구현
함수 분리로 재사용성 향상
JSON 형식으로 구조화된 데이터 관리


📁 프로젝트 구조
ksw/
├── api/
│   ├── __init__.py      # 패키지 초기화
│   ├── menu.py          # 메뉴 시스템
│   ├── crud.py          # CRUD 기능
│   ├── input.py         # 입력 헬퍼 함수
│   └── file.py          # 파일 입출력
├── data/
│   └── members.json     # 회원 데이터 저장
└── main.py              # 메인 실행 파일

🔧 구현된 기능
api/menu.py

menu_pop(): 메뉴 출력
menu_choice(): 사용자 선택 입력 및 유효성 검사

api/input.py

date_input(text: str) -> str: 날짜 입력 및 형식 검증 (YYYY-MM-DD)

api/file.py

load_members(): JSON 파일에서 회원 데이터 로드
save_members(members_data): 회원 데이터를 JSON 파일로 저장

api/crud.py

init_data(): 프로그램 시작시 파일 데이터를 메모리로 로드
member_input(): 회원가입 (이름, 생년월일, 비밀번호, 가입일시)
member_list_get(): 전체 회원 목록 출력
member_get(): 이름으로 특정 회원 조회
member_update(): 회원 정보 수정 (이름/생년월일/비밀번호)
member_delete(): 회원 삭제 (미구현)
file_save(): 메모리 데이터를 파일로 저장

main.py

메뉴 루프 시스템
딕셔너리 매핑으로 함수 호출 관리


💡 핵심 학습 포인트
1. 메모리 vs 파일 저장

작업은 메모리(members_data)에서 수행
명시적 저장 명령시에만 파일 쓰기
프로그램 종료시 미저장 데이터는 소실

2. 모듈 구조화

기능별 파일 분리 (menu, crud, input, file)
global 변수는 파일(모듈) 단위로 관리
import/export를 통한 모듈간 데이터 전달

3. 예외 처리

try-except로 날짜 형식 검증
메뉴 선택 입력값 검증
for-else 구문으로 검색 실패 처리

4. Python 특수 문법

for-else: break 없이 끝나면 else 실행
문자열 곱셈: '*' * 5 → '*****'
enumerate(list, 1): 1부터 시작하는 인덱스
strip(): 문자열 앞뒤 공백 제거

5. 타입힌트

def function() -> int: 반환 타입 명시
def function(param: str): 매개변수 타입 명시


✅ 완료된 작업

 프로젝트 구조 설계
 메뉴 시스템 구현
 날짜 입력 헬퍼 함수
 회원 가입 기능
 전체 목록 조회
 개별 회원 조회
 회원 정보 수정
 파일 입출력 모듈 분리

📝 남은 작업

 회원 삭제 기능
 파일 저장 기능 완성
 종료시 저장 확인
 중복 회원 검증


📊 JSON 데이터 구조
json[
    {
        "name": "김철수",
        "birth_date": "1990-05-15",
        "register_date": "2025-01-22 09:17:05",
        "password": "1234"
    }
]

🚀 다음 학습 계획

회원 삭제 기능 구현
파일 저장 완성 및 변경사항 추적
프로그램 종료시 저장 확인 로직
데이터 유효성 검증 강화
에러 처리 보완