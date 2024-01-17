# ---------------------- DFS ----------------------
import sys
input = sys.stdin.readline
from heapq import heappush, heappop
sys.setrecursionlimit(10**9)
    
def dfs(node, t, c):
    global answer

    # 목표 노드에 도달한 경우 최소비용 갱신
    if node == N - 1:
        answer = min(answer, c)
        return

    # 방문하지 않은 노드 중 시간/비용이 되는 곳으로 이동
    for next, time, cost in graph[node]:
        if not visited[next]:
            if t + time <= T and c + cost <= M:
                visited[next] = True
                dfs(next, t + time, c + cost)
                visited[next] = False

# 건물의 개수
N = int(input())

# 남은 시간, 잔고
T, M = map(int, input().split())

# 간선의 개수
L = int(input())

INF = 10**9

# 간선의 시간과 비용
graph = [[] for _ in range(N)]

for _ in range(L):
    a, b, time, cost = map(int, input().split())
    a -= 1
    b -= 1
    graph[a].append((b, time, cost))
    graph[b].append((a, time, cost))

answer = INF
visited = [False]*N
visited[0] = True

dfs(0, 0, 0)

if answer == INF:
    print(-1)
else:
    print(answer)