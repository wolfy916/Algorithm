# 아기 상어 2

def bfs(q):
    while q:
        vi, vj, step = q.pop(0)
        for di, dj in delta:
            ni, nj = vi+di, vj+dj
            if 0 <= ni < N and 0 <= nj < M:
                if not graph[ni][nj] and visited[ni][nj] > step + 1:
                    visited[ni][nj] = step + 1
                    q.append((ni, nj, visited[ni][nj]))
    return max(map(max, visited))


N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
INF = 100
visited = [[INF] * M for _ in range(N)]
delta = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

q = []
for i in range(N):
    for j in range(M):
        if graph[i][j]:
            visited[i][j] = -1
            q.append((i, j, 0))

print(bfs(q))
