import sys
from collections import deque

input = sys.stdin.readline

# 주어지는 원판은 아래에 있는 것부터 시작함
# deque를 사용해서 12345회 안에 이동시키기
# 각 횟수마다 이동하는 원판의 출발 및 도착지를 저장해서 출력

# def hanoi(saucer, start, end, mid):
#     if saucer == 1:
#         print(start, end)
#         return
    
#     hanoi(saucer - 1, start, end, mid)
#     print(start, end)
#     hanoi(saucer - 1, mid, end, start)

# 기존의 하노이 탑은 이상적인 모습으로 탑이 쌓여있다.
# 그러나 이 경우에는 탑의 모양이 무작위임
# 무작위로 옮길 것이 아니라 올라갈 수 있는 곳에 올려야 한다

N = int(input())
saucers = [list(map(int, input().split())), [], []]
move_max = 12345
count = 0 

# 잘 정렬되고 있는지 체크
def check(lst):
    if lst == sorted(lst, reverse=True):
        return True
    else:
        return False

def hanoi(saucer, start, end, mid):
    # 탈출 조건 (마지막 기둥에 1을 뺀 모든 원판이 올라감)
    if len(saucer[2]) + 1 == N:
        print(start, end)
        return
    
    
    
    if check(saucer[1] + [saucer[0][-1]]):
        saucer[1] = saucer[1] + [saucer[0][-1]]
        saucer[0] = saucer[0][::-1]
        
        hanoi()
    
    hanoi(saucer - 1, start, end, mid)
    print(start, end)
    hanoi(saucer - 1, mid, end, start)


hanoi(N, 1, 3, 2)
