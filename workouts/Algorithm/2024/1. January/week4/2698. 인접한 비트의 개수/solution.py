# 길이가 n일 때 최대 k의 수는 n - 1
# 각 길이(2~n)를 0~k까지 수열의 개수를 누적시키며 결과를 얻을 수 있다.

import sys
input = sys.stdin.readline

t = int(input())

def solution(n, k):
    answer = 0
    return answer

for _ in range(t):
    n, k = map(int, input().split())

    print(solution(n, k))