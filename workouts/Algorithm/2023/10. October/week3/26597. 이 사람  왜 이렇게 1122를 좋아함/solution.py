import sys
input = sys.stdin.readline

Q = int(input())
start, end = -10**18, 10**18
answer = "Hmm..."
count = 0
guesses = list(input().split() for _ in range(Q))

for i in range(1, Q+1):
    num, updown = int(guesses[i-1][0]), guesses[i-1][1]

    if updown == "^":
        if num < start:
            continue
        if num < end:
            start = num + 1
        else:
            answer = "Paradox!"
            count = i
            break

    elif updown == "v":
        if num > end:
            continue
        if num > start:
            end = num - 1 
        else: 
            answer="Paradox!"
            count=i 
            break

    if start == end and answer == "Hmm..." :
        answer, count= 'I got it!', i 


print(answer)
if count > 0:
    print(count)
