import sys
input = sys.stdin.readline

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

r, g, b = 0, 0, 0

dp = [[0]*n for _ in range(n)] # 2차원 dp


test = []
for i in grid:
    for j in i:
        test.append(j)

print(sorted(test)[:n+1], sum(sorted(test)[:n+1]))