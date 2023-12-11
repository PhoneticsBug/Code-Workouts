import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
picture = [input().rstrip() for _ in range(n)]

# 적록색약인 사람은 적색과 녹색을 하나의 덩어리로 봄
# 그래프 탐색으로 개수를 찾기 (색약O, 색약X로 두번?)

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

def bfs(graph, visited, x, y, weakness):
    queue = deque([x, y])
    color = graph[x][y] # 현위치

    while queue:
        x_now, y_now = queue.popleft()

        for i in range(4):
            nx, ny = x_now + dx[i], y_now + dy[i]

            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if weakness and (color == 'R' or color == 'G'):
                    if graph[nx][ny] == 'R' or graph[nx][ny] == 'G':
                        visited[nx][ny] = True
                        queue.append((nx, ny))
                    else:
                        if graph[nx][ny] == color:
                            visited[nx][ny] = True
                            queue.append((nx, ny))

def counter(graph, weakness):
    cnt = 0
    visited = [[False]*n for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                visited[i][j] = True
                bfs(graph, visited, i, j, weakness)
                cnt += 1

    return cnt

print(counter(picture, False), counter(picture, True))



####################### answer 

from collections import deque

# 상하좌우 이동을 위한 좌표 변화량
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(graph, visited, x, y, is_weakness):
    queue = deque([(x, y)])
    color = graph[x][y]  # 현재 위치의 색상

    while queue:
        current_x, current_y = queue.popleft()

        for i in range(4):
            nx, ny = current_x + dx[i], current_y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                # 적록색약인 경우에는 빨강과 초록을 같은 색으로 처리
                if is_weakness and (color == 'R' or color == 'G'):
                    if graph[nx][ny] == 'R' or graph[nx][ny] == 'G':
                        visited[nx][ny] = True
                        queue.append((nx, ny))
                else:
                    if graph[nx][ny] == color:
                        visited[nx][ny] = True
                        queue.append((nx, ny))

def count_regions(graph, is_weakness):
    regions = 0
    visited = [[False] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                visited[i][j] = True
                bfs(graph, visited, i, j, is_weakness)
                regions += 1

    return regions

# 입력 받기
n = int(input())
picture = [input().rstrip() for _ in range(n)]

# 적록색약이 아닌 경우와 적록색약인 경우의 구역 수 계산
normal_regions = count_regions(picture, False)
weak_regions = count_regions(picture, True)

# 결과 출력
print(normal_regions, weak_regions)
