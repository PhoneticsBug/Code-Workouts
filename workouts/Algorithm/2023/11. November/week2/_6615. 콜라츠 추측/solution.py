# while문 두개를 사용해보기 (두 수를 나눠서 while문을 사용해보기)
# A 수열을 구한 다음 B 수열을 만들면서 비교

import sys
input = sys.stdin.readline

def colatz(num):
    if num % 2 == 0:
        return num // 2
    else:
        return 3 * num + 1

while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    a_start, b_start = a, b
    a_step, b_step = 0, 0

    while True:
        if colatz(a) == colatz(b) or colatz(a) == 1 or colatz(b) == 1:
            break
        else:
            if a > b:
                a = colatz(a)
                a_step += 1
            else:
                b = colatz(b)
                b_step += 1

    print(f"{a_start} needs {a_step} steps, {b_start} needs {b_step} steps, they meet at {a}")