from itertools import permutations

def solution(numbers):
    answer = ''
    temp = list(permutations(str(i) for i in numbers))

    max_num = 0
    for tpl in temp:
        num = ''
        for i in tpl:
            num += i
        if int(num) > max_num:
            max_num = int(num)
    answer = str(max_num)

    return answer

#### 시간초과 ####

def solution(numbers):
    # 받은 숫자들을 string화 해서 리스트에 넣어줌
    str_nums = list(map(str, numbers))

    # 정렬된 숫자들을 만들어줌 (뒤가 0인 숫자가 가장 뒤로 갈 수 있도록)
    sorted_nums = sorted(str_nums, key=lambda x: x*3, reverse=True)
  
    # answer에 추가
    answer = ''.join(sorted_nums)

    # 0000이 나오는 경우 대비해서 한번 정수화한 다음 다시 str화
    return str(int(answer))

print(solution(	[0, 0, 0, 0]))