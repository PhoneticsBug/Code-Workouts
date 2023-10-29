import sys
input = sys.stdin.readline

# 총인원 N, 사람 수 K, 목표 메시지의 번호 Q
N, K, Q = map(int, input().split())
unread = set(chr(ord('A') + i) for i in range(N))
unread.remove('A') # A는 항상 첫번째 문자를 읽으므로

# K번만큼 메시지를 읽지 않은 사람의 수 R, 송신자의 이름 P
messages = [[0, 0]] + [input().split() for _ in range(K)]
res = []

# 메시지를 보낸 사람은 앞의 메시지를 읽었다 (제거)
for i in range(Q, len(messages)):
    if messages[i][1] in unread:
        unread.remove(messages[i][1])

# 반대의 순서로, 이전과 읽은 횟수가 같다면 이전 채팅을 쓴 사람이 그걸 봤다는 뜻이므로
for i in range(Q - 1, 0, -1):
    if messages[i][0] == messages[Q][0]:
        if messages[i][1] in unread:
            unread.remove(messages[i][1])

res = sorted(list(unread))

# 만약 모두 읽었다면
if messages[Q][0] == '0': 
    print(-1)
else:
    print(*res, sep=' ')