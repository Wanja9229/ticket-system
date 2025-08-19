"""
validators.py - 입력 검증 모듈
사용자가 입력한 데이터가 올바른지 확인하는 함수들을 모아둔 파일입니다.
이름, 날짜, 패스워드 등의 유효성을 검사합니다.
"""

# 필요한 모듈들을 가져옵니다
from datetime import datetime  # 날짜 형식 검증을 위해 사용
from typing import List, Dict  # 타입 힌트를 위한 모듈

# 상수를 가져옵니다
from __init__ import MIN_NAME_LENGTH, MIN_PASSWORD_LENGTH, MAX_AGE, DATE_FORMAT


def validate_date(date_str: str) -> bool:
    """
    날짜 문자열이 올바른 형식(YYYY-MM-DD)인지 검증하는 함수입니다.
    
    매개변수:
        date_str: 검증할 날짜 문자열
    
    반환값: bool - 올바른 형식이면 True, 아니면 False
    
    예시:
        validate_date("2024-08-19") -> True
        validate_date("2024-13-01") -> False (13월은 없음)
        validate_date("24-08-19") -> False (연도가 4자리가 아님)
    """
    try:
        # strptime()은 문자열을 날짜 객체로 변환합니다
        # 형식이 맞지 않거나 유효하지 않은 날짜면 예외가 발생합니다
        datetime.strptime(date_str, DATE_FORMAT)
        return True
    except ValueError:
        # 예외가 발생하면 올바르지 않은 날짜 형식입니다
        return False


def validate_name(name: str, members: List[Dict[str, str]]) -> bool:
    """
    회원 이름이 유효한지 검증하는 함수입니다.
    
    매개변수:
        name: 검증할 이름
        members: 현재 등록된 회원들의 리스트
    
    반환값: bool - 유효하면 True, 아니면 False
    
    검증 조건:
        1. 이름이 비어있으면 안됨
        2. 이름이 2자 이상이어야 함
        3. 이미 등록된 이름이면 안됨
    """
    # strip()으로 앞뒤 공백을 제거한 후 검사
    name = name.strip()
    
    # 조건 1: 이름이 비어있는지 확인
    if not name:
        print("❌ 이름을 입력해주세요.")
        return False
    
    # 조건 2: 이름이 최소 길이 이상인지 확인
    if len(name) < MIN_NAME_LENGTH:
        print(f"❌ 이름은 {MIN_NAME_LENGTH}자 이상이어야 합니다.")
        return False
    
    # 조건 3: 중복된 이름인지 확인
    if is_duplicate_member(name, members):
        print("❌ 이미 등록된 회원입니다.")
        return False
    
    return True


def validate_password(password: str) -> bool:
    """
    패스워드가 유효한지 검증하는 함수입니다.
    
    매개변수:
        password: 검증할 패스워드
    
    반환값: bool - 유효하면 True, 아니면 False
    
    검증 조건:
        1. 패스워드가 비어있으면 안됨
        2. 패스워드가 4자 이상이어야 함
    """
    # 조건 1: 패스워드가 비어있는지 확인
    if not password:
        print("❌ 패스워드를 입력해주세요.")
        return False
    
    # 조건 2: 패스워드가 최소 길이 이상인지 확인
    if len(password) < MIN_PASSWORD_LENGTH:
        print(f"❌ 패스워드는 {MIN_PASSWORD_LENGTH}자 이상이어야 합니다.")
        return False
    
    return True


def is_duplicate_member(name: str, members: List[Dict[str, str]]) -> bool:
    """
    주어진 이름이 이미 등록된 회원인지 확인하는 함수입니다.
    
    매개변수:
        name: 확인할 이름
        members: 현재 등록된 회원들의 리스트
    
    반환값: bool - 중복이면 True, 아니면 False
    """
    # for 반복문으로 모든 회원을 순회하면서 확인
    for member in members:
        # 대소문자를 구분하여 정확히 일치하는지 확인
        if member['name'] == name:
            return True
    
    # 중복된 이름을 찾지 못하면 False 반환
    return False


def validate_birth_date(birth_date_str: str) -> bool:
    """
    생년월일이 유효한지 추가로 검증하는 함수입니다.
    날짜 형식뿐만 아니라 논리적으로도 타당한지 확인합니다.
    
    매개변수:
        birth_date_str: 검증할 생년월일 문자열
    
    반환값: bool - 유효하면 True, 아니면 False
    """
    # 먼저 날짜 형식이 올바른지 확인
    if not validate_date(birth_date_str):
        print("❌ 올바른 날짜 형식이 아닙니다. (YYYY-MM-DD)")
        return False
    
    try:
        # 문자열을 날짜 객체로 변환
        birth_date = datetime.strptime(birth_date_str, DATE_FORMAT)
        current_date = datetime.now()
        
        # 미래 날짜인지 확인
        if birth_date > current_date:
            print("❌ 생년월일은 미래 날짜일 수 없습니다.")
            return False
        
        # 나이가 너무 많은지 확인
        age = current_date.year - birth_date.year
        if age > MAX_AGE:
            print(f"❌ 유효하지 않은 생년월일입니다. (최대 {MAX_AGE}세)")
            return False
        
        return True
        
    except ValueError:
        return False


def validate_filename(filename: str) -> bool:
    """
    파일명이 유효한지 검증하는 함수입니다.
    
    매개변수:
        filename: 검증할 파일명
    
    반환값: bool - 유효하면 True, 아니면 False
    """
    # 파일명이 비어있는지 확인
    if not filename.strip():
        print("❌ 파일명을 입력해주세요.")
        return False
    
    # 파일명에 사용할 수 없는 문자가 있는지 확인
    # Windows에서 파일명에 사용할 수 없는 문자들
    invalid_chars = ['<', '>', ':', '"', '/', '\\', '|', '?', '*']
    for char in invalid_chars:
        if char in filename:
            print(f"❌ 파일명에 사용할 수 없는 문자가 포함되어 있습니다: {char}")
            return False
    
    # .json 확장자가 없으면 자동으로 추가될 것임을 알려줌
    if not filename.endswith('.json'):
        print("💡 .json 확장자가 자동으로 추가됩니다.")
    
    return True