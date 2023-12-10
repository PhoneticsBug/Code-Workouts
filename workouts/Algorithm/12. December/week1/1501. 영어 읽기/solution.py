import sys
input = sys.stdin.readline

dic_num = int(input())
dic = [str(input()) for _ in range(dic_num)]
sent_num = int(input())
sent = [str(input()) for _ in range(sent_num)]

def words(dic, sent):
    # 문장의 각 단어마다 단어 길이로 한번 체크
    # 길이가 같은 경우 정렬한 값이 같은지 체크
    # 애너그램이 가능한 경우만 모아서 숫자를 별도로 저장
    # 1 * a * b *c * d . . . 같은 형식으로 하면 좋을듯?
    group = {}

    for word in dic:
        key = (word[0], word[-1])
        if key not in group:
            group[key] = []
        group[key].append(word)

    result = 1

    for word in sent.split():
        key = (word[0], word[-1])
        if key in group:
            group_words = group[key]
            cnt = len(set(word[1:-1]))
            result *= len(group_words * cnt)

    return result

for sentence in sent:
    result = words(dic, sentence)
    print(result)