names = ["철수", "영희", "민수"]
scores = [7, 52, 10]

extra_names = ["민수", "영희", "철수", "지은", "수진", "민호", "예린", "도윤", "하늘", "지민"]
extra_scores = [10, 84, 30, 27, 98, 73, 15, 59, 78, 98]

# for i, val in enumerate(extra_names):
#     names.append(val)
#     scores.append(extra_scores[i])

# names.extend(extra_names)
# scores.extend(extra_scores)

names = extra_names+names
scores = extra_scores+scores

print(names)
for name, score in zip(names, scores):
    if score >= 90:
        print(f"{name} : {score} (A)")
    elif score >= 80:
        print(f"{name} : {score} (B)")
    elif score >= 70:
        print(f"{name} : {score} (C)")
    elif score >= 60:
        print(f"{name} : {score} (D)")
    else:
        print(f"{name} : {score} (F)")

grade = dict(zip(names, scores))
for i, item in enumerate(grade.items(), start=1):
    rank = ''
    if item[1] >= 90:
        rank = 'A'
    elif item[1] >= 80:
        rank = 'B'
    elif item[1] >= 70:
        rank = 'C'
    elif item[1] >= 60:
        rank = 'D'
    else:
        rank = 'F'

    print(f"{i}. {item[0]} : {item[1]}({rank})")