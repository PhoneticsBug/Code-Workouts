import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

def bfs(start):
    queue = deque(start)
    visited = [[False]*m for _ in range(n)]
    max_time = 0

    while queue:
        r, c, time = queue.popleft()

    return