# import sys
# input = sys.stdin.readline

# n, l = map(int, input().split())
# lake = 0

# for _ in range(n):
#     start, end = map(int, input().split())
#     lake += (end - start)

# if lake % l == 0:
#     print(lake//l)
# else:
#     print(lake//l + 1)

# ----- 널빤지가 웅덩이 사이를 덮고 다음 웅덩이로 넘어가버리는 경우를 생각해야 함 ----

# bridge = 0
# path = []
# for _ in range(n):
#     start, end = map(int, input().split())
#     path.append([start , end])

# path.sort() # 정렬?

# for i in range(len(path)):
#     fond = path[i]
#     lefty = 0
#     bridge += (fond[1] - fond[0])//l
#     lefty = (fond[1] - fond[0])%l
#     if i != 0 and (fond[1] + lefty) > path[i+1][0]:
#         path[i+1][0] += ((fond[1] + lefty) - path[i+1][0])

# print(bridge)

# ----- ----- ----- -----

import sys
input = sys.stdin.readline

n, l = map(int, input().split())

path = []
for _ in range(n):
    start, end = map(int, input().split())
    path.append([start , end])

path.sort()

bridge = 0
prev_end = 0

for start, end in path:
    