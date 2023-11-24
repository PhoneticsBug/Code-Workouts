import sys
input = sys.stdin.readline

# 학생 수, 친구관계 수, 가진 돈
n, m, k = map(int, input().split())
payment = list(map(int, input().split()))
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False]*(n + 1)
friends = []

# 최소한의 비용으로 모든 학생을 친구로 만들어야 함
# for문을 돌려서 sort된 리스트 안에서 사용할 수 있는 만큼 친구를 만듦

# dfs 함수
def dfs(v, arr): # v, arr만 남기기
    for i in graph[v]:
        if not visited[i]:
            visited[i] = True
            arr.append(i)
            dfs(i, arr)

# dfs 실행 
for i in range(1, n + 1):
    if not visited[i]:
        arr = [i]
        visited[i] = True
        dfs(i, arr)
        friends.append(arr)

result = 0

# 친구 그룹에서 가장 금액이 적은 것을 더해줌
for friend in friends:
    cost = float('inf')  # 초기값을 무한대로 설정
    for j in friend:
        cost = min(cost, payment[j - 1])  # 학생 번호를 인덱스로 사용하므로, 1을 빼서 사용
    result += cost

if result <= k:
    print(result)
else:
    print("Oh no")
