# 페르마의 소정리 / 분할 정복을 이용한 거듭제곱, 모듈로 곱셈 역원 필요


# 페르마의 소정리 해설
# 10을 3으로 나눴을 때의 나머지는 1 => 10 = 1 (mod 3)
# 어떤 수 a와 소수 p가 있을 때 a % p = a 자신임
# 페르마의 소정리는 a % (p-1) = 1이 된다는 것

# 활용
# a / b 를 계산할때 b의 역원 b`를 알면  a/b == a*b`이 됨
# b`는 b*b` = 1(mod p)를 만족하는 숫자임
# 이는 a/b = a * b**(p-2)로 치환할 수 있다.

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
p = 1_000_000_007

# 팩토리얼: 이전 팩토리얼 값으로 곱한 후 p로 나눈 나머지 추가
factorial = [1, 1]
for i in range(2, 4_000_001):
    factorial.append(factorial[-1] * i % p)

# 거듭제곱 계산 (분할 정복): x = 모수, y = 지수
def power (x, y):
    # 지수가 0일 때
    if y == 0:
        return 1
    else:
        # 지수를 반으로 나눠 계산
        temp = power(x, y//2)
        # 지수가 홀수일 때 x를 한번 더 곱해줌
        if y % 2:
            return temp * temp * x % p
        # 아닌 경우 그대로 반환
        else:
            return temp * temp % p
        
# nCk = {n! * (n-k) ** (p-2) * k ** (p-2)} % p
print(factorial[n] * power(factorial[n-k] * factorial[k] % p, p-2) % p)