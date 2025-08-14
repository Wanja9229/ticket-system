# 리스트 메서드
# Python - 더 간단!
# arr = [1, 2, 3]
# arr.append(4)      # 끝에 추가
# arr.insert(2, 3)   # 위치 지정 삽입
# arr.remove(2)      # 값으로 삭제
# arr.sort()         # 정렬

nums = [4,5,7,8]
for i in range(3, 0, -1):
    nums.insert(0, i)
nums.append(9)
# print(nums)

evenNums = []
for i in nums:
    if i%2 == 0:
        evenNums.append(i)
# print(evenNums)

def is_even(i):
    return i%2 == 0
    
result = filter(is_even, nums);
evenNums = list(result)
# print(evenNums)

evenNums = list(filter(lambda x: x%2 == 0, nums))
# print(evenNums)

reverse_nums = list(reversed(nums))
# print(reverse_nums)

reverse_nums = [i for i in nums[::-1]]
# print(reverse_nums)

reverse_nums = [i for i in reversed(nums)]
# print(reverse_nums)

def plus_nums(i):
    return i + 10
plus_nums = list(map(plus_nums, nums))
# print(plus_nums)

plus_nums = list(map(lambda i : i+10, nums))
# print(plus_nums)

plus_nums = [i+10 for i in nums]
# print(plus_nums)

nums = [4,5,7,8]
numsExtra = [1,2,3]
nums = numsExtra+nums
# print(nums)

nums = [4,5,7,8]
for i in reversed(range(1, 4)):
    nums.insert(0, i)
# print(nums)

nums = [4,5,7,8]
numsExtra = [1,2,3,4,5,7,8]
nums1 = numsExtra[0:3]
nums = nums1+nums
# print(nums)

nums = [4,5,7,8]
nums.remove(4)
# print(nums)
# fruits = ['apple', 'banana', 'apple', 'orange']
# fruits.remove('apple')  # 첫 번째 'apple' 삭제
# print(fruits)  # ['banana', 'apple', 'orange']

nums = [4,5,7,8]
last = nums.pop(0)
# print(last)
# print(nums)

nums = [4,5,7,8]
numsExtra = [1,2,3]
nums = nums+numsExtra
# print(nums)
nums.sort(reverse=True)
# print(nums)
nums.sort()
# print(nums)

# 딕셔너리 메서드
user = {'name': 'John', 'age': 30, 'city': 'Seoul'}
# print(user.keys())
# print(user.values())
# print(user.get('name'))