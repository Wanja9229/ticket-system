# print("Hello, Python!")

# name = "홍길동"
# age = 30

# print(f"이름이오:{name}, 나이는 {age}세라오.")


# #주석이랍니다

# '''주석입니다'''

# """주석이라구요"""

# text = "안녕하십니까"
# num = 2025
# float_num = 3.14
# is_act = True
# noting = None

# print(f"타입 확인: {type(text)}, {type(num)}, {type(is_act)}")

# array = ["사과", "바나나", "오렌지"]

# print(f"과일목록 {array}")
# print(f"첫번쨰과일 {array[0]}")

# print(f"룰루랄라 과일이다 {array[2]}")


# array.append("거봉")
# array.insert(0, "딸기")
# array.extend(["복숭아"])


# if age > 20:
#     print("hi~")
# elif age == 20:
#     print("hello~")
# else:
#     print("bye~")


# status = "성인" if age >= 18 else "미성년자"


for dan in range(1, 10):
	print(f"{dan}단 입니다.")
	for num in range(1, 10):
		result = dan * num
		print(f"{dan} x {num} = {result}")


for dan2 in range(2, 10, 2):
	print(f"{dan2}단 입니다.")
	for num2 in range(2,10,2):
		result2 = dan2 * num2
		print(f"{dan2} x {num2} = {result2}")
		

test_dic = {"name":"shinmingee", "age":"32", "loc":"seoul"}

for key, value in test_dic.items():
	print(f"{key} : {value}")

students = {
    "철수": 87,
    "영희": 92,
    "민수": 49
}

grade = ""
for key, value in students.items():
	if value > 90:
		grade = "A등급"
	elif value > 80:
		grade = "B등급"
	elif value > 70:
		grade = "C등급"
	elif value > 60:
		grade = "D등급"
	else:
		grade = "F등급"
		
	print(f"{key} -> {grade}")






