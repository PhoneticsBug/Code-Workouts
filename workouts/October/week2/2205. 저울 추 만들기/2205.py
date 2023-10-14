import sys
input = sys.stdin.readline

n = int(input())

def solution(n):

    square = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384]
    zinc = [1] + [0 for i in range(0,n)]

    # 뒤에서부터 각 납덩어리를 처리하면서, 그에 대응되는 주석덩어리 탐색
    for lead in range(len(zinc)-1,0,-1):
        # 가능한 한 가장 크면서도 그보다 크지 않은 2의 거듭제곱 값을 탐색
        for k in range(0,len(square)):
            if square[k] - lead <= n and square[k] > lead:  
                if zinc[lead] == 0 and zinc[square[k]-lead] == 0: 
                    zinc[lead] = square[k] - lead  
                    zinc[square[k]-lead] = lead 
                    break

    print(*zinc[1::], sep='\n')

solution(n)


