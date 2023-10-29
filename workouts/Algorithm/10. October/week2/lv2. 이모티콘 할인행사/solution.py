import sys
input = sys.stdin.readline
from itertools import product

users = list(map(int, input().split()))
emoticons = list(map(int, input().split()))

def check(users, emoticons, discounts):
    subscribe = 0 
    emoji_purchase = 0
    for threshold, budget in users:
        purchased = 0
        # 이용권 혹은 구매한 이모티콘 추가 
        for emoticon, discount in zip(emoticons, discounts):
            if threshold <= discount:
                purchased += emoticon * (100 - discount) // 100

        if budget <= purchased:
            subscribe += 1
        else:
            emoji_purchase += purchased
    
    return [subscribe, emoji_purchase]

# 할인율 찾기
def solution(users, emoticons):
    answer = [0, 0]
    discounts = [10, 20, 30, 40]

    for i in product(discounts, repeat=len(emoticons)):
        rslt = check(users, emoticons, i)
        if answer[0] < rslt[0] or (answer[0] == rslt[0] and answer[1] < rslt[1]):
            answer = rslt

    return answer


