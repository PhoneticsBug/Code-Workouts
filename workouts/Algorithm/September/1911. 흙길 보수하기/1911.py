import sys
input = sys.stdin.readline

n, l = map(int, input().split())

path = []
for _ in range(n):
    start, end = map(int, input().split())
    path.append([start , end])

path.sort()

bridge = 0
cnt = 0

for start, end in path:
    if start > end: 
        continue

    if bridge > start: # 이전 널빤지에서 이어지는 경우
        start = bridge
    
    while start < end: # 웅덩이 메우기
        start += l 
        cnt += 1
    bridge = start

print(cnt)