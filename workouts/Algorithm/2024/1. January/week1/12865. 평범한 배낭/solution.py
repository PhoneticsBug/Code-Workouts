import sys
input = sys.stdin.readline

# n = 가방 속 물건 후보의 개수, k = 가방의 최대 무게
# weight, value (list)
n, k = map(int, input().split())
bag = [[0, 0]] + [list(map(int, input().split())) for _ in range(n)]

# 무게와 가치로 정렬한 다음 
dp = [[0 for _ in range(k+1)] for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, k+1):
        weight = bag[i][0]
        value = bag[i][1]
        
        # 용량이 초과되면 현재 물건을 뺌
        if j < weight:
            dp[i][j] = dp[i-1][j]
        # 아닌 경우 = 현재 + 남은용량과 이전까지의 값을 비교해서 더 큰 값 선택
        else:
            dp[i][j] = max(value + dp[i-1][j-weight], dp[i-1][j])

print(dp[n][k])