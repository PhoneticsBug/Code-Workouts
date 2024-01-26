# n명과 친구관계 수 m이 주어짐
# n회만큼 a와 b가 친구임을 알려주는 숫자가 입력됨
# 가능한 경우에는 1, 아닌 경우는 0 출력

# 각 간선들이 연속적으로 연결되어 있어야 함
# 연결구조가 A-B-C-D-E와 같은 형태를 가질 수 있는지 확인해야 함
# 즉, 모든 참가자에 대해서 어떤 다른 참가자에게 도달하기까지 
# n개의 간선으로 이동하는 경우가 하나 이상 존재해야 함

import sys
input = sys.stdin.readline

# 사람의 수 n, 간선의 수 m
n, m = map(int, input().split())
friends = [[] for _ in range(n)]

# friends 갱신 (양방향 그래프)
for _ in range(m):
    a, b = map(int, input().split())
    friends[a].append(b)
    friends[b].append(a)

answer = False
visited = [False] * 2001 # 사람의 수 (최대값: 2000)

def dfs(idx, depth):
    global answer

    visited[idx] = True
    # 깊이가 4에 도달하면 (모두 친구관계가 성립하면) 종료
    if depth == 4:
        answer = True
        return
    # 아닌 경우에는 계속 탐색 진행
    for i in friends[idx]:
        if not visited[i]:
            dfs(i, depth+1)
            visited[i] = False

for i in range(n):
    dfs(i, 0)
    visited[i] = False
    if answer: # 조건이 성립하면 루프 탈출
        break
    
if answer: 
    print(1) 
else: 
    print(0)