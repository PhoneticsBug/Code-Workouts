# 키차이의 값의 루트 값은 걸리는 날짜보다 작거나 같다

x, y = map(int, input().split())
if x == y:
    print(0) # 키가 같으면 바로 out
else:
    r = int((y - x) ** 0.5) # 루트 (정수화)
    if r ** 2 == y - x: # 다시 제곱했을 때 원래 값과 같으면
        print(2*r - 1) 
    else:
        s = (y - x) - r**2
        if s <= r:
            print(2*r)
        else:
            print(2*r + 1)