sequence = [2, 3, -6, 1, 3, -1, 2, 4]	

def solution(sequence):
    answer = 0
    pul, se = [], []
    for i in sequence:
        if i % 2 == 0:
            pul.append(-i)
            se.append(i)
        else:
            pul.append(i)
            se.append(-i)
    pul, se = [i for i in pul if i > 0], [i for i in se if i > 0] 

    print(pul, se)
    print(sum(pul), sum(se))
    return max(sum(pul), sum(se))

print(solution(sequence))


### 용일님 카데인 알고리즘

def kadane(sequence):
    max_sum = sequence[0]
    current_sum = sequence[0]

    for num in sequence[1:]:
        current_sum = max(num, current_sum+num)
        max_sum = max(max_sum, current_sum)

    return max_sum


def solution(sequence):
    p1 = [s if i%2==0 else -s for i, s in enumerate(sequence)]
    p2 = [-s if i%2==0 else s for i, s in enumerate(sequence)]

    answer = max(kadane(p1), kadane(p2))

    return answer