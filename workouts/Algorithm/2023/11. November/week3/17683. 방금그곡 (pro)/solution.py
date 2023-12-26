from datetime import datetime
import sys
input = sys.stdin.readline

# 시간(분) 계산 후 그만큼 반복된 문자열을 넣어서 새로 만들기 > 해당하는 곡이 있는지 확인 
# > 여러개인 경우는 가장 긴 곡 > 시간도 같으면 먼저 나온 곡 > 없으면 (None) 반환

# 파이썬 시간계산 라이브러리가 있던거 같은데 그걸로...?


m = "CC#BCC#BCC#BCC#B"
musicinfos = ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]

def process_sharp(note):
    return note.replace('A#', 'a').replace('C#', 'c').replace('D#', 'd').replace('F#', 'f').replace('G#', 'g')

def check(list1, list2):
    # 리스트 list1의 원소들이 list2에 순서대로 존재하는지 확인하는 함수
    n = len(list1)
    m = len(list2)
    
    i, j = 0, 0
    
    while i < n and j < m:
        if list1[i] == list2[j]:
            i += 1
        j += 1
    if i == n:
        return True
    else:
        return False


def solution(m, musicinfos):
    answer = []
    m = process_sharp(m)

    for music in musicinfos:
        temp = music.split(',')
        # 시간 구하기
        start, end = temp[0].split(':'), temp[1].split(':')
        minutes = (int(end[0]) - int(start[0])) * 60 + int(end[1]) - int(start[1])
        title = temp[2]
        note = process_sharp(temp[3])

        # 음악이 반복되는 부분을 고려하여 악보 생성
        song = (note * (minutes // len(note) + 1))[:minutes]
        
        print(title, m , song)
        
        # 기억한 멜로디가 정확히 존재하는지 확인
        if check(list(m), list(song)): 
            answer.append([title, minutes])

    answer.sort(key=lambda x: x[1], reverse=True)

    if answer:
        return answer[0][0]
    else:
        return "(None)"

# 73점대

###############################################################################################

def sharp(note):
    return note.replace('A#', 'a').replace('C#', 'c').replace('D#', 'd').replace('F#', 'f').replace('G#', 'g')

def solution(m, musicinfos):
    answer = "(None)"
    m = sharp(m)
    max_time = 0

    for music in musicinfos:
        start, end, title, song = music.split(',')
        start, end = start.split(':'), end.split(':')
        time = (int(end[0]) - int(start[0])) * 60 + int(end[1]) - int(start[1])

        song = sharp(song)
        song = song * (time // len(song)) + song[0:time % len(song)]
        
        if m in song and time > max_time:
            max_time = time
            answer = title
    return answer