print("Hello, Python!")

name = "홍길동"
age = 30

print(f"이름이오:{name}, 나이는 {age}세라오.")


#주석이랍니다

'''주석입니다'''

"""주석이라구요"""

text = "안녕하십니까"
num = 2025
float_num = 3.14
is_act = True
noting = None

print(f"타입 확인: {type(text)}, {type(num)}, {type(is_act)}")

array = ["사과", "바나나", "오렌지"]

print(f"과일목록 {array}")
print(f"첫번쨰과일 {array[0]}")

print(f"룰루랄라 과일이다 {array[2]}")


array.append("거봉")
array.insert(0, "딸기")
array.extend(["복숭아"])


if age > 20:
    print("hi~")
elif age == 20:
    print("hello~")
else:
    print("bye~")


status = "성인" if age >= 18 else "미성년자"






