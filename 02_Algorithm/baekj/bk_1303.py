# 전쟁-전투

def dfs(s_i, s_j, color):
    STACK = [[s_i, s_j]]
    while STACK:
        STACK

N, M = map(int, input().split())
area = [list(input()) for _ in '_'*M]

delta = [[-1, 0], [1, 0], [0, -1], [0, 1]]
visited = [[0]*N for _ in '_'*M]
result_W = 0
result_B = 0

for i in range(M):
    for j in range(N):
        if visited[i][j] == 0:
            if area[i][j] == 'W':
                visited[i][j] = 1
                dfs(i, j, 1)
            else:
                visited[i][j] = 2
                dfs(i, j, 2)

