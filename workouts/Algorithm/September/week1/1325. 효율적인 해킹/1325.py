from collections import deque
import sys
input = sys.stdin.readline


# bfs 함수
def bfs(start):
    cnt = 1
    visited = [0 for _ in range(n+1)]
    visited[start] = 1
    queue = deque([start])
    while queue: # 각 컴퓨터가 방문할 수 있는 컴퓨터 확인
        t = queue.popleft()
        for i in arr[t]:
            if not visited[i]:
                queue.append(i)
                visited[i] = 1
                cnt += 1

    return cnt


n, m = map(int, input().split())
arr = [[] for _ in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    arr[b].append(a)

res = []
for i in range(1, n+1):
    res.append(bfs(i))

result = max(res) # 가장 많이 해킹할 수 있는 컴퓨터의 인덱스 + 1
for i in range(len(res)):
    if result == res[i]:
        print(i+1, end=' ')
