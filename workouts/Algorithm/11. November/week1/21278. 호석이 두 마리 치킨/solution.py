# 1. 가중치가 없음
# 2. 모든 건물에 대해 거리를 계산하고, 그 값이 가장 작은 시작점 두개와 거리의 합(모든 도시에서의 왕복시간의 합)
# 3. 건물 두개를 설치했을 때의 거리를 계산하기
# 4. 공기청정기 문제와 비슷함

import sys
from itertools import combinations
input = sys.stdin.readline

n, m = map(int, input().split()) # 건물의 개수, 도로의 개수


def solution(n, m):
    distances = [[float("inf")]*(n+1) for _ in range(n+1)] # 거리를 저장하기 위한 초기화값

    for _ in range(m):
        a, b = map(int, input().split()) # 도로의 정보
        distances[a][b] = 1
        distances[b][a] = 1

    # 플로이드 워셜
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                if a != b:
                    distances[a][b] = min(distances[i][j], distances[i][k] + distances[k][j])
    
        # 조합 리스트
        combination = list(combinations(range(1, n+1), 2))

        # 정렬
        combination.sort(key = lambda x : [sum([2 * min(distances[i][x[0]], distances[i][x[1]]) for i in range(1, n + 1) if i not in x]), min(x), max(x)])
        n1, n2 = combination[0][0], combination[0][1]

    print(*combination[0], sum([2*min(distances[i][n1], distances[i][n2]) for i in range(1, n+1) if i not in (n1, n2)]))

solution(n, m)