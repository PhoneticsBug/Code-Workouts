import sys
input = sys.stdin.readline

# 각 산 정상까지의 거리는 sqrt.(i**2 *2) + sqrt(i+1)**2 *2

n = int(input())
mountains = list(map(int, input().split()))
cnt = 0

def solution(n, mountains):
    dp = [0]*(n+1)
    for i in range(1, n):
        dp[i] = float('inf')
        for j in range(i):
            dp[i] = min()