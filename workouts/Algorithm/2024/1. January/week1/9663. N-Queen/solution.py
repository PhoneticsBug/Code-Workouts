# 배치된 퀸의 직선 및 대각선상에 아무것도 놓을 수 없음
# 퀸의 개수는 총 n개이므로 n * n 배열 위를 오가며 n개의 퀸을 놓을 수 있는 곳을 찾아야 함
# 브루트포스로 풀었을 때의 시간복잡도는 O(n**2)
# 백트래킹으로 풀었을 때 좀 더 효율적으로 풀 수 있음
# 받는 배열은 2차원이 아니라 1차원으로 받아야 시간초과가 발생하지 않는다.
# 즉, 퀸이 놓인 배열의 위치만 저장해도 충분히 풀 수 있음

import sys
input = sys.stdin.readline

n = int(input())
row = [0] * n
ans = 0

# 퀸 체크 함수
def isQueen(x):
    for i in range(x):
        if row[x] == row[i] or abs(row[x] - row[i]) == abs(x-i):
            return False
    return True

def nQueens(x):
    global ans
    if x == n:
        ans += 1
        return
    
    else:
        for i in range(n):
            row[x] = i
            if isQueen(x):
                nQueens(x+1)

nQueens(0)
print(ans)