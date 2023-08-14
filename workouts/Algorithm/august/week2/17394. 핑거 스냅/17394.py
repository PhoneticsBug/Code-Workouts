import sys
input = sys.stdin.readline

t = int(input())
n, a, b = map(int, input().split()) # 생명체 수, 줄여나갈 목표범위

# 소수 리스트 먼저 생성하기 (에라토스테네스의 체)
sosu = [True]*(a*b+1)
for i in range(2, len(sosu)):
    if sosu[i] == True:
        for j in range(i + i, len(sosu), i):
            sosu[j] = False
sosu[0], sosu[1] = False, False

def solution():
    return

for _ in range(t):
    life = list(map(int, input().split()))
    print(solution(life))

# 소수 리스트를 만들고
# 이분탐색으로 찾다가 범위 안에 있는 소수 중 가장 작은 수 찾기
# 없으면 -1 출력