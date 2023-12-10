import sys
input = sys.stdin.readline

# 애너그램이 맞는지 확인할 수 있도록 정렬된 값을 반환
def get_word(word):
    length = len(word)
    key = str(length) + word[0] + word[length - 1] + ''.join(sorted(word[1:-1]))
    return key

# 딕셔너리에 단어 저장
n = int(input())
dic = dict()
for _ in range(n):
    arr = list(input().rstrip())
    key = get_word(arr)

    if dic.get(key) is not None:
        dic[key] += 1
    else:
        dic[key] = 1

# 문장 입력 후 단어마다 체크해서 출력
m = int(input())
for _ in range(m):
    arr = list(input().rstrip().split())
    result = 1
    check = 0
    
    for i in arr:
        key = get_word(i)

        if dic.get(key) is not None:
            result *= dic[key]
            check += 1

    if not check:
        print(0)
    else:
        print(result)
