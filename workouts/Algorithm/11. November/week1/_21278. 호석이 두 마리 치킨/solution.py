import sys
input = sys.stdin.readline

n, m = map(int, input().split()) # 건물의 개수, 도로의 개수
road = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split()) # 도로의 정보
    road[a-1].append(b)
    road[b-1].append(a)
distance = [0]*(m+1)

# 1. 가중치가 없음
# 2. 모든 건물에 대해 거리를 계산하고, 그 값이 가장 작은 시작점 두개와 거리의 합(모든 도시에서의 왕복시간의 합)

print(road)