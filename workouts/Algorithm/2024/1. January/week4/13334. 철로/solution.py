# 집과 사무실의 거리가 철로의 길이보다 짧을 때에만 철로를 놓는 것이 의미가 있다.
# 

import sys
from heapq import heappop, heappush
input = sys.stdin.readline

n = int(input())

# 일단 모든 데이터를 받아줌
roads, temp = [], []
for _ in range(n):
    temp.append(sorted(list(map(int, input().split()))))
# 철로의 길이
length = int(input())
# 전체 철로의 길이보다 짧은 경우에만 roads에 입력
for road in temp:
    s, e = road
    if (e - s) <= length:
        roads.append(road)
# end 값으로 정렬
roads.sort(key = lambda x: x[1])

answer = 0
q = []

# 각 도로를 순회하며 설치여부 확인
for road in roads:
    # q가 비어있으면 일단 설치
    if not q:
        heappush(q, road)
    else:
        # 출퇴근거리가 철도 위에 있는지 확인
        # 없으면 제거
        while q[0][0] < road[1] - length:
            heappop(q)
            if not q:
                break
        # 조건이 만족되면 철도 설치
        heappush(q, road)
    # 최대값 추출
    answer = max(answer, len(q))
print(answer)


