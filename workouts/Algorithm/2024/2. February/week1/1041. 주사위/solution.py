# 주사위를 쌓아서 정육면체를 만들고 나면, 숫자가 보이는 면은 위치에 따라 변함

# 면 3개 주사위(각 꼭짓점) = 4개
# 면 2개 주사위(각 모서리) = 4*(n-1) + 4*(n-2)
# 면 1개 주사위(각 평면체) = 4*(n-2)*(n-1) + (n-2)**2


import sys
input = sys.stdin.readline

n = int(input())
dice = list(map(int, input().split()))
answer = 0

mini = []

if n == 1:
    dice.sort()
    answer

else:
    # 주사위의 각 면이 정해져 있음 (0~5 = A~F)
    # A/F B/E C/D == 0/5 1/4 2/3
    mini.append(min(dice[0], dice[5]))
    mini.append(min(dice[1], dice[4]))
    mini.append(min(dice[2], dice[3]))
    mini.sort()

    min1 = mini[0]
    min2 = mini[0] + mini[1]
    min3 = sum(mini)

    n1 = 4*(n-2)*(n-1) + (n-2)**2
    n2 = 4*(n-1) + 4*(n-2)
    n3 = 4

    answer = (min1*n1 + min2*n2 + min3*n3)

print(answer)

### 

import sys
input = sys.stdin.readline

n = int(input())
dice = list(map(int, input().split()))
answer = 0

mini = []

if n == 1:
    dice.sort()
    answer = sum(dice[i] for i in range(5))

else:
    # 주사위의 각 면이 정해져 있음 (0~5 = A~F)
    # A/F B/E C/D == 0/5 1/4 2/3
    mini.append(min(dice[0], dice[5]))
    mini.append(min(dice[1], dice[4]))
    mini.append(min(dice[2], dice[3]))
    mini.sort()

    min1 = mini[0] * (4*(n-2)*(n-1) + (n-2)**2)
    min2 = mini[0] + mini[1] * (4*(n-1) + 4*(n-2))
    min3 = sum(mini) * 4


    answer = min1 + min2 + min3

print(answer)