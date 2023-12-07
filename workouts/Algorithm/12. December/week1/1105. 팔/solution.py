import sys
input = sys.stdin.readline

l, r = map(int, input().split())
length = len(str(r)) # 최대길이

for num in range(l, r+1):
    if length == 0:
        break
    elif num > l and length > len(str(r)):
        continue
    else:
        length = min(length, str(num).count('8'))

print(length)

#################

import sys
input = sys.stdin.readline

l, r = map(int, input().split())
length = len(str(r)) # 최대길이

for num in range(l, r+1):
    if length == 0:
        break
    length = min(length, str(num).count('8'))

print(length)