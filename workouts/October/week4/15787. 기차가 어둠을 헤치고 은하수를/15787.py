# import sys
# input = sys.stdin.readline

# # 기차의 개수 m, 명령의 개수 n

# N, M = map(int, input().split())
# trains = [[0]*(21) for _ in range(N+1)]

# for _ in range(M):
#     orders = list(map(int, input().split())) # order, train, seat
#     order, train = orders[0], orders[1]
#     if len(orders) == 3:
#         seat = orders[-1]
#     else:
#         seat = 0

#     if order == 1 and trains[train][seat] == 0:
#         trains[train][seat] += 1
#     elif order == 2 and trains[train][seat] == 1:
#         trains[train][seat] -= 1
#     elif order == 3:
#         # 모든 승객을 뒤로 보냄 (0, 1번 좌석이 비워짐)
#         trains[train] = [0]*2 + trains[train][:-2]
#     elif order == 4:
#         # 모든 승객을 앞으로 보냄 (0, 20번 좌석이 비워짐)
#         trains[train] = [0] + trains[train][2::] + [0]


# answer = set([str(i) for i in trains if sum(i) != 0])

# print(*answer, sep="\n")
# print(len(answer))

import sys
input = sys.stdin.readline

# 기차의 개수 N, 명령의 개수 M

N, M = map(int, input().split())
trains = [[0] * 20 for _ in range(N)]

for _ in range(M):
    orders = list(map(int, input().split()))  # order, train, seat
    order, train = orders[0], orders[1]  - 1
    if len(orders) == 3:
        seat = orders[-1] - 1  # 좌석 번호를 0부터 19로 변경
    else:
        seat = 0

    if order == 1 and trains[train][seat] == 0:
        trains[train][seat] = 1
    elif order == 2 and trains[train][seat] == 1:
        trains[train][seat] = 0
    elif order == 3:
        # 모든 승객을 뒤로 보냄 (0, 1번 좌석이 비워짐)
        for i in range(19, 1, -1):
            trains[train][i] = trains[train][i - 1]
        trains[train][0] = 0
    elif order == 4:
        # 모든 승객을 앞으로 보냄 (0, 19번 좌석이 비워짐)
        for i in range(19):
            trains[train][i] = trains[train][i + 1]
        trains[train][19] = 0

answer = []
for train in trains:
    passenger = ''.join(str(i) for i in train)
    answer.append(passenger)

print(*answer, sep='\n')
print(len(set(answer)))
