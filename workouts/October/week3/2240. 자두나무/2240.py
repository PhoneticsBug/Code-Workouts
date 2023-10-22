import sys
input = sys.stdin.readline

T, W = map(int, input().split()) # T = 자두의 갯수 W = 움직이는 횟수
plums = [0] + list(int(input()) for _ in range(T))
dp = [[0]*(W+1) for _ in range(T+1)]

for i in range(T+1):
    # 1번 나무에서 안움직이는 경우

    # 1번 나무에서 자두가 떨어지면
    if plums[i] == 1:
        dp[i][0] = dp[i-1][0] + 1 # 하나 더해줌
    # 2번인 경우엔
    else:
        dp[i][0] = dp[i-1][0] # 그대로

    # 1번 이상 움직이는 경우엔
    for j in range(1, W+1):

        # 2번 나무에서 떨어질 때 2번 나무에 있다면
        if plums[i] == 2 and j % 2 == 1:
            # 움직여서 받아먹기 vs 지금 위치 유지하기
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + 1 
        
        # 1번 나무에서 떨어지고, 지금 1번에 있다면
        elif plums[i] == 1 and j % 2 == 0:
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + 1

        # 못 받아먹는 경우
        else: 
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j])

print(max(dp[T]))