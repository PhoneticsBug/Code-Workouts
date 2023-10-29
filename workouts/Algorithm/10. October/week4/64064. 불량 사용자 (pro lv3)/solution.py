from itertools import permutations

# 하나가 선택되면 다른 하나를 선택할 수 없는 경우가 있다. crodo, frodo가 "*rodo", "*rodo"인 경우
def solution(user_id, banned_id):

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
        