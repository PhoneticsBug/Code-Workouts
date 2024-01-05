import sys
input = sys.stdin.readline

direction = ("U", "R", "D", "L")
dx, dy = (-1, 0, 1, 0), (0, 1, 0, -1)
p, q = (1, 0, 3, 2), (3, 2, 1, 0)

n, m = map(int, input().split())
a = [["C"]*(m+2)]

for _ in range(n):
    a.append(["C"] + list(input().strip()) + ["C"])

a.append(["C"]*(m+2))

sr, sc = map(int, input().split()) # 탐사선의 위치

def solution():
    maxtime, maxdir = 0, 0
    for sd in range(4):
        r, c, d, time = sr, sc, sd, 1 # 시작위치, 시작방향, 이동시간

        while True:
            # 블랙홀을 만나거나 항성계를 벗어냔 경우
            if a[r + dx[d]][c + dy[d]] == "C":
                break

            r += dx[d]
            c += dy[d]

            # 방향 전환
            if a[r][c] == "/":
                d = p[d]
            elif a[r][c] == "\\":
                d = q[d]
            time += 1

            # 처음 출발한 지점을 동일한 방향으로 접근한 후 무한 루프
            if (r, c, d) == (sr, sc, sd):
                print(direction[sd])
                print("Voyager")
                return
            # 값이 클 때만 이동시간 및 현재 방향 갱신
            if maxtime < time:
                maxtime = time
                maxdir = sd

    print(direction[maxdir])
    print(maxtime)

solution()