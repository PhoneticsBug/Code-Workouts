import sys
input = sys.stdin.readline

N = int(input())
hanoi = [list(map(int, input().split())), [], []]
cnt = 0

# 기본적인 구조는 다음과 같다.
# 기둥 1과 2를 오가면서 3번 기둥에 올라갈 수 있는 원판이 제일 위에 오게 반복함
# 그 과정을 hanoi[2]에 넣음 (마지막 기둥은 어차피 n~1이 될 것이므로 과정만 넣기)

while N > 0: 

    # 첫번째 기둥에 있다면
    if N in hanoi[0]:
        while hanoi[0]:
            now = hanoi[0].pop() # 가장 마지막 숫자를 꺼내서 now에 저장
            if now == N:
                hanoi[2].append("1 3")
                cnt += 1
                N -= 1
                break
            else:
                hanoi[2].append("1 2") # 두번째 스택으로 이동
                cnt += 1
                hanoi[1].append(now)
    
    # 두번째 기둥에 있다면
    elif N in hanoi[1]:
        while hanoi[1]:
            now = hanoi[1].pop() # 마지막 숫자를 꺼내서 저장
            if now == N:
                hanoi[2].append("2 3")
                cnt += 1
                N -= 1
                break
            else:
                hanoi[2].append("2 1")
                cnt += 1
                hanoi[0].append(now)

print(cnt)
print("\n".join(hanoi[2]))
