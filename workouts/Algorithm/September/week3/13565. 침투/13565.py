import sys
input = sys.stdin.readline

M, N = map(int, input().split())
grid = [input().strip() for _ in range(M)]

def solution(grid):
    visited = [[False] * N for _ in range(M)]

    # 시작 지점 찾기
    for j in range(N):
        if grid[0][j] == '0':
            visited[0][j] = True
            stack = [(0, j)]

            # DFS를 사용하여 전류가 침투 가능한지 확인
            while stack:
                x, y = stack.pop()
                if x == M - 1:
                    return True  # 마지막 행에 도달하면 성공

                # 상하좌우 이동
                moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]
                for dx, dy in moves:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < M and 0 <= ny < N and not visited[nx][ny] and grid[nx][ny] == '0':
                        visited[nx][ny] = True
                        stack.append((nx, ny))

    return False

# 결과 출력
if solution(grid):
    print("YES")
else:
    print("NO")
