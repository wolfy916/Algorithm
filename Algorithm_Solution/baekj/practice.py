# 그림
def solution():
    
    def dfs(r, c):
        sum = 1
        for i in range(len(delta)):
            nr, nc = r + delta[i][0], c + delta[i][1]
            if nr < 0 or nc < 0 or nr >= N or nc >= M or visited[nr][nc] or not board[nr][nc]: continue
            visited[nr][nc] = True
            sum += dfs(nr, nc)
        return sum

    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    visited = [[False] * M for _ in range(N)]
    answer = [0, 0]

    for i in range(N):
        for j in range(M):
            if visited[i][j] or not board[i][j]: continue
            visited[i][j] = True
            size = dfs(i, j)
            answer[0] += 1
            if size > answer[1]:
                answer[1] = size

    return "\n".join(map(str, answer))
    
print(solution())