# g kg = 현재 몸무게의 제공ㅂ에서 기억하고 있던 몸무게의 제곱을 뺀 값

# while 문 안에서 start와 end를 1씩 증가시키면서 어느 하나를 늘리는 것으로는 두 값의 차이를 더 벌릴 수 없을 때 (10만 이하)

# 입력받은 수가 어느 숫자의 제곱값 근처인지 확인하고 그보다 큰 수의 약수에서 찾으면 될듯함
# g kg = 현재 몸무게의 제공ㅂ에서 기억하고 있던 몸무게의 제곱을 뺀 값

import sys
import math
input = sys.stdin.readline

g = int(input())

ans = []
t = 1

mini, maxi = math.floor(g**0.5), math.floor(g**0.5)+1

while True:
    if maxi >= 100000:
        break
    if maxi**2 - (maxi-1)**2 > g:
        break
    for i in range(1, maxi):
        if maxi**2 - i**2 == g:
            ans.append(maxi)
    t += 1
    maxi *= t
ans = sorted(list(set(ans)))

if len(ans) == 0:
    print(-1)
else:
    print(*ans, sep='\n')


left, right = 1, 1
result = []

while True:
    diff = right**2 - left**2
    if right - left == 1 and diff > g:
        break

    if diff > g:
        left += 1
    elif diff < g:
        right += 1
    else:
        result.append(right)
        right += 1

if result:
    print(*result, sep='\n')
else:
    print(-1)