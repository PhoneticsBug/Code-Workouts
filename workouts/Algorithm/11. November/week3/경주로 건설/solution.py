import sys
input = sys.stdin.readline

from collections import deque
from math import inf


# def is_out_ofrange(maximum, row, col):
#     if 0 <= row < maximum and 0 <= col < maximum:
#         return False

#     return True


# UP, RIGHT, DOWN, LEFT = 0, 1, 2, 3


# def bfs(board, maximum):
#     # row, col, direction, cost
#     queue = deque([(0, 0, RIGHT, 0), (0, 0, DOWN, 0)])

#     costs = [[[inf] * maximum for  in range(maximum)] for _ in range(4)]
#     for i in range(4):
#         costs[i][0][0] = 0

#     # up, right, down, left
#     movements = [(-1, 0), (0, 1), (1, 0), (0, -1)]

#     while queue:
#         row, col, prev_d, cost = queue.popleft()

#         for curr_d, (rd, cd) in enumerate(movements):
#             nr, nc = row + rd, col + cd
#             if is_out_of_range(maximum, nr, nc):
#                 continue

#             if board[nr][nc] == 1:
#                 continue

#             curr_cost = cost + (100 if curr_d == prev_d else 600)

#             if costs[curr_d][nr][nc] <= curr_cost:
#                 continue

#             queue.append((nr, nc, curr_d, curr_cost))
#             costs[curr_d][nr][nc] = curr_cost

#     return min([costs[i][-1][-1] for i in range(4)])


# def solution(board):
#     return bfs(board, len(board))