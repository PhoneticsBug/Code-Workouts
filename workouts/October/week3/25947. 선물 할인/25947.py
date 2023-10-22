import sys
input = sys.stdin.readline

n, b, a = map(int, input().split()) # n: 선물의 개수 b: 예산 a: 반값할인이 가능한 최대 선물의 수
gifts = sorted(list(map(int, input().split())))
left, right = 0, 0

# 예산 안에서 제한된 할인을 모두 사용해 살 수 있는 최대의 선물 갯수를 찾기
# 정렬한 다음 작은 것부터 더하다가 예산을 넘어버리면 반값 시도 

def solution(n,b, a, gifts):
    left, right = 0, 0
    for i in range(a):
        b -= gifts[i]//2
        right = i+1
        if b < 0:
            return i
    
    while right < n:
        if right - left < a:
            b -= gifts[right]//2
            if b < 0:
                break
            right += 1
        else:
            if a > 0:
                b -= gifts[left]//2
                left += 1
            else:
                b -= gifts[right]
                if b< 0:
                    break
                right += 1
    return right

print(solution(n, b, a, gifts))