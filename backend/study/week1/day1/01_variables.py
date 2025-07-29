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

if age >= 20:
    print("성인입니다.")
    print('안녕')
else:
    print("미성년자입니다.")

nm = "김기호"
kind = "돼지띠"
print(f"이름 : {nm}, 띠 : {kind}")

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

sports = ["축구", "야구", "배구"]
print(f"스포츠목록 중 1번 째  : {sports[0]}")
print(f"스포츠목록 중 2번 째  : {sports[1]}")
print(f"스포츠목록 중 3번 째  : {sports[2]}")

sports.append("농구")  # PHP: array_push($sports, "농구");
sports.insert(0, "농구2")  # PHP: array_push($sports, "농구");
sports.extend(["컬링", "수영"]) # 여러 개 끝에 추가
print(f"추가 후 스포츠 목록: {sports}")

# 삭제 메서드들
sports.remove("수영")       # 값으로 삭제 (첫 번째 것만)
deleted = sports.pop()        # 마지막 요소 삭제하고 반환
print(f"삭제 후 반환값: {deleted}")
deleted = sports.pop(0)       # 특정 인덱스 삭제하고 반환
print(f"삭제 후 반환값: {deleted}")
# sports.clear()                # 모든 요소 삭제

print(f"삭제 후 스포츠 목록: {sports}")
          
          
# 기타 유용한 메서드
numbers = [3, 1, 4, 1, 5]
numbers.sort()                # 정렬 [1, 1, 3, 4, 5]
numbers.reverse()             # 역순 [5, 4, 3, 1, 1]
count = numbers.count(1)      # 특정 값의 개수: 2
index = numbers.index(4)      # 특정 값의 인덱스: 1

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
