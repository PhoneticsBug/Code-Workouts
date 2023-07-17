from collections import defaultdict 

n = int(input())
input()
students = map(int, input().split())
candidates = defaultdict(lambda: 0) # 기본값을 0으로 하는 딕셔너리 생성

for student in students:
    if len(candidates) == n and student not in candidates.keys(): # 후보 수가 가득 차있고, 새로운 학생이라면
        key = list(candidates.keys()) 
        val = list(candidates.values())
        temp = val.index(min(val))
        del(candidates[key[temp]]) # 가장 적은 경우를 제거
    candidates[student] += 1

print(*sorted(candidates.keys())) 