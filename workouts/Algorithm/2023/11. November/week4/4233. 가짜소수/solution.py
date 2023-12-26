import sys
input = sys.stdin.readline

checkers = []

while True:
    checker = list(map(int, input().split()))
    if checker == [0, 0]:
        break
    checkers.append(checker)

limit = max(max(checkers))
primes = [True] * (limit + 1)
primes[0] = primes[1] = False

for i in range(2, int(limit**0.5) + 1):
    if primes[i]:
        for j in range(i * i, limit + 1, i):
            primes[j] = False
    
for checker in checkers:    
    p, a = checker[0], checker[1]
    if not primes[p]:
        if a**p%p == a:
            print("yes")
        else:
            print("no")
    else:
        print("no")

## 시간초과

import sys
input = sys.stdin.readline

def prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def solution(x, n, mod):
    ret = 1
    while n:
        if n % 2: # n이 홀수인 경우
            ret = ret * x % mod
        x = x * x % mod
        n >>= 1
    return ret

while True:
    p, a = map(int, input().split())
    if p == 0 and a == 0:
        break

    prime_num = prime(p)
    result = not prime_num and solution(a, p, p) == a
    print("yes" if result else "no")