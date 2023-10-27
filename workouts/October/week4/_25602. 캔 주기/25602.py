import sys
input = sys.stdin.readline

N, K = map(int, input().split())
A = list(map(int, input().split())) # 집사가 가진 캔의 수 배열
M = [list(map(int(input().split()))) for _ in range(K)] # 메리의 선호도
R = [list(map(int(input().split()))) for _ in range(K)] # 랑이의 선호도

# 각 날마다의 만족도를 고려해서 가장 높은 만족도를 만들기
# 주는 캔은 하루에 한 고양이당 하나
