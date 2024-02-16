import sys
input = sys.stdin.readline
from collections import deque

cony, brown = 11, 2

def solution(a, b):
    limit = 200_000
    # 코니 = +1, +2, +3... (매 초마다 n초만큼 더 이동함)
    # 브라운 = b-1, b+1, 2*b
    visited = [0]**(limit+1)
    q = deque()
    q.append(a)
    while q:
        x = q.popleft()
        if x == b:
            return visited[x]
            break
        for j in (x-1, x+1, x*2):
            if 0 <= j <= limit and not visited[j]:
                visited[j] = visited[x] + 1
                q.append(j)

print(solution(cony, brown))