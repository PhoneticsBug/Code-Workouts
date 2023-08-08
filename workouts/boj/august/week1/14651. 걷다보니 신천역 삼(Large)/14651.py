import sys
from itertools import combinations
input = sys.stdin.readline

n = int(input())

arr = [1, 2, 0]*n

test = list(combinations(arr, n))
cnt = 0
for i in set(test):
    if i[0] != 0:
        temp = int("".join(str(j) for j in i))
        if temp % 3 == 0:
            # print(temp)
            cnt += 1
if cnt > 0:
    print(cnt, cnt%(1000000009))
else: print(cnt)


### 이런거 다 필요없었다... 
# -------------------------------------------------------------
# 0, 2, 6, 18 . . .  << 2부터 계속 3씩 곱하고 있음

arr = 2
n = int(input())
if n == 1:
    print(0)
else:
    arr = arr * (3 ** (n-2))
    print(arr%1000000009)