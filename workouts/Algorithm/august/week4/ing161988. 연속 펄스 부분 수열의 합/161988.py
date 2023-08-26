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
