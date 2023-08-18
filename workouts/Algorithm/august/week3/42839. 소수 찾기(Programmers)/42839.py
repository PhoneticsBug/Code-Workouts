from itertools import permutations

def solution(numbers):
    max_num = 9999999

    prime = [False, False] + [True for _ in range(max_num+1)]
    for num in range(2, max_num+1):
        if prime[num] == True:
            for multi_num in range(2*num, max_num+1, num):
                prime[multi_num] = False

    answer = 0
       
    nums = list(numbers)
    nums_list = []
    for i in range(1, len(nums)+1):
        nums_list = nums_list + list([int(''.join(j for j in i)) for i in permutations(nums, i)])
    nums_list = set(nums_list)
    for i in nums_list:
        if prime[i] == True:
            answer += 1
            

    return answer

print(solution("011"))