import sys
from heapq import heappop, heappush
input = sys.stdin.readline

n = int(input())
m = int(input())
cost = [list(map(int, input().split())) for _ in range(m)] # a와 b를 연결하는 비용 c
distance = []

def dijkstra(node):
    heap = []
    heappush(heap, (0, node))
    distance[node] = 0

    while heap:
        d, n = heappop(heap)
        if distance[n] < d:
            continue
        for i in cost[n]:
            cost = d + i[1] 

            if cost < distance[i[0]]:
                heappush(heap, (cost, i[0]))
                distance[i[0]] = cost

