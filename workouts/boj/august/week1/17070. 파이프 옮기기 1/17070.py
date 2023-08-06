import sys
input = sys.stdin.readline

# (1, 0에서 시작해서 오로지 세가지 이동방향(대각선일 때만) 으로만 이동했을 때 n * m 까지 이동이 가능한지)

n = int(input())
room = [list(map(int, input().split())) for _ in range(n)]
dp = [[[0 for _ in range(n)] for _ in range(n)] for _ in range(3)]
# 가로 파이프 개수, 대각선 파이프 개수, 세로 파이프 개수 순서
#  첫번째 행은 언제나 가로 파이프만 올 수 있다.

dp[0][0][1] = 1 # 최초에 가로 파이프가 [0][1] 칸에 놓여있으므로 
for i in range(2, n):
    if room[0][i] == 0:
        dp[0][0][i] = dp[0][0][i - 1]


for r in range(1, n):
    for c in range(1, n):
        # 대각선으로 움직이는 조건
        if room[r][c] == 0 and room[r][c-1] == 0 and room[r-1][c] == 0:
            dp[1][r][c] = dp[0][r-1][c-1] + dp[1][r-1][c-1] + dp[2][r-1][c-1]

        # 가로세로 파이프
        if room[r][c] == 0:
            dp[0][r][c] = dp[0][r][c-1] + dp[1][r][c-1]
            dp[2][r][c] = dp[2][r-1][c] + dp[1][r-1][c]

print(sum(dp[i][n-1][n-1] for i in range(3)))