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