'''
색종이 - 백준 실버5
분류 : 누적합
'''
import sys

# [A] 입력함수 초기화
def input():
    return sys.stdin.readline().rstrip('\n')

# [B] 로직함수
def solution(attachs):
    # [1] 2차원 누적합 포인트 표시
    area = [[0] * 101 for _ in range(101)]
    for x, y in attachs:
        area[y][x] += 1
        area[y + 10][x] -= 1
        area[y][x + 10] -= 1
        area[y + 10][x + 10] += 1

    # [2] 2차원 누적합 진행
    for i in range(1, 101):
        for j in range(1, 101):
            area[i][j] += area[i - 1][j]
    for i in range(1, 101):
        for j in range(1, 101):
            area[i][j] += area[i][j - 1]

    # [3] 카운트
    cnt = 0
    for i in range(101):
        for j in range(101):
            if area[i][j] < 1: continue
            cnt += 1

    return cnt

# [Main]
if __name__ == '__main__':
    N = int(input())
    attachs = [tuple(map(int, input().split())) for _ in range(N)]

    print(solution(attachs))