# 동철이의 일 분배
def dfs(i, cal):
    global maxV

    # 가지치기~
    if maxV >= cal:
        return

    # maxV 갱신
    if i == N:
        if maxV < cal:
            maxV = cal
    else:
        for j in range(N):
            if not visited[j]:
                visited[j] = 1
                dfs(i+1, cal * table[i][j]/100)
                visited[j] = 0  # visited 초기화


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    table = [list(map(int, input().split())) for _ in '_'*N]
    maxV = -1
    visited = [0] * N
    dfs(0, 100)

    print(f'#{tc} {maxV:.6f}')