import sys
input = sys.stdin.readline

v, e = map(int, input().split())
graph = [tuple(map(int, input().split())) for _ in range(e)]
graph.sort(key = lambda x : x[2])

def find_root(parent, x):
    if parent[x] == x:
        return x
    parent[x] = find_root(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    root_a = find_root(parent, a)
    root_b = find_root(parent, b)

    if root_a < root_b:
        parent[root_b] = root_a
    else:
        parent[root_a] = root_b

def kruskal(graph):
    parent =  [i for i in range(v+1)]
    min_cost = 0

    for i in graph:
        a, b, c = i
        if find_root(parent, a) != find_root(parent, b):
            union(parent, a, b)
            min_cost += c
    
    return min_cost

print(kruskal(graph))