"""
__init__.py - 프로젝트 전역 상수 정의
회원 관리 시스템에서 사용하는 상수들을 한 곳에서 관리합니다.
"""

# 파일 관련 상수
DEFAULT_FILENAME = "members.json"  # 기본 회원 정보 저장 파일명

# 검증 관련 상수
MIN_NAME_LENGTH = 2  # 이름 최소 길이
MIN_PASSWORD_LENGTH = 4  # 패스워드 최소 길이
MAX_AGE = 150  # 최대 나이

# 날짜 형식 상수
DATE_FORMAT = "%Y-%m-%d"  # 날짜 형식 (YYYY-MM-DD)
DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"  # 날짜시간 형식

# 메시지 관련 상수
WELCOME_MESSAGE = "🎉 회원 관리 시스템에 오신 것을 환영합니다!"
EXIT_MESSAGE = "👋 회원 관리 시스템을 종료합니다. 감사합니다!"

# 테이블 출력 관련 상수
TABLE_WIDTH = 55  # 회원 목록 테이블 너비
COLUMN_WIDTHS = {
    "number": 5,
    "name": 10,
    "birth_date": 12,
    "register_date": 20
}