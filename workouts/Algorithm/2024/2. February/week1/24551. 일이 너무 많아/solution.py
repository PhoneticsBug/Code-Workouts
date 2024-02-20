# 정수 n이 주어졌을 때 1 이상 n 이하의 정수 중 1로만 이루어진 수의 개수를 찾아보기

# n 이하의 자연수 중 x의 배수인 수의 개수는 n/x개임

# 2개 이상의 1로만 이루어진 수의 배수인 수
#   1. 11, 111, 1111, ... 임
#   2. 1111은 11의 배수임 <<< 길이가 소수인 수만 카운트해주면 나머지는 이미 되어있음

# A의 배수들로 이루어진 집합과 B의 배수들로 이루어진 집합의 교집합은 A와 B의 최소공배수로 이루어져 있음

from math import gcd
import sys
input = sys.stdin.readline

n = int(input())
ans = n
arr = [11, 111, 11111, 1111111, 11111111111, 1111111111111, 11111111111111111]

# 최소공배수 찾기 // 두 수의 곱을 최대공약수로 나눔(gcd)
def gongbaesu(a, b):
    return a*b // gcd(a, b)

# 이진수에서 1의 개수 찾기 (비트마스크)
def cnt_one(num):
    cnt = 0
    # i번 왼쪽으로 넘긴 값의 비트가 0이라면 cnt 1 추가
    for i in range(0, 7):
        if num & (1 << i) != 0:
            cnt += 1
    
    return cnt


def solution(num):
    ans = 1
    # 해당하는 숫자들에 대해 ans와 arr[i]의 최소공배수 저장
    for i in range(0, 7):
        if num & (1 << i) != 0:
            ans = gongbaesu(ans, arr[i])
    
    return ans

for i in range(0, (1 << 7)):
    # 짝수 연산
    if cnt_one(i) % 2 == 0:
        ans -= n//solution(i)
    # 홀수 연산
    else:
        ans += n//solution(i)

print(ans)
