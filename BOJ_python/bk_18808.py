# 스티커 붙이기
import sys

# [A] 입력 함수 초기화
def input():
    return sys.stdin.readline().rstrip('\n')

# [B] 스티커를 시계방향 90도 회전시키는 함수
def rotate(r, c, matrix):
    new_matrix = [[0] * r for _ in range(c)]
    for i in range(r):
        for j in range(c):
            new_matrix[j][r - i - 1] = matrix[i][j]
    return c, r, new_matrix

# [C] 스티커를 붙일 수 있는지 확인하는 함수
def check(x, y, r, c, matrix):
    for i in range(x, x + r):
        for j in range(y, y + c):
            if i < 0 or j < 0 or i >= N or j >= M:
                return False
            if notebook[i][j] and matrix[i - x][j - y]:
                return False
    return True

# [D] 스티커를 붙이는 함수
def attach(x, y, r, c, matrix):
    for i in range(x, x + r):
        for j in range(y, y + c):
            if matrix[i - x][j - y]:
                notebook[i][j] = 1

# [1] 데이터 입력 및 초기화
N, M, K = map(int, input().split())
delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]
notebook = [[0] * M for _ in range(N)]

# [2] 각 스티커마다 회전하며, 위치를 확인하고 붙임
for _ in range(K):
    R, C = map(int, input().split())
    sticker = [list(map(int, input().split())) for _ in range(R)]
    flag = False
    for _ in range(4):
        for i in range(N):
            for j in range(M):
                if check(i, j, R, C, sticker):
                    attach(i, j, R, C, sticker)
                    flag = True
                    break
            if flag: break
        if flag: break
        R, C, sticker = rotate(R, C, sticker)
print(sum(map(sum, notebook)))