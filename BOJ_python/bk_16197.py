# 두 동전
import sys
from collections import deque as dq

# [A] 입력 함수 초기화
def input():
    return sys.stdin.readline().rstrip('\n')

# [B] bfs
def bfs(N, M, board, coins):
    delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    q = dq([coins + [0]])
    while q:
        coin1, coin2, cnt = q.popleft()
        # [B-1] 종료 조건
        if cnt >= 10:
            return -1
        # [B-2] 두 개의 동전이 동시에 이동
        for di, dj in delta:
            ni1, nj1 = coin1[0] + di, coin1[1] + dj
            ni2, nj2 = coin2[0] + di, coin2[1] + dj
            flag1 = flag2 = False
            if ni1 < 0 or nj1 < 0 or ni1 >= N or nj1 >= M: flag1 = True
            if ni2 < 0 or nj2 < 0 or ni2 >= N or nj2 >= M: flag2 = True
            # [B-3] 두 개의 동전이 모두 땅에 떨어지면 안되므로 베타적 논리 연산
            if flag1 ^ flag2: return cnt + 1  # A ^ B 두 변수의 boolean값이 다를때만 True를 반환함
            if flag1 and flag2: continue
            ti1, tj1 = coin1
            ti2, tj2 = coin2
            if board[ni1][nj1] == '.':  # 벽이 아니면 좌표 이동
                ti1, tj1 = ni1, nj1
            if board[ni2][nj2] == '.':
                ti2, tj2 = ni2, nj2
            q.append([[ti1, tj1], [ti2, tj2], cnt + 1])

# [C] 메인 로직 함수
def solution(N, M, board):
    # [C-1] 동전 위치 저장
    coins = []
    for i in range(N):
        for j in range(M):
            if board[i][j] == 'o':
                board[i][j] = '.'
                coins.append([i, j])
    # [C-2] bfs
    return bfs(N, M, board, coins)

# [main]
if __name__ == '__main__':
    N, M = map(int, input().split())
    board = [list(input()) for _ in range(N)]
    print(solution(N, M, board))