import sys
input = sys.stdin.readline

# LCS와 같은 알고리즘 (Longest Commom Subsequence)
# 2차원 dp 배열을 생성한 후 dp의 앞의 값을 가져와 더하면서 갱신

n = int(input())
nums = list(map(int, input().split()))

dp = [[0]*(n+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, n+1):
        # 현재 보고있는 두 숫자가 같다면 대각선 위의 값 (이전에 계산한 값)에 1을 더함
        if nums[-i] == nums[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        # 다른 경우에는 이전 행열에서의 최대값을 가져옴
        else:
            dp[i][j] = max(dp[i][j-1], dp[i-1][j])

print(n - dp[n][n])


