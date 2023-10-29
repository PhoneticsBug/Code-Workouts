import sys
input = sys.stdin.readline

words = 0
target = 0
begin = 0

# visited[true, true ... ]를 이용해 target에 도달할 때까지 방문
# 더 멀리 돌아가는 경우나 빠르게 도달하는 경우 등 변수가 있을 수 있음
# len(visited == true)의 min 값을 도출