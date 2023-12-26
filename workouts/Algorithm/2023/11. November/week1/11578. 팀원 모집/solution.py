import sys
from itertools import combinations
input = sys.stdin.readline

n, m = map(int, input().split())
students = [list(map(int, input().split())) for _ in range(m)]
# problems = [i for i in range(1, n+1)]

def solution(n, m, students):
    min_team = float('inf')

    # 팀의 인원 수 조절
    for r in range(1, m+1):
        # 해당 인원 수에서 나올 수 있는 팀 조합
        for team in combinations(range(m), r):
            problems = set()

            # 풀 수 있는 문제 합
            for member in team:
                problems.update(students[member][1:])

            # 모든 문제를 다 풀 수 있다면
            if len(problems) == n:
                min_team = min(min_team, len(team))

    if min_team == float('inf'):
        return -1
    else:
        return min_team
    
print(solution(n, m, students))
