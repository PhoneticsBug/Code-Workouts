import sys
from string import ascii_uppercase
input = sys.stdin.readline

name = input()

def solution(name):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    spell_move = 0 # 알파벳 변경 횟수
    cursor_move = len(name) - 1 # 커서 이동 횟수

    for i, spell in enumerate(name):
        # 왼쪽으로 이동할지 오른쪽으로 이동할지 확인 (26 == len(alphabet))
        spell_move += min(alphabet.index(spell), 26 - alphabet.index(spell))

        # 해당 알파벳 다음부터 연속된 A 문자열 찾기 (좌우 이동 고려)
        next = i + 1
        # 다음 글자가 마지막 글자가 아닌 동시에 'A'인 경우에는
        while next < len(name) and name[next] == 'A':
            next += 1 # 하나씩 증가

        # 업데이트 값
        # 1. 지금까지의 이동횟수
        # 2. 현재까지 이동한 거리에서 뒤로 돌아가서 다시 앞으로 이동하는 경우 (2 곱함)
        # 3. 남은 문자열을 뒤에서부터 쭉 이동하는 경우
        cursor_move = min(cursor_move, 2*i + len(name) - next, i+2*(len(name) - next))

    return spell_move + cursor_move

