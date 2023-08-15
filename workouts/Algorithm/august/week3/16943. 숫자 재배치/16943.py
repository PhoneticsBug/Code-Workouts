import sys
from itertools import permutations
input = sys.stdin.readline

# 백트래킹 기본 구조
# n, m = map(int, input().split())
# visited = [False] * (n+1)
# answer = []

# def backtracking(depth, n, m):
    
#     if depth == m:
#         print(' '.join(map(str, answer)))

#     for i in range(1, n+1):
#         if not visited[i]:
#             visited[i] = True
#             answer.append(i)
#             backtracking(depth+1, n, m)
#             visited[i] = False
#             answer.pop()

# backtracking(0, n, m)

# =============================================================
# a를 입력받았을 때 a의 구성요소로 이루어진 숫자 중 가장 큰 숫자를 찾는 문제
# 단순히 문자열로 받아서 실행하면 빠르게 될거같은데...? 
# a의 자릿수가 b보다 크면 -1 출력


# a, b = map(int, input().split())
# c = 1
# visited = [False]*(10e9+1)

# def track(start, a, b):
#     return True


# if a > b:
#     print(-1)
# else:
#     track(c, a, b)

# 백트래킹으로 풀 방법이 생각나지 않으니 일단 permutation으로 풀어보자

import sys
from itertools import permutations
input = sys.stdin.readline

a, b = map(int, input().split())

# permutations를 이용해 만들 수 있는 모든 순열 생성 
perm = [int(''.join(j for j in i)) for i in permutations(str(a))]
# 순열 중 b보다 작고 맨 앞에 0이 오지 않는 수만 남기기 (앞에 0이 오면 길이가 달라짐)
perm = list(filter(lambda x: x < b and len(str(x)) == len(str(a)), perm))

if len(perm) == 0 :
    print(-1)
else:
    print(max(perm)) 
# 성공