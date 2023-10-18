import sys
input = sys.stdin.readline

N, M = map(int, input().split())
budget = list(int(input()) for _ in range(N))
withdraw = 0
money = 0


while True:
    if withdraw >= M:
        money = 0
        break
    
    for use in budget:
        withdraw += 1
        money += use

# 가장 합리적으로 나누는 방법은 sum(budget) // len(budget)만큼 사용하는 것
# print((100 + 400 + 300 + 100 + 500 + 101 + 400 )//7) = 1901 // 7 >>> 271
# 이분 탐색으로 푸는 경우에는: use 중 가장 작은 값과 큰 값의 중간을 찾으면 될거 같다
# 초기값 mid를 구성한 다음, 마지막 날까지 갈 수 있을 때까지 더하고 빼기
# start = min(budget), end = max(budget), mid = (max(budget) + min(budget)) // 2
# 