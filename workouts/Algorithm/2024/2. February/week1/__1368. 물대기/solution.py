# 최소 스패닝 트리(Minimum Spanning Tree - MST) 알고리즘 사용
# 통신/도로/유통망에서 길이/구축비용/전송시간을 최소로 하기 위해 사용됨
# 이번 문제에서 사용되는 경우는 그리디를 접목한 크루스칼!

# 풀이 방?법
#   1. 가상의 노드를 하나 더 만듦
#   2. 이를 루트로 해서 우물을 직접 파는 비용 추가
#   3. 우물을 직접 파고 논을 연결하는 비용을 모두 한 그래프로 연결가능

# 하나의 그래프로 모든 이동을 가능하게 만들 수 있다.

import sys
input = sys.stdin.readline

n = int(input())
water = [int(input()) for _ in range(n)]
field = [list(map(int, input().split())) for _ in range(n)]

