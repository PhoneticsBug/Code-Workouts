# 크루스칼 알고리즘의 기본원리
# 1. 한붓 그리기 형태로 그래프들을 연결한다
# 2. 연결된 그래프의 경로 가중치가 최소값이어야 한다.

import sys
from heapq import heappop, heappush
input = sys.stdin.readline

n = int(input())
m = int(input())
cost = [tuple(map(int, input().split())) for _ in range(m)] # a와 b를 연결하는 비용 c
# 비용 기준 정렬
cost.sort(key=lambda x: x[2])

# 각 노드의 루트 노드 찾기
def find_root(parent, x):
    if parent[x] == x:
        return x
    parent[x] = find_root(parent, parent[x])
    return parent[x]

# 노드 합치기
def union(parent, a, b):
    root_a = find_root(parent, a)
    root_b = find_root(parent, b)

    # 더 큰 노드에 종속시키기
    if root_a < root_b:
        parent[root_b] = root_a
    else:
        parent[root_a] = root_b

def kruskal(cost):
    # 초기값: 각 노드의 부모가 자기 자신
    parent =  [i for i in range(n+1)]
    min_cost = 0

    for i in cost:
        a, b, c = i
        # 사이클이 발생하지 않으면 이어주기
        if find_root(parent, a) != find_root(parent, b):
            union(parent, a, b)
            min_cost += c
    
    return min_cost

print(kruskal(cost))