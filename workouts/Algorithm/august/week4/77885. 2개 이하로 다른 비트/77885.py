numbers = [2, 7]

def solution(numbers):
    answer = []
    for num in numbers:
        binary = ['0'] + list(str(format(num, 'b')))

        idx = ''.join(binary).rfind('0')
        binary[idx] = '1'

        if num % 2 == 1:
            binary[idx + 1] = '0'

        answer.append(int(''.join(binary), 2))
    return answer

print(solution(numbers))

# 