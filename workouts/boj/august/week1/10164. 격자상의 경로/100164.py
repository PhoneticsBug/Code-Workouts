import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
graph = [[0]*m for _ in range(n)]
result = 1

if k == 0:
    for i in range(n):
        for j in range(m):
            if i == 0 or j == 0:
                graph[i][j] = 1
            else: # 이전 양쪽 칸의 숫자를 더함
                graph[i][j] = graph[i][j-1] + graph[i-1][j]
    result *= graph[n-1][m-1]

else:
    mx, my = ((k - 1) // m), ((k - 1) % m) # O가 그려진 지점 

    for i in range(mx + 1):
        for j in range(my + 1):
            if i == 0 or j == 0:
                graph[i][j] = 1
            else: # 이전 양쪽 칸의 숫자를 더함
                graph[i][j] = graph[i][j-1] + graph[i-1][j]
    result *= graph[mx][my]

    for i in range(mx, n):
        for j in range(my, m):
            if i == mx or j == my:
                graph[i][j] = 1
            else: # 이전 양쪽 칸의 숫자를 더함
                graph[i][j] = graph[i][j-1] + graph[i-1][j]

    result *= graph[n-1][m-1]

print(result)