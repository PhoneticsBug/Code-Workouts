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
input = sys.stdin.readline
t = int(input()) 

for _ in range(t):
    a, b, c = map(int, input().split())
    ab, bc, ca = map(int, input().split())

    result = 0

    for ing1 in range(min(a, b) + 1):
        ing2 = min(b - ing1, c)
        ing3 = min(c - ing2, a - ing1)

        # 1차 약품 제작
        result = max(result, ing1*ab + ing2*bc + ing3*ca)

        # 2-3차 약품 제작
        ing3 = min(c, a - ing1)
        ing2 = min(b - ing1, c - ing3)

        result = max(result, ing1*ab + ing2*bc + ing3*ca)

    print(result)