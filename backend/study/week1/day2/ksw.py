# name = input('이름를 입력하세요 : ')
# kor_score = int(input('국어 점수를 입력하세요 : '))
# math_score = int(input('수학 점수를 입력하세요 : '))
# eng_score = int(input('영어 점수를 입력하세요 : '))

# def average(*score):
#     tot_score = 0
#     for i in score:
#         tot_score = tot_score+int(i)
#     return tot_score/len(score)

def average(*score):
    return sum(score)/len(score)

# aver = average(kor_score, math_score, eng_score)
# print(f"{name}의 평균점 : {aver}")


def symbol_ck():
    num1 = int(input("첫번째 숫자 : "))
    while True:
        symbol = input("연산자 입력 : ")
        if symbol in ['+', '-', '*', '/']:
            break
        else:
            print('올바른 기호를 입력해주세요.')
    num2 = int(input("두번째 숫자 : "))

    if symbol == '+':
        result = num1 + num2
    elif symbol == '-':
        result = num1 - num2
    elif symbol == '*':
        result = num1 * num2
    elif symbol == '/':
        result = num1 / num2
    
    print(f'{num1} {symbol} {num2} = {result}')

# symbol_ck()

num = int(input('숫자를 입력하세요 : '))

calc = {
    '제곱':lambda i : i**2,
    '세제곱':lambda i : i**3,
    '2배':lambda i : i*2,
}
# print(f'제곱 : {(lambda i : i ** 2)(num)}')
# print(f'세제곱 : {(lambda i : i ** 3)(num)}')
# print(f'2배값 : {num*2}')

def calculate(num, **calc_du):
    for key, val in calc_du.items():
        print(f"{key} : {val(num)}")

calculate(num, **calc)