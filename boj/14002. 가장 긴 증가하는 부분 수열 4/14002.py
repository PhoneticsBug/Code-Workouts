length = int(input())
nums = list(map(int, input().split()))

dp = [1]*length

# 부분수열이 될 수 있는 순서 만들기
for i in range(length):
    for j in range(i):
        if nums[j] < nums[i] and dp[i] < dp[j] + 1: 
            dp[i] = dp[j] + 1
# print(dp)
print(max(dp)) # 가장 큰 수가 부분수열의 최대길이

# 가장 긴 부분수열 찾기
ans = []
mx = max(dp) # 가장 큰 수부터 시작
for i in range(length-1, -1, -1): # 가장 큰 수부터 반대로 
    if dp[i] == mx:
        ans.append(nums[i])
        mx -= 1

print(' '.join(map(str, ans[::-1])))

# 6
# 10 20 10 30 20 50