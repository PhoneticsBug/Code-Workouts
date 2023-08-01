N = int(input()) # 1~9 사이의 수
number = int(input()) # 받는 입력값 (n으로 표현할 수)

#----------------------------------------------------

def solution(N, number):
    S = [{N}]
    for  i in range(2, 9):
        temp = [int(str(N)*i)]
        for j in range(0, int(i/2)):
            for x in S[j]:
                for y in S[i - j - 2]:
                    temp.append(x+y)
                    temp.append(x-y)
                    temp.append(y-x)
                    temp.append(x*y)
                    if x != 0:
                        temp.append(y//x)
                    if y != 0:
                        temp.append(x//y)
        if number in set(temp):
            return i
        S.append(temp)
    return -1