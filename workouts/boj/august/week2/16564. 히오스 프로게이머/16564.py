import sys
input = sys.stdin.readline

n, k = map(int, input().split())
x = list(map(int, input().split()))

start, end = min(x), min(x) + k 

result = 0
while start <= end:
    mid = (start + end) // 2

    temp = 0
    for i in x:
        if mid > i:
            temp += (mid - i)
    if temp <= k:
        start = mid + 1
        result = max(mid, result)
    else:
        end = mid - 1

print(result)