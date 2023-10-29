import sys
from collections import deque, defaultdict
input = sys.stdin.readline

max_num = 100_000

def bfs(prime, a, b, start):
    queue = deque([(start, 0)])
    visited = defaultdict(lambda: False)

    # 시작 수가 a 이상 b 이하의 소수인 경우
    if (a <= start <= b) and prime[start]:
        return 0
    visited[start] = True

    while queue:
        curr, count = queue.popleft()

        movements = [curr//2, curr//3, curr+1]
        if curr != 0:
            movements.append(curr-1)
        
        for nxt in movements:
            if visited[nxt]:
                continue
            if (a <= nxt <= b) and prime[nxt]:
                return count + 1
            
            queue.append((nxt, count+1))
            visited[nxt] = True

def solution():
    # 소수 판별: 에라토스테네스의 체
    prime = [False, False] + [True for _ in range(max_num+1)]
    for num in range(2, max_num+1):
        if prime[num] == True:
            for multi_num in range(2*num, max_num+1, num):
                prime[multi_num] = False
    return prime
prime = solution()

t = int(input())

for _ in range(t):
    n, a, b = map(int, input().split()) # 생명체 수, 줄여나갈 목표범위
    print(bfs(prime, a, b, n))


# 소수 리스트를 만들고
# 이분탐색으로 찾다가 범위 안에 있는 소수 중 가장 작은 수 찾기
# 없으면 -1 출력