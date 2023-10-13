import sys
input = sys.stdin.readline

n = int(input())
damage = [0] + list(map(int, input().split()))
heal = [0] + list(map(int, input().split()))

# n = 8
# damage = [0, 100, 26, 13, 17, 24, 33, 100, 99]
# heal = [0, 34, 56, 21, 1, 24, 34, 100, 99]

dp = [[0] * 101 for _ in range(n + 1)]

for i in range(1, n+1):
    for j in range(1, 101):
        if damage[i] <= j:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j - damage[i]] + heal[i]) # 더 큰 값을 더함
        else:
            dp[i][j] = dp[i-1][j]

print(dp[n][99]) # 마지막 인덱스는 죽어버린 경우가 됨 

print(*dp, sep='\n')