# n의 최대값 = 8 <<< 천만
# ex) 7331의 경우 나오는 조합은 7, 73, 733, 7331 네가지
# 맨 앞자리에 올 수 있는 숫자는 2, 3, 5, 7로 한정되어 있음
# n만큼 그 뒤에 숫자를 하나씩 붙여가며 검사하기

import sys
input = sys.stdin.readline

n = int(input())

# 소수 판별 함수
def eratosthenes(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

# [2, 3, 5, 7]에 1~9 사이의 숫자를 넣으며 소수 판별하기
def solution(n, num):
    if n == 0:
        print(num)
        return
    # n이 0이 될때까지 재귀함수를 불러옴 (다중 for문)
    for i in range(10):
        temp = num * 10 + i
        if eratosthenes(temp):
            solution(n-1, temp)

for i in [2, 3, 5, 7]:
    solution(n-1, i)