# 틱택토
import sys

# [A] 입력 함수 초기화
def input():
    return sys.stdin.readline().rstrip('\n')

# [B] 2차원 좌표 => 1차원화
def tr(i, j):
    return 3 * i + j

# [C] 로직 함수
def solution(boards):
    answer = []
    for board in boards:
        # [C-1] X, O의 갯수 카운트
        cnt = {'X': 0, 'O': 0}
        trio = {'X': 0, 'O': 0}
        for i in range(3):
            # [C-2] 가로 방향 3칸 완성 탐색
            if board[tr(i, 0):tr(i, 3)].count('X') == 3:
                trio['X'] += 1
            if board[tr(i, 0):tr(i, 3)].count('O') == 3:
                trio['O'] += 1
            for j in range(3):
                if board[tr(i, j)] == '.': continue
                cnt[board[tr(i, j)]] += 1

        # [C-3] 세로 방향 3칸 완성 탐색
        for j in range(3):
            if board[tr(0, j)] == '.': continue
            if board[tr(0, j)] == board[tr(1, j)] == board[tr(2, j)]:
                trio[board[tr(0, j)]] += 1

        # [C-4] 대각선 방향 3칸 완성 탐색
        if board[tr(0, 0)] != '.':
            if board[tr(0, 0)] == board[tr(1, 1)] == board[tr(2, 2)]:
                trio[board[tr(0, 0)]] += 1
        if board[tr(1, 1)] != '.':
            if board[tr(2, 0)] == board[tr(1, 1)] == board[tr(0, 2)]:
                trio[board[tr(1, 1)]] += 1

        # [C-5] 조건 분기
        case = 'invalid'
        if cnt['X'] == cnt['O'] + 1:
            if trio['X'] >= 1 and trio['O'] == 0:
                case = 'valid'
            elif trio['X'] == 0 and trio['O'] == 0 and sum(cnt.values()) == 9:
                case = 'valid'
        elif cnt['X'] == cnt['O']:
            if trio['O'] >= 1 and trio['X'] == 0:
                case = 'valid'

        answer.append(case)

    return '\n'.join(answer)

# [main]
if __name__ == '__main__':
    boards = []
    while True:
        line = input()
        if line == 'end': break
        boards.append(line)
    print(solution(boards))