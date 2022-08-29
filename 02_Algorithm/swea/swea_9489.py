T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    area = [list(map(int, input().split())) for _ in '_'*N]

    delta = [[1, 0], [0, 1]]
    maxV = 0
    for i in range(N):
        for j in range(M):
            if area[i][j] == 1:
                for di, dj in delta:
                    ni = i + di
                    nj = j + dj
                    cnt = 1
                    while True:
                        if 0 <= ni < N and 0 <= nj < M and area[ni][nj] == 1:
                            cnt += 1
                            ni += di
                            nj += dj
                        else:
                            break
                    if maxV < cnt:
                        maxV = cnt

    print(f'#{tc} {maxV}')