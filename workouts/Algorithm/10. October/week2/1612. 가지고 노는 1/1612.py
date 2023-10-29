import sys
input = sys.stdin.readline

n = int(input())

if int(str(n)[-1]) % 2 != 0 or int(str(n)[-1]) % 5 != 0:
    # 나머지를 저장하는 set 생성 // 메모리 용량이 넉넉하면 defaultdict 쓰는게 나을 수 있음
    remainder_set = set() 
    remainder = 0

    # 길이가 n+1인 '1'로만 이루어진 숫자까지 검사
    for length in range(1, n+2):
        remainder = (remainder * 10 + 1) % n

        if remainder == 0:   # 나머지가 없다면 현재 길이 출력 후 종료
            print(length)
            break
            
        elif remainder in remainder_set:   # 만약 같은 나머지가 이미 있었다면, -1 출력 후 종료 (반복되는 수열)
            print(-1)
            break
            
        else:   # 그렇지 않다면, 현재의 나머지 값을 set에 추가 
            remainder_set.add(remainder)

else:
    print(-1)   # 마찬가지로, n의 마지막 자리가 짝수거나 5의 배수인 경우 -1 출력 



# 11 초과의 1로만 이루어진 모든 숫자는 자연수로 나누어 떨어진다
# 이 때 11...11 의 길이 k는 n+2보다 크거나 같다.


# 메모리 용량이 넉넉하면 defaultdict 쓰는게 나을 수 있음

# remainder_set = defaultdict(lambda: False)
# remainder_set[remainder] = remainder
# if remainder_set[remainder]:
# O(1) 복잡도