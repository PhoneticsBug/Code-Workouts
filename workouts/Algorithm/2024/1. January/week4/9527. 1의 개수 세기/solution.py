# 주어지는 수의 범위는 10000조 (log 시간복잡도가 필요함)
# 규칙은 2가지가 있다

# 2진수로 변환했을 때 2**n - 1까지의 반복되는 패턴이 존재함
# 2**n 부터 2**(n+1)-1까지는 2**(n-1)~2**(n)-1까지의 이진수 패턴의 앞에 1을 붙여준 것과 같음

# 1의 개수를 누적합으로 구할 경우, 1부터 2**n -1까지의 수를 점화식으로 구할 수 있다.
# 1**n - 1 까지의 1의 개수 누적 합은 2**(n-1) + 2 * (2**(n-1))이 된다.

import sys, math
input = sys.stdin.readline

# 입력
a, b = map(int, input().split())

def solution(x):
    # 만약 x가 0 이하인 경우는 그대로 0 반환 
    if x <= 0:
        return 0
    # x의 제곱근보다 작은 가장 큰 정수 찾기
    square = int(math.log2(x))
    temp = 2**square
    # x가 2의 거듭제곱인 경우
    if temp == x:
        # 등차수열의 합 공식을 이용해 결과 반환
        return square * x // 2 + 1
    # 아닌 경우에는
    diff = x - temp
    # 재귀를 이용해 될때까지 반환
    return solution(temp) + diff + solution(diff)

print(solution(b) - solution(a-1))