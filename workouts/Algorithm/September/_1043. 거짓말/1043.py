import sys
input = sys.stdin.readline

n, m = map(int, input().split()) # 사람 수, 파티 수
truth =  list(map(int, input().split())) # 진실을 아는 사람의 수와 번호
parties = [list(map(int, input().split())) for _ in range(m)]


if truth[0] == 0: # 진실을 아는 사람이 없음
    print(m)
else:
    watcher = truth[1:]
    
    