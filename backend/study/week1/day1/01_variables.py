"""
Week 1 - Day 1: Python vs PHP 변수와 자료형

PHP 개발자를 위한 Python 변수 이해하기
"""

print("=== 1. 변수 선언 ===")
# PHP: $name = "홍길동";
# Python: $ 기호 없음!
name = "홍길동"
age = 30
print(f"이름: {name}, 나이: {age}")

print("\n=== 2. 자료형 ===")
# 문자열
text = "Python 문자열"  # PHP: $text = "PHP 문자열";
number = 42          # PHP: $number = 42;
floating = 3.14      # PHP: $floating = 3.14;
is_active = True     # PHP: $is_active = true; (소문자)
nothing = None       # PHP: $nothing = null; (소문자)

print(f"타입 확인: {type(text)}, {type(number)}, {type(is_active)}")

print("\n=== 3. 리스트 (PHP 배열) ===")
# PHP: $fruits = array("사과", "바나나", "오렌지");
# 또는: $fruits = ["사과", "바나나", "오렌지"];
fruits = ["사과", "바나나", "오렌지"]
print(f"과일 목록: {fruits}")
print(f"첫 번째 과일: {fruits[0]}")  # PHP: $fruits[0]

# 리스트에 추가
fruits.append("포도")  # PHP: array_push($fruits, "포도");
print(f"추가 후: {fruits}")

print("\n=== 4. 딕셔너리 (PHP 연관배열) ===")
# PHP: $user = array("name" => "김철수", "age" => 25);
# 또는: $user = ["name" => "김철수", "age" => 25];
user = {"name": "김철수", "age": 25}
print(f"사용자: {user}")
print(f"이름: {user['name']}")  # PHP: $user['name']

# 값 추가/수정
user["email"] = "kim@example.com"  # PHP: $user["email"] = "kim@example.com";
print(f"이메일 추가 후: {user}")

print("\n=== 5. 문자열 처리 ===")
# PHP: $greeting = "안녕, " . $name . "님!";
# Python: 여러 방법 가능
greeting1 = "안녕, " + name + "님!"  # 문자열 연결
greeting2 = f"안녕, {name}님!"      # f-string (권장!)
greeting3 = "안녕, {}님!".format(name)  # format 메서드

print(greeting1)
print(greeting2)
print(greeting3)

print("\n=== 6. 형변환 ===")
# PHP: $str_num = "123"; $int_num = (int)$str_num;
str_num = "123"
int_num = int(str_num)  # PHP: (int)$str_num
float_num = float(str_num)  # PHP: (float)$str_num
str_again = str(int_num)  # PHP: (string)$int_num

print(f"문자열 -> 정수: {int_num}, 타입: {type(int_num)}")

print("\n=== 7. 주요 차이점 정리 ===")
print("""
PHP vs Python:
1. 변수: $var (PHP) -> var (Python)
2. True/False/None: 첫 글자 대문자!
3. 배열 -> 리스트: array() -> []
4. 연관배열 -> 딕셔너리: array("a"=>1) -> {"a": 1}
5. 문자열 연결: . (PHP) -> + 또는 f-string (Python)
6. null -> None
7. 세미콜론(;) 불필요!
""")
