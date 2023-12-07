import sys
input = sys.stdin.readline

from heapq import heappop, heappush

jobs = [[0, 3], [1, 9], [2, 6]]

def solution(jobs):
    count, last, answer = 0, -1, 0
    heap = []
    jobs.sort()
    time = jobs[0][0]
    while count < len(jobs):
        # 현재 시간 이하의 모든 요청을 heap에 추가
        for s, t in jobs:
            if last < s <= time:
                heappush(heap, (t, s))
        # heap에 이미 작업이 있는 경우 (옮기는 중일 때)
        if len(heap) > 0:
            count += 1 # 기다리는 시간 추가
            last = term, start = heappop(heap)
            time += term
            answer += (time - start)
        else:
            time += 1
    return answer // len(jobs)