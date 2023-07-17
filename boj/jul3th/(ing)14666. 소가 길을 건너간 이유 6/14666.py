n, k, r = map(int, input().split())

roads = []
cows = []

for _ in range(n):
    roads.append(list(map(int, input().split())))

for _ in range(k):
    cows.append(list(map(int, input().split())))

# 예제 1의 경우
# roads = [[2, 2, 2, 3], [3, 3, 3, 2], [3, 3, 2, 3]]
# cows = [[3, 3], [2, 2], [2, 3]]