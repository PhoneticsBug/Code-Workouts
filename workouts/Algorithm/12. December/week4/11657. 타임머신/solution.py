import sys
input = sys.stdin.readline

n, m = map(int, input().split())

# A = 시작도시, B = 도착도시, C = 이동시간
# C == 0: 순간이동, C < 0: 시간을 되돌아감
buses = [list(map(int, input().split())) for _ in range(m)]
# 1의 가중치는 0인 상태로 2~n까지의 거리를 갱신
routes = [float('inf')] + [0] + [float('inf')]*(n-1)
# 음의 사이클 (최단거리까지의 시간이 계속하여 줄어들 수 있는 경우) 
check = False

# 
for i in range(n):
    for j in range(m):
        start, destination, time = buses[j]
        # 최단시간이 무한이 아니면서 시작도시를 거쳐가는 시간보다 큰 경우
        if routes[start] != float('inf') and routes[destination] > routes[start] + time:
            routes[destination] = routes[start] + time

for i in range(m):
    start, next_mode, time = buses[i]
    # 음의 사이클에 해당하는 경우 check = True (-1 하나만 출력하게 됨)
    if routes[start] != float('inf') and routes[next_mode] > routes[start] + time:
        check = True
        break

if check:
    print(-1)
else:
    for i in range(2, n+1):
        print(-1 if routes[i] == float('inf') else routes[i])