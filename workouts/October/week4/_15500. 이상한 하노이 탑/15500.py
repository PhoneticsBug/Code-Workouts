import sys
from collections import deque

input = sys.stdin.readline

# 주어지는 원판은 아래에 있는 것부터 시작함
# deque를 사용해서 12345회 안에 이동시키기
# 각 횟수마다 이동하는 원판의 출발 및 도착지를 저장해서 출력

# 기존의 하노이 탑은 이상적인 모습으로 탑이 쌓여있다.
# 그러나 이 경우에는 탑의 모양이 무작위임
# 무작위로 옮길 것이 아니라 올라갈 수 있는 곳에 올려야 한다

# 1 > 3, 2 > 3, 2 > 1 세가지의 경우를 모두 넣어줘서 구현하는 방법이 있음!


N = int(input())
saucers = [list(map(int, input().split())), [], []]
hanoi = [saucers, [], []]
target_num = N
cnt = 0
result = []

# 마지막 기둥에 있어야 하는 원판은 고정하는 쪽이 편할거 같다

while target_num > 0: 

    # 첫번째 기둥에 있다면
    if target_num in hanoi[0]:
        while hanoi[0]:
            now = hanoi[0].pop() # 가장 마지막 숫자를 꺼내서 now에 저장
            if now == target_num:
                result.append("1 3")
                cnt += 1
                break
            else:
                result.append("1 2") # 두번째 스택으로 이동
                cnt += 1
                hanoi[1].append(now)
    
    # 두번째 기둥에 있다면
    elif target_num in hanoi[1]:
        while hanoi[1]:
            now = hanoi[1].pop() # 마지막 숫자를 꺼내서 저장
            if now == target_num:
                result.append("2 3")
                cnt += 1
                break
            else:
                result.append("2 1")
                cnt += 1
                hanoi[0].append(now)

print(cnt)
print("\n".join(result))
