import sys
input = sys.stdin.readline

c, n = map(int, input().split()) # 고객의 수, 도시의 수
city = [list(map(int, input().split())) for _ in range(n)] 
#내부 인덱스 0은 금액, 1은 늘어나는 고객 수

# range(c+101) 이 값은 100보다 작거나 같은 자연수이다.
dp = [2e9 for _ in range(10001)] 
dp[0] = 0

for cost, customer in city:
    for i in range(customer, 10001):
        dp[i] = min(dp[i - customer] + cost, dp[i])
print(min(dp[c:]))