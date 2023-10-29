import sys
input = sys.stdin.readline

from itertools import permutations

# ban 가능성 체크
def check(users, banned_id):
    for i in range(len(banned_id)):
        if len(users[i]) != len(banned_id[i]):
            return False

        for j in range(len(users[i])):
            if banned_id[i][j] == "*":
                continue
            if banned_id[i][j] != users[i][j]:
                return False
    return True

def solution(user_id, banned_id):
    # 가능성이 있는 아이디의 개수를 각자 곱하면 됨
    # 각 아이디는 총 8개, 유저 아이디도 8자 이내이기 때문에 최대 64회까지만 루프를 돌려도 됨
    # 이럼 그냥 무식하게 돌려도 될거 같은데... 
    
    # 하나가 선택되면 다른 하나를 선택할 수 없는 경우가 있다. crodo, frodo가 "*rodo", "*rodo"인 경우
    

    
    users = list(permutations(user_id, len(banned_id)))
    banned_users = []
    
    for user in users:
        if not check(user, banned_id):
            continue
        else:
            user = set(user)
            if user not in banned_users:
                banned_users.append(user)
    return len(banned_users)
        