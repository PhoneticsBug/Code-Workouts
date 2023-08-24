works = [4, 3, 3]
n = 4

# ----- try 1 -----
def solution(n, works):
    answer = 0
    while n > 0:
        for i in range(len(works)):
            if n <= 0:
                break
            n -= 1
            works[i] -= 1

    for j in works:
        if j <= 0:
            temp = works.index(j)
            works = works[:temp] + works[temp+1:]
            
    answer = sum(i**2 for i in works) 

    return answer

# ----- try 2 ----- 
# 효율성 테스트에서 0점이 나옴

def solution(n, works):
    answer = 0
    while n > 0 and max(works) > 0: # 시간이 남아있는 동안, 마이너스가 되지 않게 하기
        max_idx = works.index(max(works))
        works[max_idx] -= 1
        n -= 1

    answer = sum(i**2 for i in works)
    return answer

# ----- try 3 -----

import heapq

def solution(n, works):
    answer = 0

    # 시간 안에 모든 작업을 끝내는 경우
    if n >= sum(works): 
        return 0
    # 최대 힙을 사용하기 위해 음수로 저장
    heap = [-work for work in works] 
    heapq.heapify(heap)

    while n > 0:
        # 최대값 갱신, 최대값이 0이면 break
        maxwork = -heapq.heappop(heap)
        if maxwork == 0:
            break
        # 최대값이 1 감소할 때마다 시간도 1 감소
        heapq.heappush(heap, -(maxwork - 1)) 
        n -= 1

    answer = sum(i**2 for i in heap)
    return answer

# ----- answer -----

print(solution(n, works))