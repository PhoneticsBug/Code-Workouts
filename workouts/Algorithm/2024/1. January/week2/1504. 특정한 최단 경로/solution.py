

# import sys
# input = sys.stdin.readline

# n , e = map(int, input().split())

# for _ in range(e):
#     # a 정점에서 b 까지의 양방향 길의 거리(weight)는 c이다.
#     a, b, c = map(int, input().split())



##################################
    

import sys, heapq
input = sys.stdin.readline
inf = float('inf')

# 정점의 개수 n, 간선의 개수 e
n, e = map(int, input().split())
graph = [[] for _ in range(n+1)]

# 정점 a에서 b까지의 거리 c
for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

# 두 정점 u, v
u, v = map(int, input().split())

# function
def dijkstra(start):
    # 최단거리 리스트
    distance = [inf] * (n + 1)
    distance[start] = 0
    
    heap = []
    heapq.heappush(heap, (0, start))

    while heap:
        dist, now = heapq.heappop(heap) 
        # 최단거리가 이미 계산된 노드는 제외
        if distance[now] < dist:
            continue
        # 현재 노드의 인접노드에 대한 거리 갱신
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(heap, (cost, i[0]))

    return distance

start, mid, end = dijkstra(1), dijkstra(u), dijkstra(n)

v1 = start[u] + mid[v] + end[v]
v2 = start[v] + mid[v] + end[u]

if v1 == v2 == inf:
    print(-1)
else:
    print(min(v1, v2))
