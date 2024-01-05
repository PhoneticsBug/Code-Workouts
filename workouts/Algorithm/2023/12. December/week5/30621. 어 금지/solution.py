import sys
input = sys.stdin.readline

# 입력
n = int(input())

# t  = 어? 를 외칠 수 있는 시간
# b = 어? 를 외칠 수 없는 시간(앞의 시간부터 i시 까지)
# e = 어? 가 줄 수 있는 혼란 점수
time = list(map(int, input().split()))
breaktime = list(map(int, input().split()))
effect = list(map(int, input().split()))

# DP
dp = [0] * n
dp[0] = effect[0]

# 이진탐색
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return start

# DP 계산
for i in range(1, n):
    # 어?를 외친 마지막 인덱스 찾기
    previous = binary_search(time, time[i] - breaktime[i], 0, i)

    # 이전까지의 최대 혼란점수와 현재 시간의 가능한 최대 점수를 찾고 저장하기
    dp[i] = max(dp[i - 1], effect[i])
    if previous > 0:
        dp[i] = max(dp[i], dp[previous - 1] + effect[i])

# 결과 출력
print(dp[-1])
