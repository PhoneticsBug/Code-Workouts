import sys
input = sys.stdin.readline

# 다이아, 철, 돌
picks = [1, 3, 2]
minerals = ["diamond", "diamond", "diamond", "iron", "iron", "diamond", "iron", "stone"]
workigue = [[1, 1, 1], 
        [5, 1, 1], 
        [25, 5, 1]]

# 모든 곡괭이는 5회 사용할 수 있고, 한번 사용하기 시작하면 내구도가 다 하기 전까지는 교체할 수 없다

# 다 다 다 철 철 다 철 석
# 다 다 다 다 다 철 철 철
# 1  1  1  1  1  5  1  1 = 12

# DFS
def solution(picks, minerals):

    workigue = 0

    diamond, iron, stone = picks

    diamond_workigue = {"diamond":1, "iron":1, "stone":1}
    iron_workigue = {"diamond":5, "iron":1, "stone":1}
    stone_workigue = {"diamond":25, "iron":5, "stone":1}
    
    # 광물을 5개 단위로 나누고 곡괭이의 개수만큼 선택
    minerals = [minerals[i:i+5] for i in range(0, len(minerals), 5)][:sum(picks)]

    # 광물을 다이아, 철, 돌의 개수에 따라 내림차순으로 정렬 << ????
    minerals.sort(key=lambda x: (x.count('diamond'), x.count('iron'), x.count('stone')), reverse=True)

    for mineral in minerals:
        # 곡괭이별로 각 광물 채굴
        if diamond > 0:
            for name in mineral:
                workigue += diamond_workigue[name]
            diamond -= 1
        elif iron > 0:
            for name in mineral:
                workigue += iron_workigue[name]
            iron -= 1
        elif stone > 0:
            for name in mineral:
                workigue += stone_workigue[name]
            stone -= 1
    return workigue


# DP
def solution(picks, minerals):
    cost = [[1, 1, 1], [5, 1, 1], [25, 5, 1]]
    n = min(sum(picks), ((len(minerals)-1)//5)+1)
    mapping = {'diamond':0, 'iron':1, 'stone':2}

    minerals = [mapping[i] for i in minerals]
    minerals - [[sum(cost[k][x] for x in minerals[i:i+5]) for k in range(3)] for i in range(0, n*5, 5)]

    q = {'000': 0}

    for i in range(n):
        tmp = {}

        for picked, work in q.items():
            picked = list(map(int, picked))
            for k in range(3):
                if picked[k] == picks[k]:
                    continue
                picked[k] += 1
                cm = ''.join(map(str, picked))
                cf = work * minerals[i][k]
                if cm in tmp:
                    tmp[cm] = min(tmp[cm], cf)
                else:
                    tmp[cm] = cf
                picked[k] -= 1
        q = tmp
    return min(q.values())

# 최적화 버전 DP

def solution(picks, minerals):
    # 곡괭이별 채굴 피로도
    cost = [[1, 1, 1], [5, 1, 1], [25, 5, 1]]
    # 채굴 가능 회수 (곡괭이 하나당 5회 할 수 있으므로 5로 나눈 값과 비교)
    n = min(sum(picks), ((len(minerals)-1)//5)+1)

    # 광물을 정수형으로 변환
    mapping = {"diamond": 0, "iron": 1, "stone": 2}
    # 피로도 계산
    minerals = [[sum(cost[k][mapping[m]] for m in minerals[i:i+5]) for k in range(3)] for i in range(0, n*5, 5)]
    
    q = {(0, 0, 0): 0}

    for mineral in minerals:
        tmp = {}
        # 광물별 채굴 피로도
        for picked, work in q.items():
            # 곡괭이별로 계산
            for k in range(3):
                # 이미 채굴한 경우는 제외
                if picked[k] == picks[k]:
                    continue
                # 해당 곡괭이로 채굴하는 경우의 피로도 계산
                new_picked = picked[:k] + (picked[k] + 1,) + picked[k+1:]
                new_work = work + mineral[k]
                # 갱신
                tmp[new_picked] = min(new_work, tmp.get(new_picked, float('inf')))
        q = tmp       
    return min(q.values())
