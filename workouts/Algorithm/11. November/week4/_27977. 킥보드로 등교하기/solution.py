import sys
input = sys.stdin.readline

def solution(l, n, k, station):
    # left, right = max(station[i+1] - station[i], station[i]) if i < len(station)-1 else l - station[i] for i in range(len(station)), l # <<< 제대로 작동 안됨
    right = l
    left = -2000001
    for i in range(n):
        if i == 0: # 0번 인덱스의 경우만
            left = max(station[i], station[i+1] - station[i]) # 현재값과 다음값 - 현재값 중 더 큰 값
        elif i == n - 1: # 마지막 인덱스의 경우 
            left = max(left, l - station[-1]) # left와 l - 마지막 인덱스
        else:
            left = max(left, station[i+1] - station[i])

    station += [l] # 도착지점 표시
    while left <= right: # 이분탐색 기본조건
        mid = (left + right) // 2 
        cnt, now = 0, mid
        for idx, d in enumerate(station): # 인덱스, 요소 in enumerate():
            dist = d - station[idx -1] if idx > 0 else d
            if now < dist:
                now = mid - dist
                cnt += 1
            else:
                now -= dist
        if cnt > k: # 방문 횟수가 k보다 큰 경우 / 같거나 작은 경우
            left = mid + 1
        else:
            right = mid - 1
    return left
        
# 학교까지의 거리, 충전소 개수, 최대 충전소 방문 횟수
l, n, k = map(int, input().split())
station = list(map(int, input().split()))

print(solution(l, n, k, station))


#####

import sys
input = sys.stdin.readline

def solution(l, n, k, station):
    values = [max(station[i+1] - station[i], station[i]) if i < len(station)-1 else l - station[i] for i in range(len(station))]
    left, right = max(values), l

    station += [l] # 도착지점 표시
    while left <= right: # 이분탐색 기본조건
        mid = (left + right) // 2 
        cnt, now = 0, mid
        for idx, d in enumerate(station): # 인덱스, 요소 in enumerate():
            dist = d - station[idx -1] if idx > 0 else d
            if now < dist:
                now = mid - dist
                cnt += 1
            else:
                now -= dist
        if cnt > k: # 방문 횟수가 k보다 큰 경우 / 같거나 작은 경우
            left = mid + 1
        else:
            right = mid - 1
    return left
        
# 학교까지의 거리, 충전소 개수, 최대 충전소 방문 횟수
l, n, k = map(int, input().split())
station = list(map(int, input().split()))

print(solution(l, n, k, station))