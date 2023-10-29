import sys
input = sys.stdin.readline

N, M = map(int, input().split())
budget = list(int(input()) for _ in range(N))

start, end = max(budget), sum(budget)
answer = end

while start <= end:
    mid = (start + end) // 2 # 인출값
    money = 0
    count = 0

    for use in budget:
        if money < use:
            money = mid # 인출
            count += 1 
        money -= use

    if count > M:
        start = mid + 1
    else:
        answer = min(answer, mid) 
        end = mid - 1
print(answer)