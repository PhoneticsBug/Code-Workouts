import sys
input = sys.stdin.readline

scores = [[2,2],[1,4],[3,2],[3,2],[2,1]]

# 정렬하기...?
# 조건
# 두 점수 다 다른사람에게 뒤쳐지면 안됨 
# 두 점수의 합이 높은 순서대로 석차
# 같은 경우 동석차 >>> 1등이 2명이면 다음 순서는 3등

# 1. 꼴지가 되어야 하는 경우 색출
# 2. 아닌 케이스 중 점수 합을 기준으로 정렬
# 3. 인덱스 순서대로 해서 완호 찾기

def solution(scores):
    wanho = scores[0]

    for score in scores[1:]:
        if score[0] > wanho[0] and score[1] > wanho[1]:
            return -1

    scores = sorted(scores, key=sum, reverse=True)

    return scores.index(wanho) + 1

# 72점


def solution(scores):
    wanho = scores[0]
    candidate = []

    for i, score1 in enumerate(scores):
        for j, score2 in enumerate(scores):
            if i != j and score1[0] < score2[0] and score1[1] < score2[1]:
                break
        else:
            candidate.append(score1)

    if wanho not in candidate:
        return -1

    candidate.sort(key=sum, reverse=True)

    return candidate.index(wanho) + 1

# 88점 (시간초과)

def solution(scores):
    answer = 1 # 완호의 석차

    # 완호룰 제외한 모든 사원 중 점수 합이 완호보다 큰 경우에 완호의 등수를 뒤로 미룸
    for i in range(1, len(scores)):
        if sum(scores[i]) > sum(scores[0]):
            if check(scores[i], scores):
                answer += 1

    # 완호보다 두 점수가 모두 높은 사원이 한명이라도 있다면 -1 리턴
    for i in range(1, len(scores)):
        if scores[i][0] > scores[0][0] and scores[i][1] > scores[0][1]:
            return -1

    return answer


def check(arr, scores):
    for score in scores:
        if arr[0] < score[0] and arr[1] < score[1]:
            return False
    return True

# 92점 (시간초과 - 마지막 두 케이스)