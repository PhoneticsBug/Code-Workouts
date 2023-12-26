n, money = 5, [1, 2, 5]

def solution(n, money):
    dp = [1] + [0]*n

    for coin in money: # 리스트 안의 동전만큼 반복(누적)
        for price in range(coin, n+1): # 해당 동전의 값부터 끝까지
            if price >= coin:
                dp[price] += dp[price - coin] # 앞의 경우의 수를 더한 값
    print(dp)
    return dp[n] % 1_000_000_007

print(solution(n, money))