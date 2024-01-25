# n명과 친구관계 수 m이 주어짐
# n회만큼 a와 b가 친구임을 알려주는 숫자가 입력됨
# 가능한 경우에는 1, 아닌 경우는 0 출력

# 각 간선들이 연속적으로 연결되어 있어야 함
# 연결구조가 A-B-C-D-E와 같은 형태를 가질 수 있는지 확인해야 함
# 즉, 모든 참가자에 대해서 어떤 다른 참가자에게 도달하기까지 
# n개의 간선으로 이동하는 경우가 하나 이상 존재해야 함

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
dp = [[] for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().split())
    dp[a].append(b)
    dp[b].append(a)

def dfs(v, depth):
    answer = 0
    visited[v] = True
    if depth == 4:
        answer = 1
    for i in dp[v]:
        if not visited[i]:
            dfs(i, depth+1)
            visited[i] = False

    return answer

visited = [False] * n
answer = []

for i in range(n):
    answer.append(dfs(i, 0))
    visited[i] = False

if sum(answer) == len(answer):
    print(1)
else:
    print(0)

