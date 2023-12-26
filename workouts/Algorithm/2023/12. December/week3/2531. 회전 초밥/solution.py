import sys
from collections import defaultdict
input = sys.stdin.readline

# n = 초밥 접시 수 
# d = 초밥 종류
# k = 연속해서 먹는 접시 수
# c = 쿠폰 번호
n, d, k, c = map(int, input().split())
sushi = [int(input()) for _ in range(n)]

# 쿠폰 번호를 포함하는 k+1의 배열을 찾기
# 쿠폰번호 c는 여러개가 존재하므로 모든 배열을 찾아야? 함
# 이 값들의 set() 길이를 answer에 저장 후 갱신

def solution():
    counts = defaultdict(int)
    varieties = 0

    # 각 초밥의 종류별 개수 저장
    for i in range(k):
        counts[sushi[i]] += 1

    # 쿠폰이 있는 초밥은 하나 더 먹을 수 있으므로
    counts[c] += 1

    varieties = len(counts)

    # 슬라이딩 윈도우로 한칸씩 이동하며 가짓수 갱신
    for i in range(k, n + k):
        # 윈도우 밖의 초밥 제거
        counts[sushi[i- k]] -= 1
        if counts[sushi[i - k]] == 0:
            del counts[sushi[i - k]]

        # 윈도우 안에 들어오는 초밥
        counts[sushi[i % n]] += 1

        # 쿠폰 처리
        if counts[c] == 0:
            varieties = max(varieties, len(counts) + 1)
        else:
            varieties = max(varieties, len(counts))
        
    return varieties

print(solution())

