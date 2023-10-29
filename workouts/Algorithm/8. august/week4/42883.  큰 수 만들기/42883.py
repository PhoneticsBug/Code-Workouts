from itertools import permutations, combinations

k = 4
number = "4177252841"

# from itertools import combinations

# def solution(number, k):
#     answer = ''
#     numlist = list(number)
#     maxlen = len(number) - k
    
#     comb = list(int(''.join(i)) for i in combinations(numlist, maxlen))
    
#     answer += str(max(comb))
    
#     return answer
# --------------- 시간 초과 ---------------

def solution(number, k):
    answer = ''
    for i in number:
        if not answer: # answer이 비어있다면
            answer += i # 일단 하나 추가
            continue
        while answer[-1] < i and k > 0: # 새로 들어오는 i가 answer의 마지막보다 큰지 확인
            answer = answer[:-1] # answer 뒷부분 제거
            k -= 1 # k 줄이기
            if not answer or k <= 0: # k가 0이 되면 while문 나가기
                break
        answer += i # 계속 추가
        if len(answer) == len(number) - k: # 최대 길이에 도달하면 for문 나가기
            break
    return answer

print(solution(number, k))