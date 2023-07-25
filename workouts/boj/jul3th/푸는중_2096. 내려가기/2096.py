import sys 
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

# 양끝단의 경우 [0, 1], [1, 2], 그 외의 경우 아래의 모든 인덱스 중 최대값/최소값 검색

for i in range(n):
    for j in range(n):
        