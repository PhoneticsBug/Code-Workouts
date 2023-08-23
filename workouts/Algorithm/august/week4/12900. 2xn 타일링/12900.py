def solution(n):
    dp = [0] * (n+1)
    dp[1], dp[2] = 1, 2 # 경우의 수가 고정되어 있음
    
    for i in range(3, n+1):
        dp[i] = (dp[i-1] + dp[i-2]) % 100_000_007

    return dp[n]