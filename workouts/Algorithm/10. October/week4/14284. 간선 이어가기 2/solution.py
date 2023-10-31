import sys
from heapq import heappop, heappush
input = sys.stdin.readline

# 기존의 다익스트라를 어느정도 활용하되, 시작점과 도착점이 고정되어 있음
# 출발점에서의 가중치를 계산한 다음 마지막에 대한 값만 출력하면 된다
def dijkstra(node):
    heap = []
    heappush(heap, (0, node))
    distance[node] = 0

    while heap:
        d, n = heappop(heap)
        if distance[n] < d:
            continue
        for i in graph[n]:
            cost = d + i[1] 

            if cost < distance[i[0]]:
                heappush(heap, (cost, i[0]))
                distance[i[0]] = cost


n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
distance = [float("inf") for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

s, t = map(int, input().split())

dijkstra(s)
print(distance[t])