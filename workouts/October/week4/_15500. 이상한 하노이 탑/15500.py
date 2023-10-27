import sys
from collections import deque

input = sys.stdin.readline

# 주어지는 원판은 아래에 있는 것부터 시작함
# deque를 사용해서 12345회 안에 이동시키기
# 각 횟수마다 이동하는 원판의 출발 및 도착지를 저장해서 출력

N = int(input())
saucers = list(map(int, input().split()))
move_max = 12345
count = 0 

def hanoi(saucers, start, end, mid):
    if saucers == 1:
        print(start, end)
        return
    
    hanoi(saucers[::-1], start, end, mid)
    print(start, end)
    hanoi(saucers[::-1], mid, end, start)