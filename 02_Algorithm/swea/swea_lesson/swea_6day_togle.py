T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    area = [list(map(int, input().split())) for _ in range(N)]

    for k in range(1, M+1):
        for i in range(N):
            for j in range(N):
                if M % k == 0:
                    area[i][j] += 1
                    continue
                if (i + j + 2) % k == 0:
                    area[i][j] += 1

    cnt = 0
    for x in range(N):
        for y in range(N):
            if area[x][y] % 2:
                cnt += 1

    print(f'#{tc} {cnt}')

