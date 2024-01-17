import sys
input = sys.stdin.readline

n, m = map(int, input().split())

male = list(map(int, input().split()))
female = list(map(int, input().split()))

dp = [[float('inf')]*n for _ in range(m)]

for man in male:
    for woman in female:
        dp[man][woman] = abs(man - woman)

print(min(dp))

######################################### 

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
man = list(map(int, input().split()))
woman = list(map(int, input().split()))

if n > m:
    man, woman = woman, man
    n, m = m, n

dp = [[0]*m for _ in range(n)]
man.sort()
woman.sort()

dp[0][0] = abs(man[0] - woman[0])

for j in range(1, m - (n-1)):
    dp[0][j] = min(abs(man[0] - woman[j]), dp[0][j-1])

for i in range(1, n):
    for j in range(i, m-(n-i-1)):
        if i == j:
            dp[i][j] = dp[i-1][j-1] + abs(man[i] - woman[j])
        else:
            dp[i][j] = min(dp[i-1][j-1] + abs(man[i] - woman[j]), dp[i][j-1])

print(dp[n-1][m-1])