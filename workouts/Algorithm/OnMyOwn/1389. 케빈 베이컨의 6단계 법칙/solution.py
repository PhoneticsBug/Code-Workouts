import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

def solution(v):
    q = deque([v])
    visited[v] = 0
    while q:
        target = q.popleft()

        for i in graph[target]:
            if not visited[i]:
                visited[i] = visited[target] + 1
                q.append(i)
answer = []

for i in range(1, n+1):
    visited = [0]*(n+1)
    solution(i)
    visited[i] = 0
    answer.append(sum(visited))
print(answer.index(min(answer))+1)