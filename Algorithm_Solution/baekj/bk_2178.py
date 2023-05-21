# 미로 탐색
N, M = map(int, input().split())
maze = [list(map(int, input())) for _ in '_'*N]
delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]
visited = [[0]*M for _ in '_'*N]
visited[0][0] = 1
q = [(0, 0)]
while q:
    vi, vj = q.pop(0)
    if (vi, vj) == (N-1, M-1):
        print(visited[vi][vj])
        break
    else:
        for di, dj in delta:
            ni, nj = vi+di, vj+dj
            if 0 <= ni < N and 0 <= nj < M:
                if not visited[ni][nj] and maze[ni][nj]:
                    visited[ni][nj] = visited[vi][vj] + 1
                    q.append((ni, nj))