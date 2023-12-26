import sys
input = sys.stdin.readline

num = float(input())
ans = []

for i in range(1, 1001):
    timed = i * num
    if timed == int(str(i)[1::] + str(i)[0]):
        ans.append(i)

if ans:
    print(*ans, sep="\n")
else:
    print("No solution")
