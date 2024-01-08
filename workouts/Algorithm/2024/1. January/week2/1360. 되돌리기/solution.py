# 되돌리기가 되돌리기 되는 경우도 있으므로 history를 가지고 있을 필요가 있음
# undo 실행 이전에 마지막 chore를 기억하게 한 후 앞이 undo이면 앞에서 했던 일을 다시 되돌려야 함

import sys
input = sys.stdin.readline

n = int(input())
history = [['', 0]]


for _ in range(n):
    chore, letter, time = map(str, input().split())
    
    if chore == 'type':
        history.append([history[-1][0] + letter, int(time)])

    elif chore == 'undo':
        target = int(time) - history[-1][1]

        if 0 <= target <= len(history):
            history.append([history[target][0], int(time)])
        else:
            history.append([history[-1][0], time])

print(history[-1][0])

# =======================================================================================

### 이거 보고 수정하기
import sys
input = sys.stdin.readline

n = int(input())
hist = []
now = ''

for _ in range(n):
    flag = False
    command, char, time = map(str, input().split())
    if command == "type":
        now += char
        hist.append([int(time), now])
    else:
        char, time = int(char), int(time)
        for i in range(len(hist) - 1, -1, -1):
            if hist[i][0] >= (time - char):
                continue
            flag = True
            now = hist[i][1]
            hist.append([time, now])
            break
        if not flag:
            now = ''
            hist.append([time, now])

print(hist[-1][1])