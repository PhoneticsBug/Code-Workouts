import sys
input = sys.stdin.readline

n = int(input())
rurals = list(map(int, input().split()))
budget = int(input())

start, end  = 0, max(rurals)

while start <= end:
    mid = (start + end) // 2
    budget_sum = 0

    for r in rurals:
        budget_sum += min(r, mid)

    if budget_sum <= budget:
        start = mid + 1
    else:
        end = mid - 1
print(mid)