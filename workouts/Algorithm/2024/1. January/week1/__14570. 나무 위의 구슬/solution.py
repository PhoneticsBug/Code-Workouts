import sys
input = sys.stdin.readline

n = int(input())
tree = [[]*n]

for _ in range(n):
    u, v = map(int, input().split())
    if u == -1 or v == -1:
        continue
    else:
        tree[u].append(v)
        tree[v].append(u)

k = int(input())

