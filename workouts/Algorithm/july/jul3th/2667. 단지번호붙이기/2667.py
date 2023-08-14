import sys 
from collections import deque
input = sys.stdin.readline

dx, dy =  [-1, 0, 1, 0], [0, 1, 0, -1]

def bfs(graph, a, b):
    n = len(graph)
    queue = deque()
    queue.append((a, b))
    graph[a][b] = 0
    count = 1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0 # 0으로 바꿔 재방문 방지
                queue.append((nx, ny))
                count += 1
    return count

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
cnt = []

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1: # 집이 있다면(시작지점)
            cnt.append(bfs(graph, i, j)) # bfs 실행, cnt에 단지별 집 개수 추가

print(len(cnt))
print(*sorted(cnt), sep='\n')
