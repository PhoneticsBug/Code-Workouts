import sys
input = sys.stdin.readline

n = int(input())
buses = list(list(map(str, input().split())) for _ in range(n))
maintainance = n

for i in range(n):
    for j in range(n):
        if buses[i][1] == buses[j][0]:
            maintainance -= 1

print(maintainance)

# 가장 간단한 방법이지만 n이 10만개까지 존재하므로 시간초과 발생 (2중 for문 사용하면 안됨)

import sys
from heapq import heappush, heappop
input = sys.stdin.readline

n = int(input())
buses = list(list(map(str, input().split())) for _ in range(n))
buses.sort()

heap = []
heappush(heap, buses[0][1])

for i in range(1, n):
    # 버스가 새로 왔을 때 빈 공간이 없다면 heap에 추가, 있으면 그대로 추가
    if buses[i][0] >= heap[0]:
        heappop(heap)
        heappush(heap, buses[i][1])
    else:
        heappush(heap, buses[i][1])

print(len(heap))