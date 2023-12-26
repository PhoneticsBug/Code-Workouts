# 가장 간단하게 풀 수 있는 방법은?
# bridge_length만큼 다리를 만든 다음 한칸씩 옮겨가면서 시간을 재는 것
# while sum(deque) < weight


import sys
from collections import deque
input = sys.stdin.readline

bridge_length = 2
weight = 10
truck_weights = [7, 4, 5, 6]
# bridge_length = 100
# weight = 100
# truck_weights = [10]

def solution(bridge_length, weight, truck_weights):
    bridge = deque([0] * bridge_length)
    trucks = deque(truck_weights)
    time = 0
    total_weight = 0

    while True:
        time += 1

        # 다리 위의 트럭 무게 갱신
        total_weight -= bridge.popleft()
        
        # 대기 중인 트럭이 다리에 올라갈 수 있으면 올림
        if trucks and total_weight + trucks[0] <= weight:
            truck = trucks.popleft()
            bridge.append(truck)
            total_weight += truck
        else:
            bridge.append(0)

        # 모든 트럭이 다리를 지날 때까지 반복
        if not trucks and total_weight == 0:
            break

    return time

print(solution(bridge_length, weight, truck_weights))

