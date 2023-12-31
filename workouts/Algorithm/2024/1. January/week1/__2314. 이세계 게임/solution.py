import sys
input = sys.stdin.readline

# bfs 탐색
# 1. 수평방향을 고려한 이동
# 2. 수직방향을 고려한 이동
# - 큐에서 pop된 값을 목표값과 비교하며 진행

from collections import deque

def arr2bit(arr):
    bit = ''
    for i in range(4):
        for j in range(4):
            bit += arr[i][j]

        return bit
    
def bit2arr(bit):
    arr = []
    for i in range(4):
        arr.append(list(bit[i*4:(i+1)*4]))
    
    return arr

inputs = []

while len(inputs) < 8:
    tmp = input()
    if not tmp:
        continue
    inputs.append(list(tmp.rstrip()))

current_board = inputs[:4]
target_board = inputs[4:]

trans = {
    'L' : '0',
    'P' : '1'
}

for i in range(4):
    for j in range(4):
        current_board[i][j] = trans[current_board[i][j]]
        target_board[i][j] = trans[target_board[i][j]]

targetbit = arr2bit(target_board)
startbit = arr2bit(current_board)

q = deque()
q.append(startbit)

visited = dict()
visited[startbit] = 0

