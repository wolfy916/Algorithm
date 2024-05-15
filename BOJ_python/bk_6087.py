# 레이저 통신
import sys
from heapq import heappop, heappush

# [A] 입력 함수 초기화
def input():
    return sys.stdin.readline().rstrip('\n')

# [B] bfs + heapq
def bfs(si, sj):
    delta = [(0, -1), (-1, 0), (0, 1), (1, 0)]
    visited = [[[float('inf')] * 4 for _ in range(W)] for _ in range(H)]
    for k in range(4):
        visited[si][sj][k] = 0
    q = [(-1, si, sj)]
    while q:
        d, vi, vj = q.pop(0)
        if area[vi][vj] == 'C' and (si, sj) != (vi, vj):
            ti, tj = vi, vj
            continue
        for k in range(4):
            if d != -1 and (d + 2) % 4 == k: continue
            ni, nj = vi + delta[k][0], vj + delta[k][1]
            if ni < 0 or nj < 0 or ni >= H or nj >= W: continue
            if area[ni][nj] == '*': continue
            if d != -1:
                if (d + 1) % 4 == k or (k + 1) % 4 == d:
                    if visited[vi][vj][d] + 1 >= visited[ni][nj][k]: continue
                    visited[ni][nj][k] = visited[vi][vj][d] + 1
                else:
                    if visited[vi][vj][d] >= visited[ni][nj][k]: continue
                    visited[ni][nj][k] = visited[vi][vj][d]
            else:
                visited[ni][nj][k] = visited[vi][vj][d]
            q.append((k, ni, nj))

    return min(visited[ti][tj])

# [main]
if __name__ == '__main__':
    # 데이터 입력 및 초기화
    W, H = map(int, input().split())
    area = [list(input()) for _ in range(H)]

    # 시작 지점 탐색
    si, sj = -1, -1
    for i in range(H):
        for j in range(W):
            if area[i][j] != 'C': continue
            si, sj = i, j
            break
        if si != -1: break

    # bfs 결과 출력
    print(bfs(si, sj))