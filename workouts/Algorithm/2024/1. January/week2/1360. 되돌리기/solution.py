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

# 일부만 맞춰서 잘 안됨

# =======================================================================================

import sys
input = sys.stdin.readline

n = int(input())
history = []
word = ""

for _ in range(n):
    isUndo = False
    command, char, time = map(str, input().split())

    # 입력해야 하는 경우 > word를 갱신하고 hist에 저장
    if command == "type":
        word += char 
        history.append([int(time), word])

    # undo 명령어인 경우에는
    else:
        char, time = int(char), int(time) # int형으로 변환

        for i in range(len(history)-1, -1, -1): # 역순으로 확인
            # word를 바꿀 수 없는 경우 (되돌리는 시간이 입력값의 위치만큼 가지 못함)
            if history[i][0] >= (time - char):
                continue
            
            isUndo = True
            # 해당하는 시간대의 문자열로 회귀
            word = history[i][1]
            history.append([time, word])
            break
        # undo되지 않은 경우
        if not isUndo:
            word = ""
            history.append([time, word])

print(history[-1][1])