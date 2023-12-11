import sys
from collections import deque
input = sys.stdin.readline

# 적의 위치와 탑의 위치가 정해짐 << 2차원 배열은 어떻게 만들지?
# 사정거리 안에 적이 존재하지 않고, 다른 탑이 있는 경우 에너지를 몰아줄 수 있다 (위력 절반으로 하락)
# 적에게 닿지 않는 탑의 경우 범위 안의 가장 가까운 탑을 찾는 것이 중요
# 필요한 함수
# 1. 적에게 바로 공격할 수 있는 탑 찾기
# 2. 적에게 닿지 않는 탑 중 범위 안에 다른 탑이 있는지 체크 + 에너지 주기
# >>> 모든 에너지의 합 출력

# 적
# \     \
# 탑    탑 
#   \            \            \ 
#    탑*거리/2  탑*거리/2    탑*거리/2

# 탑의 개수, 사정거리, 초기 에너지, 적 좌표 X, 적 좌표 Y
n, r, d, x, y = map(int, input().split())
towers = {tuple(map(int, input().split())) for _ in range(n)}
answer = 0

def solution(x, y):
    global towers, answer

    q = deque([(x, y, 0)])

    while q:
        x, y, depth = q.popleft()
        if depth:
            # 깊이만큼 초기 에너지가 감소 (2*n제곱만큼 나누어줌)
            answer += d / (2 ** (depth - 1))

        attackable = [] # 공격 가능한 탑 
        for tower in towers:
            # 적과의 거리가 사정거리 이내인 탑들을 찾아서 attackable에 추가
            # 적과 탑 사이의 거리 (직각삼각형의 긴 변)
            if (x - tower[0]) ** 2 + (y - tower[1]) ** 2 <= r ** 2:
                attackable.append(tower)
        
        # 공격 가능한 탑들을 탑 목록에서 제거하고 추가 (depth 갱신)
        for attack in attackable:
            # 각 stack마다 공격할 수 있으면 공격, 그렇지 않은 경우 depth를 증가시키면서 대기
            q.append((attack[0], attack[1], depth + 1))
        towers -= set(attackable)
    if type(answer) == int:
        return f'{answer}.0'
    else:
        return answer

print(solution(x, y))

# 정수형으로 변환이 가능한 경우 소수점이 없는 정수로 출력, 그렇지 않은 경우 그대로 출력

