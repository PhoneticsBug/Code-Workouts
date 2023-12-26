import sys, heapq
input = sys.stdin.readline

# n = n개의 도시
# k = 이동할 수 있는 최단거리
# road = 도시 사이를 이어주는 도로 (단방향)
# x = 시작하는 도시 번호
# x 도시에서 k 만큼 이동했을 때 그 거리가 최단거리인 도시를 오름차순으로 출력

n, m, k, x = map(int, input().split())
roads = [list(map(int, input().split())) for _ in range(m)]

graph = [[] for _ in range(n+1)]
for road in roads: # 각 도시에서 이동할 수 있는 도시
    graph[road[0]].append(road[1])

def daijkstra(start):
    distance = [float('inf')] * (n+1)
    distance[start] = 0
    heap = [(0, start)]

    # 최단거리 계산
    while heap:
        dist, now = heapq.heappop(heap)
        # 이미 최소거리가 있다면 패쓰
        if distance[now] < dist:
            continue
        # 연결된 도시 순회
        for next_city in graph[now]:
            cost = dist + 1
            # 기존 이동거리보다 더 짧은 거리가 있는경우 갱신
            if cost < distance[next_city]:
                distance[next_city] = cost
                heapq.heappush(heap, (cost, next_city))

    return distance

distance = daijkstra(x)
result = [i for i in range(1, n+1) if distance[i] == k]

if result:
    print(*result, sep="\n")
else:
    print(-1)
