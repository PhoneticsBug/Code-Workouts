import sys
input = sys.stdin.readline

n = int(input())
dots = [list(map(int, input().split())) for _ in range(n)]

# 해당하는 점이 정사각형의 변 위에만 올라가야 함
# 변이 대각선으로 존재하는 경우는 고려하지 않는듯함

# 좌표(x, y)와 길이 1로 정의된 정사각형이 모든 점을 포함하는지 확인
def solution(dots, x, y, l):
    for dot in dots:
        # 현재 점이 정사각형 안에 들어가는지 확인
        if min(x, x + l) <= dot[0] <= max(x, x + l) and (dot[1] == y or dot[1] == y + l):
            continue
        elif (dot[0] == x or dot[0] == x + l) and min(y, y + l) <= dot[1] <= max(y, y + l):
            continue
        else:
            return False
    else:
        return True

minx, miny = min([dots[i][0] for i in range(n)]), min([dots[i][1] for i in range(n)])
maxx, maxy = max([dots[i][0] for i in range(n)]), max([dots[i][1] for i in range(n)])

# 정사각형의 변 길이
l = max(maxx - minx, maxy - miny)

if solution(dots, minx, miny, l) or solution(dots, maxx, miny, l) or solution(dots, minx, maxy, l) or solution(dots, maxx, maxy, l) or solution(dots, maxx, maxy, -l):
    print(l)
else:
    print(-1)