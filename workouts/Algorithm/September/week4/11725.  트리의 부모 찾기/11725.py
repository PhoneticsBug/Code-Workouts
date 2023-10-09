import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n+1)]
parent = [0] * (n+1)

for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(node):
    for neighbor in graph[node]:
        if parent[neighbor] == 0:  # 아직 방문하지 않은 노드인 경우
            parent[neighbor] = node  # 현재 노드를 부모로 설정
            dfs(neighbor)

dfs(1)

for i in range(2, n+1):
    print(parent[i])
