import sys
input = sys.stdin.readline
# 2차원 리스트 eggs의 각 리스트 속 인덱스는 내구도와 무게임

def solution(start):
    global answer

    if start == n: # 종료 조건
        total = 0
        for i in range(n):
            if eggs[i][0] <= 0:
                total += 1
        answer = max(answer, total)
        return # answer에 저장

    if eggs[start][0] <= 0: # 지금 든 계란이 깨지면
        solution(start+1) 
        return # 다음 게란으로 넘김
    
    check = True # 계란의 깨짐 여부
    for i in range(n):
        if i == start:
            continue
        if eggs[i][0] > 0: 
            check = False
            break
    
    if check: # 계란이 다 깨진 경우
        answer = max(answer, n-1) # n-1 = 자신을 제외한 전부 
        return
    
    for i in range(n):
        if i == start or eggs[i][0] <= 0:
            continue
        eggs[start][0] -= eggs[i][1]
        eggs[i][0] -= eggs[start][1]
        solution(start+1)
        eggs[start][0] += eggs[i][1]
        eggs[i][0] += eggs[start][1]


n = int(input())
eggs = [list(map(int, input().split())) for _ in range(n)]
answer = 0

solution(0)
print(answer)