import sys
input = sys.stdin.readline

n = int(input()) # 과수원의 크기 (정사각형)
harvest = [list(map(int, input().split())) for _ in range(n)] # 수확 시 손/이득
k = 0 # 수확할 땅의 크기

# 누적합이나 브루트포스를 이용해 사이즈 키우기
def solution(n, harvest):
    max_profit = float('-inf')  # 최대 총이익을 저장할 변수를 음의 무한대로 초기화합니다.

    for i in range(n):
        for j in range(n):
            for k in range(1, n+1):
                if i + k > n or j + k > n:
                    break

                total_profit = 0
                for x in range(i, i+k):
                    for y in range(j, j+k):
                        total_profit += harvest[x][y]

                max_profit = max(max_profit, total_profit)

    return max_profit

print(solution(n, harvest))

