# 문제 설명

# n명의 학생들이 x번 마을에 모여 파티를 벌이기로 함
# 마을 사이에는 m개의 단방향 도로가 있고, i번째 길을 지날 때 t 시간을 소비함

# 파티에 가기 위해서는 걸어서 그들의 마을로 돌아가야 함
# 단방향 도로선상에서 n명의 학생들 중 가장 긴 시간동안 오가야 하는 사람은?

# 풀이 전략
# - 각 학생이 파티장소로 갈 때의 최단거리와 집으로 돌아갈 때의 최단거리 구하기
# - 다익스트라 알고리즘(2회)
# - 이 둘을 더한 값을 계산하고 최대값을 찾아 출력함

import sys, heapq
input = sys.stdin.readline

# 학생 수 n, 도로 수 m, 목적지 x
n, m, x = map(int, input().split())

path = [[] for _ in range(n+1)]

# 단방향 도로 
# i번째 도로의 시작점, 끝점, 소요시간
for i in range(1, m+1):
    start, destination, time = map(int, input().split())
    path[start].append([destination, time])

# 다익스트라 함수
def solution(start):
    # 각 포인트에 대한 거리(무한대) 지정 및 시작점 초기화
    distances = [float('inf')]*(n+1)
    distances[start] = 0
    queue = [(0, start)]

    while queue:
        dist, node = heapq.heappop(queue)

        # 이미 갱신된 노드는 패쓰
        if distances[node] < dist:
            continue

        # 인근 노드와 거리 확인 
        for near, weight in path[node]:
            distance = dist + weight
            # 더 짧은 거리가 있다면 갱신
            if distance < distances[near]:
                distances[near] = distance
                heapq.heappush(queue, (distance, near))

    return distances

# 집에서 파티로 가는 거리, 돌아가는 거리
party = solution(x)
home = [0]*(n+1)
# 돌아가는 거리 갱신
for i in range(1, n+1):
    if i != x:
        home[i] = solution(i)[x]
# 둘을 합친 것 중 최대값 출력
answer = max(party[i] + home[i] for i in range(1, n+1))

print(answer)