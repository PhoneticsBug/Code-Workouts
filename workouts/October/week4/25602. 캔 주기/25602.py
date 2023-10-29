import sys
import itertools
input = sys.stdin.readline

N, K = map(int, input().split()) # 캔의 종류, K일
A = list(map(int, input().split())) # 집사가 가진 캔의 수 배열
R = [list(map(int, input().split())) for _ in range(K)]  # 랑이의 선호도
M = [list(map(int, input().split())) for _ in range(K)]  # 메리의 선호도


# 각 날마다의 만족도를 고려해서 가장 높은 만족도를 만들기
# 주는 캔은 하루에 한 고양이당 하나

ans = float("-inf")

def solution(cat, day, arr):
    global ans

    # 마지막 날일때 메리에게 간식 주고 끝내기 (최대값 갱신)
    if day == K: 
        if cat == "R":
            solution("M", 0, arr)
        else:
            ans = max(ans, arr)
        return

    # 그 전에는 계속 간식주기
    for treat in range(N):
        # 간식을 다 줬다면, 패스
        if A[treat] == 0:
            continue

        A[treat] -= 1

        if cat == 'R':
            solution(cat, day + 1, arr + R[day][treat])
        else:
            solution(cat, day + 1, arr + M[day][treat])

        A[treat] += 1

solution('R', 0, 0)

print(ans)