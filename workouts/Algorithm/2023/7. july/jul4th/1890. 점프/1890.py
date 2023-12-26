import sys
input = sys.stdin.readline

n = int(input())
game = [list(map(int, input().split())) for _ in range(n)]
visited = [[0]*n for _ in range(n)]
visited[0][0] = 1

for i in range(n):
    for j in range(n):
        # 방문하지 않았고, 움직일 수 있는 곳이라면
        temp = game[i][j]
        if game[i][j] != 0 and visited[i][j] != 0:
            if i + game[i][j] < n: # 행방향 증가
                visited[i + game[i][j]][j] += visited[i][j]
            if j + game[i][j] < n: # 열방향 증가
                visited[i][j + game[i][j]] += visited[i][j]
print(visited[-1][-1])