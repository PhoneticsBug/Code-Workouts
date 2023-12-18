import sys
input = sys.stdin.readline

# 10 이상의 수를 사용하는 n진법은 0~9 이후에 알파벳 ABCD...를 이용하여 10 이후의 숫자를 표현
# ex) 0 1 2 3 4 5 6 7 8 9 A(10) B(11) C(12) D(13) . . .


a, b = map(str, input().split())

numbers = dict()
count = 0
answer = [0, 0]

# 0부터 9까지
for i in range(0, 10):
    numbers[str(i)] = i

# a부터 z까지
for i in range(26):
    numbers[chr(97+i)] = i+10

# numbers에는 각 정수에 대한 n진법상의 숫자값이 저장됨

# 각 입력의 최댓값 (알파벳의 가장 뒤 숫자가 받아짐)
a_max = max(list(a))
b_max = max(list(b))

# 10진법으로 변환
def solution(string, notation):
    temp = 0
    for i in range(len(string)):
        # 변환된 값 * 자릿수 ** 진법
        digit = numbers[string[-1 - i]]
        temp += digit * notation**i
    return temp

# 0~z까지의 길이 (len(numbers))
for i in range(numbers[a_max]+1, 37):
    for j in range(numbers[b_max]+1, 37):
        if i == j:
            continue
        # X를 A진법 및 B진법으로 변환했을 때 일치하는지 확인
        if solution(a, i) == solution(b, j):
            # X 제한범위 초과 여부 확인 (파이썬에서는 필요없지만 필요없는 계산을 제외함으로써 속도 개선... 할 줄 알았는데 똑같음)
            if solution(a, i) >= 2**63: 
                continue
            # 정답 업데이트 및 조합 갯수 기록
            answer[0] = i
            answer[1] = j
            count += 1

if count == 0:
    print("Impossible")
elif count > 1:
    print("Multiple")
elif count == 1:
    print(solution(a, answer[0]), answer[0], answer[1])

