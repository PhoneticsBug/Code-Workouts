import sys
input = sys.stdin.readline

n = int(input()) # 라이언이 가진 화살의 개수
info = list(map(int, input().split())) # 어피치가 맞힌 과녁의 점수

def solution(n, info):
    answer = [0]*11 
    board = [0]*11
    diff = 0

    for subset in range(1, 1 << 10): # 서브셋 사용(1024개?의 부분집합?)
        ryan, appeach = 0, 0
        cnt = 0

        for i in range(10):
            if subset & (1<<i): # 현재 탐색중인 부분집합에서 i번째 원소가 포함되는지 확인
                ryan += 10 - i
                board[i] = info[i] + 1 # 해당 점수를 얻기 위한 최소조건 (한번 더 맞춘다)
                cnt += board[i]
            else:
                board[i] = 0
                if info[i]: # 어피치만 맞춘 점수인 경우
                    appeach += 10 - i

        if cnt > n:
            continue

        board[10] = n - cnt # 나머지 화살은 전부 0점으로

        # 낮은 점수를 더 많이 맞추는지 확인
        if ryan - appeach == diff:
            for j in reversed(range(11)):
                if board[j] > answer[j]:
                    diff = ryan - appeach
                    answer = board[:]
                    break
                elif board[j] < answer[j]:
                    break

        elif ryan - appeach > diff:
            diff = ryan - appeach
            answer = board[:]

    if diff == 0:
        answer = [-1]

    return answer

# info의 i 번째 원소는 10 - i점을 맞힌 화살의 개수
# 화살이 남는 경우 전부 0점에 몰아주면 됨

