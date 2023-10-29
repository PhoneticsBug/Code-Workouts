import sys
input = sys.stdin.readline

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

visited = [False for _ in range(n+1)]

result = float('inf')

def btr(l, idx):
    global result

    # 최소값 찾아서 배치하기
    if l == n//2:
        a, b = 0, 0 # 비교용
        for i in range(n):
            for j in range(n):
                if visited[i] and visited[j]:
                    a += grid[i][j]
                elif not visited[i] and not visited[j]:
                    b += grid[i][j]
        result = min(result, abs(a-b)) 
        return
    # 이미 둘러본 부분 이후를 모두 False화
    for i in range(idx, n):
        if not visited[i]:
            visited[i] = True
            btr(l+1, i+1)
            visited[i] = False
btr(0, 0)
print(result)