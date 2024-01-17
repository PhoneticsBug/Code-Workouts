import sys
input = sys.stdin.readline

n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]

dp = [[0]*n for _ in range(n)]

# 행렬끼리의 간격을 1부터 n-1까지 갱신
# i = 시작 행렬, j = 끝 행렬의 인덱스
# k = i와 j 사이의 행렬값
for cnt in range(n-1):
    for i in range(n - 1 - cnt):
        j = i + cnt + 1
        dp[i][j] = float('inf')

        for k in range(i, j):
            # i부터 k까지의 행렬곱셈 연산 횟수와 k+1부터 j까지의 행렬곱셈 연산 횟수
            # i부터 k, k+1부터 j의 행렬들을 곱하는데 필요한 연산 횟수를 더한 값과 비교하여 갱신
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1][j] + matrix[i][0] * matrix[k][1] * matrix[j][1])

print(dp[0][-1])
