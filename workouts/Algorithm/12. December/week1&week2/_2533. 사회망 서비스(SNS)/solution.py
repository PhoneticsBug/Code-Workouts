import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)

n = int(sys.stdin.readline())
dp = [[0, 0] for _ in range(n + 1)]
visited = [0 for _ in range(n + 1)]
friends = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    a, b = map(int, sys.stdin.readline().split())
    friends[a].append(b)
    friends[b].append(a)

def dfs(node):
    visited[node] = 1

    if not friends[node]:
        dp[node][1] = 1
        dp[node][0] = 0
    else:
        for child in friends[node]:
            if not visited[child]:
                dfs(child)
                dp[node][1] += min(dp[child][0], dp[child][1])
                dp[node][0] += dp[child][1]
        dp[node][1] += 1



# 결과 출력
dfs(1)
print(min(dp[1][0], dp[1][1]))
