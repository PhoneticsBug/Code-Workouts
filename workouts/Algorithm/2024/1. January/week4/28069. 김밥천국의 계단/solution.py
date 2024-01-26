# 무수한 계단(0부터 시작) 중 김밥천국의 위치는 n번째 계단
# 민희의 이동방법은 매번 2가지로, k번 선택하여 이동할 수 있음
# 정확히 k번 이동해서 도달해야 김밥을 먹을 수 있다.

# 행동루틴
# 1. 계단 한 칸을 올라간다
# 2. i + [i/2] 번째 계단으로 순간이동
# i + i//2 로 이동할 수 있다.

# 먹을 수 있으면 minigimbob, 없으면 water 출력

import sys
input = sys.stdin.readline

# 김밥집의 위치 n, 이동가능한 횟수 k
n, k = map(int, input().split())

# 현재 위치
now = 0
# 민희가 선택한 이동방식 // 1 = A, 2 = B
dp = [[False]*(k+1) for _ in range(n+1)]
dp[0][0] = True

# 한 계단 올라가기
def A(i):
    return i + 1

# 순간이동하기
def B(i):
    return i + i//2

for i in range(n+1):
    for j in range(k):
        if dp[i][j]: # i번 계단에 j번의 이동으로 도달하면
            # 이동 A
            if A(i) <= n and j+1 <= k:
                dp[A(i)][j+1] = True
            # 이동 B
            if B(i) <= n and j+1 <= k:
                dp[B(i)][j+1] = True

if dp[n][k]:
    print('minigimbob')
else:
    print('water')

# 시간초과 ----------------------------------------------------

# i == 0일때 2번 연산을 사용하면 언제나 결과값이 0이 됨
# 따라서 실제로는 k번 이내에 도달하기만 하면 됨
import sys
input = sys.stdin.readline

# 김밥집의 위치 n, 이동가능한 횟수 k
n, k = map(int, input().split())

dp = [0] + [float('inf')]*n

for i in range(n):
    # 1칸 올라가기
    dp[i+1] = min(dp[i+1], dp[i] + 1)
    # 순간이동
    m = i + i // 2
    if m <= n:
        dp[m] = min(dp[m], dp[i] + 1)

print('minigimbob' if dp[n] <= k else 'water')
