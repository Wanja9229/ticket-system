"""
Week 1 - Day 2: 모듈과 패키지

PHP의 include/require와 Python의 import 시스템
"""

# Python의 모듈 시스템은 PHP의 include/require보다 더 체계적입니다

print("=== 1. 기본 import ===")
# PHP: require_once 'math_functions.php';
# Python: 
import math
import random
import datetime

# 사용
print(f"원주율: {math.pi}")
print(f"랜덤 숫자: {random.randint(1, 10)}")
print(f"현재 시간: {datetime.datetime.now()}")

print("\n=== 2. from import ===")
# 특정 함수/클래스만 가져오기
from math import sqrt, ceil, floor
from datetime import datetime, timedelta

print(f"제곱근: {sqrt(16)}")
print(f"올림: {ceil(4.3)}")
print(f"내림: {floor(4.7)}")
print(f"일주일 후: {datetime.now() + timedelta(days=7)}")

print("\n=== 3. 별칭(alias) 사용 ===")
# PHP에는 없는 기능
import datetime as dt
from math import pi as PI

now = dt.datetime.now()
print(f"현재: {now}")
print(f"PI 값: {PI}")

print("\n=== 4. 모듈 만들기 ===")
# my_module.py 파일 내용 (예시)
"""
# my_module.py
def greet(name):
    return f"안녕하세요, {name}님!"

def calculate(a, b):
    return {
        "sum": a + b,
        "diff": a - b,
        "mult": a * b,
        "div": a / b if b != 0 else None
    }

PI = 3.14159
"""

# 실제로는 별도 파일로 만들어야 하지만, 여기서는 설명만
print("모듈 파일 구조:")
print("my_module.py <- 이 파일을 만들고")
print("import my_module <- 이렇게 사용")

print("\n=== 5. 패키지 구조 ===")
# PHP의 namespace와 유사하지만 더 체계적
print("""
패키지 구조 예시:
myproject/
    __init__.py      # 패키지 초기화 파일
    models/
        __init__.py
        user.py      # User 클래스
        product.py   # Product 클래스
    utils/
        __init__.py
        helpers.py   # 도우미 함수들
        validators.py # 검증 함수들
""")

# 사용 예시
# from myproject.models.user import User
# from myproject.utils.helpers import format_date

print("\n=== 6. 내장 모듈 활용 예시 ===")
# os 모듈 - 운영체제 관련
import os
print(f"현재 디렉토리: {os.getcwd()}")
# print(f"환경변수 PATH: {os.environ.get('PATH')}")

# sys 모듈 - 시스템 관련
import sys
print(f"Python 버전: {sys.version.split()[0]}")
print(f"플랫폼: {sys.platform}")

# json 모듈 - JSON 처리
import json
data = {"name": "김철수", "age": 25}
json_str = json.dumps(data, ensure_ascii=False)
print(f"JSON 문자열: {json_str}")

# re 모듈 - 정규표현식
import re
email = "test@example.com"
if re.match(r"[^@]+@[^@]+\.[^@]+", email):
    print(f"{email}은 유효한 이메일입니다")

print("\n=== 7. 서드파티 패키지 설치 ===")
print("""
PHP의 Composer와 유사한 pip 사용:

# 설치
pip install requests
pip install fastapi

# requirements.txt 파일 생성
pip freeze > requirements.txt

# requirements.txt로 일괄 설치
pip install -r requirements.txt
""")

print("\n=== 8. __name__ == '__main__' 패턴 ===")
# PHP에는 없는 Python 특유의 패턴
def main():
    print("이 모듈이 직접 실행될 때만 동작")

# 이 파일이 직접 실행될 때만 main() 호출
# import될 때는 실행되지 않음
if __name__ == "__main__":
    main()

print("\n=== 주요 차이점 정리 ===")
print("""
PHP vs Python 모듈 시스템:
1. include/require -> import
2. include_once/require_once -> import (자동으로 한 번만)
3. 파일 경로 대신 모듈명 사용
4. namespace -> 패키지 (폴더 구조)
5. use -> from ... import
6. Composer -> pip
7. composer.json -> requirements.txt
8. autoload -> 자동 (import 시)
""")

# 실습을 위한 간단한 모듈 예시
print("\n=== 실습: 간단한 계산기 모듈 ===")

# calculator.py 라는 파일을 만들고 아래 내용 저장
calculator_code = '''
# calculator.py
"""간단한 계산기 모듈"""

def add(a, b):
    """두 수를 더합니다"""
    return a + b

def subtract(a, b):
    """두 수를 뺍니다"""
    return a - b

def multiply(a, b):
    """두 수를 곱합니다"""
    return a * b

def divide(a, b):
    """두 수를 나눕니다"""
    if b == 0:
        raise ValueError("0으로 나눌 수 없습니다")
    return a / b

class Calculator:
    """계산기 클래스"""
    
    def __init__(self):
        self.result = 0
    
    def add(self, value):
        self.result += value
        return self
    
    def subtract(self, value):
        self.result -= value
        return self
    
    def get_result(self):
        return self.result
    
    def reset(self):
        self.result = 0
        return self
'''

print("calculator.py 파일 내용:")
print(calculator_code)

print("\n사용 예시:")
print("""
# 다른 파일에서
import calculator

# 함수 사용
result = calculator.add(5, 3)

# 또는
from calculator import Calculator

# 클래스 사용
calc = Calculator()
calc.add(10).subtract(3).add(5)
print(calc.get_result())  # 12
""")
