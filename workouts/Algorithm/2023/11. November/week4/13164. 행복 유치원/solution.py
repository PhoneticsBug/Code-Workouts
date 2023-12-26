import sys
input = sys.stdin.readline

n, k = map(int, input().split())
kids = list(map(int, input().split()))

kinder = []
for i in range(1, n):
    kinder.append(kids[i] - kids[i-1]) # sort된 리스트의 각 차 구하기
kinder.sort(reverse=True)

print(sum(kinder[k-1:]))