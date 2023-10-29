import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
if m != 0:
    btn = set(map(int, input().split()))
else:
    btn = ()

def solution(channel, btn): # 이동 가능한 채널 검사
    if channel == 0: # 0인 경우 0 버튼만 확인
        if 0 in btn:
            return False
        return True

    while channel > 0: # 자릿수를 옮겨가며 검사
        digit = channel % 10 
        if digit in btn:
            return False
        channel //= 10
    return True

min_press_cnt = abs(n - 100)

for channel in range(1_000_001): # 이동할 전체 채널 중에서 검사
    if solution(channel, btn):
        press_count = len(str(channel)) + abs(n - channel)
        min_press_cnt = min(min_press_cnt, press_count)

print(min_press_cnt)
