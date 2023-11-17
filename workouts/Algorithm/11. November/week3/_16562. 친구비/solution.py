import sys
input = sys.stdin.readline

# 학생 수, 친구관계 수, 가진 돈
n, m, k = map(int, input().split())
friend_pay = list(map(int, input().split()))
friendship = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    friendship[a-1] = b