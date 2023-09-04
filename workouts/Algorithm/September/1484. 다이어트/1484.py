# g kg = 현재 몸무게의 제공ㅂ에서 기억하고 있던 몸무게의 제곱을 뺀 값

# while 문 안에서 start와 end를 1씩 증가시키면서 어느 하나를 늘리는 것으로는 두 값의 차이를 더 벌릴 수 없을 때 (10만 이하)

# 입력받은 수가 어느 숫자의 제곱값 근처인지 확인하고 그보다 큰 수의 약수에서 찾으면 될듯함
# g kg = 현재 몸무게의 제공ㅂ에서 기억하고 있던 몸무게의 제곱을 뺀 값

import sys
input = sys.stdin.readline

g = int(input())
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