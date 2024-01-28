import sys, math
input = sys.stdin.readline

a, b = map(int, input().split())

def solution(x):
    if x <= 0:
        return 0
    
    square = int(math.log2(x))
    temp = 2**square
    if temp == x:
        return square * x // 2 + 1
    
    diff = x - temp
    return solution(temp) + diff + solution(diff)

print(solution(b) - solution(a-1))