from datetime import datetime
import sys
input = sys.stdin.readline

# 시간(분) 계산 후 그만큼 반복된 문자열을 넣어서 새로 만들기 > 해당하는 곡이 있는지 확인 
# > 여러개인 경우는 가장 긴 곡 > 시간도 같으면 먼저 나온 곡 > 없으면 (None) 반환

# 파이썬 시간계산 라이브러리가 있던거 같은데 그걸로...?


m = "ABCDEFG"
musicinfos = ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]

for music in musicinfos:
    temp = music.split(',')
    # 시간 구하기
    t1, t2 = datetime.strptime(temp[0], '%H:%M'), datetime.strptime(temp[1], '%H:%M')
    minutes = int((t2 - t1).total_seconds() / 60)
    title = temp[2]
    note = temp[3]*(minutes//len(temp[3]))
    print(minutes, title, note)
def solution():


    return 