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
