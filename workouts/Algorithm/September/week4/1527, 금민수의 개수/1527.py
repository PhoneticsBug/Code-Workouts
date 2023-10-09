import sys
from itertools import product # 두 리스트의 모든 조합을 생성
input = sys.stdin.readline

a, b = map(int, input().split())
x, y = len(str(a)), len(str(b))
cnt = 0

for i in range(x, y + 1):
    lst = list(product([4, 7], repeat=i))
    for num in lst:
        n = int(''.join(map(str, num))) # 정수화
        if a <= n <= b:
            cnt += 1
            
print(cnt)