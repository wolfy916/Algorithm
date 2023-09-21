# 현수막
import sys
from collections import deque as dq

# [A] 입력 함수 초기화
def input():
    return sys.stdin.readline().rstrip('\n')

# [B] bfs
def bfs(si, sj):
    q = dq([(si, sj)])
    visited[si][sj] = True
    while q:
        vi, vj = q.popleft()
        for di, dj in delta:
            ni, nj = vi+di, vj+dj
            if ni < 0 or nj < 0 or ni >= N or nj >= M: continue
            if visited[ni][nj] or not arr[ni][nj]: continue
            visited[ni][nj] = True
            q.append((ni, nj))

# [main]
if __name__ == '__main__':
    N, M = map(int, input().split())
    arr = [tuple(map(int, input().split())) for _ in range(N)]
    delta = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    visited = [[False] * M for _ in range(N)]
    answer = 0

    for i in range(N):
        for j in range(M):
            if not arr[i][j] or visited[i][j]: continue
            answer += 1
            bfs(i, j)

    print(answer)