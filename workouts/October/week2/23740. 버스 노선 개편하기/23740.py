import sys
input = sys.stdin.readline

# route [0] = 출발점
# route [1] = 종점
# route [2] = 요금

# [0] 기점으로 sort 시킨 다음에 새로운 2차원 리스트를 return
# return 된 값에서 len(list). *list, sep='\n'

def solution(routes):
    answer = []
    for route in routes:
        if not answer:
            answer.append(route)
        else:
            prev = answer[-1] # 등록된 구간의 마지막
            if prev[1] >= route[0]: # 등록된 구간의 끝이 기존 구간의 앞과 겹친다면
                answer[-1] = [prev[0], max(prev[1], route[1]), min(prev[2], route[2])]
            else:
                answer.append(route)
    return len(answer), answer


if __name__ == "__main__":
    n = int(input())
    routes = sorted([list(map(int, input().split())) for _ in range(n)])

    num_routes, new_routes = solution(routes)

    print(num_routes)
    for route in new_routes:
        print(*route)
