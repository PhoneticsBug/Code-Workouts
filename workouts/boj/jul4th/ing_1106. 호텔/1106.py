# import sys
# input = sys.stdin.readline

# c, n = map(int, input().split()) # 고객의 수, 도시의 수
# city = [map(int, input().split()) for _ in range(n)] 
#내부 인덱스 0은 금액, 1은 늘어나는 고객 수


temp = [[10, 3], [3, 1], [2, 2], [1, 3]]
temp.sort()

money = 0
c = 0
while True:
    for i in range(3):
        if c >= 10:
            break
        else:
            money += temp[i][0]*(10//temp[i][0])
            c += temp[i][0]*(10//temp[i][0])

print(money, c)
        
https://www.acmicpc.net/problem/1106