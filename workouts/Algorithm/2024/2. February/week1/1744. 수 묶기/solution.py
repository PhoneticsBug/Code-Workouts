# arr의 요소들을 묶어서 곱한 값들을 더했을 때 최대값이 되게 한다
# 묶을 때 모든 수를 다 묶을 필요는 없다, 필요에 따라 묶으면 됨

# 조건
# 1. 양수끼리는 묶는게 무조건 이득
# 2. 0이 있는 경우 안묶는게 나음
# 3. 음수끼리는 묶는게 무조건 좋음

# 예외처리해야 하는 항목
# 1. 수열의 홀수/짝수 여부 (홀수인 경우 모든 수가 묶일 수 없음)
# 각 경우에 따라서 
#   1. 양수 수열만 존재하는 경우
#   2. 음수 수열만 존재하는 경우
#   3. 혼합 수열이 존재하는 경우


import sys
input = sys.stdin.readline

n = int(input())
arr = [int(input()) for _ in range(n)]
arr.sort()

answer = sum(arr)

# 배열의 모든 값이 짝을 이루지 않을 경우
if n%2 == 1:
    temp = arr[-1]
    arr = arr[:-1]
    for i in range(0, len(arr)//2, 2):
        temp += arr[i]*arr[i+1]
    answer = max(answer, temp)
else:
    for i in range(0, len(arr)//2, 2):
        temp = 0
        print(temp, arr[i])
        temp += arr[i]*arr[i+1]
    answer = max(answer, temp)

print(answer)

#############################

import sys
input = sys.stdin.readline

n = int(input())
# 양수와 음수로 나눠 처리
plus, minus = [], []
ans = 0
for _ in range(n):
    a = int(input())
    if a > 1:
        plus.append(a)
    elif a <= 0:
        minus.append(a)
    else: # 1은 그냥 더하는게 이득이다
        ans += a

# 단독으로 더해지는 수는 작을 수록 이득임
plus.sort(reverse=True) 
minus.sort()

# 양쪽에 넣는 함수
def solution(arr):
    res = 0
    # 2개씩 체크하면서
    for i in range(0, len(arr), 2):
        # 마지막 배열인 경우엔 그대로 더해주기
        if i+1 >= len(arr):
            res += arr[i]
        # 아닌 경우엔 곱해서 더해주기
        else:
            res += (arr[i]*arr[i+1])
    
    return res

ans = ans + solution(plus) + solution(minus)

print(ans)
