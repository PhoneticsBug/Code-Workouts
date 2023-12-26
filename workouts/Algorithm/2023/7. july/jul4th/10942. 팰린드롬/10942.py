import sys
input = sys.stdin.readline

n = int(input())
# nums = list(map(int, input().split()))
nums = "".join(map(str, input().split()))
dp = [[0]*(n) for _ in range(n)]

for i in range(n):
    for j in range(i, n):
        if nums[i : j+1] == nums[i : j+1][::-1]:
            dp[i][j] = 1

# print(*dp, sep='\n')
m = int(input())
for _ in range(m):
    start, end = map(int, input().split()) 
    print(dp[start-1][end-1])

# ------------------------------------------

import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split())) #"".join(map(str, input().split()))
dp = [[0]*(n) for _ in range(n)]

for i in range(n): # 단독
    dp[i][i] = 1

for i in range(n-1): # 거리가 2인 경우
    if nums[i] == nums[i+1]:
        dp[i][i+1] = 1

for i in range(n-2): # 그 외의 경우
    for j in range(n-2-i):
        k = i+j+2
        if nums[j] == nums[k] and dp[j+1][k-1] == 1:
            # 처음과 끝이 같고 그 사이도 팰린드롬이라면 
            dp[j][k] = 1

m = int(input())
for i in range(m):
    s, e = map(int, input().split())
    print(dp[s-1][e-1])