import sys
input = sys.stdin.readline

T, W = map(int, input().split())
plums = list(int(input()) for _ in range(T))
dp = [[0]*(T+1) for _ in range(W+1)]

# 