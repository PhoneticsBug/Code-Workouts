import sys
input = sys.stdin.readline

t = int(input())

# 화학약품별 가격차이가 있는 경우
# 값이 가장 큰 약품부터 시작해서 줄여나감
# 없는 경우
# 순서대로 줄여나감

for _ in range(t):
    ingredients = list(map(int, input().split()))
    ab, bc, ac = map(int, input().split())

    chemical = [('ab', ab), ('bc', bc), ('ac', ac)]
    chemical = sorted(chemical, key = lambda x: x[1], reverse=True)
    cost = 0

    def mix(price, ing1, ing2):
        global cost
        while True:
            if ingredients['abc'.index(ing1)] == 0 or ingredients['abc'.index(ing2)] == 0:
                return False
            ingredients['abc'.index(ing1)] -= 1
            ingredients['abc'.index(ing2)] -= 1
            cost += price

    for i in range(3):
        mix(chemical[i][1], chemical[i][0][0], chemical[i][0][1])
    print(cost)

 ####################################################
    
import sys

T = int(sys.stdin.readline())  # 테스트 케이스의 수를 입력 받음
for _ in range(T):
    a, b, c = map(int, sys.stdin.readline().split())  # 각 화학 물질의 수량을 입력 받음
    abP, bcP, caP = map(int, sys.stdin.readline().split())  # 각 화학 제품의 가격을 입력 받음

    maxPrice = 0  # 최대 이익을 저장할 변수

    # AB를 만드는 수량을 0부터 min(a, b)까지 반복
    for abNum in range(min(a, b)+1):
        # 남은 b와 c 중 작은 값만큼 BC를 만듦
        bcNum = min(b - abNum, c)
        # 남은 c와 a 중 작은 값만큼 CA를 만듦
        caNum = min(c - bcNum, a - abNum)

        # 현재 만든 화학 제품들로 얻을 수 있는 이익을 계산하고, 이가 최대 이익이라면 저장
        maxPrice = max(maxPrice, abNum * abP + bcNum * bcP + caNum * caP)

        # 남은 c와 a 중 작은 값만큼 CA를 만듦
        caNum = min(c, a - abNum)
        # 남은 b와 c 중 작은 값만큼 BC를 만듦
        bcNum = min(b - abNum, c - caNum)

        # 현재 만든 화학 제품들로 얻을 수 있는 이익을 계산하고, 이가 최대 이익이라면 저장
        maxPrice = max(maxPrice, abNum * abP + bcNum * bcP + caNum * caP)

    # 최대 이익 출력
    print(maxPrice)
