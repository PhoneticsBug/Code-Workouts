import sys
input = sys.stdin.readline

n, m = map(int, input().split())
staff = list(map(int, input().split()))

start = 1
end = m*max(staff)

while start
