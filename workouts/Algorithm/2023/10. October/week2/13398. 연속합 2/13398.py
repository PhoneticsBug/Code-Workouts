import sys
input = sys.stdin.readline

n = int(input())
row = list(map(int, input().split()))

# i번째 수를 포함/포함하지 않는 연속합(0, 1)
dp = [[0]*n for _ in range(2)]

dp[0][0] = row[0]
dp[1][0] = -1*float('inf') # 

for i in range(1, n):
    dp[0][i] = max(dp[0][i-1] + row[i], row[i])
    dp[1][i] = max(dp[1][i-1] + row[i], dp[0][i-1], row[i])

print(max(max(dp[0]), max(dp[1])))