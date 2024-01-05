import sys
input = sys.stdin.readline
from collections import deque


m, n = map(int, sys.stdin.readline().split())
box = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

queue = deque()

# 익은 토마토 위치를 큐에 추가
for i in range(n):
    for j in range(m):
        if box[i][j] == 1:
            queue.append([i, j])

# BFS 실행
while queue:
    x, y = queue.popleft()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        # box 밖으로 빠져나갔을 때
        if 0 <= nx < n and 0 <= ny < m and box[nx][ny] == 0:
            box[nx][ny] = box[x][y] + 1
            queue.append([nx, ny])

answer = max(map(max, box))-1

# 모든 토마토가 익었는지 확인
for b in box:
    if 0 in b:
        answer = -1

print(answer)
