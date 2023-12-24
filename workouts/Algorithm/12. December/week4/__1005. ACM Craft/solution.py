import sys
from collections import deque
input = sys.stdin.readline

def solution():
    q = deque()
    dp = [0] * (n + 1) # 건물 i를 짓는데에 걸리는 시간
    line = [0] * (n + 1) # 건물 i로 들어오는 간선의 수
    graph = [[] for _ in range(n + 1)] # i 건물을 지은 후 지을 수 있는 건물의 수
    time = [0] + list(map(int, input().split()))

    # 건물간의 관계 등록
    for _ in range(k):
        x, y = map(int, input().split())
        line[y] += 1
        graph[x].append(y)

    # 건물 번호 입력
    building = int(input())

    # 바로 지을 수 있는 건물 먼저 큐에 삽입
    for i in range(1, n + 1):
        if line[i] == 0:
            q.append(i)
            dp[i] = time[i]
    
    # bfs >>> 최초 건설 후 지을 수 있는 건물 탐색
    while q:
        now = q.popleft()

        # 목표 건물 도달 후 종료
        if now == building:
            print(dp[now])
            break

        # 다음에 지을 건물 찾기
        for i in graph[now]:
            line[i] -= 1
            dp[i] = max(dp[i], dp[now] + time[i])

            # 확인 후 큐에 삽입
            if line[i] == 0:
                q.append(i)

t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    solution()