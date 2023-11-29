import sys
from string import ascii_uppercase
input = sys.stdin.readline

name = input()

def solution(name):
    move = list(ascii_uppercase)
    target = "A" * len(name)
    cursor = True # if True: right, if False: left
    cnt = 0

    for i, char in enumerate(name): # name[i](인덱스로 찾아야됨)에서 target[i]를 뺀 것과 name[-1] - name[i] + target[i] 사이에서 비교
        # cnt += min( (move.index(name[i]) - move.index(target[i])), (len(move) - move.index(name[i]) + move.index(target[i])) )
        # 이전 커서가 우측을 향하고 있었다면
        if cursor: 
            nextmove = [move.index(name[i]) - move.index(target[i]), len(move) - move.index(name[i]) + move.index(target[i])]
            if nextmove[0] > nextmove[1]:
                cursor = False
                cnt += nextmove[1]
                cnt += 1
            else: 
                cnt += nextmove[0]

        # 이전에 왼쪽으로 이동했었다면
        else:
            nextmove = [move.index(name[i]) - move.index(target[i]), len(move) - move.index(name[i]) + move.index(target[i])]
            if nextmove[0] < nextmove[1]:
                cursor = True
                cnt += nextmove[0]
                cnt += 1
            else: 
                cnt += nextmove[1]


    return cnt


# a b c d e f g h i j k l m n o p q r x y z

# 이전 커서가 왼쪽 방향이었는지 오른쪽 방향이었는지까지 확인해줘야 함
# AAA 일때 JAA > JEE > JET 같이 뒷부분이 모두 한번에 바뀌어야 파악하기 편함
