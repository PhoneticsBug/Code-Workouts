# import sys
# import math
# input = sys.stdin.readline

# num = int(input())


# def pibonacci(n): 
#     pi = math.pi
#     if 0 <= n <= pi: # 1이 되는 조건
#         return 1
#     return (pibonacci(n - 1) + pibonacci(n - pi)) # p[n]의 조건

# print(pibonacci(num)%1000000000000000000)


# ----------

import sys
import math
input = sys.stdin.readline

num = int(input())

fibs = {}  # 메모이제이션을 위한 딕셔너리

def pibonacci(n): 
    pi = math.pi
    if 0 <= n <= pi: # 1이 되는 조건
        return 1

    if n in fibs:  # 계산된 값이 메모에 저장되어 있다면 불러옴
        return fibs[n]

    result = pibonacci(n - 1) + pibonacci(n - pi) # p[n]의 조건
    fibs[n] = result  # 계산된 값을 메모에 저장
    print(fibs)
    return result

print(pibonacci(num) % 1000000000000000000)

