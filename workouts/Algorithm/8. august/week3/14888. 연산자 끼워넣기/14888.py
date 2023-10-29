import sys
input = sys.stdin.readline

n = int(input())
num = list(map(int, input().split()))
calc = list(map(int, input().split())) # plus, minus, multiply, divide
min_result, max_result = 10e9, -10e9 
def calculate(a, b, op):
    # 두 숫자와 연산자로 입력을 받음
    if op == 0:
        return a + b
    if op == 1:
        return a - b
    if op == 2:
        return a * b
    else:
        if a < 0: # 0보다 작을 때
            return -((-a)//b)
        else: # 0보다 클 때
            return a//b     

def solution(idx, result, add, sub, mul, div):
    # 일단은 모든 경우를 검색함
    global min_result, max_result

    # 모든 숫자를 처리한 다음에는
    if idx == n:
        max_result = max(max_result, result)
        min_result = min(min_result, result)     
        return
    if add:
        solution(idx+1, calculate(result, num[idx], 0), add-1, sub, mul, div)
    if sub:
        solution(idx+1, calculate(result, num[idx], 1), add, sub-1, mul, div)
    if mul:
        solution(idx+1, calculate(result, num[idx], 2), add, sub, mul-1, div)
    if div:
        solution(idx+1, calculate(result, num[idx], 3), add, sub, mul, div-1)

solution(1, num[0], calc[0], calc[1], calc[2], calc[3])

print(max_result, min_result, sep="\n")
