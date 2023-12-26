def solution(n, s):
    answer = []
    # 최고의 집합을 도출할 수 없는 경우
    if n > s:
        answer.append(-1)
    # 그 외의 경우
    else:
        div = s//n
        rest = s%n
        # 몫을 갯수만큼 넣어줌
        for _ in range(n):
            answer.append(div)
        if s%n == 0: # 나머지가 0이면 이들을 곱하는게 제일 큼
            return answer
        else: # 나머지 경우에는 rest가 0이 될 때까지 1씩 더해줌
            while rest > 0: 
                for i in range(len(answer)):
                    if rest > 0:
                        answer[i] += 1
                        rest -= 1
                    else:
                        break
    return answer[::-1]