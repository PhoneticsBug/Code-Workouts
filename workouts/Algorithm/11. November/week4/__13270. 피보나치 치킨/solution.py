import sys
input = sys.stdin.readline

n = int(input())
ans = []
# fib 배열을 만든 후 n으로 정확히 나누어지는 값을 따로 모아 최소값과 최대값 출력
# 피보나치 수열 = 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987

# n의 개수에 따라서
# n = 2 >> [1]
# n = 3 >> [2]
# n = 4 >> [3]
# n = 5 >> [3]
# n = 6 >> [4]
# n = 8 >> [5]
# n = 13 >> [8]

dp = [1, 1]
while True:
    if dp[-1] > n:
        break
    dp.append(dp[-1]+dp[-2])

# n의 약수 안에서 찾는 방법
divisor = [[i, n//i] for i in range(2, n) if n%i == 0] # 1을 제외한 n의 약수와 곱하면 n이 되는 수

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

n = int(input())
dp = [0, 1, 2] + [0] * 1000000
dp2 = [0, 0, 1, 2, 2, 3, 4] + [0] * 1000000
idx = 2

# 피보나치 수열 구하기
while dp[idx] <= n:
    idx += 1
    dp[idx] = dp[idx-1] + dp[idx-2]

min_output = 0
max_output = 0
temp = n

# 최소값 계산
if temp % 2 == 1:
    temp -= 3
    min_output += 2

min_output += temp // 2
temp = n

# 최대값 계산
for i in range(7, n + 1):
    now_max = -1
    tmp_idx = 2
    while dp[tmp_idx] <= i:
        # 주어진 수 i를 만들기 위해 피보나치 수를 두 개 선택하여 최대값 갱신
        now_max = max(now_max, dp2[dp[tmp_idx]] + dp2[i - dp[tmp_idx]])
        tmp_idx += 1
    dp2[i] = now_max

# 결과 출력
print(min_output, dp2[n])
