import sys
from collections import deque
input = sys.stdin.readline

dx = [-1, -1, -1, 0, 1, 0, 1, 1]
dy = [-1, 0, 1, 1, 1, -1, 0, -1]

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

q = deque()
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1: # 상어의 위치
            q.append([i, j])
result = 0

while q:
    x, y = q.popleft()
    for d in range(8): # 상하좌우 및 대각선
        nx = x + dx[d]
        ny = y + dy[d]

        if nx < 0 or ny < 0 or nx >= n or ny >= m: # 그래프 밖 처리
            continue
        if graph[nx][ny] != 0: # 방문한 그래프 및 상어가 있는 곳 처리
            continue
        q.append([nx, ny])
        graph[nx][ny] = graph[x][y] + 1
        result = max(result, graph[x][y] + 1)
print(result - 1)
