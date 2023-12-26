n = 10

def solution(n):
    temp = [[i] for i in range(n)]


# 삼각형의 크기는 n - 1 을 1이 될때까지 반복해서 더한 값
# 
# n에 달하기 전까지는 좌상단에서 좌하단으로 내려감
# 그 이후 n-1만큼 우하단으로 이동
# 이동이 끝나면 n-2만큼 위로 이동
# n-3만큼 아래로 이동
# n-4만큼 우로 이동
# n-5만큼 위로 이동
# n-... 만큼 우-상-하-우-상-하 순서로 이동
# 실제 순서는 하 > 우 > 상
# 
# 1
# 2 9
# 3 10 8
# 4 5 6 7 

lst = [[0]*i for i in range(1, n+1)]
p = n
dx, dy = 0, 0
num = 1
final = sum([i for i in range(1, n+1)]) # 마지막 숫자
print('final: ', final)

while num <= final:
    # 내려가기
    if lst[dx][dy] != 0:
            dx += 1
            p -= 1
    if lst[dx][dy] != 0:
        dy += 1
        p -= 1
    for i in range(p):
        lst[dx][dy] = num
        num += 1
        dx += 1
    p -= 1
    dx -= 1
    dy += 1
    # 오른쪽으로 가기
    for i in range(p):
        lst[dx][dy] = num
        num += 1
        dy += 1
    p -= 1
    dx -= 1
    dy -= 2

    # 위로 가기
    for i in range(p):
        if lst[dx][dy] == 0:
            lst[dx][dy] = num
            num += 1
            dx -= 1
            dy -= 1
    if dx == 0 and dy == 0:
        dx += 1
        dy += 1
    
        
        # break
print(dx, dy, p, num)
print(*lst, sep='\n')

# 루프를 돌려줄 조건을 찾기가 힘들고 비효율적임... 
# ------------- 정답코드 -------------

def solution(n):
    answer = [[0]*i for i in range(1, n+1)]
    dx, dy = -1, 0
    num = 1
    # 루프 안의 값을 바꿔가면서 이동함
    for i in range(n): # 방향 
        for _ in range(i, n): # 좌표 이동만큼
            if i % 3 == 0: # i = 1, 하강
                dx += 1
            elif i % 3 == 1: # i = 2, 우향
                dy += 1
            else: # 상향
                dx -= 1
                dy -= 1
            answer[dx][dy] = num
            num += 1
    print(*answer, sep='\n')
    return sum(answer, [])

print(solution(n))