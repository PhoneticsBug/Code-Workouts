import sys
input = sys.stdin.readline

# 에라토스테네스의 체를 이용해서 두 수 사이의 소수의 제곱수를 찾기

A, B = map(int, input().split())

# 에라토스테네스의 체
def isPrime(n):
    prime_list = [True] * (n + 1)
    prime_list[0] = prime_list[1] = False

    for p in range(2, n+1):
        if prime_list[p]:
            for i in range(p * p, n + 1, p):
                prime_list[i] = False

    return prime_list

# 최대값의 sqrt 만큼 루프를 돌려 cnt += 1
maxval = int(B ** 0.5)
prime = isPrime(maxval)
cnt = 0

for n in range(2, maxval + 1):
    if prime[n]:
        pp = n * n
        while pp <= B:
            if pp >= A:
                cnt += 1
            pp *= n

print(cnt)
