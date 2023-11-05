import sys
input = sys.stdin.readline

# ax + b 일때 정해진 수 x를 분배해서 모든 결과를 똑같이 만들기

n = int(input())
equasion = [list(map(int, input().split())) for _ in range(n)]
liquid = int(input())

