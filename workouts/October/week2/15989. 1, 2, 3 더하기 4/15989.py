import sys
input = sys.stdin.readline

def solution(number):
    dp = [[0]*4 for _ in range(number+1)]
    dp[0][1] = 1
    for i in range(1, number+1):
        # 직전의 경우의 수를 하나씩 더함 
        dp[i][1] = dp[i-1][1]
        if i >= 2:
            dp[i][2] = dp[i-2][1] + dp[i-2][2]
        if i >= 3:
            dp[i][3] = dp[i-3][1] + dp[i-3][2] + dp[i-3][3]
    result = sum(dp[number])
    return result


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        print(solution(int(input())))

        