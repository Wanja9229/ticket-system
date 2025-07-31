"""
Week 1 - Day 1: 함수 정의와 사용

PHP와 Python의 함수 비교
"""

print("=== 1. 기본 함수 ===")
# PHP:
# function greet($name) {
#     return "안녕하세요, " . $name . "님!";
# }

def greet(name):
    return f"안녕하세요, {name}님!"

# 함수 호출
message = greet("김철수")
print(message)

print("\n=== 2. 기본값이 있는 함수 ===")
# PHP:
# function create_user($name, $age = 20) {
#     return array("name" => $name, "age" => $age);
# }

def create_user(name, age=20):
    return {"name": name, "age": age}

print(create_user("홍길동"))  # age는 기본값 20
print(create_user("김영희", 25))  # age는 25

print("\n=== 3. 여러 값 반환 ===")
# PHP에서는 배열로 반환
# function get_min_max($numbers) {
#     return array(min($numbers), max($numbers));
# }

def get_min_max(numbers):
    return min(numbers), max(numbers)  # 튜플로 반환

numbers = [5, 2, 8, 1, 9]
min_val, max_val = get_min_max(numbers)  # 언패킹
print(f"최소값: {min_val}, 최대값: {max_val}")

print("\n=== 4. 가변 인자 (*args) ===")
# PHP:
# function sum_all(...$numbers) {
#     return array_sum($numbers);
# }

def sum_all(*numbers):
    return sum(numbers)

print(f"합계: {sum_all(1, 2, 3, 4, 5)}")
print(f"합계: {sum_all(10, 20, 30)}")

print("\n=== 5. 키워드 인자 (**kwargs) ===")
# PHP에는 직접적인 대응이 없음
def create_profile(**info):
    return info

profile = create_profile(name="박지민", age=28, city="서울")
print(f"프로필: {profile}")

print("\n=== 6. 람다 함수 (익명 함수) ===")
# PHP:
# $double = function($x) { return $x * 2; };
# 또는 화살표 함수: $double = fn($x) => $x * 2;

double = lambda x: x * 2
print(f"10의 두 배: {double(10)}")

# 리스트에 적용
numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))
print(f"전체 두 배: {doubled}")

print("\n=== 7. 함수 내부 함수 ===")
def calculate(operation):
    def add(a, b):
        return a + b
    
    def multiply(a, b):
        return a * b
    
    if operation == "add":
        return add
    else:
        return multiply

# 함수를 반환받아 사용
add_func = calculate("add")
result = add_func(5, 3)
print(f"5 + 3 = {result}")

print("\n=== 8. 문서화 (Docstring) ===")
def calculate_area(width, height):
    """
    사각형의 넓이를 계산합니다.
    
    Args:
        width: 가로 길이
        height: 세로 길이
    
    Returns:
        넓이 값
    """
    return width * height

# 함수 설명 보기
print(calculate_area.__doc__)

print("\n=== 주요 차이점 정리 ===")
print("""
PHP vs Python 함수:
1. function 키워드 없음, def 사용
2. 중괄호 {} 대신 콜론(:)과 들여쓰기
3. return 생략 시 None 반환 (PHP는 NULL)
4. 여러 값 반환 가능 (튜플)
5. *args, **kwargs로 유연한 인자 처리
6. 람다 함수 문법: lambda x: x * 2
""")
