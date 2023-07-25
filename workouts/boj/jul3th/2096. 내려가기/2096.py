import sys 
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
maxi, mini = arr, arr
# 양끝단의 경우 [0, 1], [1, 2], 그 외의 경우 아래의 모든 인덱스 중 최대값/최소값 검색

for _ in range(n - 1):
    arr = list(map(int, input().split()))
    # 입력받을 때마다 maxi와 mini를 갱신해줌
    maxi = [arr[0] + max(maxi[0], maxi[1]), arr[1] + max(maxi), arr[2] + max(maxi[1], maxi[2])]
    mini = [arr[0] + min(mini[0], mini[1]), arr[1] + min(mini), arr[2] + min(mini[1], mini[2])]

print(max(maxi), min(mini))