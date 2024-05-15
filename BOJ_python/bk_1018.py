'''
체스판 다시 칠하기 - 백준 실버 4
분류 : 구현
'''
import sys

def input():
    return sys.stdin.readline().rstrip('\n')

def count(i, j, idx):
    cnt = 0
    for r in range(i, i + 8):
        for c in range(j, j + 8):
            if board[r][c] != color[idx]:
                cnt += 1
            idx = (idx + 1) % 2
        idx = (idx + 1) % 2
    return cnt

if __name__ == '__main__':
    N, M = map(int, input().split())
    board = [list(input()) for _ in range(N)]
    color = ['W', 'B']

    answer = N * M
    for i in range(N - 7):
        for j in range(M - 7):
            answer = min(answer, count(i, j, 0), count(i, j, 1))

    print(answer)