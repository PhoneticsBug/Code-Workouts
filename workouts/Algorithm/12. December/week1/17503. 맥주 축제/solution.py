import sys
from heapq import heappop, heappush
input = sys.stdin.readline

# 축제기간, 선호도 합, 맥주 종류의 수
n, m, k = map(int, input().split())
beers = [list(map(int, input().split())) for _ in range(k)]
beers = sorted(beers, key=lambda x: (x[1], x[0]))  # 도수 레벨을 기준으로 정렬

answer, like, arr = -1, 0, []

for beer in beers:
    like += beer[0]
    heappush(arr, beer[0])  # 현재 선택된 맥주의 선호도를 우선순위 큐에 추가

    if len(arr) == n:
        if like >= m:  # 총 선호도가 M 이상인 경우
            answer = beer[1]  # 현재의 간 레벨을 결과에 저장
            break
        else:
            like -= heappop(arr)  # 가장 선호도가 낮은 맥주를 우선순위 큐에서 제거

print(answer)
