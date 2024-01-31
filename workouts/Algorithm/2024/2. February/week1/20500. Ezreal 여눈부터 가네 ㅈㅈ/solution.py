# 주어지는 n자리의 양의 정수 중에서 15의 배수가 몇개인지 확인
# n은 1015자리수까지 주어짐
# dp 혹은 수학을 이용하여 풀어야 함

# n = 2일때 나올 수 있는 수는 15 
# n = 3일때 나올 수 있는 수는 555
# n = 4일때 나올 수 있는 경우의 수는
# 1115 1155 1555 1515 5115 5155 5515 5555
# 이 중에서 15의 배수는 1155 1515 5115 3개

# 일단 어떤 경우에도 1자리수는 5가 와야 함


import sys
from itertools import product
input = sys.stdin.readline

n = int(input())


temp = [''.join(p) for p in product('15', repeat=(n)) if p[-1] == '5']
ans = 0
for i in temp:
    if int(i)%15 == 0:
        ans += 1
print(ans)

####

# 1과 5로 만들고, 마지막 자리수가 5인 경우 나올 수 있는 나머지의 수는 0, 5, 10임
# 1. 나머지가 0인 개수는 이전에 나머지가 5인 개수 + 10인 개수
# 2. 나머지가 5인 개수는 이전에 나머지가 0인 개수 + 10인 개수
# 3. 나머지가 10인 개수는 이전에 나머지가 0인 개수 + 5인 개수
import sys
input = sys.stdin.readline

n = int(input())
# dp의 각 요소는 나머지가 0, 5, 10인 수의 개수를 의미함
dp = [[0 for _ in range(3)] for _ in range(1516)]
dp[1][1] = 1

for i in range(2, 1516):
    dp[i][0] = dp[i-1][1] + dp[i-1][2]
    dp[i][1] = dp[i-1][0] + dp[i-1][2]
    dp[i][2] = dp[i-1][0] + dp[i-1][1]

print(dp[n][0] % 1000000007)