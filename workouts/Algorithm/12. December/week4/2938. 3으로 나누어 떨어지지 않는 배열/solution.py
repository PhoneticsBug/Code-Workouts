# import sys
# from itertools import permutations

# input = sys.stdin.readline

# n = int(input())
# arr = list(map(int, input().split()))

# arrs = list(permutations(arr))

# def check(a, b):
#     if (a + b) % 3 == 0:
#         return False
#     return True

# to_remove = []

# for ar in arrs:
#     # 바로 다음 요소와의 합 확인
#     for i in range(len(ar) - 1):
#         if not check(ar[i], ar[i+1]):
#             to_remove.append(ar)
#             break  # 중복 삭제 방지

# # 임시 리스트에 저장된 요소 삭제
# for item in to_remove:
#     arrs.remove(item)

# print(*arrs[0])

###############################################################################################

from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

# 3으로 나눈 나머지로 분류할 큐 생성
q = [deque() for _ in range(3)]

# 각 숫자를 3으로 나눈 나머지를 저장
for i in range(n):
    q[arr[i] % 3].append(arr[i])

# 불가능한 경우
# 1. 3으로 나누어 떨어지는 수가 절반 이상
# 2. 3으로 나누어 떨어지지 않는 수가 없음
if len(q[0]) > (n + 1)//2 or len(q[0]) == 0 and len(q[1]) != 0 and len(q[2]) != 0:
    print(-1)
    
# 나머지가 1을 출력하면서 남아있는 인덱스 0도 함께 출력 (하나는 남겨둘 것)
while len(q[1]) != 0:
    if len(q[0]) > 1:
        print(q[0].popleft(), end=' ') 
    print(q[1].popleft(), end=' ')

# 나머지 0 출력
if len(q[0]) != 0:
    print(q[0].popleft(), end=' ')

# 나머지 2 출력
while len(q[2]) != 0:
    print(q[2].popleft(), end=' ')
    if len(q[0]):
        print(q[0].popleft(), end=' ')




