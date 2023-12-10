import sys
input = sys.stdin.readline

# 탑의 개수, 사정거리, 초기 에너지, 적 좌표 X, 적 좌표 Y
n, r, d, x, y = map(int, input().split())
towers = list(map(int, input().split()) for _ in range(n))
map = 