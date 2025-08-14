# ========== 과제 1: 평균 점수 계산 함수 ==========
""" 
def get_score(subject):
  while True:
    user_input = input(f"{subject} 점수를 입력하세요: ")
    if user_input.isdigit(): # 숫자 체크
      return int(user_input)
    else:
      print(" 숫자를 입력해주세요 ")
      

def calc_avg(*scores):
  if len(scores) == 0:
    return 0
  total = sum(scores)
  avg = total / len(scores)
  return len(scores), avg

subject1 = get_score("국어")
subject2 = get_score("수학")
subject3 = get_score("영어")
subject4 = get_score("지구과학")

cnt, avg = calc_avg(subject1, subject2, subject3, subject4)

print(f"총과목수 : {cnt} 개 / 평균점 수 : {avg}")
""" 

# ========== 과제 2: 계산기 함수 (사칙연산 처리) ==========
""" 
def get_number(num):
  while True:
    rnum = input(f"{num} 숫자를 입력하세요").strip()
    if rnum.isdigit():
      return int(rnum)
    else:
      print("숫자를 입력하세요")

def get_operator():
  while True:
    op = input("연산 기호를 입력하세요 (+, -, *, /): ")
    if(op in ['+','-',"*", "/"]):
      return op
    else:
      print("연산기롤 입력하세요 ex: +,-,*,/")
    

def calc(num1, op, num2):
  if op == '+':
    return num1 + num2
  elif op == '-':
    return num1 - num2
  elif op == '*':
    return num1 * num2
  elif op == '/':
    return num1 / num2
  else :
    print(f"연산오류 입니다.")
    
n1 = get_number("1번째")
n2 = get_number("2번째")
op = get_operator()

result_num = calc(n1, op, n2)
print(f"계산결과는 {result_num} 입니다.")
"""

# ========== 과제 3: lambda를 활용한 간단 연산 함수 ==========
""" 
#def get_number():
  #return int(input("숫자를 입력하세요: "))
get_number = lambda: int(input("숫자를 입력하세요: "))
resx1 = lambda x: x ** 2
resx2 = lambda x: x ** 3
resx3 = lambda x: x * 2

num = get_number()
num1 = resx1(num)
num2 = resx2(num)
num3 = resx3(num)

print(f"제곱: {num1}")
print(f"세제곱: {num2}")
print(f"2배값: {num3}")
 """