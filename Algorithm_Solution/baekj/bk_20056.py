# 마법사 상어와 파이어볼
import sys
import math

# [A] 입력 함수 초기화
def input():
    return sys.stdin.readline().rstrip('\n')

# [main]
if __name__ == '__main__':
    N, M, K = map(int, input().split())
    board = [[[] for _ in range(N)] for _ in range(N)]
    fireballs = []
    for _ in range(M):
        i, j, m, s, d = map(int, input().split())
        board[i-1][j-1].append((0, m, s, d))
        if (i-1, j-1) in fireballs: continue
        fireballs.append((i-1, j-1))

    delta = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1),  (0, -1), (-1, -1)]
    for i in range(1, K + 1):
        nxt = []
        for vi, vj in fireballs:
            while board[vi][vj]:
                if board[vi][vj][0][0] == i: break
                c, m, s, d = board[vi][vj].pop(0)
                ni, nj = (vi + delta[d][0] * s) % N, (vj + delta[d][1] * s) % N
                board[ni][nj].append((c + 1, m, s, d))
                if (ni, nj) in nxt: continue
                nxt.append((ni, nj))

        nxt2 = []
        for j in range(len(nxt)):
            vi, vj = nxt[j]
            if len(board[vi][vj]) < 2:
                nxt2.append((vi, vj))
                continue
            sm = ss = cnt = 0
            dir = []
            while board[vi][vj]:
                c, m, s, d = board[vi][vj].pop(0)
                sm += m
                ss += s
                cnt += 1
                dir.append(bool(d % 2))
            if math.floor(sm / 5) < 1: continue
            if dir.count(False) == cnt or dir.count(True) == cnt:
                delta2 = [0, 2, 4, 6]
            else:
                delta2 = [1, 3, 5, 7]
            for d in delta2:
                board[vi][vj].append((i, math.floor(sm / 5), math.floor(ss / cnt), d))
            nxt2.append((vi, vj))

        fireballs = nxt2

    answer = 0
    for vi, vj in fireballs:
        for _, m, _, _ in board[vi][vj]:
            answer += m

    print(answer)