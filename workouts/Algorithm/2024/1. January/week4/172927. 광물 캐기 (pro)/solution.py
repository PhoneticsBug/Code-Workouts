import sys
input = sys.stdin.readline

# 다이아, 철, 돌
picks = [1, 3, 2]
minerals = ["diamond", "diamond", "diamond", "iron", "iron", "diamond", "iron", "stone"]
fatigue = [[1, 1, 1], 
        [5, 1, 1], 
        [25, 5, 1]]

# 모든 곡괭이는 5회 사용할 수 있고, 한번 사용하기 시작하면 내구도가 다 하기 전까지는 교체할 수 없다

# 다 다 다 철 철 다 철 석
# 다 다 다 다 다 철 철 철
# 1  1  1  1  1  5  1  1 = 12

# DFS
def solution(picks, minerals):

    fatigue = 0

    diamond, iron, stone = picks

    diamond_fatigue = {"diamond":1, "iron":1, "stone":1}
    iron_fatigue = {"diamond":5, "iron":1, "stone":1}
    stone_fatigue = {"diamond":25, "iron":5, "stone":1}
    
    # 광물을 5개 단위로 나누고 곡괭이의 개수만큼 선택
    minerals = [minerals[i:i+5] for i in range(0, len(minerals), 5)][:sum(picks)]

    # 광물을 다이아, 철, 돌의 개수에 따라 내림차순으로 정렬 << ????
    minerals.sort(key=lambda x: (x.count('diamond'), x.count('iron'), x.count('stone')), reverse=True)

    for mineral in minerals:
        # 곡괭이별로 각 광물 채굴
        if diamond > 0:
            for name in mineral:
                fatigue += diamond_fatigue[name]
            diamond -= 1
        elif iron > 0:
            for name in mineral:
                fatigue += iron_fatigue[name]
            iron -= 1
        elif stone > 0:
            for name in mineral:
                fatigue += stone_fatigue[name]
            stone -= 1
    return fatigue


# DP
def solution(picks, minerals):
    cost = [[1, 1, 1], [5, 1, 1], [25, 5, 1]]
    n = min(sum(picks), ((len(minerals)-1)//5)+1)
    mapping = {'diamond':0, 'iron':1, 'stone':2}

    minerals = [mapping[i] for i in minerals]
    minerals - [[sum(cost[k][x] for x in minerals[i:i+5]) for k in range(3)] for i in range(0, n*5, 5)]

    q = {'000': 0}