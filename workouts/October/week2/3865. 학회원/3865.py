import sys
input = sys.stdin.readline

#  (학회) : [소속 인원]
# 특정 학회의 모든 회원이 다른 학회에 속한 경우 그 학회의 이름이 들어감



def solution():
    return



if __name__ == "__main__":
    while True:
        n = int(input())
        if n == 0:
            break
        else:
            study, members = input().rstrip("\n").split(":")
            members = members.rstrip(".").split(",")
            target = [study] + members
            print(target)
