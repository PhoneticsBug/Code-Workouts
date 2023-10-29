import sys
from itertools import combinations
input = sys.stdin.readline

players = [0] + list(map(float, input().split()))

def score(player):
    array = []
    for i in player:
        array.append(players[i])
    array.sort()
    score = 1 - (abs((array[0] + array[3])/2 - (array[1] + array[2])/2)/10)
    return score


def solution(players):
    ans = 0
    temp = combinations(range(1, 9), 4)
    for t1 in temp:
        t2 = [i for i in range(1, 9) if i not in t1]
        ans = max(ans, min(score(t1), score(t2)))
    return (round(ans, 2))

print(solution(players))