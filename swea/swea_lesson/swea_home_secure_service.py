# 홈 방범 서비스

for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    area = [list(map(int, input().split())) for _ in '_'*N]

    K = 1
    delta = [[-1, 1], [-1, -1], [1, -1], [1, 1]]
    values = []
    while K != 41:
        operation = K ** 2 + (K - 1) ** 2
        max_houses = 0
        for i in range(N):
            for j in range(N):
                houses = 0
                if area[i][j] == 1:
                    houses += 1
                if K == 1:
                    continue
                if K >= 2:
                    for l in range(1, K):
                        x, y = i + l, j
                        for dx, dy in delta:
                            for _ in range(l):
                                x += dx
                                y += dy
                                if 0 <= x < N and 0 <= y < N and area[x][y] == 1:
                                    houses += 1

                revenue = houses * M
                profits = revenue - operation
                if profits >= 0:
                    if max_houses < houses:
                        max_houses = houses
        values += [max_houses]
        K += 1

    print(f'#{tc} {max(values)}')