T = int(input())
for tc in range(1, T+1):
    N = int(input())  # 5 <= N <= 20
    area = [list(input()) for _ in '_'*N]

    delta = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
    result = 'NO'
    for i in range(N):
        for j in range(N):
            if area[i][j] == 'o':
                for di, dj in delta:
                    ni = i + di
                    nj = j + dj
                    cnt = 1
                    while True:
                        if 0 <= ni < N and 0 <= nj < N and area[ni][nj] == 'o':
                            cnt += 1
                            ni += di
                            nj += dj
                        else:
                            break
                    if cnt >= 5:
                        result = 'YES'
                        break
            if result == 'YES':
                break
        if result == 'YES':
            break

    print(f'#{tc} {result}')
