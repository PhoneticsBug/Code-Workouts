import sys
input = sys.stdin.readline

code = list(map(int, input().rstrip())) # 각 숫자로 이뤄진 리스트 형성
size = len(code) # 리스트의 길이

dp = [0] * (size + 1)
dp[0], dp[1] = 1, 1

if code[0] == 0: # 처음부터 0이 나오면 암호가 아에 성립될 수 없음
    # 그 외의 경우는 어디서 나와도 가능
    print(0) 
else:
    for i in range(1, size):
        if code[i] > 0:
            dp[i + 1] += dp[i]
        if 10 <= code[i] + code[i-1]*10 <= 26:
            dp[i + 1] += dp[i-1]
    print(dp[size] % 1000000)