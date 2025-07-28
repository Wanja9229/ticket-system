"""
Week 1 - Day 1: 제어문 (조건문과 반복문)

PHP와 Python의 제어문 비교
"""

print("=== 1. if 조건문 ===")
# PHP:
# $age = 20;
# if ($age >= 18) {
#     echo "성인입니다";
# } else {
#     echo "미성년자입니다";
# }

age = 20
if age >= 18:
    print("성인입니다")
else:
    print("미성년자입니다")

print("\n=== 2. elif (PHP의 elseif) ===")
score = 85

if score >= 90:
    grade = "A"
elif score >= 80:  # PHP: elseif
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "F"

print(f"점수: {score}, 등급: {grade}")

print("\n=== 3. 삼항 연산자 ===")
# PHP: $status = $age >= 18 ? "성인" : "미성년자";
status = "성인" if age >= 18 else "미성년자"
print(f"상태: {status}")

print("\n=== 4. for 반복문 - 범위 ===")
# PHP:
# for ($i = 0; $i < 5; $i++) {
#     echo $i;
# }

print("0부터 4까지:")
for i in range(5):  # 0, 1, 2, 3, 4
    print(i, end=" ")
print()

print("1부터 5까지:")
for i in range(1, 6):  # 1, 2, 3, 4, 5
    print(i, end=" ")
print()

print("\n=== 5. for 반복문 - 리스트 ===")
# PHP:
# $fruits = ["사과", "바나나", "오렌지"];
# foreach ($fruits as $fruit) {
#     echo $fruit;
# }

fruits = ["사과", "바나나", "오렌지"]
print("과일 목록:")
for fruit in fruits:
    print(f"- {fruit}")

print("\n=== 6. 인덱스와 함께 반복 ===")
# PHP:
# foreach ($fruits as $index => $fruit) {
#     echo $index . ": " . $fruit;
# }

print("인덱스와 함께:")
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")

print("\n=== 7. 딕셔너리 반복 ===")
# PHP:
# $user = ["name" => "김철수", "age" => 25, "city" => "서울"];
# foreach ($user as $key => $value) {
#     echo $key . ": " . $value;
# }

user = {"name": "김철수", "age": 25, "city": "서울"}

print("키만 출력:")
for key in user:
    print(key)

print("\n키와 값 함께:")
for key, value in user.items():
    print(f"{key}: {value}")

print("\n=== 8. while 반복문 ===")
# PHP:
# $count = 0;
# while ($count < 3) {
#     echo $count;
#     $count++;
# }

count = 0
print("while 반복:")
while count < 3:
    print(count, end=" ")
    count += 1  # Python에는 ++ 연산자가 없음!
print()

print("\n=== 9. break와 continue ===")
print("break 예제 (5에서 중단):")
for i in range(10):
    if i == 5:
        break
    print(i, end=" ")
print()

print("\ncontinue 예제 (짝수만 출력):")
for i in range(10):
    if i % 2 == 1:  # 홀수면 건너뛰기
        continue
    print(i, end=" ")
print()

print("\n=== 10. List Comprehension (Python 특징) ===")
# PHP에는 없는 Python만의 강력한 기능!

# 기존 방식
squares = []
for i in range(5):
    squares.append(i ** 2)
print(f"제곱수 (기존): {squares}")

# List Comprehension
squares = [i ** 2 for i in range(5)]
print(f"제곱수 (간단): {squares}")

# 조건 포함
evens = [i for i in range(10) if i % 2 == 0]
print(f"짝수만: {evens}")

print("\n=== 주요 차이점 정리 ===")
print("""
PHP vs Python 제어문:
1. 중괄호 {} 대신 콜론(:)과 들여쓰기
2. elseif -> elif
3. foreach -> for ... in
4. ++ 연산자 없음 (+=1 사용)
5. range() 함수로 숫자 범위 생성
6. enumerate()로 인덱스와 값 동시 접근
7. List Comprehension으로 간결한 리스트 생성
""")
