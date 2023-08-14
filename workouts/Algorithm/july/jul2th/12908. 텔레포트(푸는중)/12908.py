start = list(map(int, input().split()))
end = list(map(int, input().split()))

teleport = [] # [list(map(int, input().split())) for _ in range(3)]
for i in range(3):
    temp = list(map(int, input().split()))
    if sum(temp[2:]) - sum(temp[:2]) > 10: # 텔레포트 하는 거리가 10보다 큰지 아닌지 확인 (유효성 검?사)
        if temp[0] > start[0] and temp[1] > start[1]: # 텔레포트 시작이 실제 시작보다 멀리 있는지
            if temp[2] < end[0] and temp[3] < end[1]: # 텔레포트 끝이 실제 끝보다 앞에 있는지 
                teleport.append(temp)

time = 0

### 아... 구현문제가 아니었네 