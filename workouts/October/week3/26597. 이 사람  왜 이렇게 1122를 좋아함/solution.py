import sys
input = sys.stdin.readline

Q = int(input())
start, end = int(-1 * 1e18) , int(1e18) + 1
answer = "Hmm..."
count = 0

for i in range(1, Q+1):
    num, updown = input().split()
    num = int(num)
    if updown == "^":
        start = max(num, start)

    elif updown == "v":
        end = min(num, end)

    diff = end - start

    if diff < 2:
        answer = "Paradox!"
        count = i
        break
    elif diff == 2 and count == 0:
        count = i
        answer = "I got it!"
        

print(answer)
if count > 0:
    print(count)