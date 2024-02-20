import sys
from collections import deque
input = sys.stdin.readline

# 전체 사람의 수
n = int(input())

# 촌수를 계산해야하는 사람들의 번호
a, b = map(int, input().split())

# 부모 자식들간의 관계 수
m = int(input())

family = [[] for _ in range(n+1)]
for _ in range(m):
    x, y = map(int, input().split())
    family[x].append(y)
    family[y].append(x)

visited = [False]*(n+1)
answer = -1

def solution(start, end, cnt):
    global answer
    
    cnt += 1
    visited[start] = True

    if start == end:
        answer = cnt
    
    for i in family[start]:
        if not visited[i]:
            solution(i, end, cnt)

solution(a, b, -1)
print(answer)