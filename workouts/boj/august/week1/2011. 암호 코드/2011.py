import sys
input = sys.stdin.readline

code = list(map(int, input().split()))
size = len(code)

dp = [0]*(size+1)
dp[0], dp[1] = 1, 1

if code[0] == 0:
    print(0)
else:
    for i in range(1, size):
        idx = i + 1
        if code(i) > 0:
            dp[idx] += dp[idx-1]
        if 10 <= code[i] + code[i-1]*10 <= 26:
            dp[idx] += dp[idx-2]
    print(dp[size]%1000000)
            
# -----------

import sys
input = sys.stdin.readline

data = list(map(int, input().split()))
len = len(data)

dp = [0] ** (len + 1)
dp[0] = 1
dp[1] = 1

if data[0] == 0:
    print(0)
else:
    for k in range(1, len):
        i = k + 1
        if data[k] > 0:
            dp[i] += [i-1]
        if 10 <= data[k] + data[k-1]*10 <= 26:
            dp[i] += dp[i-2]
    print(dp[len] % 1000000)