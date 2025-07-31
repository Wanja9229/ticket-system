nm = "김기호"
loc = "대구"
birth = "1990-01-01"

print(f"안녕하세요. {nm}입니다. {loc}에 살고 있구요. 내 생일은 {birth}입니다.")

number = 10
pi = 3.14
is_ok = True # False
fruits = ["apple", "banana"]
info = {"name" : "김기호", "loc" : "대구", "birth" : "1990-01-01"} # Dictionary

print(f"info: {info['name']}")

if loc != "대구":
    print("대구가 아니다")
elif loc == "대구":
    print("대구다")
else:
    print("else 결과")

#for($i = 2; $i <= 9; $i = $i + 1)
# 시작점, 끝지점, 증감값
for i in range(2, 9):
    print(f"{i}단")
    for j in range(1, 10):
        print(f"{i} * {j} = { i * j }")


dan1 = [2, 3, 4, 5, 6, 7, 8, 9]
dan2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f"===for문 구구단===")
for i in dan1:
    print(f"{i}단")
    for j in dan2:
        print(f"{i} * {j} = { i * j }")

print(f"===while문 구구단===")
i = 0
while i <= 9:
    print(f"{i}단")
    j = 1
    while j <= 9:
        print(f"{i} * {j} = { i * j }")
        j += 1 
    i += 1




######################################################################
# 변수
name = ""
age = 30

# 출력
print("Hello", name)

# 주석
# 이것은 주석입니다

# 자료형
number = 10          # int
pi = 3.14            # float
is_ok = True         # bool
fruits = ["apple", "banana"]  # list
info = {"name": "Tom"}        # dict

# 조건문
if age >= 18:
    print("성인입니다.")
elif age >= 13:
    print("청소년입니다.")
else:
    print("어린이입니다.")

# 반복문
for i in range(3):
    print("반복", i)

count = 0
while count < 3:
    print("while 반복", count)
    count += 1
