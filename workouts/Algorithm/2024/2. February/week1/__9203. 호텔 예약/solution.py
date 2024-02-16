import sys
input = sys.stdin.readline

# 테스트 케이스
t = int(input())

for _ in range(t):
    # 예약의 수, 한 방을 청소하는데에 걸리는 시간
    b, c = map(int, input().split())
    for _ in range(b):
        # 예약코드, 입실시간, 퇴실시간
        reserv, in_date, in_time, out_date, out_time = map(str, input().split())