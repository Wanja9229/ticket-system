nums = [4,5,7,8]

# 주어진 배열에서 4 앞에 1,2,3 의 값 추가하기(ex [1,2,3,4,5,7,8])
nums.insert(0,1)
nums.insert(1,2)
nums.insert(2,3)

# 주어진 배열에서 8뒤에 9 값 추가하기 (ex [1,2,3,4,5,7,8,9])
nums.append(9)
nums.insert(5,6)
print(f"{nums}")

# 주어진 배열에서 짝수만 추출 후 출력 - 컴프리헨션으로 안하기

# 이렇게 하면 v 에 배열 value 도출
for v in nums:
  if v % 2 == 0 :
    print(f"짝수1 === {v}")

# 이렇게 하면 k 에 배열 index 값 도출
for k in range(len(nums)):
  if nums[k] % 2 == 0 :
    print(f"짝수2 === {nums[k]}")

# 컴프리헨션 사용해서 짝수 출력
evens = [x for x in nums if x % 2 == 0]
print(evens)
for i in evens :
  print(f"{i}")
  
# 컴프리헨션 filter 활용해서 홀수만 출력
evens = list(filter(lambda x : x % 2 != 0, nums))
print(evens)

# 컴프리헨션으로 숫자 역정렬 출력
# evens.sort(reverse=True)
print([x for x in sorted(nums, reverse=True)])
rev_int = [x for x in sorted(nums, reverse=True)]
print(rev_int)

# 주어진 배열에서 map() 내장함수 활용해서 모든 숫자 +10 해서 출력하기
plus10 = list(map(lambda x : x + 10, nums))
print(plus10)

students = {
    "철수": 87,
    "영희": 92,
    "민수": 49,
    "지민": 73,
    "수지": 65,
    "정우": 91,
    "하늘": 58,
    "민지": 100,
    "도윤": 77,
    "예린": 84
}
# enumerate 로 for문 작성 
# 등급별 표시 (이름 : 점수(등급) ) EX: 철수:87점(B)
# 그냥 출력


# 등급 함수정의
def get_score(score):
  if score >= 90 : 
    return "A"
  elif score >= 80 : 
    return "B"
  elif score >= 80 : 
    return "C"
  elif score >= 80 : 
    return "D"
  elif score >= 70 : 
    return "F"
  else :
    return "F"

# 그냥 출력
print("=======그냥 출력")
for i, (name, score) in enumerate(students.items(), 1):
  grade = get_score(score)  
  print(f"{name} : {score}({grade})")
  
# 점수순 출력
print("=======점수순 출력")
"""
sorted(students.items(), key=lambda x: x[1], reverse=True)
iterable: 정렬할 대상 (리스트, 튜플, 딕셔너리 등)
key: 정렬 기준을 정하는 함수 (예: key=lambda x: x[1] → 두 번째 값 기준)
reverse: True이면 내림차순, False이면 오름차순 (기본값: False)
"""
for i, (name, score) in enumerate(sorted(students.items(), key=lambda x : x[1], reverse=True), 1):
  grade = get_score(score)
  print(f"{name} : {score}({grade})")

# 이름 가나다순 출력
print("=======이름 가나다순 출력")
for i, (name, score) in enumerate(sorted(students.items()), 1):
  grade = get_score(score)
  print(f"{name} : {score}({grade})")
