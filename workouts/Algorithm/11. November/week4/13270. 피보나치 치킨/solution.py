import sys
input = sys.stdin.readline

n = int(input())
ans = []
# fib 배열을 만든 후 n으로 정확히 나누어지는 값을 따로 모아 최소값과 최대값 출력
# 피보나치 수열 = 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987

# n보다 작은 수로 피보나치 수열 만들기
dp = [1, 1]
while True:
    if dp[-1] > n:
        break
    dp.append(dp[-1]+dp[-2])

# n의 약수 안에서 찾는 방법
divisor = [[i, n//i] for i in range(2, n) if n%i == 0] # 1을 제외한 n의 약수와 곱하면 n이 되는 수

# 각 약수와 곱하면 그 수가 되는 수를 피보나치 수열 안에서 검색
for num, x in divisor: 
    for i in range(len(dp)): 
        if num <= dp[i]:
            chicken = dp[i-1] * x
            if chicken < n:
                ans.append(chicken)
                print(chicken)
            continue

print(ans[0], ans[-1])

# n이 7일때 출력되는 수가 없음 

###################################

import sys
input = sys.stdin.readline

n = int(input())
# 피보나치 수열, 최대값
dp = [0, 1, 2] + [0] * n
dp2 = [0, 0, 1, 2, 2, 3, 4] + [0] * n
idx = 2

# n보다 작거나 같은 피보나치 수열 구하기
while dp[idx] <= n:
    idx += 1
    dp[idx] = dp[idx-1] + dp[idx-2]

min_output, max_output = 0, 0
temp = n

# 최소값 계산
if temp % 2 == 1:
    temp -= 3 # 짝수로 만들기 위해 더 작은 수(-1 -2)로 이동
    min_output += 2

min_output += temp // 2
temp = n

# 최대값 계산
for i in range(7, n + 1): # dp2의 초기값 이후부터 실행
    now_max = -1
    tmp_idx = 2
    while dp[tmp_idx] <= i:
        # 주어진 수 i를 만들기 위해 피보나치 수를 두 개 선택하여 최대값 갱신
        now_max = max(now_max, dp2[dp[tmp_idx]] + dp2[i - dp[tmp_idx]])
        tmp_idx += 1
    dp2[i] = now_max

# 결과 출력
print(min_output, dp2[n])
