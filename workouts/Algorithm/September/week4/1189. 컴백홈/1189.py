import sys
input = sys.stdin.readline

r, c, k = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(r)]

dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
ans = 0

def dfs(x, y, dist):
    global ans

    if dist == k and y == c-1 and x == 0:
        ans += 1
    else:
        graph[x][y] = 'T'  # 방문 처리
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 백트래킹
            if 0 <= nx < r and 0 <= ny < c and graph[nx][ny] == '.':
                graph[nx][ny] = 'T'
                dfs(nx, ny, dist + 1)
                graph[nx][ny] = '.'

dfs(r - 1, 0, 1)
print(ans)
