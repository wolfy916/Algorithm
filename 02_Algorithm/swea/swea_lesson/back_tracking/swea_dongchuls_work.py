# 동철이의 일 분배
def dfs(i, j, n, cal):
    global maxV
    if maxV

    if n == N:
        if maxV < cal:
            maxV = cal
    else:
        for k in range(N):
            if not visited[k]:
                visited[k] = 1
                dfs(i+1, j, n+1, cal * table[i][k]/100)
                visited[k] = 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    table = [list(map(int, input().split())) for _ in '_'*N]
    maxV = 0
    visited = [0] * N
    dfs(0, 0, 0, 100)

    print(f'#{tc} {maxV: .6f}')