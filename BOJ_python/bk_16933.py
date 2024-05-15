# 벽 부수고 이동하기 3
from collections import deque as dq
from sys import stdin
input = stdin.readline
delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def bfs(si, sj, sk):
    q = dq([(si, sj, sk)])
    day = 1
    while q:
        if day % 2:
            night = False
        else:
            night = True
        for _ in '_' * len(q):
            vi, vj, k = q.popleft()
            if vi == N - 1 and vj == M - 1:
                return day
            else:
                for di, dj in delta:
                    ni, nj = vi + di, vj + dj
                    if 0 <= ni < N and 0 <= nj < M:
                        if maze[ni][nj] == '0':
                            if not visited[ni][nj][k]:
                                visited[ni][nj][k] = True
                                q.append((ni, nj, k))
                        else:
                            if not night:
                                if k < K and not visited[ni][nj][k + 1]:
                                    visited[ni][nj][k + 1] = True
                                    q.append((ni, nj, k + 1))
                            else:
                                q.append((vi, vj, k))
        day += 1
    return -1

N, M, K = map(int, input().split())
maze = [list(input().rstrip('\n')) for _ in '_'*N]
visited = [[[False]*(K+1) for _ in '_'*M] for _ in '_'*N]
visited[0][0] = [True]*(K+1)
print(bfs(0, 0, 0))