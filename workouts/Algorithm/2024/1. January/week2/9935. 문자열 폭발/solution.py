import sys
input = sys.stdin.readline

letter = input().rstrip()
tnt = input().rstrip()

while letter.count(tnt) > 0:
    letter = ''.join(letter.split(tnt))

if letter:
    print(letter)
else:
    print('FRULA')

# 시간 초과
    
import sys
input = sys.stdin.readline

letter = input().rstrip()
tnt = input().rstrip()
stack = []
length = len(tnt)

# 스택 사용
# 문자열을 글자 하나씩 돌면서 마지막 글자가 tnt에 해당하면 지우고 계속함
for char in letter:
    stack.append(char)
    if ''.join(stack[-length:]) == tnt:
        del stack[-length:]

result = ''.join(stack)
print(result if result else 'FRULA')