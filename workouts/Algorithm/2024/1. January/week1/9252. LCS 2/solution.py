# import sys
# input = sys.stdin.readline

# a = input()
# b = input()

# dp = [['']*(len(b)+1) for _ in range(len(a)+1)]

# for i in range(1, len(a)+1):
#     for j in range(1, len(b)+1):
#         if a[i-1] == b[j-1]:
#             dp[i][j] = dp[i-1][j-1] + a[i-1]
#         else:
#             dp[i][j] = max(dp[i-1][j], dp[i][j-1], key=len)

# answer = dp[-1][-1]

# print(len(answer))
# if len(answer) > 0: print(answer)

# 틀림

import sys
input = sys.stdin.readline

a = [""] + list(input().rstrip())
b = [""] + list(input().rstrip())
# 2차원 DP 형태로 받아주기
answer = [[""]*len(b) for _ in range(len(a))]

for i in range(1, len(a)):
    for j in range(1, len(b)):
        # 두 문자열의 위치가 같으면 왼쪽 대각선 위에 추가하기
        if a[i] == b[j]:
            answer[i][j] = answer[i-1][j-1] + a[i]
        # 아닌 경우 위쪽/왼쪽 다르게 설정하기 
        else:
            if len(answer[i-1][j]) >= len(answer[i][j-1]):
                answer[i][j] = answer[i-1][j]
            else:
                answer[i][j] = answer[i][j-1]

print(len(answer[-1][-1]), answer[-1][-1], sep='\n')

# ACAYKP
# CAPCAK
# ['', '', '', '', '', '', '']
# ['', '', 'A', 'A', 'A', 'A', 'A']
# ['', 'C', 'A', 'A', 'AC', 'AC', 'AC']
# ['', 'C', 'CA', 'CA', 'AC', 'ACA', 'ACA']
# ['', 'C', 'CA', 'CA', 'AC', 'ACA', 'ACA']
# ['', 'C', 'CA', 'CA', 'AC', 'ACA', 'ACAK']
# ['', 'C', 'CA', 'CAP', 'CAP', 'ACA', 'ACAK']