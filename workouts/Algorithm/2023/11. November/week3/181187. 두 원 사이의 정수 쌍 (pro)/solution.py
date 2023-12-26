import sys
input = sys.stdin.readline

# r2와 r1 사이에 존재하는 모든 점의 개수 찾기 
# 큰 원에 닿는건 언제나 4개
# 작은 원에서의 

def solution(r1, r2):
    answer = 0
    for x in range(1, r2+1):
        a = int((r2**2 - x**2)**0.5)*2 + 1 # r2 원의 y좌표 계산
        b = 0

        if x < r1:
            b = (r1**2 - x**2)**0.5 # r1원의 y좌표 계산
            if b == int(b): # y좌표가 정수인 경우 포함시키기
                b = b*2 - 1
            else: # y좌표가 정수가 아닌 경우 그보다 작은 정수 포함시키기
                b = int(b)*2 + 1

        answer += (a - b) # 우측 구간의 정수좌표 넣기

    answer = (answer)*2 + 2*(r2 - r1 + 1) # x2 해서 1, 4분면(좌측)의 좌표 추가, 2 * (r2 - r1 + 1) = x가 0일 때의 값 추가
    
    return answer