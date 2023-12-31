import sys
input = sys.stdin.readline

# 2차원 dp를 만든 후 dp[i][j]인 경우 i~j번째의 합을 넣어주는 방식
# 누적합 배열을 이용해서 0~i까지를 계산할 수 있도록 함
    
t = int(input())

for _ in range(t):
    k = int(input())
    files = [0] + list(map(int, input().split()))

    # 누적합
    prefix_sum = [0 for _ in range(k+1)]

    for i in range(1, k+1):
        prefix_sum[i] = prefix_sum[i-1] + files[i]

    dp = [[0 for _ in range(k+1)] for _ in range(k+1)]

    # j부터 j + i - 1까지의 최소비용 계산
    for i in range(2, k+1):
        for j in range(1, k + 2 - i):
            dp[j][j+i-1] = min([dp[j][j+l] + dp[j+l+1][j+i-1] for l in range(i-1)]) + (prefix_sum[j+i-1]- prefix_sum[j-1]) 

    print(dp[1][k])