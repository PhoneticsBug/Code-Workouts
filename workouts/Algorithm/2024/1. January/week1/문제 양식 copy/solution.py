import sys
input = sys.stdin.readline

n = int(input())
buses = list(list(map(str, input().split())) for _ in range(n))
maintainance = n

for i in range(n):
    for j in range(n):
        if buses[i][1] == buses[j][0]:
            maintainance -= 1

print(maintainance)

# 가장 간단한 방법이지만 n이 10만개까지 존재하므로 시간초과 발생 (2중 for문 사용하면 안됨)