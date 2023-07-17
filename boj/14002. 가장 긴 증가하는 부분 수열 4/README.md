
# [14002. 가장 긴 증가하는 부분 수열 4](https://www.acmicpc.net/problem/14002)

문제

    수열 A가 주어졌을 때, 가장 긴 증가하는 부분 수열을 구하는 프로그램을 작성하시오.

    예를 들어, 수열 A = {10, 20, 10, 30, 20, 50} 인 경우에 가장 긴 증가하는 부분 수열은 A = {10, 20, 10, 30, 20, 50} 이고, 길이는 4이다.

입력

    첫째 줄에 수열 A의 크기 N (1 ≤ N ≤ 1,000)이 주어진다.

    둘째 줄에는 수열 A를 이루고 있는 Ai가 주어진다. (1 ≤ Ai ≤ 1,000)

출력

    첫째 줄에 수열 A의 가장 긴 증가하는 부분 수열의 길이를 출력한다.

    둘째 줄에는 가장 긴 증가하는 부분 수열을 출력한다. 그러한 수열이 여러가지인 경우 아무거나 출력한다.

예제 입력 1 

    6
    10 20 10 30 20 50

예제 출력 1 

    4
    10 20 30 50

풀이
```python
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

```
