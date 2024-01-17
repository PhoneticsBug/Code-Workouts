# -------------------- 다익스트라 --------------------
import sys
input = sys.stdin.readline
from heapq import heappush, heappop
sys.setrecursionlimit(10**9)

# 건물의 개수
n = int(input())

# 남은 시간, 잔고
t, m = map(int, input().split())

# 건물 사이의 길과 시간, 비용 
roads = [[] for _ in range(n+1)]
for _ in range(int(input())):
    a, b, time, cost = map(int, input().split())
    roads[a].append((b, time, cost))
    roads[b].append((a, time, cost))

INF = float('inf')
distcost = [[INF for _ in range(10001)] for _ in range(n+1)]
distcost[1][0] = 0

# 시작 지점 (건물 1)
q = [(0, 0, 1)]

while q:
    time, cost, now = heappop(q) # 현재 위치 추출

    # 이미 더 짧은 시간/비용으로 간 적이 있다면 패쓰
    if distcost[now][cost] < time:
        continue

    # 잔고 이내에서 이동할 수 있는 건물로 이동
    for next, n_time, n_cost in roads[now]:
        t_time, t_cost = time + n_time, cost + n_cost

        if t_time <= t and t_cost <= m:
            if t_time < distcost[next][t_cost]:
                distcost[next][t_cost] = t_time
                heappush(q, (t_time, t_cost, next))

answer = INF

for i in range(m+1):
    if distcost[n][i] <= t and i < answer:
        answer = i

if answer <= m:
    print(answer)
else:
    print(-1)