# 정사각형 방
def dfs(i, j):
    stack = [[i, j, 1]]
    max_cnt = 0
    while stack:
        x, y, cnt = stack.pop()

        if max_cnt <= cnt:
            max_cnt = cnt

        for dx, dy in delta:
            nx, ny = x+dx, y+dy
            if 0 <= nx < N and 0 <= ny < N:
                if area[x][y]+1 == area[nx][ny]:
                    stack += [[nx, ny, cnt+1]]
    return max_cnt


for tc in range(1, int(input())+1):
    N = int(input())
    area = [list(map(int, input().split())) for _ in '_'*N]

    delta = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    values = []
    for i in range(N):
        for j in range(N):
            values += [[area[i][j], dfs(i, j)]]

    values.sort()
    values.sort(key=lambda x: x[1], reverse=True)

    print(f'#{tc} {values[0][0]} {values[0][1]}')