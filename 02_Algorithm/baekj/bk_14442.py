# 벽 부수고 이동하기 2
from collections import deque as dq
delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def bfs(si, sj, sk):
    q = dq([(si, sj, sk)])
    while q:
        vi, vj, k = q.popleft()
        if (vi, vj) == (N-1, M-1):
            return visited[vi][vj][k]
        else:
            for di, dj in delta:
                ni, nj = vi+di, vj+dj
                if 0 <= ni < N and 0 <= nj < M:
                    if not maze[ni][nj] and not visited[ni][nj][k]:
                        visited[ni][nj][k] = visited[vi][vj][k] + 1
                        q.append((ni, nj, k))
                    elif maze[ni][nj] and k < K and not visited[ni][nj][k+1]:
                        visited[ni][nj][k+1] = visited[vi][vj][k] + 1
                        q.append((ni, nj, k + 1))
    return -1

N, M, K = map(int, input().split())
maze = [list(map(int, input())) for _ in '_'*N]
visited = [[[0]*(K+1) for _ in '_'*M] for _ in '_'*N]
visited[0][0][0] = 1
print(bfs(0, 0, 0))