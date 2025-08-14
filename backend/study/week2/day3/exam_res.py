# ========== 과제 1: 평균 점수 계산 함수 ==========
'''
평균 점수 계산 함수
input()으로 국어, 수학, 영어 점수를 각각 입력받아
세 과목의 평균을 계산해 출력하는 함수를 작성하세요.
# 예시
국어 점수를 입력하세요: 90
수학 점수를 입력하세요: 80
영어 점수를 입력하세요: 70
평균 점수: 80.0
'''

def get_score(subject):
  while True:
    num = input(f"{subject}의 점수를 입력하세요: ")
    if num.isdigit():
      return int(num)
    else:
      print("숫자가 아닙니다. 다시 입력하세요");

def calc(*scores):
  if len(scores) == 0:
    return 0
  avg = sum(scores) / len(scores)
  return round(avg,1)

sub1 = get_score("국어")
sub2 = get_score("수학")
sub3 = get_score("영어")

res_num = calc(sub1, sub2, sub3)
print(f"평균 점수: {res_num}")

# ========== 과제 2: 계산기 함수 (사칙연산 처리) ==========
'''
계산기 함수 (사칙연산 처리)
input()으로 첫 번째 숫자, 연산 기호(+, -, *, /), 두 번째 숫자를 차례대로 입력받아
해당 연산 결과를 반환하고 출력하는 함수를 작성하세요.
#예시
첫 번째 숫자를 입력하세요: 10
연산 기호를 입력하세요 (+, -, *, /): *
두 번째 숫자를 입력하세요: 5
결과: 50
'''

def get_number(ord):
  while True:
    num = input(f"{ord} 숫자를 입력하세요: ")
    if num.isdigit():
      return int(num);
    else:
      print("숫자를 다시 입력하세요")
      
def get_op():
  while True:
    op = input("연산 기호를 입력하세요 (+, -, *, /): ")
    if op in ['+','-','*','/']:
      return op
    else:
      print("연산기롤 다시 입력하세요. (+, -, *, /)")
      
def calc(num1, op, num2):
  if op == "+":
    return num1 + num2
  elif op == "-":
    return num1 - num2
  elif op == "*":
    return num1 * num2
  elif op == "/":
    return num1 / num2
  
n1 = get_number("첫 번째")
n2 = get_number("두 번째")
op = get_op()

res = calc(n1, op, n2)
print(f"결과: {res}")


# ========== 과제 3: lambda를 활용한 간단 연산 함수 ==========
'''
lambda를 활용한 간단 연산 함수
input()으로 숫자 하나를 입력받아,
람다 함수를 이용해 제곱, 세제곱, 2배값을 계산해 각각 출력하는 프로그램을 작성하세요.
#예시
숫자를 입력하세요: 4
제곱: 16
세제곱: 64
2배값: 8
'''

get_number = lambda: int(input("숫자를 입력하세요: "))
r1 = lambda x: x ** 2
r2 = lambda x: x ** 3
r3 = lambda x: x * 2

def calc():
  num = get_number()
  n1 = r1(num)
  n2 = r2(num)
  n3 = r3(num)
  print(f"제곱: {n1:,}")
  print(f"세제곱: {n2:,}")
  print(f"2배값: {n3:,}")
  
calc()
