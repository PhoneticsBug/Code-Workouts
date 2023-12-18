import sys
input = sys.stdin.readline

n, b = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
mod = 1000

# 행렬의 크기만큼 제곱한 결과를 보여주기

def multiply(a, b, mod):
    result = [[0]*len(b[0]) for _ in range(len(a))]
    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)):
                result[i][j] += a[i][k] * b[k][j]
                result[i][j] %= mod

    return result

def power(matrix, exponent, mod):
    if exponent == 1:
        return matrix
    # 지수가 짝수인 경우 절반을 거듭제곱하여 한번만 곱셈
    elif exponent % 2 == 0:
        half = power(matrix, exponent//2, mod)
        return multiply(half, half, mod)
    # 지수가 홀수인 경우 행렬을 한번 더 곱한 후 절반을 곱함
    else:
        return multiply(matrix, power(matrix, exponent-1, mod), mod)
    
for i in power(grid, b, mod):
    print(*i)

#
    
def multi(u, v):
    n = len(u)
    z = [[0]*n for _ in range(n)]
    
    for row in range(n):
        for col in range(n):
            e = 0
            for i in range(n):
                e += u[row][i] * v[i][col]
            z[row][col] = e % 1000
    return z

def square(a, b):
    if b == 1:
        for x in range(len(a)):
            for y in range(len(a)):
                a[x][y] %= 1000
        return a
    
    tmp = square(a, b//2)

    if b % 2:
        return multi(multi(tmp, tmp), a)
    else:
        return multi(tmp, tmp)
    
result = square(grid, b)
for i in result:
    print(*i)