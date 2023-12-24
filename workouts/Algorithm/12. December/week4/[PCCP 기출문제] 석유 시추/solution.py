import sys
input = sys.stdin.readline

from collections import deque

# bfs로 석유 위치를 찾은 다음 다시 반복문을 돌려서 덩어리 탐색 후 누적

def solution(land):
    n, m = len(land), len(land[0])
    dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
    result = [0 for _ in range(m + 1)]
    visited = [[0 for _ in range(m)] for _ in range(n)]

    def bfs(a, b):
        count = 0
        visited[a][b] = 1
        q = deque()
        q.append((a, b))
        miny, maxy = float('inf'), -1 * float('inf')

        while q:
            x, y = q.popleft()
            miny, maxy = min(miny, y), max(maxy, y)
            count += 1

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if nx < 0 or nx >= n or ny < 0 or ny >= m:
                    continue
                if visited[nx][ny] == 0 and land[nx][ny] == 1:
                    visited[nx][ny] = 1
                    q.append((nx, ny))
                
        for i in range(miny, maxy + 1):
            result[i] += count

    for i in range(n):
        for j in range(m):
            if visited[i][j] == 0 and land[i][j] == 1:
                bfs(i, j)

    return max(result)