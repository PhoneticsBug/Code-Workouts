# 0, 0에서 시작해서 마지막까지 가는 값을 계속 갱신해야 함

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
dp = []

for _ in range(n):
    dp.append(list(map(int, input().split())))

for j in range(1, m):
    dp[0][j] += dp[0][j-1]

for i in range(1, n):
    lr = dp[i][:] # 우측으로 이동
    rl = dp[i][:] # 좌측으로 이동

    # 왼쪽에서 오른쪽으로 갈 때
    for j in range(m):
        # 첫번째 열에서는 내려오는 경우만 존재
        if j == 0:
            lr[j] += dp[i-1][j]
        # 내려오기 vs 우측으로 이동
        else:
            lr[j] += max(dp[i-1][j], lr[j-1])

    # 오른쪽에서 왼쪽으로 갈 때
    for j in range(m-1, -1, -1):
        # 마지막 열로 가면 내려가는 경우만 존재함
        if j == m - 1:
            rl[j] += dp[i-1][j]
        # 내려오기 vs 좌측으로 이동
        else:
            rl[j] += max(dp[i-1][j], rl[j+1])

    for j in range(m):
        dp[i][j] = max(lr[j], rl[j])

print(dp[n-1][m-1])

