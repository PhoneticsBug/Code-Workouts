import sys
input = sys.stdin.readline

# 빛의 돌의 개수 n, 옮기는 방식을 바꾸는 비용 k
n, k = map(int, input().split())
# 돌을 끌고가는 비용과 들고가는 비용
drag = list(map(int, input().split()))
pull = list(map(int, input().split()))
cost = 0
dp = [False for _ in range(n)] # False = drag, True = pull

# 돌을 옮길 때 다음에 할 방법 (그대로 옮기기, 바꿔옮기기 + 비용)

for i in range(n):

    if i == 0: # 첫번째 돌 때
        min_cost = min(drag[i], pull[i])
        if min_cost == drag[i]:
            dp[i] = False
        else:
            dp[i] = True

    elif dp[i-1] == False: # 앞에서 끌고간 경우
        min_cost = min(drag[i], pull[i]+k) # 끌고 가는 것과 밀고 가는 것(+k) 비교
        if min_cost != drag[i]:
            dp[i] = True
        
    elif dp[i-1] == True: # 앞에서 밀고간 경우
        min_cost = min(drag[i]+k, pull[i]) # 밀고 가는 것과 끌고 가는 것(+k) 비교
        if min_cost != pull[i]:
            dp[i] = False

    cost += min_cost # cost 값 갱신
    last_move = min_cost # 마지막 이동값 갱신

print(cost)

# 5점, 어떻게 하면 되는지 잘 모르겠다... 
        
