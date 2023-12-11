import sys
input = sys.stdin.readline

from heapq import heappop, heappush

jobs = [[0, 3], [1, 9], [2, 6]]


def solution(jobs):
    time, task = 0, 0
    length = len(jobs)
    jobs.sort(key = lambda x: x[1])

    while len(jobs) > 0:
        for i in jobs:
            if i[0] <= time:
                jobs.remove(i)
                time += i[1] - 1
                task += time - i[0] + 1
                break
        time += 1
    return task // length
    

def solution(jobs):
    answer, now, cnt = 0, 0, 0
    start = -1
    heap = []

    while cnt < len(jobs):
        for i in jobs:
            if start < i[0] <= now:
                heappush(heap, [i[1], i[0]])
        if len(heap) > 0:
            current = heappop(heap)
            start = now
            now += current[0]
            answer += (now - current[1])
            cnt += 1
        else:
            now += 1
    return answer // len(jobs)