# 미친 로봇
# N은 14보다 작거나 같은 자연수, 모든 확률은 100보다 작거나 같은 자연수 또는 0
# 동서남북으로 이동할 확률을 모두 더하면 100


def dfs(vi, vj, N, cnt, value):
    global result
    if cnt == N:
        result += value
    else:
        for i in range(4):
            ni, nj = vi+delta[i][0], vj+delta[i][1]
            if 0 <= ni < 2*N+1 and 0 <= nj < 2*N+1:
                if not visited[ni][nj] and p_direction[i]:
                    visited[ni][nj] = 1
                    dfs(ni, nj, N, cnt+1, value * p_direction[i]/100)
                    visited[ni][nj] = 0


N, e, w, s, n = map(int, input().split())
delta = [(0, 1), (0, -1), (1, 0), (-1, 0)]
p_direction = [e, w, s, n]
result = 0
visited = [[0]*(2*N+1) for _ in '_'*(2*N+1)]
visited[N][N] = 1
dfs(N, N, N, 0, 1)
print(result)

