
# 이분탐색을 이용해서 10000000 * n 이 되는 두 값을 찾으면 됨

import sys
input = sys.stdin.readline

while True:
    try:
        x = int(input())*10_000_000 # 구멍의 너비
        n = int(input()) # 레고 조각의 개수
        blocks = sorted([int(input()) for _ in range(n)]) # n개의 블록들

        start, end = 0, n-1
        ans = True
        while start < end:
            if blocks[start] + blocks[end] == x:
                print(f'yes {blocks[start]} {blocks[end]}')
                ans = False
                break
            elif blocks[start] + blocks[end] < x:
                start += 1
            else:
                end -= 1
        if ans:
            print('danger')
    except:
        break
