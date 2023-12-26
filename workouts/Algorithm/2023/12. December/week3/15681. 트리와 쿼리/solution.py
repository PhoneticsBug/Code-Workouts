import sys
sys.setrecursionlimit(10**5) 
input = sys.stdin.readline

# n = 정점의 수
# r = 루트의 번호
# q = 쿼리의 수
n, r, q = map(int, input().split())
nodes = [[] for _ in range(n+1)]

for _ in range(n-1):
    a, b = map(int, input().split())
    nodes[a].append(b)
    nodes[b].append(a)

# 서브트리의 정점 수 저장
dp = [-1 for _ in range(n+1)]

def solution(n):
    dp[n] = 1

    for i in nodes[n]:
        if dp[i] == -1:
            dp[n] += solution(i)

    return dp[n]

solution(r)

# U 입력
for _ in range(q):
    print(dp[int(input())])
