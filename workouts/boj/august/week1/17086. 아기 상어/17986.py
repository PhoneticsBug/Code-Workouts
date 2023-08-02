import sys
from collections import deque
input = sys.stdin.readline

m, n = map(int, input().split())
ocean = [list(map(int, input().split())) for _ in range(m)]

dx = [0, 0, -1, 1, -1, 1, 1, -1]
dy = [-1, 1, 0, 0, -1, 1, -1, 1]
# 상 하 좌 우 좌상 우하 우상 좌하

def bfs():
    queue = deque()

    # 상어의 위치를 deque에 추가
    for i in range(n):
        for j in range(m):
            if ocean[i][j] == 1:
                queue.append((i, j))

    

    




# 좌표 내에 존재하는 1의 개수만큼 루프를 돌려서 좌우로 1씩 증가하게 만들기
# 상하는 매번 거리를 1로 초기화하기? <<< 최대거리가 갱신되지 않아 어려울 수 있다


