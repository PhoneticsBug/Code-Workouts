import sys 
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

visited = [[0]*n for _ in range(n)]

dx, dy =  [-1, 0, 1, 0], [0, 1, 0, -1]


# 단지 번호, 단지별 집 수 리스트, 단지 수
cnt = 0
danji_num = []
danji_cnt = 0

# DFS 함수 정의
def dfs(x, y):
    global danji_cnt
  
    # 방문한 집이 아직 방문되지 않은 집이면서 있으면 단지 수 1 증가
    if graph[x][y] == 1 and visited[x][y] == 0:
        visited[x][y] = 1
        danji_cnt += 1

        # 방문한 집이 해당 단지의 몇 번째인지 visited 배열에 입력
        danji_num[0] += 1
        visited[x][y] = danji_num[0]

        # 상하좌우 방향으로 인접한 집 검색
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 2차원 배열의 범위를 벗어난 경우 continue
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue

            # 방문한 집이 이미 방문한 경우 continue
            if visited[nx][ny] != 0:
                continue

            dfs(nx, ny)


for i in range(n):
    for j in range(n):
        # 단지 수 계산
        if graph[i][j] == 1 and visited[i][j] == 0:
            cnt += 1
            danji_num.append(0)
            dfs(i, j)

# 각 단지별 집 수 출력
danji_num.sort()
for num in danji_num:
    if num != 0:
        print(num)

# 총 단지수 출력
print(cnt)
