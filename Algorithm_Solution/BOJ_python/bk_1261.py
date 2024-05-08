# 알고 스팟
import sys
from collections import deque as dq

# [A] 입력 함수 초기화
def input():
    return sys.stdin.readline().rstrip('\n')

# [B] bfs
def bfs(N, M, maze):
    delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    # visited INF 값으로 초기화
    INF = float('inf')
    visited = [[INF] * M for _ in range(N)]
    visited[0][0] = 0
    q = dq([(0, 0, 0)])
    while q:
        vi, vj, cnt = q.popleft()
        if (vi, vj) == (N - 1, M - 1): continue
        for di, dj in delta:
            ni, nj = vi + di, vj + dj
            if ni < 0 or nj < 0 or ni >= N or nj >= M: continue
            # 벽인 경우, cnt에 1을 더한 값으로 체크
            if maze[ni][nj] and cnt + 1 >= visited[ni][nj]: continue
            # 벽이 아닌 경우 체크
            if not maze[ni][nj] and cnt >= visited[ni][nj]: continue
            visited[ni][nj] = cnt + 1 if maze[ni][nj] else cnt
            q.append((ni, nj, cnt + 1 if maze[ni][nj] else cnt))

    return visited[N-1][M-1]

# [main]
if __name__ == '__main__':
    M, N = map(int, input().split())
    maze = [list(map(int, input())) for _ in range(N)]
    print(bfs(N, M, maze))