import sys
input = sys.stdin.readline

n = int(input())
rc = [list(map(int, input().split())) for _ in range(n)]
dp = []